# When it does not work

The failures people hit in week one are almost never about the model being bad. They are about the
agent not having something it needed, usually because of where you started it. **This page is the
list, shortest first.**

## The one that gets everybody: you are in the wrong directory

**Claude Code loads its context from the directory you start it in.** Project instructions, skills,
memory, the lot. Start it somewhere else and none of that loads, and **it will not tell you.** It
will answer cheerfully and badly, and the natural conclusion is that the tool is not very good.

- Start it **in the project folder**, not your home directory.
- **A folder above the project does not work.** Nothing from the project loads.
- **A folder below the project usually does not either.** Do not start in `src/` and expect the
  project's instructions to be there.

**How to tell within ten seconds.** Ask it something only the project could answer: *"what is this
project and what are its rules?"* If the answer is generic, you are in the wrong place. Quit,
change directory, start again. There is nothing to repair.

This is worth knowing before anything else on this page, because it silently degrades everything
and it looks exactly like the model being unhelpful.

## The words, so nobody has to ask twice

Real question from the team, so it is written down rather than assumed.

| Term | What it means, in one line |
|---|---|
| **Agent** | A model that can act rather than only answer. It plans, uses tools, reads results, and keeps going until the task is done. |
| **Harness** | The program the model runs inside, which gives it tools and decides what it is allowed to do. Claude Code is a harness. The model on its own cannot open a file; the harness is what lets it. |
| **Tool** | One thing the agent can do: read a file, run a command, search. The harness supplies the list. |
| **Skill** | A markdown file of instructions and context, loaded when the task matches, that teaches the agent how you want something done. Most of this repo is examples of these. |
| **MCP** | A standard way to plug an external system into an agent, so it can reach something the harness does not ship with. |
| **Context window** | Everything the model can see at once. It is finite, and it fills up. |
| **Context decay** | What happens when it fills up. Quality drops, earlier instructions get crowded out, and the agent starts contradicting things it agreed to an hour ago. |

**Why the harness question matters practically** rather than as trivia: it is the reason the same
model behaves differently in two tools, and the reason a skill you write here works in Claude Code
and does nothing in a chat window.

## The next three, in the order you will meet them

**The session has been running too long.** Every message resends the whole conversation, so a long
session is slower, more expensive, and worse, all at once. **Use `/clear` between unrelated
tasks.** It is the highest-value habit available and it costs nothing. If the task changed, clear.

**It did too much.** Agents will happily build the whole thing when you wanted one piece. The fix
is in the spec rather than in the scolding: say what is out of scope, in writing, before it starts.
The example in `examples/feature-spec.md` has an explicit out-of-scope section for exactly this
reason, and that section is what stops it helpfully building all four phases.

**It silently drifted from the plan.** You changed a file by hand, and now the code and the spec
disagree. Ask the agent to make the change instead, so it updates the related documents at the same
time. This is the most common way a spec stops being true, and a spec that is not true is worse
than no spec.

## What is not worth worrying about yet

Model choice, token accounting, sub-agents, parallel runs. All real, none of them the reason your
first week is going badly. Come back to them once the four things above are habits.
