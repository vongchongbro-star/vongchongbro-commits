#!/usr/bin/env python3
"""
Biofloc Technology for Vannamei Shrimp (Litopenaeus vannamei)
Professional Scientific Illustration - BioRender Style
For thesis/article submission

Generates a high-quality SVG illustration showing the biofloc system
with key components: shrimp, biofloc particles, bacteria, microalgae,
nitrogen cycle, and tank system.

Author: Generated with Kiro AI
"""

import math
import os

from svg_utils import (
    arrow_marker,
    arrow_path,
    gradient_stop,
    linear_gradient,
    panel,
    radial_gradient,
    render_each,
    svg_text,
)

# ============================================================
# COLOR PALETTE - BioRender/Adobe Illustrator Professional Style
# ============================================================
COLORS = {
    'bg': '#FFFFFF',
    'tank_fill': '#E8F4FD',
    'tank_stroke': '#2C3E50',
    'water': '#B3E0F2',
    'water_deep': '#7FCDEE',
    'biofloc_1': '#8B6914',
    'biofloc_2': '#A0522D',
    'biofloc_3': '#6B4226',
    'bacteria_1': '#27AE60',
    'bacteria_2': '#2ECC71',
    'bacteria_3': '#1ABC9C',
    'microalgae': '#16A085',
    'algae_dark': '#0E6655',
    'shrimp_body': '#F5B7B1',
    'shrimp_dark': '#E74C3C',
    'shrimp_light': '#FADBD8',
    'nitrogen_arrow': '#3498DB',
    'ammonia': '#E74C3C',
    'nitrite': '#F39C12',
    'nitrate': '#27AE60',
    'carbon': '#8E44AD',
    'oxygen': '#3498DB',
    'label_text': '#2C3E50',
    'title_text': '#1A252F',
    'arrow_flow': '#5DADE2',
    'aeration': '#AED6F1',
    'substrate': '#D4AC6E',
}


def svg_header(width, height):
    gradients = "\n    ".join([
        linear_gradient("waterGrad", [
            gradient_stop("0%", COLORS['water'], 0.6),
            gradient_stop("100%", COLORS['water_deep'], 0.9),
        ]),
        linear_gradient("tankGrad", [
            gradient_stop("0%", "#34495E", 1),
            gradient_stop("100%", "#2C3E50", 1),
        ], x2="100%", y2="100%"),
        radial_gradient("bioflocGrad1", [
            gradient_stop("0%", "#C49A3C", 0.9),
            gradient_stop("100%", COLORS['biofloc_1'], 1),
        ], cx="40%", cy="40%"),
        radial_gradient("bioflocGrad2", [
            gradient_stop("0%", "#C0785A", 0.9),
            gradient_stop("100%", COLORS['biofloc_2'], 1),
        ], cx="40%", cy="40%"),
        radial_gradient("bacteriaGrad", [
            gradient_stop("0%", "#58D68D", 0.9),
            gradient_stop("100%", COLORS['bacteria_1'], 1),
        ], cx="40%", cy="40%"),
        radial_gradient("shrimpGrad", [
            gradient_stop("0%", COLORS['shrimp_light'], 1),
            gradient_stop("60%", COLORS['shrimp_body'], 1),
            gradient_stop("100%", COLORS['shrimp_dark'], 0.8),
        ], cx="50%", cy="30%"),
    ])
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {width} {height}" 
     width="{width}" height="{height}"
     style="font-family: 'Helvetica Neue', Arial, sans-serif;">
<defs>
    <!-- Gradients -->
    {gradients}
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
        <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.15"/>
    </filter>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
        <feMerge>
            <feMergeNode in="coloredBlur"/>
            <feMergeNode in="SourceGraphic"/>
        </feMerge>
    </filter>
    <!-- Bubble pattern -->
    <pattern id="bubblePattern" x="0" y="0" width="60" height="60" patternUnits="userSpaceOnUse">
        <circle cx="10" cy="10" r="2" fill="{COLORS['aeration']}" opacity="0.3"/>
        <circle cx="40" cy="25" r="1.5" fill="{COLORS['aeration']}" opacity="0.2"/>
        <circle cx="25" cy="45" r="2.5" fill="{COLORS['aeration']}" opacity="0.25"/>
    </pattern>
</defs>
'''


def svg_footer():
    return '</svg>'



def draw_tank(cx, cy, width, height):
    """Draw the biofloc tank with rounded bottom"""
    rx = width / 2
    ry = height / 2
    # Tank body (rounded rectangle)
    tank = f'''
    <!-- BIOFLOC TANK -->
    <g filter="url(#shadow)">
        <rect x="{cx - rx}" y="{cy - ry}" width="{width}" height="{height}" 
              rx="20" ry="20" fill="url(#waterGrad)" stroke="{COLORS['tank_stroke']}" 
              stroke-width="4"/>
        <!-- Water surface line -->
        <path d="M {cx - rx + 20} {cy - ry + 40} 
                 Q {cx - rx + rx/2} {cy - ry + 35}, {cx} {cy - ry + 40}
                 Q {cx + rx/2} {cy - ry + 45}, {cx + rx - 20} {cy - ry + 40}" 
              fill="none" stroke="{COLORS['water']}" stroke-width="2" opacity="0.7"/>
        <!-- Bubble overlay -->
        <rect x="{cx - rx + 4}" y="{cy - ry + 40}" width="{width - 8}" height="{height - 60}" 
              rx="16" ry="16" fill="url(#bubblePattern)" opacity="0.5"/>
    </g>
    '''
    return tank


def draw_shrimp(x, y, scale=1.0, flip=False):
    """Draw a Vannamei shrimp (Litopenaeus vannamei) - detailed illustration"""
    direction = -1 if flip else 1
    s = scale
    # Shrimp body path
    shrimp = f'''
    <!-- VANNAMEI SHRIMP -->
    <g transform="translate({x},{y}) scale({s * direction},{s})">
        <!-- Body segments -->
        <path d="M 0,0 C 10,-8 30,-12 50,-10 C 70,-8 85,-4 95,0 
                 C 85,4 70,8 50,10 C 30,12 10,8 0,0 Z" 
              fill="url(#shrimpGrad)" stroke="{COLORS['shrimp_dark']}" stroke-width="0.8"/>
        <!-- Tail fan -->
        <path d="M 95,0 C 100,-6 110,-8 115,-5 C 112,-2 112,2 115,5 C 110,8 100,6 95,0 Z" 
              fill="{COLORS['shrimp_body']}" stroke="{COLORS['shrimp_dark']}" stroke-width="0.5" opacity="0.9"/>
        <path d="M 100,0 L 118,-7 L 116,-3 Z" fill="{COLORS['shrimp_light']}" opacity="0.6"/>
        <path d="M 100,0 L 118,7 L 116,3 Z" fill="{COLORS['shrimp_light']}" opacity="0.6"/>
        <!-- Segments lines -->
        <path d="M 30,-9 C 32,-2 32,2 30,9" fill="none" stroke="{COLORS['shrimp_dark']}" stroke-width="0.4" opacity="0.5"/>
        <path d="M 42,-10 C 44,-2 44,2 42,10" fill="none" stroke="{COLORS['shrimp_dark']}" stroke-width="0.4" opacity="0.5"/>
        <path d="M 54,-9.5 C 56,-2 56,2 54,9.5" fill="none" stroke="{COLORS['shrimp_dark']}" stroke-width="0.4" opacity="0.5"/>
        <path d="M 66,-8 C 68,-2 68,2 66,8" fill="none" stroke="{COLORS['shrimp_dark']}" stroke-width="0.4" opacity="0.5"/>
        <path d="M 78,-6 C 80,-2 80,2 78,6" fill="none" stroke="{COLORS['shrimp_dark']}" stroke-width="0.4" opacity="0.5"/>
        <!-- Rostrum (head spike) -->
        <path d="M 0,0 L -20,-3 L -18,0 Z" fill="{COLORS['shrimp_dark']}" opacity="0.8"/>
        <!-- Antennae -->
        <path d="M -5,-4 C -25,-20 -40,-25 -55,-22" fill="none" 
              stroke="{COLORS['shrimp_dark']}" stroke-width="0.7" opacity="0.7"/>
        <path d="M -5,-2 C -30,-15 -50,-12 -60,-8" fill="none" 
              stroke="{COLORS['shrimp_dark']}" stroke-width="0.5" opacity="0.6"/>
        <!-- Eye -->
        <circle cx="-5" cy="-5" r="2.5" fill="#1A1A1A"/>
        <circle cx="-5.5" cy="-5.5" r="1" fill="#FFFFFF" opacity="0.6"/>
        <!-- Legs (pleopods) -->
        <path d="M 25,10 L 22,18" stroke="{COLORS['shrimp_dark']}" stroke-width="0.5" opacity="0.6"/>
        <path d="M 35,10 L 33,19" stroke="{COLORS['shrimp_dark']}" stroke-width="0.5" opacity="0.6"/>
        <path d="M 45,10 L 43,18" stroke="{COLORS['shrimp_dark']}" stroke-width="0.5" opacity="0.6"/>
        <path d="M 55,9 L 54,17" stroke="{COLORS['shrimp_dark']}" stroke-width="0.5" opacity="0.6"/>
        <path d="M 65,8 L 64,15" stroke="{COLORS['shrimp_dark']}" stroke-width="0.5" opacity="0.6"/>
    </g>
    '''
    return shrimp


def draw_biofloc_particle(x, y, size, variant=0):
    """Draw irregular biofloc aggregate particle"""
    colors = ['url(#bioflocGrad1)', 'url(#bioflocGrad2)', COLORS['biofloc_3']]
    fill = colors[variant % 3]
    # Create irregular shape using bezier curves
    r = size
    points = []
    num_pts = 8
    for i in range(num_pts):
        angle = (2 * math.pi * i) / num_pts
        # Add randomness to radius
        variation = 0.7 + (0.6 * ((i * 7 + variant * 3) % 5) / 5)
        px = x + r * variation * math.cos(angle)
        py = y + r * variation * math.sin(angle)
        points.append((px, py))

    # Build path
    path_d = f"M {points[0][0]},{points[0][1]} "
    for i in range(1, len(points)):
        # Use quadratic curves for organic look
        cpx = (points[i-1][0] + points[i][0]) / 2 + (size * 0.2 * ((-1)**i))
        cpy = (points[i-1][1] + points[i][1]) / 2 + (size * 0.15 * ((-1)**(i+1)))
        path_d += f"Q {cpx},{cpy} {points[i][0]},{points[i][1]} "
    path_d += "Z"

    particle = f'''
    <g opacity="0.85">
        <path d="{path_d}" fill="{fill}" stroke="{COLORS['biofloc_3']}" stroke-width="0.5"/>
        <!-- Internal bacteria dots -->
        <circle cx="{x - size*0.2}" cy="{y - size*0.1}" r="{size*0.15}" fill="{COLORS['bacteria_2']}" opacity="0.6"/>
        <circle cx="{x + size*0.25}" cy="{y + size*0.2}" r="{size*0.12}" fill="{COLORS['bacteria_1']}" opacity="0.5"/>
        <circle cx="{x}" cy="{y + size*0.15}" r="{size*0.1}" fill="{COLORS['microalgae']}" opacity="0.5"/>
    </g>
    '''
    return particle



def draw_bacteria(x, y, size, btype=0):
    """Draw different bacteria types (cocci, bacilli, spirilla)"""
    if btype == 0:  # Coccus (sphere)
        return f'''
        <circle cx="{x}" cy="{y}" r="{size}" fill="url(#bacteriaGrad)" 
                stroke="{COLORS['bacteria_1']}" stroke-width="0.3" opacity="0.8"/>
        '''
    elif btype == 1:  # Bacillus (rod)
        return f'''
        <rect x="{x - size}" y="{y - size*0.4}" width="{size*2}" height="{size*0.8}" 
              rx="{size*0.4}" ry="{size*0.4}" fill="{COLORS['bacteria_2']}" 
              stroke="{COLORS['algae_dark']}" stroke-width="0.3" opacity="0.8"/>
        '''
    else:  # Spirillum
        return f'''
        <path d="M {x-size},{y} C {x-size*0.5},{y-size*0.5} {x},{y+size*0.5} {x+size},{y}" 
              fill="none" stroke="{COLORS['bacteria_3']}" stroke-width="{size*0.4}" 
              stroke-linecap="round" opacity="0.8"/>
        '''


def draw_microalgae(x, y, size):
    """Draw microalgae cell"""
    return f'''
    <g>
        <circle cx="{x}" cy="{y}" r="{size}" fill="{COLORS['microalgae']}" opacity="0.7" 
                stroke="{COLORS['algae_dark']}" stroke-width="0.4"/>
        <!-- Chloroplast representation -->
        <ellipse cx="{x}" cy="{y}" rx="{size*0.6}" ry="{size*0.3}" 
                 fill="{COLORS['algae_dark']}" opacity="0.4"/>
    </g>
    '''


def draw_aeration_bubbles(x, y_start, y_end, count=8):
    """Draw rising air bubbles from aerator"""
    bubbles = '<!-- AERATION BUBBLES -->\n'
    for i in range(count):
        t = i / count
        bx = x + math.sin(t * 4 * math.pi) * 8
        by = y_start + (y_end - y_start) * t
        r = 2 + (1 - t) * 3  # Bigger at bottom, smaller at top
        opacity = 0.3 + t * 0.3
        bubbles += f'    <circle cx="{bx}" cy="{by}" r="{r}" fill="{COLORS["aeration"]}" stroke="#85C1E9" stroke-width="0.5" opacity="{opacity}"/>\n'
    return bubbles


def draw_aerator(x, y):
    """Draw aerator device at bottom of tank"""
    return f'''
    <!-- AERATOR -->
    <g>
        <rect x="{x-25}" y="{y-8}" width="50" height="16" rx="8" ry="8" 
              fill="#566573" stroke="#2C3E50" stroke-width="1.5"/>
        <!-- Air holes -->
        <circle cx="{x-15}" cy="{y}" r="2" fill="#85929E"/>
        <circle cx="{x-5}" cy="{y}" r="2" fill="#85929E"/>
        <circle cx="{x+5}" cy="{y}" r="2" fill="#85929E"/>
        <circle cx="{x+15}" cy="{y}" r="2" fill="#85929E"/>
        <!-- Pipe -->
        <rect x="{x+25}" y="{y-3}" width="40" height="6" fill="#566573" stroke="#2C3E50" stroke-width="1"/>
    </g>
    '''


def draw_nitrogen_cycle(cx, cy, radius):
    """Draw the nitrogen transformation cycle diagram"""
    nh3_label = svg_text(cx, cy - radius*0.6 - 3, "NH&#x2083;/NH&#x2084;&#x207A;",
                         size=9, weight="bold", fill=COLORS['ammonia'],
                         anchor="middle")
    nh3_sub = svg_text(cx, cy - radius*0.6 + 9, "Ammonia", size=7,
                       fill=COLORS['label_text'], anchor="middle")
    no2_label = svg_text(cx + radius*0.55, cy + radius*0.3 - 3, "NO&#x2082;&#x207B;",
                         size=9, weight="bold", fill=COLORS['nitrite'],
                         anchor="middle")
    no2_sub = svg_text(cx + radius*0.55, cy + radius*0.3 + 9, "Nitrite", size=7,
                       fill=COLORS['label_text'], anchor="middle")
    no3_label = svg_text(cx - radius*0.55, cy + radius*0.3 - 3, "NO&#x2083;&#x207B;",
                         size=9, weight="bold", fill=COLORS['nitrate'],
                         anchor="middle")
    no3_sub = svg_text(cx - radius*0.55, cy + radius*0.3 + 9, "Nitrate", size=7,
                       fill=COLORS['label_text'], anchor="middle")

    nitrosomonas_arrow = arrow_path(
        f"M {cx + 15},{cy - radius*0.6 + 15} C {cx + radius*0.4},{cy - radius*0.2} "
        f"{cx + radius*0.5},{cy + radius*0.05} {cx + radius*0.5},{cy + radius*0.3 - 18}",
        COLORS['nitrogen_arrow'])
    nitrosomonas_label = svg_text(cx + radius*0.38, cy - radius*0.1, "Nitrosomonas",
                                  size=6, style="italic", fill=COLORS['bacteria_1'],
                                  anchor="middle")
    nitrobacter_arrow = arrow_path(
        f"M {cx + radius*0.55 - 20},{cy + radius*0.3 + 15} C {cx + radius*0.1},{cy + radius*0.55} "
        f"{cx - radius*0.1},{cy + radius*0.55} {cx - radius*0.55 + 20},{cy + radius*0.3 + 15}",
        COLORS['nitrogen_arrow'])
    nitrobacter_label = svg_text(cx, cy + radius*0.55 + 5, "Nitrobacter",
                                 size=6, style="italic", fill=COLORS['bacteria_1'],
                                 anchor="middle")
    assimilation_arrow = arrow_path(
        f"M {cx - radius*0.55},{cy + radius*0.3 - 18} C {cx - radius*0.4},{cy - radius*0.15} "
        f"{cx - radius*0.2},{cy - radius*0.4} {cx - 15},{cy - radius*0.6 + 15}",
        COLORS['nitrogen_arrow'], dashed=True)
    assimilation_label = svg_text(cx - radius*0.42, cy - radius*0.12, "Assimilation",
                                  size=6, fill=COLORS['carbon'], anchor="middle")

    cycle = f'''
    <!-- NITROGEN CYCLE -->
    <g>
        <!-- Central circle background -->
        <circle cx="{cx}" cy="{cy}" r="{radius}" fill="white" opacity="0.85" 
                stroke="#BDC3C7" stroke-width="1" stroke-dasharray="4,2"/>
        
        <!-- NH3/NH4+ (Ammonia) - Top -->
        <g>
            <circle cx="{cx}" cy="{cy - radius*0.6}" r="22" fill="{COLORS['ammonia']}" opacity="0.15"/>
            {nh3_label}
            {nh3_sub}
        </g>
        
        <!-- NO2- (Nitrite) - Right -->
        <g>
            <circle cx="{cx + radius*0.55}" cy="{cy + radius*0.3}" r="22" fill="{COLORS['nitrite']}" opacity="0.15"/>
            {no2_label}
            {no2_sub}
        </g>
        
        <!-- NO3- (Nitrate) - Left -->
        <g>
            <circle cx="{cx - radius*0.55}" cy="{cy + radius*0.3}" r="22" fill="{COLORS['nitrate']}" opacity="0.15"/>
            {no3_label}
            {no3_sub}
        </g>
        
        <!-- Arrows between nodes -->
        <!-- NH3 -> NO2 (Nitrosomonas) -->
        {nitrosomonas_arrow}
        {nitrosomonas_label}
        
        <!-- NO2 -> NO3 (Nitrobacter) -->
        {nitrobacter_arrow}
        {nitrobacter_label}
        
        <!-- NO3 -> Microbial protein (uptake) -->
        {assimilation_arrow}
        {assimilation_label}
    </g>
    '''
    return cycle


def draw_carbon_source(x, y):
    """Draw carbon source input indicator"""
    title = svg_text(x, y-2, "Carbon", size=8, weight="bold",
                     fill=COLORS['carbon'], anchor="middle")
    subtitle = svg_text(x, y+9, "Source (C:N)", size=7, fill=COLORS['carbon'],
                        anchor="middle")
    return f'''
    <!-- CARBON SOURCE -->
    <g>
        <rect x="{x-30}" y="{y-15}" width="60" height="30" rx="6" ry="6" 
              fill="{COLORS['carbon']}" opacity="0.15" stroke="{COLORS['carbon']}" stroke-width="1.5"/>
        {title}
        {subtitle}
    </g>
    '''


def draw_feed_input(x, y):
    """Draw feed input"""
    label = svg_text(x, y-30, "FEED", size=6, weight="bold", fill="#5D4E37",
                     anchor="middle")
    return f'''
    <!-- FEED INPUT -->
    <g>
        <path d="M {x},{y} L {x-12},{y-25} L {x+12},{y-25} Z" fill="#D4AC6E" stroke="#8B6914" stroke-width="1"/>
        <rect x="{x-12}" y="{y-40}" width="24" height="15" rx="3" ry="3" fill="#C49A3C" stroke="#8B6914" stroke-width="1"/>
        {label}
        <!-- Feed pellets -->
        <circle cx="{x-3}" cy="{y-8}" r="2" fill="#D4AC6E"/>
        <circle cx="{x+4}" cy="{y-5}" r="1.8" fill="#C49A3C"/>
        <circle cx="{x-1}" cy="{y-2}" r="1.5" fill="#B8860B"/>
    </g>
    '''


def draw_arrow_curved(x1, y1, x2, y2, color, label="", label_offset=(0,0)):
    """Draw a curved arrow with optional label"""
    # Control point for quadratic bezier
    cpx = (x1 + x2) / 2 + (y2 - y1) * 0.2
    cpy = (y1 + y2) / 2 - (x2 - x1) * 0.2
    arrow = f'''
    {arrow_path(f"M {x1},{y1} Q {cpx},{cpy} {x2},{y2}", color, opacity=0.8)}
    '''
    if label:
        lx = (x1 + x2) / 2 + label_offset[0]
        ly = (y1 + y2) / 2 + label_offset[1]
        arrow += svg_text(lx, ly, label, size=7, fill=color, anchor="middle",
                          style="italic")
    return arrow



def draw_legend(x, y):
    """Draw figure legend"""
    items = [
        (COLORS['biofloc_1'], 'Biofloc aggregate'),
        (COLORS['bacteria_1'], 'Nitrifying bacteria'),
        (COLORS['microalgae'], 'Microalgae'),
        (COLORS['shrimp_body'], 'L. vannamei'),
        (COLORS['aeration'], 'Aeration/O\u2082'),
        (COLORS['carbon'], 'Carbon source'),
    ]
    header = panel(x, y, 150, len(items)*22 + 20, "LEGEND",
                   title_fill=COLORS['label_text'], title_dy=16)
    legend = f'''
    <!-- LEGEND -->
    <g>
        {header}
    '''
    for i, (color, label) in enumerate(items):
        iy = y + 30 + i * 22
        item_label = svg_text(x+34, iy+11, label, size=8,
                              fill=COLORS['label_text'])
        legend += f'''
        <rect x="{x+12}" y="{iy}" width="14" height="14" rx="3" ry="3" fill="{color}" opacity="0.8"/>
        {item_label}
        '''
    legend += '</g>'
    return legend


def draw_labels_and_annotations(tank_x, tank_y, tank_w, tank_h):
    """Draw all text labels and annotation lines"""
    box_x = tank_x + tank_w/2 + 30
    text_x = tank_x + tank_w/2 + 42

    tank_label = svg_text(tank_x, tank_y - tank_h/2 - 15, "Biofloc Culture Tank",
                          size=11, weight="bold", fill=COLORS['label_text'],
                          anchor="middle")

    water_panel = panel(box_x, tank_y - 60, 145, 100, "Water Quality",
                        title_fill=COLORS['label_text'])
    water_rows = [
        (tank_y - 25, "pH: 7.0 - 8.0"),
        (tank_y - 12, "DO: &gt; 5 mg/L"),
        (tank_y + 1, "TAN: &lt; 1 mg/L"),
        (tank_y + 14, "C:N ratio: 15-20:1"),
        (tank_y + 27, "Floc vol: 10-15 mL/L"),
    ]
    water_text = "\n            ".join(
        svg_text(text_x, ry, content, size=7.5, fill=COLORS['label_text'])
        for ry, content in water_rows)

    benefits_panel = panel(box_x, tank_y + 55, 145, 85, "Key Benefits",
                          title_fill=COLORS['label_text'])
    benefit_rows = [
        (tank_y + 90, "&#x2022; Zero water exchange"),
        (tank_y + 103, "&#x2022; In-situ bioremediation"),
        (tank_y + 116, "&#x2022; Supplemental nutrition"),
        (tank_y + 129, "&#x2022; Reduced FCR"),
    ]
    benefits_text = "\n            ".join(
        svg_text(text_x, ry, content, size=7.5, fill=COLORS['label_text'])
        for ry, content in benefit_rows)

    annotations = f'''
    <!-- ANNOTATIONS -->
    <g>
        <!-- Tank label -->
        {tank_label}
        
        <!-- Water quality parameters box -->
        <g>
            {water_panel}
            {water_text}
        </g>
        
        <!-- Benefits box -->
        <g>
            {benefits_panel}
            {benefits_text}
        </g>
    </g>
    '''
    return annotations


def draw_title(width):
    """Draw the main title and subtitle"""
    title = svg_text(width / 2, 40, "Biofloc Technology (BFT) System",
                     size=18, weight="bold", fill=COLORS['title_text'],
                     anchor="middle", extra='letter-spacing="0.5"')
    subtitle = svg_text(
        width / 2, 60,
        "for Litopenaeus vannamei (Pacific White Shrimp) Culture",
        size=12, fill=COLORS['label_text'], anchor="middle", style="italic")
    return f'''
    <!-- TITLE -->
    {title}
    {subtitle}
    '''


def draw_process_arrows():
    """Draw process flow arrows showing the biofloc cycle"""
    markers = "\n        ".join([
        arrow_marker("arrowhead", COLORS['nitrogen_arrow']),
        arrow_marker("arrowhead_red", COLORS['ammonia']),
        arrow_marker("arrowhead_green", COLORS['nitrate']),
    ])
    return f'''
    <!-- PROCESS FLOW ARROWS -->
    <defs>
        {markers}
    </defs>
    '''


def generate_illustration():
    """Main function to generate the complete biofloc illustration"""
    # Canvas dimensions (suitable for A4/letter journal figure)
    W = 900
    H = 650
    
    # Tank dimensions and position
    tank_cx = 350
    tank_cy = 360
    tank_w = 450
    tank_h = 350
    
    svg_parts = []
    svg_parts.append(svg_header(W, H))
    
    # Background
    svg_parts.append(f'<rect width="{W}" height="{H}" fill="{COLORS["bg"]}"/>')
    
    # Title
    svg_parts.append(draw_title(W))
    
    # Arrow markers
    svg_parts.append(draw_process_arrows())
    
    # Tank
    svg_parts.append(draw_tank(tank_cx, tank_cy, tank_w, tank_h))
    
    # Aerator
    svg_parts.append(draw_aerator(tank_cx - 50, tank_cy + tank_h/2 - 40))
    
    # Aeration bubbles
    svg_parts.append(draw_aeration_bubbles(tank_cx - 50, tank_cy + tank_h/2 - 55, tank_cy - tank_h/2 + 60, 12))
    svg_parts.append(draw_aeration_bubbles(tank_cx - 35, tank_cy + tank_h/2 - 50, tank_cy - tank_h/2 + 80, 8))
    
    # Shrimp - multiple at different positions
    svg_parts.append(draw_shrimp(tank_cx - 120, tank_cy + 40, 1.2, False))
    svg_parts.append(draw_shrimp(tank_cx + 50, tank_cy + 80, 1.0, True))
    svg_parts.append(draw_shrimp(tank_cx - 40, tank_cy + 110, 0.9, False))
    svg_parts.append(draw_shrimp(tank_cx + 100, tank_cy - 10, 0.8, True))
    
    # Biofloc particles - scattered throughout water column
    biofloc_positions = [
        (tank_cx - 150, tank_cy - 80, 12, 0),
        (tank_cx - 80, tank_cy - 40, 9, 1),
        (tank_cx + 30, tank_cy - 60, 11, 2),
        (tank_cx + 120, tank_cy - 30, 10, 0),
        (tank_cx - 100, tank_cy + 20, 8, 1),
        (tank_cx + 80, tank_cy + 30, 13, 2),
        (tank_cx + 150, tank_cy + 60, 9, 0),
        (tank_cx - 160, tank_cy + 80, 10, 1),
        (tank_cx + 40, tank_cy + 130, 8, 2),
        (tank_cx - 50, tank_cy - 100, 7, 0),
        (tank_cx + 100, tank_cy + 100, 11, 1),
        (tank_cx - 130, tank_cy + 130, 9, 2),
    ]
    svg_parts.extend(render_each(draw_biofloc_particle, biofloc_positions))
    
    # Bacteria - scattered
    bacteria_positions = [
        (tank_cx - 170, tank_cy - 50, 4, 0),
        (tank_cx + 160, tank_cy - 70, 5, 1),
        (tank_cx - 60, tank_cy - 120, 4, 2),
        (tank_cx + 50, tank_cy - 100, 3.5, 0),
        (tank_cx + 130, tank_cy + 120, 4, 1),
        (tank_cx - 140, tank_cy - 110, 3, 2),
    ]
    svg_parts.extend(render_each(draw_bacteria, bacteria_positions))
    
    # Microalgae
    algae_positions = [
        (tank_cx - 170, tank_cy - 100, 5),
        (tank_cx + 170, tank_cy - 90, 4),
        (tank_cx - 20, tank_cy - 130, 4.5),
        (tank_cx + 90, tank_cy - 120, 3.5),
        (tank_cx - 100, tank_cy - 130, 4),
    ]
    svg_parts.extend(render_each(draw_microalgae, algae_positions))
    
    # Nitrogen cycle diagram (positioned to the upper-left area inside tank)
    svg_parts.append(draw_nitrogen_cycle(tank_cx - 140, tank_cy - 80, 70))
    
    # Carbon source label
    svg_parts.append(draw_carbon_source(tank_cx + tank_w/2 + 100, tank_cy + 170))
    
    # Feed input
    svg_parts.append(draw_feed_input(tank_cx, tank_cy - tank_h/2 - 10))
    
    # Annotations and labels
    svg_parts.append(draw_labels_and_annotations(tank_cx, tank_cy, tank_w, tank_h))
    
    # Legend
    svg_parts.append(draw_legend(20, H - 170))
    
    # Process description at bottom
    description = svg_text(
        W/2, H - 20,
        "Fig. 1. Schematic representation of Biofloc Technology (BFT) system for "
        "Litopenaeus vannamei culture showing nitrogen cycling and microbial community.",
        size=8, fill=COLORS['label_text'], anchor="middle")
    svg_parts.append(f'''
    <!-- PROCESS DESCRIPTION -->
    {description}
    ''')
    
    # Connection arrows (shrimp waste -> ammonia)
    waste_arrow = arrow_path(
        f"M {tank_cx - 80},{tank_cy + 30} C {tank_cx - 100},{tank_cy} "
        f"{tank_cx - 120},{tank_cy - 20} {tank_cx - 140},{tank_cy - 40}",
        COLORS['ammonia'], width=1.5, marker="arrowhead_red", dashed=True,
        opacity=0.7)
    excretion_label = svg_text(tank_cx - 125, tank_cy + 5, "Excretion", size=6,
                               fill=COLORS['ammonia'], style="italic")
    svg_parts.append(f'''
    <!-- Waste arrow from shrimp to nitrogen cycle -->
    {waste_arrow}
    {excretion_label}
    ''')
    
    # Arrow from biofloc to shrimp (food source)
    food_arrow = arrow_path(
        f"M {tank_cx + 80},{tank_cy + 25} C {tank_cx + 70},{tank_cy + 45} "
        f"{tank_cx + 60},{tank_cy + 60} {tank_cx + 55},{tank_cy + 70}",
        COLORS['nitrate'], width=1.5, marker="arrowhead_green", dashed=True,
        opacity=0.7)
    grazing_label = svg_text(tank_cx + 90, tank_cy + 55, "Grazing", size=6,
                             fill=COLORS['nitrate'], style="italic")
    svg_parts.append(f'''
    <!-- Biofloc as food for shrimp -->
    {food_arrow}
    {grazing_label}
    ''')
    
    # Carbon source arrow into tank
    carbon_arrow = arrow_path(
        f"M {tank_cx + tank_w/2 + 70},{tank_cy + 165} "
        f"L {tank_cx + tank_w/2 + 10},{tank_cy + 120}",
        COLORS['carbon'], opacity=0.7)
    svg_parts.append(f'''
    <!-- Carbon source input arrow -->
    {carbon_arrow}
    ''')
    
    svg_parts.append(svg_footer())
    
    return '\n'.join(svg_parts)


# ============================================================
# MAIN EXECUTION
# ============================================================
if __name__ == '__main__':
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(output_dir, 'biofloc_vannamei_illustration.svg')
    
    svg_content = generate_illustration()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"[SUCCESS] Illustration saved to: {output_file}")
    print(f"[INFO] File size: {os.path.getsize(output_file) / 1024:.1f} KB")
    print(f"[INFO] Format: SVG (Scalable Vector Graphics)")
    print(f"[TIP] Open in browser or convert to PDF/EPS for journal submission.")
    print(f"[TIP] Use Inkscape or Adobe Illustrator to export as high-res PNG/TIFF if needed.")
