# The opening prompt

This is the whole of what gets typed to start the demo. It is one message, written the way people
actually write to an agent, and it is the only thing prepared in advance.

**Nothing else is pre-built.** No constitution, no spec files, no plan. Those are what
`/speckit-constitution` and `/speckit-specify` produce, and watching them get produced is the
demo. Writing them beforehand and then revealing them would teach the wrong thing, which is that
this workflow is about having good documents rather than about the conversation that makes them.

**Why it is deliberately casual.** The most common failure in a spec-driven demo is an opening
prompt so elaborate that the audience concludes the technique requires an hour of writing before
you start. It does not. You need enough context that the agent stops guessing, and you get the
rest by answering its questions. Aim for something you would actually type, and let the agent pull
the detail out of you.

---

## The prompt

> Hey, I want to build a small thing and I would like to do it properly rather than just hacking
> at it, so let's start with the constitution.
>
> Here is the situation. Our team is starting to take on AI and automation requests from around
> the business, and for every one of them somebody eventually asks what the return is. Right now
> that answer gets rebuilt from scratch each time, in a different spreadsheet, with different
> assumptions, and the numbers are not comparable across initiatives. One of my colleagues owns
> the ROI template and is trying to roll it up across everything we run, which is the part that
> does not work today.
>
> There is an existing spreadsheet at `fixtures/ai-productivity-roi-calculator.xlsx` that has the
> model in it. Have a look at it before you ask me anything. It is structured on the Forrester
> TEI shape, it has an Inputs sheet and a Model sheet, and the benchmark figures on the last sheet
> are all measured on software developers, which our team mostly is not.
>
> What I want to end up with is something that takes that model and applies it consistently to
> several initiatives at once, so we can compare them and roll them up. Not a fancy UI. Probably
> something that reads the assumptions per initiative and produces a summary a non-analyst can
> act on.
>
> Two things I already know I care about. It has to report the benefit figure and the ROI
> percentage separately, because people ask for one and mean the other and I am tired of that
> conversation. And every assumption has to stay visible and editable, because the argument is
> always about the assumptions and never about the arithmetic.
>
> Ask me whatever you need to, then let's write the constitution together.

---

## What to watch for while it runs

**The agent will ask good questions.** That is the point of the demo and it should not be rushed.
Expect it to ask about scope, about where the per-initiative assumptions live, and about what
counts as done.

**Disagree with at least one of its suggestions out loud.** It will propose something reasonable
that is wrong for this context. Saying no in front of the room is the single most useful thing
that happens in the hour, because it shows the human is steering rather than accepting.

**Do not let it build.** If it starts writing code before the constitution exists, stop it and say
so. That moment is worth more than a clean run: the audience has all seen an agent charge ahead,
and seeing it pulled back is the thing they will remember.

**One question it should surface on its own**, and if it does, let the room see it: what does ROI
mean here. The spreadsheet answers it, but the agent has to go and look.
