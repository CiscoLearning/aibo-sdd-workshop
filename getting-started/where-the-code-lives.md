# Where the code lives

Written for the session on Sep 28, 2026, but useful on its own. If you have never used Git or
GitHub in anger, start here. **Nothing below assumes you have.**

This exists as a page rather than as slides on purpose. Procedural material is needed at the
moment you are stuck, which is never during a presentation.

## Git and GitHub, in six lines

| Term | What it actually is |
|---|---|
| **Git** | A history of every change to a set of files, with who made it and why. Like version history in a Word doc, except it never loses anything and two people can work at once. |
| **GitHub** | A website that hosts those histories so a team shares one copy. Cisco has an internal one. |
| **Repository, or "repo"** | One project's folder, plus its whole history. |
| **Organisation, or "org"** | A container for many repos, with shared membership and shared rules. |
| **Pull request, or "PR"** | "Here is my change, please look before it goes in." Where review happens. |
| **CI/CD** | Checks that run automatically on every change, by a machine, before a person looks. |

That is the whole vocabulary you need for this repo. Branches, merges and commits can wait until
you need them, and you will pick them up faster with something real in front of you.

## Our org, and what you get for free

Our code lives in the **`CiscoLearning`** GitHub organisation. It already existed and the wider
organisation already uses it, so nothing was created for us and nobody had to ask permission.

Repos we own are named **`aibo-<initiative>`**: `aibo-cx-qtt`, `aibo-shared-expertise`,
`aibo-speckit-template`, `aibo-albert-eval-lab`, `aibo-lantern-content-automation`, and this one.

**That prefix is not just tidiness. It attaches rules.** Any repo matching `aibo-*` automatically
gets branch protection on `main`: it cannot be deleted, it cannot be force-pushed, and changes have
to arrive through a pull request.

> **Correction to what was planned.** An earlier proposal used `AIBO-<number>-<short-name>`, with
> the Jira key in the repo name. **It was never adopted.** The real convention is
> `aibo-<initiative>`. Repeating a convention that is not actually in force is the kind of claim
> nobody checks, so it is corrected here rather than quietly carried forward.

**One thing is not automatic, and it bit this repo.** Secret scanning and push protection are
enabled **per repo** and a new repo does not inherit them. They were switched on here by hand after
creation. If you make an `aibo-*` repo, turn them on yourself and do not assume the name did it.

## Three kinds of repo, and the line between them

The boundary is drawn by **what a thing is, not by who wrote it**.

| What it holds | Where | Who sees it |
|---|---|---|
| **Shared skills, prompts, instruction layers** | `cisco-claude-workflows` | Cisco-wide. One place to look, and it already exists. |
| **An ops workspace** — notes, stakeholders, meeting records | A private workspace, per person | **Nobody.** It holds opinions about how work is going and material received in confidence. |
| **Per-initiative builds** — the actual code | `aibo-<initiative>` | Per repo. Self-contained enough to hand to someone else. |

**How the private material stays private is structural, not a scan.** Real data lives only in the
ops workspace. Build repos reach it through a link that is never committed, and commit
**synthetic test data** instead. That is why a build repo can be handed to any colleague with no
cleanup pass: the real data was never in it. This repo does the same thing, which is why every
figure in `fixtures/` is invented.

## One rule for where a fact goes: audience

The failure being designed out is the same fact in two places, drifting, until neither is trusted
by month four.

> **If a stakeholder or the requester reads it, it lives in Jira.
> If only the person building it needs it, it lives in the repo.**

| | Jira | Repo |
|---|---|---|
| Holds | Phase, epic, milestone, major decisions, sign-offs | Requirements detail, plans, tasks, tests, decision records |
| Read by | Leadership, the phase owners, the requester | Whoever is building, and whoever picks it up next |
| Shape | **Append-only.** A dated comment cannot drift | **Living.** Updated with every change |

**Jira stays the board. The repo writes into it.** This is not a second system of record, and a
phase transition can be a side effect of the work rather than a separate chore.

The test, if the rule ever feels unclear: *"is the form filtering by today's date yet?"* is a Jira
question, because a requester will ask it. *"Is task T047 done?"* is not, because nobody outside
the build ever will.

## Getting in

**Organisation membership grants nothing on its own.** The base permission is `none`, deliberately.
So a link to one of these repos will **404 for you until you are added to the AIBO team inside the
org**, and a 404 here means *not invited* rather than *broken*.

Send your GitHub user ID to Jason and you will be added. That is the whole process, and it is the
first item on the session's last slide for a reason: everything else is blocked behind it.

## If you want a workspace of your own

The middle row of that table is the one people ask about, because everyone has the same problem:
notes in four places and no single answer to "what am I actually working on." The shape is
deliberately boring:

```text
your-workspace/
├── README.md            # the master project list, one row per active thread
├── projects/
│   ├── <initiative>/
│   │   ├── notes.md     # dated sections, newest last, action items per section
│   │   └── ...          # briefs, plans, prep docs for that one thread
│   └── _general/        # ad hoc asks; promote to a folder once it is real work
├── decisions/           # numbered records: what was decided, and why
├── transcripts/         # meetings, diarized
└── notes/               # the running log, and goals
```

**The master project list is the load-bearing part**, and it is one table with five columns:
the project (linking to its notes), the Jira ticket, whether it has a build repo, the status with a
date, and **the next action**. That last column is the one that earns its place. If it is empty,
the thread is stalled and you can see it at a glance.

Two conventions do more work than they look like they should: **one folder per thread**, and
**every notes section carries its own date and its own action items**, so the file skims and
nothing has to be re-derived.

**Steal the two conventions and ignore the rest.** This is a shape, not a filing system to adopt
wholesale.
