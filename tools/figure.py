# -*- coding: utf-8 -*-
"""Home-page diagram.

Carried over from the previous site's hero illustration and redrawn for the new
palette: raw sources on the left, checked against rules in the panel, resolving
into something a business can decide on. One row is flagged, because the point
of monitoring is that it catches things.
"""

HERO_FIGURE = '''<svg viewBox="0 0 520 400" fill="none" role="img"
             aria-label="Data from several sources checked against quality rules, resolving into a decision">
          <!-- sources -->
          <circle cx="26" cy="96" r="7" fill="#111111"/>
          <circle cx="26" cy="152" r="7" fill="none" stroke="#B9B6AE" stroke-width="1.4"/>
          <circle cx="26" cy="208" r="7" fill="none" stroke="#B9B6AE" stroke-width="1.4"/>
          <g stroke="#D3D0C8" stroke-width="1.2" stroke-linecap="round">
            <path d="M36 96h20c8 0 12 4 12 12v6"/>
            <path d="M36 152h32"/>
            <path d="M36 208h20c8 0 12-4 12-12v-6"/>
          </g>

          <!-- quality panel -->
          <rect x="70" y="42" width="380" height="218" rx="4" fill="#FFFFFF" stroke="#E4E2DC"/>
          <path d="M70 80h380" stroke="#E4E2DC"/>
          <rect x="90" y="57" width="96" height="7" rx="3.5" fill="#111111" opacity="0.75"/>
          <rect x="398" y="57" width="32" height="7" rx="3.5" fill="#E4E2DC"/>

          <!-- rows that pass -->
          <g>
            <rect x="90" y="102" width="176" height="8" rx="4" fill="#E4E2DC"/>
            <circle cx="414" cy="106" r="10" fill="#304A43" fill-opacity="0.1" stroke="#304A43" stroke-opacity="0.4"/>
            <path d="M409.5 106l3 3 5.6-6" stroke="#304A43" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          </g>
          <g>
            <rect x="90" y="140" width="224" height="8" rx="4" fill="#E4E2DC"/>
            <circle cx="414" cy="144" r="10" fill="#304A43" fill-opacity="0.1" stroke="#304A43" stroke-opacity="0.4"/>
            <path d="M409.5 144l3 3 5.6-6" stroke="#304A43" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          </g>

          <!-- the row monitoring caught -->
          <g>
            <rect x="90" y="178" width="138" height="8" rx="4" fill="#6F6F6A"/>
            <circle cx="414" cy="182" r="10" fill="none" stroke="#6F6F6A" stroke-opacity="0.6"/>
            <path d="M414 177.5v5.2" stroke="#6F6F6A" stroke-width="1.6" stroke-linecap="round"/>
            <circle cx="414" cy="186.6" r="1" fill="#6F6F6A"/>
          </g>

          <g>
            <rect x="90" y="216" width="198" height="8" rx="4" fill="#E4E2DC"/>
            <circle cx="414" cy="220" r="10" fill="#304A43" fill-opacity="0.1" stroke="#304A43" stroke-opacity="0.4"/>
            <path d="M409.5 220l3 3 5.6-6" stroke="#304A43" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          </g>

          <!-- flow into the decision -->
          <path d="M244 260v14c0 8 6 14 14 14h6" stroke="#D3D0C8" stroke-width="1.2" stroke-linecap="round"/>

          <!-- decision output -->
          <rect x="248" y="288" width="236" height="104" rx="4" fill="#FFFFFF" stroke="#E4E2DC"/>
          <g fill="#111111" opacity="0.12">
            <rect x="272" y="352" width="18" height="22" rx="2"/>
            <rect x="304" y="342" width="18" height="32" rx="2"/>
            <rect x="336" y="346" width="18" height="28" rx="2"/>
            <rect x="368" y="330" width="18" height="44" rx="2"/>
            <rect x="400" y="316" width="18" height="58" rx="2"/>
          </g>
          <path d="M281 348l32-12 32 6 32-20 32-14" stroke="#304A43" stroke-width="1.8"
                stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="409" cy="308" r="4" fill="#304A43"/>
          <rect x="272" y="306" width="64" height="7" rx="3.5" fill="#E4E2DC"/>
        </svg>'''
