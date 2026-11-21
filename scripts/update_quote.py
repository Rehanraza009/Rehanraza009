#!/usr/bin/env python3
"""Generate a GitHub-profile footer quote banner.

The quote changes every six-hour UTC slot. GitHub Actions commits the
updated SVG so the profile README always displays the latest generated quote.
"""
from datetime import datetime, timezone
from html import escape
from pathlib import Path

QUOTES = [
    ("Build with curiosity. Learn without limits.", "LEARN • BUILD • GROW"),
    ("Great ideas become real through consistent work.", "THINK • CREATE • SHIP"),
    ("Turn data into insight, and insight into impact.", "DATA • INSIGHT • IMPACT"),
    ("Every bug is a lesson. Every project is progress.", "DEBUG • IMPROVE • REPEAT"),
    ("Stay curious. Keep experimenting. Make things better.", "EXPLORE • EXPERIMENT • EVOLVE"),
    ("Small steps, strong skills, meaningful results.", "PRACTICE • PROGRESS • DELIVER"),
    ("Code with purpose. Solve problems that matter.", "CODE • SOLVE • CONTRIBUTE"),
    ("The best way to learn is to build.", "LEARN BY BUILDING"),
    ("Think clearly. Build thoughtfully. Improve continuously.", "THINK • BUILD • REFINE"),
    ("Use technology to turn possibilities into solutions.", "IMAGINE • ENGINEER • IMPACT"),
    ("Consistency turns learning into capability.", "SHOW UP • LEARN • GROW"),
    ("Make every experiment a step toward something useful.", "TEST • DISCOVER • CREATE"),
]

# Stable within each six-hour period; rotates automatically over time.
slot = int(datetime.now(timezone.utc).timestamp() // (6 * 60 * 60))
quote, label = QUOTES[slot % len(QUOTES)]

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="190" viewBox="0 0 1200 190" role="img" aria-label="{escape(quote, quote=True)}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#071810"/>
      <stop offset="0.55" stop-color="#064E3B"/>
      <stop offset="1" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#34D399" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#6EE7B7" stop-opacity=".8"/>
      <stop offset="1" stop-color="#34D399" stop-opacity="0"/>
    </linearGradient>
    <filter id="soft"><feGaussianBlur stdDeviation="18"/></filter>
  </defs>
  <rect width="1200" height="190" rx="22" fill="url(#bg)"/>
  <ellipse cx="920" cy="25" rx="300" ry="95" fill="#10B981" opacity=".18" filter="url(#soft)"/>
  <path d="M0 126 C180 70 330 170 520 124 S850 50 1200 112" fill="none" stroke="#6EE7B7" stroke-opacity=".35" stroke-width="2"/>
  <path d="M0 145 C210 95 350 190 570 145 S900 75 1200 132" fill="none" stroke="#FBBF24" stroke-opacity=".28" stroke-width="1.5"/>
  <rect x="90" y="34" width="4" height="122" rx="2" fill="#6EE7B7"/>
  <text x="125" y="68" fill="#A7F3D0" font-family="Segoe UI, Arial, sans-serif" font-size="15" font-weight="700" letter-spacing="4">{escape(label)}</text>
  <text x="125" y="112" fill="#F0FDF4" font-family="Segoe UI, Arial, sans-serif" font-size="30" font-weight="700">{escape(quote)}</text>
  <text x="125" y="145" fill="#D1FAE5" fill-opacity=".78" font-family="Segoe UI, Arial, sans-serif" font-size="13" letter-spacing="2">A NOTE TO KEEP MOVING FORWARD</text>
  <rect x="90" y="173" width="1020" height="2" rx="1" fill="url(#glow)"/>
</svg>
'''

out = Path("assets/rotating-quote.svg")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(svg, encoding="utf-8")
print(f"Updated {out}: {quote}")
