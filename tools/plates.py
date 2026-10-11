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
    <path d="M14 26C170 26 214 150 292 150"/>
    <path d="M14 88C170 88 224 150 292 150"/>
    <path d="M14 212C170 212 224 150 292 150"/>
    <path d="M14 274C170 274 214 150 292 150"/>
  </g>
  <path d="M14 150h278" stroke="{line}" stroke-width="1.2" stroke-linecap="round"/>

  <g fill="{line}">
    <circle cx="14" cy="26" r="3"/>
    <circle cx="14" cy="88" r="3"/>
    <circle cx="14" cy="150" r="3"/>
    <circle cx="14" cy="212" r="3"/>
    <circle cx="14" cy="274" r="3"/>
  </g>

  <!-- the point where it is reconciled -->
  <circle cx="292" cy="150" r="22" stroke="{line}" stroke-width="1" stroke-dasharray="3 5"/>
  <circle cx="292" cy="150" r="7" fill="{accent}"/>

  <!-- one answer out -->
  <path d="M314 150h152" stroke="{accent}" stroke-width="2" stroke-linecap="round"/>
  <path d="M452 136l14 14-14 14" stroke="{accent}" stroke-width="2"
        stroke-linecap="round" stroke-linejoin="round"/>
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
    <path d="M150 170C190 90 250 56 330 52"/>
    <path d="M150 170C210 140 300 120 420 122"/>
    <path d="M150 170C230 180 320 206 432 226"/>
    <path d="M150 170C190 250 250 284 330 292"/>
    <path d="M150 170C100 130 70 90 46 56"/>
    <path d="M150 170C96 214 64 262 44 294"/>
  </g>
  <circle cx="150" cy="170" r="46" stroke="{line}" stroke-width="1" stroke-dasharray="3 5"/>
  <g fill="#FFFFFF" stroke="{ink}" stroke-width="1">
    <circle cx="330" cy="52" r="8"/>
    <circle cx="420" cy="122" r="8"/>
    <circle cx="432" cy="226" r="8"/>
    <circle cx="330" cy="292" r="8"/>
    <circle cx="46" cy="56" r="8"/>
    <circle cx="44" cy="294" r="8"/>
  </g>
  <circle cx="150" cy="170" r="20" fill="{accent}"/>
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

ICON_IMPROVE = _i('Rising steps with an upward arrow', '''
  <path d="M6 56h13V44h13V32h13V20h13" stroke="{ink}"/>
  <path d="M40 8h16v16M56 8L36 28" stroke="{accent}" stroke-width="2"/>''')


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

ICON_SENIOR = _i('A person with a star above', '''
  <circle cx="32" cy="30" r="8" stroke="{ink}"/>
  <path d="M16 56c0-9 7-14 16-14s16 5 16 14" stroke="{ink}"/>
  <path d="M32 6l2.6 5.4 5.9.8-4.3 4.1 1 5.9L32 19.5 26.8 22.2l1-5.9-4.3-4.1 5.9-.8z" stroke="{accent}" stroke-width="2"/>''')

ICON_EMBEDDED = _i('Two pieces fitting together', '''
  <rect x="6" y="18" width="28" height="28" rx="3" stroke="{ink}"/>
  <path d="M34 26h8a6 6 0 1 1 0 12h-8" stroke="{accent}" stroke-width="2"/>
  <rect x="42" y="18" width="16" height="28" rx="3" stroke="{line}"/>''')

ICON_HONEST = _i('A speech bubble with a check mark', '''
  <path d="M10 10h44a4 4 0 0 1 4 4v28a4 4 0 0 1-4 4H30l-12 10V46h-8a4 4 0 0 1-4-4V14a4 4 0 0 1 4-4z" stroke="{ink}"/>
  <path d="M22 28l7 7 13-14" stroke="{accent}" stroke-width="2"/>''')

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
