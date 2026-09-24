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

## 2020 Q3 — four core characteristics, "testing without testing," and a 1997 origin story — [[../batches/2020-q3|batch]]

A blog post crystallizes what had been scattered formulations (negative
space, TOAD, attended/unattended, builder mindset) into four named
**core characteristics**: "learning, agency, opportunity cost and
systems thinking. All these four lack in so much of the testing I work
to transform these days." Separately coins **"testing without
testing"** for a pattern she names across whole-team testing, tool
courses, and the tester role itself — practices and job titles that
invoke testing while doing little of the actual thinking — see
[[whole-team-testing]] for that thread. Traces her own origin story
further back than the 2019 Q4 historical research did: her first job in
Finland (1997, Microsoft) had a team lead assign her exploratory
testing and hand her Cem Kaner's *Testing Computer Software* to read,
in a country where "'formal' was never that big" compared to the US
community that organized around LAWST workshops. Also draws a clean
distinction between "testing the verb" (always exploratory) and
"testing the noun" (not necessarily) — resolving, for herself, a
long-running ambiguity in "all testing is exploratory" claims. The
credit dispute with [[../entities/james-bach|Bach]] over the term
itself reopens this quarter — see
[[cdt-community-culture]] for that account.

Representative posts:
- https://twitter.com/maaretp/status/1307607393904349184
- https://twitter.com/maaretp/status/1310204196881399809
- https://twitter.com/maaretp/status/1297588611316174853
- https://twitter.com/maaretp/status/1310302388901810180

## 2020 Q4 — the "automationist's gambit," and a year-end automation taxonomy — [[../batches/2020-q4|batch]]

The verb/noun distinction from Q3 gets applied one step further, to a
neighboring term: "agile testing" is a noun, not a verb — "people have
agile testing, they don't agile test" — sharpening the boundary between
her own always-verb framing of exploratory testing and the practices
around it. A borrowed metaphor from @cm_stead becomes a named personal
style: the **"automationist's gambit"**, exploratory testing that
attacks like a chess opening, requiring the system under test to
"defend properly" — she credits him directly and adopts it as a
recurring self-description. Two blog posts extend the four-
characteristics formulation: "What Exploratory Testing Is Depends on
Who You Are" and "The One Thing That Turns Testing to Exploratory."
Closes the year with a concrete taxonomy of what automation is *for*
within exploratory testing — documenting, extending reach, alerting to
attend, guiding to detail, fast-forwarding to a starting point,
repeating for beyond regression — the clearest operationalization yet
of "you can't automate well without exploring, you can't explore well
without automating."

Representative posts:
- https://twitter.com/maaretp/status/1317420609228443648
- https://twitter.com/maaretp/status/1326400838567407623
- https://twitter.com/maaretp/status/1329843041318952961
- https://twitter.com/maaretp/status/1330442880075386880
- https://twitter.com/maaretp/status/1344405987462144007

## 2021 Q1 — "Contemporary Exploratory Testing," a code/systems split, and "stealth" named — [[../batches/2021-q1|batch]]

Opens the year naming a new umbrella for the whole 2018–2020 writing
stretch: **Contemporary Exploratory Testing** — "the difference from
before, and the sameness" — becomes a blog series, an updated two-day
course, and eventually the quarter's closing keynote pitch. Sharpens the
verb/noun work from 2020 Q3–Q4 into a cleaner split: **"testing of code
we create"** (four benefits — spec, feedback, regression, granularity;
different in kind under TDD vs. test-after) versus **"testing of
systems the code ends up in"** (split further into building systems
that test systems, and testing those systems) — "it's not either or. It
is both. And the modern optimization problem... is that you no longer
can optimize one like testers used to." Names the management pattern
she's pushed against implicitly for years, this time directly: **ET as
"stealth"** — "one of the most common ways of managing
#ExploratoryTesting is 'stealth'. We hide it and focus on what the
organization expects... I'm seeking ways to stop hiding it." Closes the
quarter with a matching metaphor for how much ET a team actually needs:
**"sprinkle on top vs. sprinkle all around"** — sprinkle-on-top is fine
the way "everyone loves a good steak," but sprinkling it through the
whole process "turns a good team excellent," and the amount needed
scales inversely with how exploratory the rest of the testing already
is. Also crowdsources a list of **ET traps** with @g33klady (bugs,
premature algorithm development, extensive research, hacking inputs,
meetings) and, separately, trials a new self-description for the
tester-adjacent accelerator work she does — **"grounded management"** —
"working on what we create, hands-on, with end in mind while not
minding just my own business." Closes with a corrected career tally:
442 sessions, her 7th year keynoting, 21st year of public speaking.

Representative posts:
- https://twitter.com/maaretp/status/1345696528120360960
- https://twitter.com/maaretp/status/1355587375632707588
- https://twitter.com/maaretp/status/1364560200427012104
- https://twitter.com/maaretp/status/1365971076304543744
- https://twitter.com/maaretp/status/1374776976049893378
- https://twitter.com/maaretp/status/1375077344545796103
- https://twitter.com/maaretp/status/1372618193601228802
- https://twitter.com/maaretp/status/1371541084061437954

## 2022 Q1 — a 25-year milestone, a book rewrite, and RF leaves the course itself — [[../batches/2022-q1|batch]]

Marks 25 years in software testing with an unusually specific honesty
about the learning curve: "It took me 8 years of doing the work before
I started telling myself... that I can be good at it." Starts a
**complete 2022 rewrite** of her Exploratory Testing book, and updates
**Exploratory Testing Foundations to version 2.0**, replacing Robot
Framework with pytest — the 2021 Q4 removal wasn't just a personal
tooling choice, it reached her actual teaching materials. A new blog,
"In Search of a Contemporary Exploratory Tester," continues defining
the term named in 2021 Q1. She also notices convergent, independent
work: James Lyndsay's teaching material lands on very similar ground,
described appreciatively rather than as a priority dispute — a
different register than most of this page's attribution fights.

Representative posts:
- https://twitter.com/maaretp/status/1497637410020249607
- https://twitter.com/maaretp/status/1497638946662191105
- https://twitter.com/maaretp/status/1497939204701147143
- https://twitter.com/maaretp/status/1498398409874677760
- https://twitter.com/maaretp/status/1484631405284007938
- https://twitter.com/maaretp/status/1509190245039972353
