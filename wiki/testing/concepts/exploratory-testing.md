---
tags: [concept]
sources: [twitter]
---

# Exploratory Testing

## 2010 — [[../batches/2010|batch]]

The dominant theme of her earliest surviving tweets. She already practices
exploratory testing (ET) as her default mode, formed at a previous employer,
and spends 2010 trying to transplant it into a new, plan- and
document-driven sector — [[../entities/ilmarinen|Ilmarinen]], a pension
insurance company with data-intensive systems and heavy subcontractor
involvement, though she doesn't name the employer in the archive until 2012.

Recurring points:
- ET doesn't require a UI — colleagues assumed it did; she pushes back with
  examples from other interfaces.
- ET isn't "for the unprepared" — before a session she wants to already know
  the app: "ET should not be seen as way for the unprepared."
- Resistance is structural, not personal: "sector-wise not ready for
  exploratory testing. Will do in one company only."
- By August she's testing the limit-tests-in-progress idea (kanban-style
  constraint on test design) as a way to manage ET at scale rather than let
  ideas sprawl without completion.
- Year ends with a real foothold: first acceptance test completed in the new
  context after 16 months, and "some news of support for my traditional to
  exploratory -change."

Representative posts:
- https://twitter.com/maaretp/status/15654246393
- https://twitter.com/maaretp/status/22602415712
- https://twitter.com/maaretp/status/27853719558
- https://twitter.com/maaretp/status/20190136692113408

## 2011 — [[../batches/2011|batch]]

The ET throughline gets more sophisticated rather than louder. Key
developments:

- **Session-based vs. thread-based test management.** Picked up at
  [[cast-conference|CAST 2011]]: sessions are supposed to be uninterrupted,
  debriefable chunks; she dislikes the "30–90 minute rule," runs both
  shared (team) and private (tester-only) sessions, and debriefs shared
  ones as rarely as weekly. Threads stay open longer and can be interrupted
  — she describes herself as "in between" the two models.
- **What counts as ET, and whether low-quality ET is distinguishable from
  not-ET at all** — the center of the week-long debate with
  [[../entities/james-bach|Bach]], [[../entities/michael-bolton|Bolton]],
  and [[../entities/juha-itkonen|Itkonen]] over Itkonen's dissertation. Her
  landing point: "I care for better testing, ET or not" — more interested
  in testing quality than in defending the ET label itself.
- **Paired exploratory testing** as a new practice area — runs a workshop,
  finds she's "bad at pairing," ties successful pairing to matching
  technique/expectations to the information and collaboration goal.
- Explicitly disagrees with the idea that all testing is exploratory in a
  way that makes the label do useful work — pushes for more precise
  vocabulary throughout.

Representative posts:
- https://twitter.com/maaretp/status/101288461369217024
- https://twitter.com/maaretp/status/137983101946171392
- https://twitter.com/maaretp/status/138855497817264128

## 2012 — [[../batches/2012|batch]]

The scripted-vs-exploratory continuum stops working for her as a model:
"Scripted vs. exploratory continuum just doesn't clarify it for me. I
often create the script after I've explored. Hands-on with sw first." She
lands on a cleaner personal formulation — the type of testing she actually
does "isn't exploratory, just opposite to overplanned" — planning and
exploring aren't opposites, overplanning is the actual enemy. Practical
consequence at her new job: masquerades session-based test management as
"tool support" to get a script-averse contractor to accept it without a
terminology fight. Also sharpens an epistemic point: "you can only test
things you can imagine. Testing gets quick and easy when you lack
imagination" — imagination, not thoroughness, is the actual bottleneck on
testing quality.

Representative posts:
- https://twitter.com/maaretp/status/163280801507721217
- https://twitter.com/maaretp/status/164787038825086976
- https://twitter.com/maaretp/status/256837406609797121

## 2018 Q3 — a prolific writing stretch — [[../batches/2018-q3|batch]]

Close to a dozen blog posts in three months, each refining the concept
from a slightly different angle rather than repeating the same ground:
"Refining a 34 Year Old Practice," "There's Such a Thing as Low Quality
Exploratory Testing," "The Line Between Exploratory Testing and
Managing It," "Going Meta: Writing an Article about What is Exploratory
Testing," and "Three Kinds of Testing" among them. The
automation-vs-exploring debate that's run since 2016 sharpens into a
clean rejection of the dichotomy itself, in a sustained exchange with
@CuriousAgilist: "What separates those two now is a belief in
pre-made choice of opportunity cost" — automation code gets explored
just as much as an application does, "like an invitation to explore"
when a script fails unexpectedly. Also names a sharper distinction
between exploratory testing and *managing* it (sessions, scopes,
debriefs) — the label describes the thinking, not the management
layer wrapped around it.

Representative posts:
- https://twitter.com/maaretp/status/1022735208653758464
- https://twitter.com/maaretp/status/1024008013135458312
- https://twitter.com/maaretp/status/1024033765146992642
- https://twitter.com/maaretp/status/1038127527208923136
- https://twitter.com/maaretp/status/1019462639267786752

## 2019 Q2 — "35 next year," a coined umbrella term, and asserts reframed as exploration — [[../batches/2019-q2|batch]]

Two new formulations extend the 2018 Q3 writing stretch rather than
repeating it. First, a **negative-space model**: "when modeling for
#ExploratoryTesting we build shapes. Looking at those shapes from the
perspective of negative space is powerful. What is missing, if you turn
the model around just a little, do you see it?" — imagination-as-
bottleneck (2012) now has a concrete visualization technique attached.
Second, she coins **#toad — Testing, Observability and DevOps** — "for
y'all who think the testing we've been thinking of as testing isn't
testing... testing++" — a defensive umbrella term built specifically to
avoid restating the automation-vs-exploring argument yet again with
@DanAshby04 and @noahsussman (see
[[../concepts/cdt-community-culture]] for the harassment/community-
culture side of that same exchange). Within that exchange she also
sharpens the automation relationship past 2018 Q3's "rejection of the
dichotomy": "asserts are a tool for exploring... I use the word intent
rather than expectation when I do TDD. I formulate an intent but I'm
doing so to learn, not to document" — assertion as a magnifying glass,
not a checkpoint. Starts publicly preparing to mark **exploratory
testing turning 35** in 2020, treating the anniversary as a rediscovery
project (consistent with [[../entities/et19|ET19]]'s framing) rather
than a retrospective one.

Representative posts:
- https://twitter.com/maaretp/status/1136552124261765120
- https://twitter.com/maaretp/status/1143188129949597696
- https://twitter.com/maaretp/status/1143777939248623616
- https://twitter.com/maaretp/status/1143965910807564289
- https://twitter.com/maaretp/status/1144159044539752454

## 2019 Q4 — tracing the term back decades, a third pyramid dimension, and "continuous testing" — [[../batches/2019-q4|batch]]

The **#35YearsOfExploratoryTesting** project (announced 2019 Q2) becomes
genuine historical research rather than just a slogan: a public,
back-and-forth thread with Cem Kaner (@DrCemKaner) himself traces the
earliest documented uses of "exploratory testing" —
the term appears in a general psychology journal as early as 1940 (not
in a software context), then in Kaner's own *Testing Computer Software*
(1999 edition, though she owns and checks the 1990 edition too) and
Elfriede Dustin's 1999 writing on automated testing, converging on 1994
as the concept's likely software-testing origin per a 2006 talk. Closes
the research with a pointed, forward-looking line rather than a
nostalgia piece: "time to start making progress and stop clinging on
the past." Two new working models extend the
[[../batches/2019-q3|Q3]] attended/unattended vocabulary: a **third
pyramid dimension** — "the third side of the pyramid is attended vs.
unattended execution. Second side is exploratory testing (as in when
tests are created)" — turning what had been a simple triangle into a
3-axis model; and a preferred new term, **"continuous testing,"** for
testing that is truly ongoing and therefore must include automation as
a core part, not an add-on. A related identity shift, named directly
for the first time: "more and more of the testing I do comes from a
**builder mindset**. There is still use for the breaker/reporter
mindset, but my impact with that is better when it is built on a more
constructive foundation."

Representative posts:
- https://twitter.com/maaretp/status/1197891756098019334
- https://twitter.com/maaretp/status/1197917892584574979
- https://twitter.com/maaretp/status/1197930405464285184
- https://twitter.com/maaretp/status/1197962936616136706
- https://twitter.com/maaretp/status/1192542562999062528
- https://twitter.com/maaretp/status/1203639285309755392
- https://twitter.com/maaretp/status/1203709272615469061

## 2019 Q3 — "we have not retired it," ET19's second edition, and "attended/unattended" — [[../batches/2019-q3|batch]]

The Ashby/Sussman deprecation fight from 2019 Q2 gets a public, settled
rebuttal rather than more debate: "Service announcement. We have not
retired #ExploratoryTesting. We are rediscovering it." The 35th-
anniversary rediscovery project announced in Q2 gets its concrete
second event: **[[../entities/et19|ET19]]'s second edition runs 16
August at CAST19** (Cocoa Beach, FL) — resolving the open thread from
both 2019 Q1 and Q2 batches about whether the August sequel would
actually happen. A genuinely new vocabulary proposal emerges from a
sustained thread: replacing "manual vs. automated" with **"attended vs.
unattended"** — "the dichotomy is not exploratory testing / test
automation - I explore with automation... attended/unattended would
capture the intent better." Extends the frame concretely to her own
numbers: "the testing that happens unattended isn't exploratory. It
turns again exploratory when we need to analyze problems. 50% of our
testing is unattended. The other half is exploratory" — a cleaner
successor to 2018 Q3's "automation gets explored too" argument, with a
name for the axis that was previously unnamed.

Representative posts:
- https://twitter.com/maaretp/status/1156646250906902528
- https://twitter.com/maaretp/status/1162332295237447686
- https://twitter.com/maaretp/status/1171313808004063232
- https://twitter.com/maaretp/status/1171320928774578177
- https://twitter.com/maaretp/status/1172046256488816640
