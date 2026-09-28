---
tags: [concept, testing]
sources: [mastodon]
---

# AI in Testing

## 2023 — GenAI arrives, and she reaches for skepticism first — [[../batches/2023|batch]]

ChatGPT's public release (late 2022) turns into a running experiment
across the whole year, distinct in tone from her generally optimistic
adoption of other new tools. She tests it directly against her own
expertise and finds it "confidently incorrect" — inventing a book
attribution for one colleague and a founding credit for another,
"makes stuff up and looks plausible" — coining the phrase **"hallucination
testing"** as a new budget line item for the practice, only half-joking:
"it used to be called fact checking but we're rebranding it to match
generative AI needs." A deeper ethical thread runs alongside the
practical one: she names a "significant personal integrity problem with
paying in organizational scale for licenses to a service based on
pillaging digital content without consent & compensation," weighing
"offsetting the damage" against outright refusal to use AI code
generation. She still finds real, bounded uses — TestingDozen sessions
built around exploring ChatGPT together, arguing (and losing) with it
over a failing test, Copilot used while drafting a book (noticeably
better at technical prose than at explaining exploratory testing) — but
closes the year unconvinced by a colleague's demo claiming AI coding is
"55% faster" while live-generating incorrect code: "Writing wrong code
fast is not a positive trait." A recurring throughline: people readily
trust AI-generated documentation and code they would never trust from
an unfamiliar human source.

Representative posts:
- https://mas.to/@maaretp/109659751892222239
- https://mas.to/@maaretp/110378322601416173
- https://mas.to/@maaretp/111450537185003318
- https://mas.to/@maaretp/111444118536529849

## 2024 — AI becomes the actual job, not just a personal experiment — [[../batches/2024|batch]]

The shift from bystander to practitioner is structural this year: her
new CGI director role (see `../entities/cgi.md`) is explicitly
AI-in-testing focused, and she'd already done the ethical groundwork
the year before — risk assessment, tooling upgrades, and three
compensations (public transparency, open-source time, and money) — to
get GitHub Copilot approved on production code at her prior employer.
Her skepticism stays consistent and sharpens into a named principle:
AI should be used to "prune, not generate" — cutting wasteful test
practices rather than automating them faster, coining "hallucination
testing" as a real line item to budget for. The CrowdStrike outage in
July becomes a case study she returns to more than once, arguing the
industry's "it's a testing failure" read misses the layered mitigations
(delayed rollout, dogfooding, throttling, architecture) that her own
security-software years had relied on. She runs her own small, costed
experiment late in the year — paying $1.13 to run six AI-generated test
cases against a genAI test-automation tool, for a blog post titled
"Cost-Constrained Exploratory Testing."

Representative posts:
- https://mas.to/@maaretp/112892260659847194
- https://mas.to/@maaretp/112762416440853561
- https://mas.to/@maaretp/112885735967594797
- https://mas.to/@maaretp/113505391862931394

## 2025 — from budget-line skepticism to a working classification — [[../batches/2025|batch]]

The skepticism from 2023–2024 stays intact but gets more precise tools
to work with. She names a self-critical classification of her own AI
use — **avoiding, trying, using, building** — and admits her bar for
"building" has been set too high, calling a third-party API call "using"
rather than "building" even when it was the point she wanted to make.
Names a new term for a familiar failure mode: **"workslop"** — AI-
generated text passed off as work product by someone who didn't know the
topic well enough to judge whether it added value — and keeps asking the
same question of colleagues: "what is the value add your processing
(with AI) added on the understanding we are creating?" Tracks how genAI
has already changed code review in practice — reviewers dismiss AI
comments more easily than human ones ("being rude to a machine is
acceptable"), but the appearance of review may discourage real review —
a blog post, "Code reviews have already changed," makes the case in
full. A vendor's genAI test tool quietly drops its per-test cost display
once it stops working for non-OpenAI APIs, read as a "design of your
defaults" problem, not a bug. She demos a friend's Claude-Code-based
"Agentic QE Fleet" tool and proposes [[../entities/selenium-project|
Selenium]] as its open-source analysis target. Closes the year unmoved
by both credulous and dismissive extremes — unimpressed by a manager
claiming weeks of work in "4 hours" of vibe-coding when the commit
history says otherwise, and equally unimpressed by "faster bad" as a
solution to a testing chain that was already broken before AI arrived.

Representative posts:
- https://mas.to/@maaretp/115274621933790173
- https://mas.to/@maaretp/115708410719051085
- https://mas.to/@maaretp/114948695012474469
- https://mas.to/@maaretp/115746022359423835
- https://mas.to/@maaretp/115700908331510701

## 2026 — "workslop" gets teeth, and results get measured, not guessed — [[../batches/2026|batch]]

"Workslop" stops being a diagnosis and becomes a working vocabulary:
"software and slopware," "human slop or AI slop," and a blunt refusal
when a project manager ignores her own testing estimates in favor of
AI-generated ones — "Yes, AI did not use them. I hate your workslop."
The skepticism gets a research arm: she publishes a public **results-
benchmark-research** repository, systematically tracking how many
issues testers (professional and otherwise) actually find against a
fixed target, after concluding "seeing problems when they are there"
is a teachable skill taught badly — professional testers average
11.5–13.5 out of 72, and she suspects (without being told) that the
rare high scorer used AI. She pushes the practice further than a
benchmark: demoing "agentic exploratory testing" that collapses
tester/developer roles and reorders the task taxonomy, met with
pushback she calls "grief" ("What about Robot Framework," "Where is
Jira in all of this"). Economics get granular and specific rather than
argued in the abstract — 1,71€ in token cost for a task people expected
to cost thousands; 32 days of duration for 5 days of effort and 2€ in
tokens — read as evidence that AI's real effect on cost is uneven and
worth measuring per-task, not claiming wholesale. She names a clear
tool preference (Claude Code over GitHub Copilot, "the latter leaves me
more tired") and closes on a standing worry that outlives any one tool:
reviewing a colleague's AI-generated analysis that had quietly drifted
from the actual assignment, she names it "cognitive surrender," not a
one-off mistake.

Representative posts:
- https://mas.to/@maaretp/116364453608669116
- https://mas.to/@maaretp/116340210011510936
- https://mas.to/@maaretp/116617978876994928
- https://mas.to/@maaretp/117128207589281184
- https://mas.to/@maaretp/116478126379399577
