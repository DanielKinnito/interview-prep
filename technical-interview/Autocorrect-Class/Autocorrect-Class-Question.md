# Question

Create a class Autocorrect that takes a list of strings (words) in its constructor:

corrector = Autocorrect(["apple", "pear", "orange"])
Then implement a method correct(word) which returns a corrected word. A match is:

Exact match, or
One letter off (only 1 mismatch allowed).

## Examples

- corrector.correct("apple") -> "apple" (exact match)
- corrector.correct("bpple") -> "apple" (one mismatch, so corrected to "apple")
- corrector.correct("bear") -> "pear" (one mismatch, so corrected to "pear")
- corrector.correct("apples") -> "apples" (no fix; length differs)
- corrector.correct("app") -> "app" (length differs, not corrected)
- corrector.correct("aisle") -> "aisle" (two mismatches from "apple," so not corrected)

## Key Points

1. Data Structure: Possibly a Trie, Hash Set, or direct string comparison.
2. One Mismatch Logic: If more than 1 mismatch is found, no correction.
3. Edge Cases: Different lengths automatically fail (except exact same length).
4. Time Complexity: Balance building the structure and querying.