#!/usr/bin/env python3
"""Shared SVG primitive helpers for vannamei aquaculture illustrations.

These small builders centralise the SVG fragments that were previously
duplicated throughout the illustration scripts: text labels, arrow markers
and paths, titled info panels and gradient definitions. Colours are passed
in by the caller so the helpers stay independent of any specific palette.
"""


def svg_text(x, y, content, *, size, fill, anchor=None, weight=None,
             style=None, extra=None):
    """Return a single ``<text>`` element.

    Optional attributes are emitted only when provided, so plain, bold,
    italic and anchored labels can all be built from this one helper.
    """
    attrs = [f'x="{x}"', f'y="{y}"']
    if anchor:
        attrs.append(f'text-anchor="{anchor}"')
    attrs.append(f'font-size="{size}"')
    if weight:
        attrs.append(f'font-weight="{weight}"')
    if style:
        attrs.append(f'font-style="{style}"')
    attrs.append(f'fill="{fill}"')
    if extra:
        attrs.append(extra)
    return f'<text {" ".join(attrs)}>{content}</text>'


def arrow_marker(marker_id, color, width=8, height=6):
    """Return an SVG ``<marker>`` arrowhead of the given colour."""
    return (
        f'<marker id="{marker_id}" markerWidth="{width}" markerHeight="{height}" '
        f'refX="7" refY="3" orient="auto">\n'
        f'            <polygon points="0 0, 8 3, 0 6" fill="{color}"/>\n'
        f'        </marker>'
    )


def arrow_path(d, color, *, width=2, marker="arrowhead", dashed=False,
               opacity=None):
    """Return a ``<path>`` arrow with a marker end and optional styling."""
    attrs = [f'd="{d}"', 'fill="none"', f'stroke="{color}"',
             f'stroke-width="{width}"']
    if dashed:
        attrs.append('stroke-dasharray="4,2"')
    attrs.append(f'marker-end="url(#{marker})"')
    if opacity is not None:
        attrs.append(f'opacity="{opacity}"')
    return f'<path {" ".join(attrs)}/>'


def panel(x, y, width, height, title, *, title_fill, title_dy=18,
          fill="white", stroke="#BDC3C7", stroke_width=1, opacity=0.95,
          rx=8, title_size=9):
    """Return the rounded background rect + centred bold title of an info box.

    Callers add their own inner content and wrapping ``<g>`` element.
    """
    rect = (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="{rx}" ry="{rx}" fill="{fill}" stroke="{stroke}" '
        f'stroke-width="{stroke_width}" opacity="{opacity}"/>'
    )
    title_el = svg_text(x + width / 2, y + title_dy, title, size=title_size,
                        fill=title_fill, anchor="middle", weight="bold")
    return f'{rect}\n        {title_el}'


def gradient_stop(offset, color, opacity=1):
    """Return a gradient ``<stop>`` element."""
    return (f'<stop offset="{offset}" '
            f'style="stop-color:{color};stop-opacity:{opacity}"/>')


def linear_gradient(grad_id, stops, x1="0%", y1="0%", x2="0%", y2="100%"):
    """Return a ``<linearGradient>`` built from ``gradient_stop`` fragments."""
    inner = "\n        ".join(stops)
    return (
        f'<linearGradient id="{grad_id}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">\n'
        f'        {inner}\n'
        f'    </linearGradient>'
    )


def radial_gradient(grad_id, stops, cx="50%", cy="50%"):
    """Return a ``<radialGradient>`` built from ``gradient_stop`` fragments."""
    inner = "\n        ".join(stops)
    return (
        f'<radialGradient id="{grad_id}" cx="{cx}" cy="{cy}">\n'
        f'        {inner}\n'
        f'    </radialGradient>'
    )


def render_each(fn, items):
    """Apply ``fn`` to each tuple of positional args in ``items``.

    Replaces the repeated ``for args in positions: parts.append(fn(*args))``
    loop used when scattering elements across the scene.
    """
    return [fn(*item) for item in items]
