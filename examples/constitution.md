# Constitution: Course Feedback Digest

> **This is a synthetic example.** The project does not exist. It is shaped like the kind of
> request the team actually gets, so the structure transfers, and it names nobody.

## Mission

Turn the free-text feedback left on internal course pages into a weekly digest a curriculum owner
can act on in ten minutes, instead of a spreadsheet nobody opens.

**Who uses it.** Curriculum owners, weekly. They are not analysts. They want to know what changed
and what needs attention, in that order.

**What success looks like.** A curriculum owner reads the digest and takes at least one concrete
action from it. If it becomes another report nobody opens, it has failed even if every number in
it is correct.

## Non-negotiable

- **No learner-identifying data in this repository.** Feedback is read from its source and the
  digest reports counts and themes. Names, email addresses and CEC IDs never land in a file here.
- **Read-only against every upstream system.** This tool never writes to a course page, a survey
  platform or a ticket.
- **Every threshold is config, not code.** What counts as a spike, how many themes to surface, how
  far back to look. Someone who does not write code should be able to change these.
- **The digest says when it does not know.** A week with too little feedback to be meaningful says
  so rather than reporting a percentage of four responses.

## Tech stack

Python, because the team already reads it and the existing board tooling is written in it. Plain
CSV in and markdown out, so every intermediate step is inspectable without a database. No
scheduled job in version one, since a human running it weekly is a smaller thing to get right.

## Roadmap

1. **Read and summarise.** Take a feedback export, produce a markdown digest, one section per
   course. Manual run.
2. **Themes.** Group the free text into recurring themes rather than listing every comment.
3. **Change over time.** Compare this week to last week and lead with what moved.
4. **Delivery.** Put it somewhere people already look, rather than sending another email.

Each phase is its own feature spec and its own branch. Phase one should be useful on its own; if
it is not, the roadmap is wrong rather than the implementation.
