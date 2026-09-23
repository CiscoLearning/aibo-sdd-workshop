# Feature spec: phase 1, read and summarise

> **Synthetic example**, matching phase 1 of [`constitution.md`](constitution.md). This is what
> exists *before* any code does. Written in conversation with the agent, then reviewed by a human,
> then committed.

## What this feature does

Take a CSV export of course feedback and produce one markdown digest, grouped by course, that a
curriculum owner can read in ten minutes.

## Requirements

1. Accept a CSV path as input. Do not go looking for files on your own.
2. Group by course identifier. One section per course, ordered by response count, most first.
3. Each section reports: response count, average rating to one decimal place, and up to three
   representative comments chosen for variety rather than sentiment.
4. **A course with fewer than five responses is reported as "not enough responses this week"** and
   shows no average. The threshold lives in config.
5. Output is a single markdown file. Nothing is printed to the terminal except the output path.
6. Rows with a missing or unparseable rating are counted and reported as a total at the end. They
   are never silently dropped.

## Explicitly out of scope

Themes, week-over-week comparison, and delivery. Those are phases 2 to 4. **Saying this here is
what stops the agent helpfully building all four.**

## How we will know it worked

- Running it against `fixtures/initiatives-sample.csv` produces a digest with no errors.
- A course with four responses shows the "not enough responses" line and no average.
- A row with a rating of `n/a` appears in the unparseable count and not in any average.
- Deleting the input file produces a clear message and a non-zero exit, not a stack trace.
- A curriculum owner who has not seen the code can read the output and say what to do next.

## Notes for the review

The fifth check is the one that matters and the only one a test cannot do for you. The first four
prove the thing runs. The fifth is the reason the feature exists, and if it fails while the others
pass, the spec was wrong rather than the code.
