import itertools

import pytest

from drumrack_builder import compare


def test_next_pair_covers_every_pair_before_repeating():
    candidates = [1, 2, 3, 4]
    votes: list[tuple[int, int]] = []
    seen = set()
    for _ in range(6):
        pair = compare.next_pair(candidates, votes)
        assert pair is not None
        seen.add(frozenset(pair))
        votes.append(pair)
    assert seen == {frozenset(p) for p in itertools.combinations(candidates, 2)}
    assert compare.next_pair([1], []) is None


def test_ranking_follows_the_votes():
    votes = [(3, 1), (3, 2), (3, 4), (2, 1), (2, 4), (4, 1)]
    ranking = compare.ranking([1, 2, 3, 4], votes)
    assert [r["sample_id"] for r in ranking] == [3, 2, 4, 1]
    assert ranking[0]["wins"] == 3 and ranking[-1]["losses"] == 3


def test_ranking_without_votes_keeps_shortlist_order():
    assert [r["sample_id"] for r in compare.ranking([5, 6, 7], [])] == [5, 6, 7]


@pytest.mark.parametrize("size", range(2, 10))
def test_bracket_always_produces_a_champion(size):
    seeds = list(range(100, 100 + size))
    bracket = compare.Bracket.create(seeds)
    matches = 0
    while (current := bracket.current()) is not None:
        _, _, match = current
        bracket.pick(min(match.a, match.b))  # the lower id always wins
        bracket = compare.Bracket.from_dict(bracket.to_dict())
        matches += 1
    assert bracket.champion == 100
    assert matches == size - 1  # every candidate but the champion loses once


def test_top_seeds_get_byes_and_meet_only_in_the_final():
    bracket = compare.Bracket.create([1, 2, 3])
    first = bracket.rounds[0]
    assert any(m.winner == 1 and None in (m.a, m.b) for m in first)
    _, _, match = bracket.current()
    assert {match.a, match.b} == {2, 3}
    bracket.pick(2)
    _, round_index, final = bracket.current()
    assert {final.a, final.b} == {1, 2}


def test_bracket_rejects_bad_input():
    with pytest.raises(ValueError):
        compare.Bracket.create([1])
    with pytest.raises(ValueError):
        compare.Bracket.create([1, 1])
    bracket = compare.Bracket.create([1, 2])
    with pytest.raises(ValueError):
        bracket.pick(3)
    bracket.pick(2)
    with pytest.raises(ValueError, match="finished"):
        bracket.pick(2)
