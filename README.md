# Spec-driven development workshop

Follow-along material for the AIBO session on **Monday, September 28, 2026**. Everything demoed in
that hour is here so you can retrace it on your own machine instead of remembering it.

**You do not need to be a programmer to use this repo.** The whole argument of the session is that
the skill being taught is specifying rather than typing. Every file here is markdown you can read.

## Start here

| If you want to | Read |
|---|---|
| **Have never really used Git or GitHub** | [`getting-started/where-the-code-lives.md`](getting-started/where-the-code-lives.md) |
| **Try it and find it is not working** | [`getting-started/when-it-does-not-work.md`](getting-started/when-it-does-not-work.md) |
| See exactly how the live demo was started | [`examples/demo-opening-prompt.md`](examples/demo-opening-prompt.md) |
| Look at the spreadsheet the demo was built around | [`fixtures/ai-productivity-roi-calculator.xlsx`](fixtures/ai-productivity-roi-calculator.xlsx) |
| Understand what a project constitution is and write one | [`examples/constitution.md`](examples/constitution.md) |
| See what a feature spec looks like before any code exists | [`examples/feature-spec.md`](examples/feature-spec.md) |
| Steal a working skill and adapt it | [`skills/overdue-report/SKILL.md`](skills/overdue-report/SKILL.md) |
| Go deeper than the hour allowed | [Resources](#resources) below |

**The examples are a different project from the demo, on purpose.** The demo builds an ROI
rollup. `examples/constitution.md` and `examples/feature-spec.md` describe a course feedback
digest. Seeing the same shape applied to two unrelated problems is more useful than seeing one
problem twice, and it makes the point that the structure is not specific to what was demoed.

## The workflow, in one paragraph

Write a **constitution** once per project: what it is for, who uses it, what it must never do, and
what the roadmap is. Then work one **feature** at a time in a loop: **specify** what you want and
how you will know it worked, let the agent **implement** it, then **validate** the result yourself.
Between features, **replan**: revise the constitution, reorder the roadmap, improve the process.
The constitution persists and the features cycle underneath it.

## The one slide worth remembering

**Write down:** goals, audience, constraints, and how you will know it is done.

**Leave alone:** variable names, which library, file layout, and how to do it. Those are the parts
you are delegating, and the agent picks better ones than you will.

Over-steering is the common beginner mistake. If you find yourself describing *how*, you have
stopped specifying and started typing.

## About the data in this repo

**Everything here is synthetic.** [`fixtures/initiatives-sample.csv`](fixtures/initiatives-sample.csv)
is invented data shaped like a real board, not an export of one, and the constitution and spec
examples describe a made-up project. That is deliberate: it keeps the repo shareable, and it means
the examples work on your machine without any access to internal systems.

When you adapt these for real work, the real data stays out of the repo. Point at it, do not commit
it.

## Access

This repo is **private to the CiscoLearning organisation**, and organisation membership on its own
grants nothing. If a link here 404s for you, that means you have not been added yet rather than
that the link is broken. Send your GitHub user ID to Jason and you will be added to the AIBO team.

## Resources

- **[GitHub Spec Kit](https://github.com/github/spec-kit)**. The open-source toolkit the workflow
  in the session is built on. Slash commands for constitution, specify, plan, tasks, implement.
- **[Spec-Driven Development with Coding Agents](https://youtu.be/hy8UstR2NEg)**. Free course from
  DeepLearning.AI with JetBrains, about an hour, instructor Paul Everett. The session borrows three
  of its explanations and says so. Worth the hour if any of this was interesting.
- **[Agent Skills](https://code.claude.com/docs/en/skills)**. What a skill is and where it lives.

## Two things the session said out loud that are easy to forget

**The agent is the muscle. The spec is the brain.** Rather than writing code by hand, you write
down the context the agent does not already have.

**Not everything deserves a spec.** A question you need answered once, a thing that already works
for free, or anything you could finish before the spec is written should just be done. Knowing
which is which is the actual skill.
