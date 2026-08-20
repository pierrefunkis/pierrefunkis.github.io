# -*- coding: utf-8 -*-
"""Insights content.

Each entry is one article: slug, category, ISO date, display date, title,
excerpt and body. The body is plain HTML dropped inside .prose. Adding a piece
means adding a dict here and rebuilding; nothing else needs touching.
"""

ARTICLES = [
    {
        'slug': 'ai-readiness-is-a-data-problem',
        'category': 'AI Readiness',
        'iso': '2026-08-04',
        'date': '4 August 2026',
        'title': 'Most AI programmes stall on the data underneath them',
        'excerpt': 'The pilot works. The rollout does not. Almost always, the reason is '
                   'sitting in the data layer, and it was there long before anyone said '
                   'the word model.',
        'desc': 'Why enterprise AI initiatives stall in proof of concept, and the data '
                'groundwork that decides whether they ship.',
        'body': '''
        <p>There is a pattern that repeats across large organisations. A team builds a
          proof of concept, it works, everyone is encouraged, and then the thing never
          reaches production. Six months later the programme is quietly rescoped.</p>

        <p>The post-mortem usually blames the model, the vendor or the change management.
          In our experience the cause is almost always further down: the data the pilot
          ran on was hand-assembled, and nothing in the organisation can produce that
          same data reliably, at scale, on a schedule, with an owner attached to it.</p>

        <h2>A pilot hides the work a rollout exposes</h2>

        <p>A proof of concept is allowed to cheat. One analyst pulls an extract, cleans
          it in a notebook, resolves the ambiguities by asking a colleague which of the
          three customer tables is the real one, and gets on with the interesting part.
          None of that is wrong. It is the correct way to test whether an idea has legs.</p>

        <p>The problem is that the cheating is invisible in the result. What gets
          presented is the output, not the forty hours of quiet reconciliation that made
          the output possible. So the decision to scale is taken on the assumption that
          the hard part is done, when in fact the hard part has not started.</p>

        <blockquote>Every judgement call an analyst made by hand during the pilot becomes,
          at production scale, a rule someone has to own.</blockquote>

        <h2>What readiness actually means</h2>

        <p>Readiness is not a maturity score. It is a set of concrete, checkable
          conditions, and they are specific to the use case rather than to the company:</p>

        <ul>
          <li><strong>Definitions.</strong> The entities the use case depends on have one
            agreed definition, written down, that the people who will be held accountable
            for the output recognise as correct.</li>
          <li><strong>Lineage.</strong> You can trace any figure the system produces back
            to the systems it came from, without a person reconstructing it from memory.</li>
          <li><strong>Reproducibility.</strong> The dataset the pilot ran on can be
            regenerated on a schedule by a pipeline, not by an analyst.</li>
          <li><strong>Ownership.</strong> Someone is named, and knows they are named, for
            each input that matters.</li>
          <li><strong>Sensitivity.</strong> You know which fields carry personal or
            commercially sensitive data, and what that permits.</li>
        </ul>

        <p>None of these are exotic. What makes them hard is that they cut across teams,
          and they surface disagreements that the organisation has been comfortably
          avoiding. Two departments have been reporting different revenue figures for
          years and both have been fine with it, because neither number was ever put in
          front of a system that had to pick one.</p>

        <h2>The useful sequence</h2>

        <p>Start from a decision, not a capability. Pick the specific thing the AI is
          meant to change: which decision, made by whom, how often, and what it costs
          today when it goes wrong. That narrows the data in scope from everything the
          company holds to a list you can write on one page.</p>

        <p>Then assess that list against the five conditions above and be blunt about the
          result. It is far cheaper to say "this use case needs three months of
          groundwork first" than to discover the same thing after the vendor contract is
          signed.</p>

        <p>Then do the groundwork as a deliverable in its own right, with its own
          outcome. Not as a preamble buried inside the AI project, where it will be the
          first thing cut when the timeline slips.</p>

        <h2>Groundwork is not a tax</h2>

        <p>The reflex objection is that this delays the interesting work. It is worth
          noticing what the groundwork actually produces: agreed definitions, traceable
          numbers, reproducible pipelines and named owners. Those are the things every
          other data initiative in the organisation has also been quietly missing.</p>

        <p>The AI use case is a good forcing function, because it makes the absence
          impossible to ignore. But the value of fixing it does not belong to the AI
          programme alone, and it should not be accounted for as if it does.</p>
''',
    },

    {
        'slug': 'migrating-without-losing-trust',
        'category': 'Migration',
        'iso': '2026-06-26',
        'date': '26 June 2026',
        'title': 'Migrating a warehouse without losing trust in the numbers',
        'excerpt': 'Moving the data is the easy half. The half that decides whether the '
                   'migration is judged a success is proving the new numbers match the '
                   'old ones, to people who are accountable for them.',
        'desc': 'A practical approach to warehouse and legacy migrations: parallel '
                'running, reconciliation, and keeping the business confident in the '
                'figures throughout.',
        'body': '''
        <p>Migrations are usually planned as an engineering problem and judged as a trust
          problem. The plan covers extraction, modelling, orchestration and cutover. The
          verdict, months later, comes down to whether the finance director believes the
          number on the new dashboard.</p>

        <p>That gap is worth planning for explicitly, because the techniques that close it
          are not the same as the techniques that move the data.</p>

        <h2>Assume the old numbers are wrong too</h2>

        <p>The first uncomfortable discovery in most migrations is that the legacy system
          was not producing correct figures either. It was producing familiar ones. People
          had learned its quirks, applied mental corrections, and built a working
          relationship with a system they knew to be approximately right.</p>

        <p>So a reconciliation that finds a discrepancy is not automatically a defect in
          the new build. Sometimes it is the new platform being correct for the first
          time. Handling that well matters enormously: if every difference is treated as a
          migration bug, the team will spend months faithfully reproducing errors.</p>

        <blockquote>Reconcile to explain the difference, not to eliminate it. An
          unexplained match is worth less than an explained gap.</blockquote>

        <h2>Parallel running earns its cost</h2>

        <p>Running both platforms side by side for a period is expensive and almost always
          worth it. It converts an argument about trust into a set of observations. Each
          reporting cycle produces two answers, and each difference gets a written
          explanation: a known legacy defect, a definitional change agreed in advance, a
          timing difference, or a genuine bug to fix.</p>

        <p>Keep that log. By cutover it is the single most persuasive document in the
          programme, because it demonstrates that every difference was noticed and
          accounted for rather than smoothed over.</p>

        <h2>Decide what you are not migrating</h2>

        <p>Every legacy warehouse contains reports nobody reads and tables nobody owns.
          Migrating them is the default because deleting them requires a decision and a
          named person to make it.</p>

        <p>Take the decision early. Usage data tells you most of what you need, and a
          short round of conversations tells you the rest. Retiring a third of the estate
          before you start is the cheapest scope reduction available, and it will never be
          politically easier than at the beginning.</p>

        <h2>Cut over in pieces if you can</h2>

        <p>A single dated cutover concentrates all the risk into one weekend and gives the
          business one opportunity to lose confidence. Where the domains are separable,
          moving one at a time is slower on paper and considerably faster in practice,
          because each successful move buys credibility for the next.</p>

        <h2>Name who signs it off</h2>

        <p>Migrations drift when nobody is clear about who declares the new platform
          trustworthy. It should be the people who use the numbers to make decisions, not
          the team that built the pipelines. Agree at the start what evidence they will
          want, then produce exactly that evidence as you go.</p>

        <p>Done that way, the final sign-off is a formality rather than an event. Which is
          what a good migration should feel like from the business side: not a launch, but
          a gradual realisation that everyone has quietly stopped opening the old system.</p>
''',
    },

    {
        'slug': 'data-quality-is-an-operating-problem',
        'category': 'Data Quality',
        'iso': '2026-05-12',
        'date': '12 May 2026',
        'title': 'Data quality is an operating problem, not a tooling problem',
        'excerpt': 'Buying a monitoring tool is the easy decision. Deciding who gets woken '
                   'up when it fires, and what they are expected to do, is the one that '
                   'determines whether quality improves.',
        'desc': 'Why data quality initiatives stall after the tooling is bought, and what '
                'makes the difference: ownership, severity, and a response people follow.',
        'body': '''
        <p>Most organisations that have a data quality problem have already bought
          something to fix it. The tool is installed, tests exist, alerts fire. And the
          business still does not trust the numbers.</p>

        <p>That is not a failure of the tool. It is what happens when detection is
          installed without a response attached to it.</p>

        <h2>An alert nobody owns is noise</h2>

        <p>The first thing that happens after a monitoring rollout is a wave of alerts.
          Some are real, most are not tuned yet, and all of them land in a channel that
          belongs to everybody, which is to say nobody. Within a few weeks the channel is
          muted. The tests are still running, faithfully, into a room with no one in it.</p>

        <p>The fix is unglamorous and organisational: every check that matters gets a named
          owner, a severity, and an agreed expectation of what happens when it fires. That
          is more work than configuring the tool, and it is the work that actually
          changes outcomes.</p>

        <blockquote>If nobody would be woken up for it, it should not page anyone. If
          somebody should be, say who, in writing, before it fires.</blockquote>

        <h2>Not everything deserves the same standard</h2>

        <p>Teams often try to apply uniform quality rules across the whole estate, which
          guarantees either that the important tables are under-protected or that the
          unimportant ones generate most of the noise.</p>

        <p>A more workable approach is to tier explicitly. A small set of assets carry
          regulatory, financial or customer-facing consequences: those get tests, monitors,
          owners and a response expectation. A larger set support internal analysis: those
          get lightweight checks and no paging. The rest are exploratory and are labelled
          as such, so nobody builds a board report on them by accident.</p>

        <p>Making the tiering visible does something else useful. It converts a vague
          complaint that "the data is bad" into a specific question about which tier an
          asset is in and whether that is the right tier.</p>

        <h2>Measure the response, not the rules</h2>

        <p>Counting tests is a poor proxy for quality. A team can double its test count
          and change nothing about how quickly a broken pipeline gets fixed.</p>

        <p>More honest measures are operational: how long between a failure occurring and
          somebody noticing, how long between noticing and resolving, how often a
          consumer discovers a problem before the monitoring does. That last one is the
          most telling of all, because it measures the gap between what you are watching
          and what people actually depend on.</p>

        <h2>Start where the pain is</h2>

        <p>Broad quality programmes struggle to hold attention because their benefit is
          diffuse. Narrow ones succeed because they are legible: pick the report that
          causes the most arguments, make that one dependable end to end, and let the
          approach spread on its own evidence.</p>

        <p>It is slower to announce and considerably faster to achieve. And it produces the
          only thing that really matters here, which is a business that stops checking the
          numbers by hand because it no longer needs to.</p>
''',
    },
]
