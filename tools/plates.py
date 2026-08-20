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
