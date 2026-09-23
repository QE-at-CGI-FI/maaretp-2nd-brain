---
tags: [concept]
sources: [twitter]
---

# Documentation Skepticism

## 2010 — [[../batches/2010|batch]]

A steady thread of frustration with testing documentation treated as a
deliverable to be produced and graded, rather than a tool that earns its
keep.

- "My dislike of documentation has grown in the last year."
- "Amazing how much people are willing to pay for useless documentation."
- Gets an accepted test plan she considers "correct but useless" and asks
  her project manager if she can rewrite it — "feels great to throw that
  out."
- Notices the same pattern from the other side: a project manager tells her
  "planning their acceptance testing has been the most difficult project
  plan he has ever done" — the documentation burden isn't just her
  complaint, it's structural to the sector.
- Distinguishes wanting test data over test cases: "all I need is the test
  data" / designs start from test data first, requirements second, in one
  approach comparison.
- Not anti-documentation in general — explicitly wants *useful*
  documentation, objects to documentation whose purpose is blame/cost
  tracking: "Useful would be nice, blame / cost focusing is not."

Ties directly into [[exploratory-testing]] — the resistance she meets
pushing ET is largely a resistance to *not* producing this kind of
documentation.

Representative posts:
- https://twitter.com/maaretp/status/17561714940
- https://twitter.com/maaretp/status/19754544316
- https://twitter.com/maaretp/status/22289840564
- https://twitter.com/maaretp/status/29010722025

## 2011 — [[../batches/2011|batch]]

Sharpens into a practice, not just a complaint: her test plans are now
deliberately ~2 pages, formatted "so that I can easily drop + add," and
explicitly "never complete." Plans as effort/investment statements (how
much, why, what, how, who) rather than as specifications to be graded for
completeness. Documented a case where she wrote 4 test cases against an
expectation of 200 and pushed back rather than pad the document.

Representative posts:
- https://twitter.com/maaretp/status/145193698542628864
- https://twitter.com/maaretp/status/145526039743967232
- https://twitter.com/maaretp/status/43037719462555648

## 2012 — [[../batches/2012|batch]]

Produces the clearest demonstration yet, twice: transforms a 47-page
document to 2 pages "without losing any information," and separately turns
39 pages / 46 copy-pasted test cases into a one-page mindmap covering 88
things to test — finding the original document was still missing 3 things
the mindmap caught from the UI directly. Names the failure mode precisely:
"Longest test specification seemed to correlate with most bugs missed."
Also calls out a specific piece of theater: a test plan "deemed
'professional'" specifically *because* it was inaccessible — "all you need
is text that others don't get. False security."

Representative posts:
- https://twitter.com/maaretp/status/189933179862384641
- https://twitter.com/maaretp/status/189976820349808641
- https://twitter.com/maaretp/status/265443617383006208

## 2014 — reversal on mindmaps — [[../batches/2014|batch]]

A genuine self-correction: the tool she championed in 2012 (39 pages → a
one-page mindmap) she now actively dislikes as a default: "I'm starting
to seriously dislike mindmaps as test documentation. It gives me a feel
of 'unable to write to audience' when all is mindmaps." Specific
complaints — they don't work as a checklist, they describe shallow
concepts instead of insights, and they don't update their structure as
the underlying document grows. The underlying value hasn't changed
(match the document to the reader and the moment of use) — what changed
is that mindmaps stopped serving that value once they became her only
format by default.

Representative posts:
- https://twitter.com/maaretp/status/465027187075448832
- https://twitter.com/maaretp/status/465140348881481728
- https://twitter.com/maaretp/status/465172934525718528

## 2019 Q1 — a costed comparison, and a Jira/PR ratio — [[../batches/2019-q1|batch]]

Two concrete data points, sharper than the usual anecdote-level argument:
"Two comparable projects in one organization where one believed in trust
and discovery and other in detailing specs. Both succeeded. The latter
cost 3M where the first was 1M. I lead testing in both" — a direct cost
comparison she can point to, not just a preference. And, on ticket
volume: "we had 500 of those [Jira tickets] pass through us last year...
10 [pull requests] for every ticket. If every Jira ticket is a minute,
that we saved a week of work" — reframing low ticket usage as a
measurable saving rather than a missing-documentation risk. The
underlying position is unchanged from 2010–2014 (documentation as tool,
not deliverable) — what's new is being able to attach numbers to it.

Representative posts:
- https://twitter.com/maaretp/status/1083644243363708928
- https://twitter.com/maaretp/status/1087286172341153792
- https://twitter.com/maaretp/status/1083368325562941440

## 2019 Q2 — Jira as "a bad proxy for quality" — [[../batches/2019-q2|batch]]

The 2019 Q1 ticket/PR ratio argument sharpens into a direct verdict:
"Four days ago our test automation alerted us on a problem. Jira case
got created. And today, it blocked our release. Lesson? Stop with the
Jira cases, they are a bad proxy for quality." A three-year practice of
skipping tickets for casual, direct bug mentions has "improved" fix
rates and "removed the pushback that was strong at first" — the earlier
numeric argument (2019 Q1) now backed by a multi-year track record
rather than a single comparison. Names a specific anti-pattern of the
tool used defensively rather than communicatively: "Jira ping pong where
you keep your list clean by having it all on other people's queues."

Representative posts:
- https://twitter.com/maaretp/status/1143475636423593986
- https://twitter.com/maaretp/status/1143763278671355905
- https://twitter.com/maaretp/status/1125785512663556096
