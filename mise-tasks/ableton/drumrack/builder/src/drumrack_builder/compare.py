"""Choose among a pad's candidates by pairwise votes or by a single-elimination bracket."""

from __future__ import annotations

import itertools
import math
from collections import Counter
from dataclasses import asdict, dataclass, field


def next_pair(candidates: list[int], votes: list[tuple[int, int]]) -> tuple[int, int] | None:
    """The pair compared least often, preferring candidates that have been heard least.

    ``votes`` holds (winner, loser) pairs. Returns None when fewer than two candidates remain.
    """
    if len(candidates) < 2:
        return None
    seen = Counter(frozenset(v) for v in votes if v[0] in candidates and v[1] in candidates)
    heard = Counter(x for v in votes for x in v)
    order = {c: i for i, c in enumerate(candidates)}

    def cost(pair: tuple[int, int]) -> tuple[int, int, int, int]:
        a, b = pair
        return seen[frozenset(pair)], heard[a] + heard[b], order[a], order[b]

    return min(itertools.combinations(candidates, 2), key=cost)


def ranking(candidates: list[int], votes: list[tuple[int, int]], iterations: int = 200) -> list[dict]:
    """Bradley–Terry strengths from pairwise votes, fitted by the minorization–maximization update.

    Each candidate gets one virtual draw against an average opponent so a candidate with no losses
    keeps a finite strength.
    """
    wins: Counter[int] = Counter()
    losses: Counter[int] = Counter()
    games: Counter[frozenset[int]] = Counter()
    for winner, loser in votes:
        if winner in candidates and loser in candidates and winner != loser:
            wins[winner] += 1
            losses[loser] += 1
            games[frozenset((winner, loser))] += 1
    strength = dict.fromkeys(candidates, 1.0)
    for _ in range(iterations):
        updated = {}
        for c in candidates:
            denominator = 1.0 / (strength[c] + 1.0)  # virtual games against strength 1
            for d in candidates:
                n = games[frozenset((c, d))] if c != d else 0
                if n:
                    denominator += n / (strength[c] + strength[d])
            updated[c] = (wins[c] + 0.5) / denominator
        total = sum(updated.values()) or 1.0
        strength = {c: v * len(candidates) / total for c, v in updated.items()}
    rows = [
        {"sample_id": c, "wins": wins[c], "losses": losses[c], "score": round(math.log(strength[c]), 3)}
        for c in candidates
    ]
    return sorted(rows, key=lambda r: (-r["score"], -r["wins"], candidates.index(r["sample_id"])))


@dataclass
class Match:
    a: int | None
    b: int | None
    winner: int | None = None


@dataclass
class Bracket:
    """Single elimination. Byes go to the top seeds; a match with one entrant resolves at once."""

    rounds: list[list[Match]] = field(default_factory=list)

    @classmethod
    def create(cls, seeds: list[int]) -> Bracket:
        if len(seeds) < 2:
            raise ValueError("a bracket needs at least two candidates")
        if len(set(seeds)) != len(seeds):
            raise ValueError("a candidate appears twice in the bracket")
        size = 1 << math.ceil(math.log2(len(seeds)))
        slots: list[int | None] = [None] * size
        for position, seed_index in enumerate(standard_order(size)):
            if seed_index < len(seeds):
                slots[position] = seeds[seed_index]
        bracket = cls(rounds=[[Match(slots[i], slots[i + 1]) for i in range(0, size, 2)]])
        while len(bracket.rounds[-1]) > 1:
            bracket.rounds.append([Match(None, None) for _ in range(len(bracket.rounds[-1]) // 2)])
        bracket.advance()
        return bracket

    def advance(self) -> None:
        for r, matches in enumerate(self.rounds):
            for i, match in enumerate(matches):
                if match.winner is None and r == 0 and (match.a is None) != (match.b is None):
                    match.winner = match.a if match.a is not None else match.b
                if match.winner is not None and r + 1 < len(self.rounds):
                    target = self.rounds[r + 1][i // 2]
                    if i % 2 == 0:
                        target.a = match.winner
                    else:
                        target.b = match.winner

    def current(self) -> tuple[int, int, Match] | None:
        for r, matches in enumerate(self.rounds):
            for i, match in enumerate(matches):
                if match.winner is None and match.a is not None and match.b is not None:
                    return r, i, match
        return None

    def pick(self, winner: int) -> None:
        found = self.current()
        if found is None:
            raise ValueError("the bracket is finished")
        _, _, match = found
        if winner not in (match.a, match.b):
            raise ValueError(f"{winner} is not in the current match")
        match.winner = winner
        self.advance()

    @property
    def champion(self) -> int | None:
        return self.rounds[-1][0].winner

    def to_dict(self) -> dict:
        return {"rounds": [[asdict(m) for m in matches] for matches in self.rounds]}

    @classmethod
    def from_dict(cls, data: dict) -> Bracket:
        return cls(rounds=[[Match(**m) for m in matches] for matches in data["rounds"]])


def standard_order(size: int) -> list[int]:
    """Seed indexes in bracket order so seed 0 and seed 1 can only meet in the final."""
    order = [0]
    while len(order) < size:
        span = len(order) * 2
        order = [x for seed in order for x in (seed, span - 1 - seed)]
    return order
