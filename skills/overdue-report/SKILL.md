---
name: overdue-report
description: Report which initiatives on a board export have no due date or a date in the past. Use when asked what is overdue, what is missing dates, or to prepare a chase list before a status meeting.
---

# Overdue report

Turns a board export into a short chase list. Built for the weekly question "what needs a date on
it before the status call", which is otherwise ten minutes of scrolling.

**This is a worked example for the spec-driven development workshop.** It is deliberately small
enough to read in one sitting, because the point is that you could have written it.

## When to use this

Use it when someone needs a chase list. Do not use it as a status report: it answers one narrow
question and answering more would make it worse.

## Input

A CSV export with at least these columns. Extra columns are ignored rather than being an error,
because board exports grow.

| Column | Meaning |
|---|---|
| `key` | The board identifier |
| `summary` | Short title |
| `owner` | Who holds it |
| `status` | Current state |
| `due` | ISO date, or empty |

A sample lives at `fixtures/initiatives-sample.csv`.

## What to produce

Three groups, in this order, because it is the order someone acts in:

1. **Overdue.** A `due` date before today, and a status that is not a done state. Sort oldest
   first. This is the only group that is urgent.
2. **No date at all.** Empty `due`, and not a done state. Sort by owner so one person's items sit
   together and the chase is one message instead of five.
3. **Due within seven days.** Early warning. Say so rather than mixing it into overdue.

Then a one-line count of items skipped because their status was a done state, so the reader can
tell the difference between "nothing overdue" and "the filter ate everything."

## Rules

- **Never write to the board.** This reads an export and produces text. If someone asks you to
  update the dates as well, say that is a different job and confirm before doing it.
- **Say what "today" is** in the output. A chase list with no date on it gets forwarded a week
  later and quietly misleads someone.
- **An empty result is a sentence, not an empty list.** "Nothing is overdue as of 2026-09-28" is
  information. A blank section looks like a bug.
- **Do not guess at a missing owner.** Report it as unassigned, which is itself the finding.
- **Do not editorialise about people.** Report what the board says. Who is behind on what is a
  fact about a board row, and framing it as a fact about a person is not this tool's job.

## Output shape

Markdown, grouped as above, with the key as a link if a base URL is configured. Keep it short
enough to paste into a message. If it runs past a screen, the filter is too loose.

## Adapting this

The three groups and the seven-day window are the parts most likely to be wrong for your board.
Change those first. The last rule is the one not to change.
