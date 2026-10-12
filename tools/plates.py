# -*- coding: utf-8 -*-
"""Line plates.

Three drawings, in the site's own palette, used as section illustrations.

They are line work only: strokes, arcs and small dots. No filled bars and no
panel frame, because the first version of this site carried a diagram built
from grey rectangles on a grey card and it read as a loading skeleton rather
than as artwork. Anything here that would look at home in a placeholder UI is
the wrong drawing.

Each plate is a plain <svg> with a viewBox and no width or height, so the
container sizes it. Colours are literal rather than currentColor: the plates
sit on three different grounds (white, mint, forest) and FOREST_* carries the
variant for the dark band.
"""

import math

INK = '#111111'
LINE = '#C2BFB6'
ACCENT = '#304A43'
ON_FOREST = 'rgba(255,255,255,0.30)'
ON_FOREST_STRONG = '#8FB3A5'


# Many sources drawn smoothly into one point, and a single line out of it.
# Diagnosis to implementation. The curves are cubics sharing an end point and
# an end tangent, so they nest instead of crossing: a fan, not a tangle.
CONVERGENCE = '''<svg class="plate" viewBox="0 0 480 300" fill="none" role="img"
     aria-label="Several lines drawn together into a single point and leaving as one">
  <g stroke="{line}" stroke-width="1.2" stroke-linecap="round">
    <path class="conv-draw" pathLength="1" style="--d:0s" d="M14 26C170 26 214 150 292 150"/>
    <path class="conv-draw" pathLength="1" style="--d:.12s" d="M14 88C170 88 224 150 292 150"/>
    <path class="conv-draw" pathLength="1" style="--d:.24s" d="M14 150h278"/>
    <path class="conv-draw" pathLength="1" style="--d:.36s" d="M14 212C170 212 224 150 292 150"/>
    <path class="conv-draw" pathLength="1" style="--d:.48s" d="M14 274C170 274 214 150 292 150"/>
  </g>

  <g fill="{line}" class="conv-fade" style="--d:.1s">
    <circle cx="14" cy="26" r="3"/>
    <circle cx="14" cy="88" r="3"/>
    <circle cx="14" cy="150" r="3"/>
    <circle cx="14" cy="212" r="3"/>
    <circle cx="14" cy="274" r="3"/>
  </g>

  <!-- the point where it is reconciled -->
  <circle class="conv-fade" style="--d:1s" cx="292" cy="150" r="22" stroke="{line}" stroke-width="1" stroke-dasharray="3 5"/>
  <circle class="conv-fade" style="--d:.9s" cx="292" cy="150" r="7" fill="{accent}"/>

  <!-- one answer out -->
  <path class="conv-draw" pathLength="1" style="--d:1.1s" d="M314 150h152" stroke="{accent}" stroke-width="2" stroke-linecap="round"/>
  <path class="conv-fade" style="--d:2s" d="M452 136l14 14-14 14" stroke="{accent}" stroke-width="2"
        stroke-linecap="round" stroke-linejoin="round"/>

  <!-- data flowing in, one dot per line, then one answer out -->
  <g class="flow-dots" fill="{accent}">
    <circle r="2.8" opacity="0"><animateMotion dur="3.4s" begin="2.2s" repeatCount="indefinite" path="M14 26C170 26 214 150 292 150"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="3.4s" begin="2.2s" repeatCount="indefinite"/></circle>
    <circle r="2.8" opacity="0"><animateMotion dur="3.4s" begin="2.8s" repeatCount="indefinite" path="M14 88C170 88 224 150 292 150"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="3.4s" begin="2.8s" repeatCount="indefinite"/></circle>
    <circle r="2.8" opacity="0"><animateMotion dur="3.4s" begin="3.4s" repeatCount="indefinite" path="M14 150h278"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="3.4s" begin="3.4s" repeatCount="indefinite"/></circle>
    <circle r="2.8" opacity="0"><animateMotion dur="3.4s" begin="4s" repeatCount="indefinite" path="M14 212C170 212 224 150 292 150"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="3.4s" begin="4s" repeatCount="indefinite"/></circle>
    <circle r="2.8" opacity="0"><animateMotion dur="3.4s" begin="4.6s" repeatCount="indefinite" path="M14 274C170 274 214 150 292 150"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="3.4s" begin="4.6s" repeatCount="indefinite"/></circle>
    <circle r="3.2" opacity="0"><animateMotion dur="2.4s" begin="3.6s" repeatCount="indefinite" path="M314 150h140"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.15;.8;1" dur="2.4s" begin="3.6s" repeatCount="indefinite"/></circle>
  </g>
</svg>'''.format(line=LINE, accent=ACCENT)


# Layers of a stack seen in oblique projection, one of them carrying the weight.
# Depth across the data estate rather than one tool.
STRATA = '''<svg class="plate" viewBox="0 0 480 320" fill="none" role="img"
     aria-label="Four stacked planes drawn in oblique projection, one picked out in green">
  <g stroke="{stroke}" stroke-width="1">
    <path d="M60 84l160-56 200 56-160 56z"/>
    <path d="M60 156l160-56 200 56-160 56z"/>
    <path d="M60 228l160-56 200 56-160 56z"/>
    <path d="M60 300l160-56 200 56-160 56z"/>
  </g>

  <!-- the layer that is actually being worked on -->
  <path d="M60 156l160-56 200 56-160 56z" stroke="{strong}" stroke-width="2"/>
  <g fill="{strong}">
    <circle cx="196" cy="140" r="3.5"/>
    <circle cx="252" cy="156" r="3.5"/>
    <circle cx="308" cy="140" r="3.5"/>
  </g>
  <g stroke="{strong}" stroke-width="1.2">
    <path d="M196 140l56 16 56-16"/>
  </g>

  <g stroke="{stroke}" stroke-width="1" stroke-dasharray="3 5">
    <path d="M220 28v216"/>
    <path d="M60 84v144"/>
    <path d="M420 84v144"/>
  </g>
</svg>'''


# A working group: several specialists, one senior lead, drawn around the
# problem rather than as a hierarchy.
CONSTELLATION = '''<svg class="plate" viewBox="0 0 480 340" fill="none" role="img"
     aria-label="A group of nodes connected around one larger node">
  <g stroke="{line}" stroke-width="1">
    <path d="M240 170L96 74M240 170l152-52M240 170L64 214M240 170l168 76M240 170l-96 122M240 170l104 108"/>
  </g>

  <g stroke="{line}" stroke-width="1" stroke-dasharray="4 6">
    <circle cx="240" cy="170" r="126"/>
  </g>

  <g fill="{white}" stroke="{ink}" stroke-width="1">
    <circle cx="96" cy="74" r="8"/>
    <circle cx="392" cy="118" r="8"/>
    <circle cx="64" cy="214" r="8"/>
    <circle cx="408" cy="246" r="8"/>
    <circle cx="144" cy="292" r="8"/>
    <circle cx="344" cy="278" r="8"/>
  </g>

  <circle cx="240" cy="170" r="26" fill="{accent}"/>
  <circle cx="240" cy="170" r="38" stroke="{accent}" stroke-width="1"/>
</svg>'''.format(line=LINE, ink=INK, accent=ACCENT, white='#FFFFFF')


def strata(on_forest=False):
    """The stack plate. On the dark band it needs its own two greens."""
    if on_forest:
        return STRATA.format(stroke=ON_FOREST, strong=ON_FOREST_STRONG)
    return STRATA.format(stroke=LINE, strong=ACCENT)


# A hub with arcs reaching out to a ring of nodes. A small team at the centre,
# a wider network around it.
NETWORK = '''<svg class="plate" viewBox="0 0 480 340" fill="none" role="img"
     aria-label="One central point connected by arcs to a wider network of nodes">
  <g stroke="{line}" stroke-width="1.2" stroke-linecap="round">
    <path class="conv-draw" pathLength="1" style="--d:0.50s" d="M150 170C190 90 250 56 330 52"/>
    <path class="conv-draw" pathLength="1" style="--d:0.70s" d="M150 170C210 140 300 120 420 122"/>
    <path class="conv-draw" pathLength="1" style="--d:0.90s" d="M150 170C230 180 320 206 432 226"/>
    <path class="conv-draw" pathLength="1" style="--d:1.10s" d="M150 170C190 250 250 284 330 292"/>
    <path class="conv-draw" pathLength="1" style="--d:1.30s" d="M150 170C100 130 70 90 46 56"/>
    <path class="conv-draw" pathLength="1" style="--d:1.50s" d="M150 170C96 214 64 262 44 294"/>
  </g>
  <circle class="conv-fade" style="--d:.1s" cx="150" cy="170" r="46" stroke="{line}" stroke-width="1" stroke-dasharray="3 5"/>
  <g fill="#FFFFFF" stroke="{ink}" stroke-width="1">
    <circle class="conv-fade" style="--d:1.60s" cx="330" cy="52" r="8"/>
    <circle class="conv-fade" style="--d:1.80s" cx="420" cy="122" r="8"/>
    <circle class="conv-fade" style="--d:2.00s" cx="432" cy="226" r="8"/>
    <circle class="conv-fade" style="--d:2.20s" cx="330" cy="292" r="8"/>
    <circle class="conv-fade" style="--d:2.40s" cx="46" cy="56" r="8"/>
    <circle class="conv-fade" style="--d:2.60s" cx="44" cy="294" r="8"/>
  </g>
  <circle class="conv-fade" style="--d:0s" cx="150" cy="170" r="20" fill="{accent}"/>

  <!-- the centre sends work out to each node in turn -->
  <g class="flow-dots" fill="{accent}">
    <circle r="2.8" opacity="0"><animateMotion dur="3.4s" begin="3.2s" repeatCount="indefinite" path="M150 170C190 90 250 56 330 52"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="3.4s" begin="3.2s" repeatCount="indefinite"/></circle>
    <circle r="2.8" opacity="0"><animateMotion dur="3.4s" begin="3.9s" repeatCount="indefinite" path="M150 170C210 140 300 120 420 122"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="3.4s" begin="3.9s" repeatCount="indefinite"/></circle>
    <circle r="2.8" opacity="0"><animateMotion dur="3.4s" begin="4.6s" repeatCount="indefinite" path="M150 170C230 180 320 206 432 226"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="3.4s" begin="4.6s" repeatCount="indefinite"/></circle>
    <circle r="2.8" opacity="0"><animateMotion dur="3.4s" begin="5.3s" repeatCount="indefinite" path="M150 170C190 250 250 284 330 292"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="3.4s" begin="5.3s" repeatCount="indefinite"/></circle>
    <circle r="2.8" opacity="0"><animateMotion dur="3.4s" begin="6.0s" repeatCount="indefinite" path="M150 170C100 130 70 90 46 56"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="3.4s" begin="6.0s" repeatCount="indefinite"/></circle>
    <circle r="2.8" opacity="0"><animateMotion dur="3.4s" begin="6.7s" repeatCount="indefinite" path="M150 170C96 214 64 262 44 294"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="3.4s" begin="6.7s" repeatCount="indefinite"/></circle>
  </g>
</svg>'''.format(line=LINE, ink=INK, accent=ACCENT)


def _icon(label, body):
    return ('<svg class="icon-plate" viewBox="0 0 64 64" fill="none" role="img" aria-label="%s"\n'
            '     stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
            % (label, body))


# Small marks for the three reasons to join. Ink line work, one accent detail.
ICON_PROBLEM = _icon('A database with a crack running through it', '''
  <ellipse cx="32" cy="14" rx="20" ry="7" stroke="{ink}"/>
  <path d="M12 14v36c0 3.9 9 7 20 7s20-3.1 20-7V14" stroke="{ink}"/>
  <path d="M12 32c0 3.9 9 7 20 7s20-3.1 20-7" stroke="{line}"/>
  <path d="M36 21l-6 8 8 4-6 10" stroke="{accent}" stroke-width="2"/>'''.format(line=LINE, ink=INK, accent=ACCENT))

ICON_GLOBAL = _icon('A globe', '''
  <circle cx="32" cy="32" r="24" stroke="{ink}"/>
  <ellipse cx="32" cy="32" rx="10" ry="24" stroke="{line}"/>
  <path d="M8 32h48M12 20h40M12 44h40" stroke="{line}"/>
  <circle cx="44" cy="22" r="3.5" fill="{accent}" stroke="none"/>'''.format(line=LINE, ink=INK, accent=ACCENT))

ICON_PAY = _icon('A banknote and a coin', '''
  <rect x="4" y="14" width="48" height="30" rx="3" stroke="{ink}"/>
  <circle cx="28" cy="29" r="8" stroke="{ink}"/>
  <path d="M10 20v.01M46 38v.01" stroke="{line}" stroke-width="3"/>
  <circle cx="48" cy="46" r="12" fill="#FFFFFF" stroke="{accent}" stroke-width="2"/>
  <path d="M48 40v12M52 43.5c-1-1.5-8-2-8 1.5s8 1.5 8 5-7 3-8 1.5" stroke="{accent}"/>'''.format(line=LINE, ink=INK, accent=ACCENT))


# Icons for the home page: the four areas of work, and the four steps.
def _i(label, body):
    return _icon(label, body.format(line=LINE, ink=INK, accent=ACCENT))


ICON_QUALITY = _i('A shield with a pulse line through it', '''
  <path d="M32 7l20 7v16c0 13-9 21-20 26C21 51 12 43 12 30V14z" stroke="{ink}"/>
  <path d="M20 32h8l3-8 5 15 3-7h5" stroke="{accent}" stroke-width="2"/>''')

ICON_AI = _i('A chip with an AI spark at its centre', '''
  <rect x="16" y="16" width="32" height="32" rx="4" stroke="{ink}"/>
  <path d="M24 8v8M32 8v8M40 8v8M24 48v8M32 48v8M40 48v8M8 24h8M8 32h8M8 40h8M48 24h8M48 32h8M48 40h8" stroke="{line}"/>
  <path d="M32 23l3 7 7 3-7 3-3 7-3-7-7-3 7-3z" stroke="{accent}" stroke-width="2"/>''')

ICON_MIGRATION = _i('Data moving from one system to another', '''
  <rect x="5" y="18" width="20" height="28" rx="3" stroke="{ink}"/>
  <path d="M9 26h12M9 32h12M9 38h12" stroke="{line}"/>
  <rect x="39" y="18" width="20" height="28" rx="3" stroke="{ink}"/>
  <path d="M43 26h12M43 32h12M43 38h12" stroke="{line}"/>
  <path d="M28 32h8M32 27l5 5-5 5" stroke="{accent}" stroke-width="2"/>''')

ICON_ANALYTICS = _i('A line chart ending in a decision point', '''
  <path d="M8 8v48h48" stroke="{line}"/>
  <path d="M14 44l12-12 10 8 14-18" stroke="{ink}"/>
  <circle cx="50" cy="22" r="5" stroke="{accent}" stroke-width="2"/>''')

ICON_TALK = _i('Two speech bubbles', '''
  <path d="M9 12h28a4 4 0 0 1 4 4v14a4 4 0 0 1-4 4H22l-8 7v-7H9a4 4 0 0 1-4-4V16a4 4 0 0 1 4-4z" stroke="{ink}"/>
  <path d="M46 24h8a4 4 0 0 1 4 4v14a4 4 0 0 1-4 4h-3v7l-8-7H30a4 4 0 0 1-4-4" stroke="{line}"/>
  <path d="M15 23h.01M23 23h.01M31 23h.01" stroke="{accent}" stroke-width="3"/>''')

ICON_DIAGNOSE = _i('A magnifying glass over a pulse line', '''
  <circle cx="27" cy="27" r="17" stroke="{ink}"/>
  <path d="M40 40l16 16" stroke="{ink}" stroke-width="2"/>
  <path d="M17 28h6l3-7 4 13 3-6h4" stroke="{accent}" stroke-width="2"/>''')

ICON_BUILD = _i('Stacked building blocks', '''
  <rect x="6" y="36" width="22" height="20" rx="2" stroke="{ink}"/>
  <rect x="34" y="36" width="22" height="20" rx="2" stroke="{ink}"/>
  <rect x="20" y="12" width="22" height="20" rx="2" stroke="{accent}" stroke-width="2"/>''')

ICON_IMPROVE = _i('Rising steps', '''
  <path d="M6 56h13V44h13V32h13" stroke="{ink}"/>
  <path d="M45 32V20h13" stroke="{accent}" stroke-width="2"/>''')


# About page: the three models, the four principles, and the five team areas.
ICON_BIGFIRM = _i('A large office building', '''
  <rect x="14" y="8" width="36" height="48" rx="2" stroke="{ink}"/>
  <path d="M22 18h6M36 18h6M22 28h6M36 28h6M22 38h6M36 38h6" stroke="{line}" stroke-width="2"/>
  <path d="M28 56V46h8v10" stroke="{accent}" stroke-width="2"/>''')

ICON_FREELANCE = _i('A single person on their own', '''
  <circle cx="32" cy="20" r="9" stroke="{ink}"/>
  <path d="M14 54c0-10 8-16 18-16s18 6 18 16" stroke="{ink}"/>
  <path d="M6 58h8M50 58h8" stroke="{line}" stroke-dasharray="2 4"/>
  <circle cx="32" cy="20" r="3" fill="{accent}" stroke="none"/>''')

ICON_SENIOR = _i('Two chevron stripes, like a military rank insignia', '''
  <path d="M10 30l22-18 22 18" stroke="{accent}" stroke-width="3"/>
  <path d="M10 46l22-18 22 18" stroke="{ink}" stroke-width="3"/>''')

ICON_EMBEDDED = _i('A member placed inside a team', '''
  <rect x="6" y="10" width="52" height="44" rx="5" stroke="{line}" stroke-dasharray="3 4"/>
  <circle cx="20" cy="26" r="4" stroke="{ink}"/>
  <circle cx="44" cy="26" r="4" stroke="{ink}"/>
  <circle cx="20" cy="42" r="4" stroke="{ink}"/>
  <circle cx="44" cy="42" r="4" fill="{accent}" stroke="none"/>
  <path d="M24 26h16M24 42h16M20 30v8M44 30v8" stroke="{line}"/>''')

ICON_RELIABLE = _i('A clock with a check mark: delivery you can count on', '''
  <circle cx="30" cy="32" r="22" stroke="{ink}"/>
  <path d="M30 18v14l9 6" stroke="{line}" stroke-width="2"/>
  <circle cx="50" cy="48" r="10" fill="#FFFFFF" stroke="{accent}" stroke-width="2"/>
  <path d="M45 48l4 4 7-8" stroke="{accent}" stroke-width="2"/>''')

ICON_ACCOUNT = _i('A target with an arrow in the centre', '''
  <circle cx="30" cy="34" r="22" stroke="{line}"/>
  <circle cx="30" cy="34" r="13" stroke="{ink}"/>
  <circle cx="30" cy="34" r="4" fill="{accent}" stroke="none"/>
  <path d="M34 30l18-18M44 12h8v8" stroke="{accent}" stroke-width="2"/>''')

ICON_T_PRODUCT = _i('A compass pointing to an outcome', '''
  <circle cx="32" cy="32" r="24" stroke="{ink}"/>
  <path d="M42 22L36 36 22 42l6-14z" stroke="{accent}" stroke-width="2"/>''')

ICON_T_ANALYTICS = _i('A bar chart', '''
  <path d="M8 56h48" stroke="{line}"/>
  <path d="M14 56V38M26 56V24M38 56V32M50 56V14" stroke="{ink}" stroke-width="3"/>
  <circle cx="50" cy="10" r="3" fill="{accent}" stroke="none"/>''')

ICON_T_ENGINEERING = _i('Three nodes joined by a pipeline', '''
  <circle cx="10" cy="32" r="5" stroke="{ink}"/>
  <circle cx="32" cy="14" r="5" stroke="{ink}"/>
  <circle cx="32" cy="50" r="5" stroke="{ink}"/>
  <circle cx="54" cy="32" r="5" stroke="{accent}" stroke-width="2"/>
  <path d="M15 30l13-12M15 34l13 12M36 18l14 11M36 46l14-11" stroke="{line}"/>''')

ICON_T_QUALITY = _i('A check mark in a circle', '''
  <circle cx="32" cy="32" r="24" stroke="{ink}"/>
  <path d="M20 33l8 8 16-18" stroke="{accent}" stroke-width="2"/>''')

ICON_T_MANAGEMENT = _i('A hierarchy of three boxes', '''
  <rect x="22" y="6" width="20" height="14" rx="2" stroke="{accent}" stroke-width="2"/>
  <rect x="6" y="42" width="20" height="14" rx="2" stroke="{ink}"/>
  <rect x="38" y="42" width="20" height="14" rx="2" stroke="{ink}"/>
  <path d="M32 20v12M16 42V32h32v10" stroke="{line}"/>''')

# The Semantic mark as an icon, for the highlighted card on the dark ground.
ICON_SEMANTIC_LIGHT = _icon('The Semantic mark', '''
  <circle cx="22" cy="32" r="17" fill="#8FB3A5" opacity="0.7" stroke="none"/>
  <circle cx="42" cy="32" r="17" fill="#FFFFFF" stroke="none"/>
  <circle cx="32" cy="32" r="7" fill="#1F332C" stroke="none"/>''')


# What We Do: one contact between the client and the specialists. A client on
# the left, Semantic in the middle, the specialists fanning out to the right.
# Drawn for the dark band only.
CONTACT_HUB = '''<svg class="plate" viewBox="0 0 480 320" fill="none" role="img"
     aria-label="A client connected through Semantic to several specialists">
  <rect x="10" y="118" width="84" height="84" rx="8" stroke="{strong}" stroke-width="1.6"/>
  <path d="M30 144h44M30 160h44M30 176h28" stroke="{stroke}" stroke-width="1.6" stroke-linecap="round"/>

  <path d="M94 160h92" stroke="{strong}" stroke-width="2.2" stroke-linecap="round"/>

  <circle cx="240" cy="160" r="54" stroke="{stroke}" stroke-width="1" stroke-dasharray="3 5"/>
  <circle cx="226" cy="160" r="28" fill="{strong}" opacity="0.7"/>
  <circle cx="254" cy="160" r="28" fill="#FFFFFF"/>
  <circle cx="240" cy="160" r="11" fill="#1F332C"/>

  <g stroke="{stroke}" stroke-width="1.4" stroke-linecap="round">
    <path d="M294 160C350 160 360 62 418 62"/>
    <path d="M294 160h124"/>
    <path d="M294 160C350 160 360 258 418 258"/>
  </g>
  <g fill="#1F332C" stroke="{strong}" stroke-width="2">
    <circle cx="430" cy="62" r="11"/>
    <circle cx="430" cy="160" r="11"/>
    <circle cx="430" cy="258" r="11"/>
  </g>
</svg>'''


def contact_hub():
    return CONTACT_HUB.format(stroke=ON_FOREST, strong=ON_FOREST_STRONG)


# Role icons for What We Do that the other pages do not already have.
ICON_T_ANALYTICS_ENG = _i('Stacked layers of a data model', '''
  <path d="M32 8l24 11-24 11L8 19z" stroke="{ink}"/>
  <path d="M8 31l24 11 24-11" stroke="{line}"/>
  <path d="M8 43l24 11 24-11" stroke="{accent}" stroke-width="2"/>''')

ICON_T_GOVERNANCE = _i('A document with a check mark', '''
  <path d="M14 6h26l12 12v40H14z" stroke="{ink}"/>
  <path d="M40 6v12h12" stroke="{line}"/>
  <path d="M22 38l7 7 13-14" stroke="{accent}" stroke-width="2"/>''')


# Our Expertise: four icons for the way we work, and an illustration of a few
# vetted specialists picked out of a pool, all reaching one contact.
ICON_W_VETTED = _i('A person with a check mark', '''
  <circle cx="26" cy="22" r="9" stroke="{ink}"/>
  <path d="M8 54c0-10 8-16 18-16 6 0 11 2 14 6" stroke="{ink}"/>
  <circle cx="46" cy="46" r="11" fill="#FFFFFF" stroke="{accent}" stroke-width="2"/>
  <path d="M41 46l4 4 7-8" stroke="{accent}" stroke-width="2"/>''')

ICON_W_MANAGED = _i('A clipboard with a progress line', '''
  <rect x="12" y="10" width="40" height="46" rx="4" stroke="{ink}"/>
  <path d="M24 10V6h16v4" stroke="{ink}"/>
  <path d="M20 26h24M20 36h16" stroke="{line}" stroke-width="2"/>
  <path d="M20 47l6-5 5 3 9-8" stroke="{accent}" stroke-width="2"/>''')

ICON_W_EMBEDDED = _i('A screen with a plug', '''
  <rect x="6" y="10" width="52" height="34" rx="4" stroke="{ink}"/>
  <path d="M24 54h16M32 44v10" stroke="{line}"/>
  <path d="M26 27h6M32 22v10M32 27h6" stroke="{accent}" stroke-width="2"/>''')

ICON_W_HANDOVER = _i('A baton passed from one box to another', '''
  <rect x="5" y="22" width="20" height="20" rx="3" stroke="{ink}"/>
  <rect x="39" y="22" width="20" height="20" rx="3" stroke="{line}"/>
  <path d="M27 32h10M33 27l5 5-5 5" stroke="{accent}" stroke-width="2"/>''')


def _person(x, y, color, width=1.6):
    return ('<circle cx="%d" cy="%d" r="9" stroke="%s" stroke-width="%s"/>'
            '<path d="M%d %d a16 16 0 0 1 32 0" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round"/>' % (x, y - 10, color, width, x - 16, y + 16, color, width))


def expertise_pool():
    """A grid of people, a few picked out, all connected to one contact."""
    xs, ys = (60, 140, 220, 300), (70, 160, 250)
    picked = {(300, 70), (220, 160), (300, 250)}
    people = []
    for y in ys:
        for x in xs:
            if (x, y) == (300, 160):
                continue  # a clear path for the middle line
            if (x, y) in picked:
                people.append('<circle cx="%d" cy="%d" r="30" stroke="%s" stroke-width="1.4" '
                              'stroke-dasharray="3 4"/>' % (x, y, ACCENT))
                people.append(_person(x, y, INK, 1.8))
            else:
                people.append(_person(x, y, LINE))
    lines = ''.join(
        '<path d="M%d %dC%d %d 360 160 396 160" stroke="%s" stroke-width="1.4" '
        'stroke-linecap="round"/>' % (x + 32, y, x + 90, y, ACCENT) for x, y in sorted(picked))
    return ('''<svg class="plate" viewBox="0 0 480 320" fill="none" role="img"
     aria-label="A few vetted specialists picked out of a larger pool, all connected to one contact">
  %s
  %s
  <rect x="396" y="132" width="70" height="56" rx="10" fill="%s"/>
  <path d="M412 150h38M412 160h38M412 170h22" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
</svg>''' % (''.join(people), lines, ACCENT))


def expertise_umbrella():
    """One contact, a canopy over three vetted specialists: we stand behind them."""
    people = ''
    for x in (130, 240, 350):
        people += _person(x, 236, INK, 1.8)
        people += ('<circle cx="%d" cy="%d" r="9" fill="#FFFFFF" stroke="%s" stroke-width="1.8"/>'
                   '<path d="M%d %dl3 3 5-6" stroke="%s" stroke-width="1.8" stroke-linecap="round" '
                   'stroke-linejoin="round"/>' % (x + 20, 228, ACCENT, x + 15, 228, ACCENT))
    return ('''<svg class="plate" viewBox="0 0 480 320" fill="none" role="img"
     aria-label="One contact standing over three vetted specialists like a canopy">
  <rect x="204" y="8" width="72" height="46" rx="9" stroke="%(ink)s" stroke-width="1.6"/>
  <path d="M220 24h40M220 34h40M220 44h24" stroke="%(line)s" stroke-width="1.6" stroke-linecap="round"/>
  <path d="M240 54v30" stroke="%(accent)s" stroke-width="2" stroke-linecap="round"/>

  <circle cx="226" cy="108" r="22" fill="%(accent)s" opacity="0.5"/>
  <circle cx="254" cy="108" r="22" fill="%(ink)s"/>
  <circle cx="240" cy="108" r="8" fill="#FFFFFF"/>

  <path d="M44 276C58 178 150 136 240 136s182 42 196 140" stroke="%(accent)s" stroke-width="2" stroke-linecap="round"/>
  <path d="M74 276C86 200 160 164 240 164s154 36 166 112" stroke="%(line)s" stroke-width="1.2" stroke-dasharray="3 5"/>
  <path d="M24 282h432" stroke="%(line)s" stroke-width="1.2" stroke-linecap="round"/>
  %(people)s
</svg>''' % {'ink': INK, 'line': LINE, 'accent': ACCENT, 'people': people})


def expertise_keystone():
    """A stone arch of five blocks. The keystone at the top carries the Semantic
    mark: the one piece that holds the rest together."""
    cx, cy, ro, ri, n, key = 240, 232, 132, 74, 5, 2
    delays = {0: 0, 4: 0, 1: .5, 3: .5, 2: 1.6}
    blocks = ''
    step = 180.0 / n
    for k in range(n):
        s, e = 180 + k * step, 180 + (k + 1) * step
        pts = []
        for r, a in ((ro, s), (ro, e), (ri, e), (ri, s)):
            pts.append((cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))))
        (x0, y0), (x1, y1), (x2, y2), (x3, y3) = pts
        is_key = (k == key)
        shape = ('<path d="M%.1f %.1fA%d %d 0 0 1 %.1f %.1fL%.1f %.1fA%d %d 0 0 0 %.1f %.1fz" '
                 'fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>'
                 % (x0, y0, ro, ro, x1, y1, x2, y2, ri, ri, x3, y3,
                    '#EDF2EE' if is_key else '#FFFFFF', ACCENT if is_key else INK,
                    '2.4' if is_key else '1.8'))
        if is_key:
            my = cy - (ro + ri) / 2
            shape += ('<circle cx="%.1f" cy="%.1f" r="14" fill="%s" opacity="0.5"/>'
                      '<circle cx="%.1f" cy="%.1f" r="14" fill="%s"/>'
                      '<circle cx="%d" cy="%.1f" r="5" fill="#FFFFFF"/>'
                      % (cx - 8.7, my, ACCENT, cx + 8.7, my, INK, cx, my))
        blocks += ('<g class="ks-block%s" style="--d:%ss">%s</g>'
                   % (' ks-key' if is_key else '', delays[k], shape))
    return ('''<svg class="plate" viewBox="0 0 480 320" fill="none" role="img"
     aria-label="A stone arch held together by its keystone, which carries the Semantic mark">
  %s
  <g class="conv-fade" style="--d:.1s">
  <path d="M%d %dV298M%d %dV298M%d %dV298M%d %dV298" stroke="%s" stroke-width="1.8"/>
  <path d="M60 298h360" stroke="%s" stroke-width="1.4" stroke-linecap="round"/>
  </g>
</svg>''' % (blocks, cx - ro, cy, cx - ri, cy, cx + ri, cy, cx + ro, cy, INK, LINE))
