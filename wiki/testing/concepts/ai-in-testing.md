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
