see-also:: [[My/Principle/Problem/Solving/3 - Incremental and Iterative Improvement]]

- When a team moves from an old framework to a new one, I prefer a [[Ratchet Migration]] policy: maintain the old thing in the old framework, but write new components in the new framework, and if we need to change more than 10% in an old component, rewrite that component in the new framework.
- Teams I've worked on have benefitted from this policy. The migration happens as part of regular work, and each change leaves less code in the old framework.
- Write the policy down, threshold included, so that everyone makes the same call when they open an old component.
