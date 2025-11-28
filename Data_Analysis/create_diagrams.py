import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Set style
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

# Figure 1: Conceptual Framework Diagram
fig1, ax1 = plt.subplots(figsize=(14, 8))
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')

# Define colors
color_primary = '#2E86AB'
color_secondary = '#A23B72'
color_tertiary = '#F18F01'
color_outcome = '#06A77D'

# Box 1: Public Transportation Systems
box1 = FancyBboxPatch((0.5, 6.5), 2.5, 2, boxstyle="round,pad=0.1", 
                       edgecolor=color_primary, facecolor=color_primary, alpha=0.3, linewidth=2)
ax1.add_patch(box1)
ax1.text(1.75, 8.2, 'Public Transportation', ha='center', va='center', fontsize=12, fontweight='bold')
ax1.text(1.75, 7.8, 'Systems', ha='center', va='center', fontsize=12, fontweight='bold')
ax1.text(1.75, 7.3, '• Bus Transit', ha='center', va='center', fontsize=9)
ax1.text(1.75, 7.0, '• Rail Systems', ha='center', va='center', fontsize=9)
ax1.text(1.75, 6.7, '• Infrastructure', ha='center', va='center', fontsize=9)

# Box 2: Energy Consumption
box2 = FancyBboxPatch((4, 6.5), 2.5, 2, boxstyle="round,pad=0.1", 
                       edgecolor=color_secondary, facecolor=color_secondary, alpha=0.3, linewidth=2)
ax1.add_patch(box2)
ax1.text(5.25, 8.2, 'Energy Consumption', ha='center', va='center', fontsize=12, fontweight='bold')
ax1.text(5.25, 7.7, '• Direct Energy Use', ha='center', va='center', fontsize=9)
ax1.text(5.25, 7.4, '• Fuel Types', ha='center', va='center', fontsize=9)
ax1.text(5.25, 7.1, '• Efficiency Metrics', ha='center', va='center', fontsize=9)
ax1.text(5.25, 6.8, '• Grid Integration', ha='center', va='center', fontsize=9)

# Box 3: Sustainability Outcomes
box3 = FancyBboxPatch((7.5, 6.5), 2.5, 2, boxstyle="round,pad=0.1", 
                       edgecolor=color_outcome, facecolor=color_outcome, alpha=0.3, linewidth=2)
ax1.add_patch(box3)
ax1.text(8.75, 8.2, 'Sustainability', ha='center', va='center', fontsize=12, fontweight='bold')
ax1.text(8.75, 7.9, 'Outcomes', ha='center', va='center', fontsize=12, fontweight='bold')
ax1.text(8.75, 7.4, '• GHG Reduction', ha='center', va='center', fontsize=9)
ax1.text(8.75, 7.1, '• Air Quality', ha='center', va='center', fontsize=9)
ax1.text(8.75, 6.8, '• Urban Resilience', ha='center', va='center', fontsize=9)

# Arrows between main boxes
arrow1 = FancyArrowPatch((3, 7.5), (4, 7.5), arrowstyle='->', mutation_scale=30, 
                         linewidth=3, color=color_primary)
ax1.add_patch(arrow1)

arrow2 = FancyArrowPatch((6.5, 7.5), (7.5, 7.5), arrowstyle='->', mutation_scale=30, 
                         linewidth=3, color=color_secondary)
ax1.add_patch(arrow2)

# Moderating factors (top)
box4 = FancyBboxPatch((3.5, 9.2), 3.5, 0.6, boxstyle="round,pad=0.05", 
                       edgecolor=color_tertiary, facecolor=color_tertiary, alpha=0.2, linewidth=1.5)
ax1.add_patch(box4)
ax1.text(5.25, 9.5, 'Moderating Factors: Urban Form, Technology, Policy', 
         ha='center', va='center', fontsize=9, style='italic')

# Connecting moderating factors
arrow3 = FancyArrowPatch((5.25, 9.2), (5.25, 8.5), arrowstyle='->', mutation_scale=20, 
                         linewidth=2, color=color_tertiary, linestyle='dashed')
ax1.add_patch(arrow3)

# Contextual factors (bottom)
context_boxes = [
    (1, 5.5, 'Urban Density'),
    (3, 5.5, 'Population Growth'),
    (5, 5.5, 'Economic Factors'),
    (7, 5.5, 'Climate Conditions'),
    (9, 5.5, 'Policy Framework')
]

for x, y, label in context_boxes:
    box = FancyBboxPatch((x-0.6, y-0.3), 1.2, 0.5, boxstyle="round,pad=0.05", 
                         edgecolor='gray', facecolor='lightgray', alpha=0.5, linewidth=1)
    ax1.add_patch(box)
    ax1.text(x, y, label, ha='center', va='center', fontsize=8)
    
    # Connect to energy consumption
    arrow = FancyArrowPatch((x, y+0.2), (5.25, 6.5), arrowstyle='->', mutation_scale=15, 
                           linewidth=1, color='gray', linestyle='dotted', alpha=0.6)
    ax1.add_patch(arrow)

ax1.text(5, 4.8, 'Contextual Factors', ha='center', va='center', fontsize=10, 
         fontweight='bold', style='italic', color='gray')

# Feedback loop
feedback_arrow = FancyArrowPatch((8.75, 6.5), (1.75, 6.5), arrowstyle='->', mutation_scale=20, 
                                 linewidth=2, color='darkred', linestyle='dashed',
                                 connectionstyle="arc3,rad=-.5")
ax1.add_patch(feedback_arrow)
ax1.text(5, 4.2, 'Feedback Loop: Policy Adjustments & System Optimization', 
         ha='center', va='center', fontsize=9, style='italic', color='darkred')

# Title
ax1.text(5, 9.8, 'Conceptual Framework: Public Transportation Energy Use and Urban Sustainability', 
         ha='center', va='top', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('figure1_conceptual_framework.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure 1 created successfully")

# Figure 2: Research Process Flowchart
fig2, ax2 = plt.subplots(figsize=(12, 14))
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 16)
ax2.axis('off')

# Define flowchart steps
steps = [
    (5, 15, 'Research Problem Identification', '#E63946', 1.8, 0.6),
    (5, 13.5, 'Literature Review & Gap Analysis', '#457B9D', 2.2, 0.6),
    (5, 12, 'Research Questions & Objectives', '#2A9D8F', 2.2, 0.6),
    (5, 10.5, 'Conceptual Framework Development', '#E9C46A', 2.2, 0.6),
]

# Data collection phase (parallel boxes)
data_steps = [
    (2.5, 8.8, 'Primary Data\n• Field surveys\n• Energy audits', '#F4A261', 1.8, 0.8),
    (5, 8.8, 'Secondary Data\n• Transit records\n• Energy databases', '#F4A261', 1.8, 0.8),
    (7.5, 8.8, 'Spatial Data\n• GIS data\n• Urban form', '#F4A261', 1.8, 0.8),
]

# Analysis steps
analysis_steps = [
    (5, 7.2, 'Data Processing & Validation', '#264653', 2.2, 0.6),
    (5, 6, 'Statistical & Spatial Analysis', '#2A9D8F', 2.2, 0.6),
    (5, 4.8, 'Energy Modeling & Simulation', '#457B9D', 2.2, 0.6),
    (5, 3.6, 'Sustainability Indicator Assessment', '#E9C46A', 2.2, 0.6),
    (5, 2.4, 'Results Interpretation & Discussion', '#F4A261', 2.2, 0.6),
    (5, 1.2, 'Conclusions & Recommendations', '#E63946', 2.2, 0.6),
]

# Draw main steps
for x, y, text, color, w, h in steps:
    box = FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.1", 
                         edgecolor=color, facecolor=color, alpha=0.3, linewidth=2)
    ax2.add_patch(box)
    ax2.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold', 
             wrap=True, multialignment='center')
    
# Draw data collection boxes
ax2.text(5, 9.8, 'Data Collection Phase', ha='center', va='center', 
         fontsize=11, fontweight='bold', style='italic')
for x, y, text, color, w, h in data_steps:
    box = FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.08", 
                         edgecolor=color, facecolor=color, alpha=0.3, linewidth=2)
    ax2.add_patch(box)
    ax2.text(x, y, text, ha='center', va='center', fontsize=8, multialignment='center')

# Draw analysis steps
for x, y, text, color, w, h in analysis_steps:
    box = FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.1", 
                         edgecolor=color, facecolor=color, alpha=0.3, linewidth=2)
    ax2.add_patch(box)
    ax2.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold')

# Draw arrows for main flow
arrow_positions = [
    (5, 14.7, 5, 14.1),
    (5, 13.2, 5, 12.6),
    (5, 11.7, 5, 11.1),
    (5, 10.2, 5, 9.8),
]

for x1, y1, x2, y2 in arrow_positions:
    arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->', mutation_scale=25, 
                           linewidth=2.5, color='black')
    ax2.add_patch(arrow)

# Arrows from data collection to processing
for x, y, _, _, _, h in data_steps:
    arrow = FancyArrowPatch((x, y-h/2), (5, 7.5), arrowstyle='->', mutation_scale=20, 
                           linewidth=2, color='#264653')
    ax2.add_patch(arrow)

# Arrows for analysis flow
analysis_arrows = [
    (5, 6.9, 5, 6.3),
    (5, 5.7, 5, 5.1),
    (5, 4.5, 5, 3.9),
    (5, 3.3, 5, 2.7),
    (5, 2.1, 5, 1.5),
]

for x1, y1, x2, y2 in analysis_arrows:
    arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->', mutation_scale=25, 
                           linewidth=2.5, color='black')
    ax2.add_patch(arrow)

# Add iteration loops
loop1 = FancyArrowPatch((6.1, 6), (6.1, 7.2), arrowstyle='->', mutation_scale=20, 
                        linewidth=1.5, color='red', linestyle='dashed',
                        connectionstyle="arc3,rad=.5")
ax2.add_patch(loop1)
ax2.text(7.2, 6.6, 'Iteration', ha='center', va='center', fontsize=8, 
         style='italic', color='red')

# Title
ax2.text(5, 15.8, 'Research Process Flowchart', ha='center', va='top', 
         fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('figure2_conceptual_framework.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure 2 created successfully")

# Figure 3: Sustainability Indicators Comparison Chart
fig3, ((ax3a, ax3b), (ax3c, ax3d)) = plt.subplots(2, 2, figsize=(14, 10))

# Data for charts
transit_modes = ['Bus (Diesel)', 'Bus (Electric)', 'Light Rail', 'Metro/Subway', 'Private Car']
co2_emissions = [95, 35, 45, 40, 180]  # g CO2/passenger-km
energy_intensity = [2.8, 1.2, 1.5, 1.3, 4.2]  # MJ/passenger-km
colors_modes = ['#E63946', '#06A77D', '#457B9D', '#2A9D8F', '#F4A261']

# Chart A: CO2 Emissions Comparison
bars1 = ax3a.barh(transit_modes, co2_emissions, color=colors_modes, edgecolor='black', linewidth=1.5)
ax3a.set_xlabel('CO₂ Emissions (g/passenger-km)', fontsize=11, fontweight='bold')
ax3a.set_title('(A) CO₂ Emissions by Transport Mode', fontsize=12, fontweight='bold', pad=15)
ax3a.grid(axis='x', alpha=0.3, linestyle='--')
ax3a.axvline(x=50, color='green', linestyle='--', linewidth=2, alpha=0.7, label='Sustainability Target')
ax3a.legend()

# Add value labels
for i, (bar, value) in enumerate(zip(bars1, co2_emissions)):
    ax3a.text(value + 5, i, f'{value}', va='center', fontweight='bold', fontsize=9)

# Chart B: Energy Intensity Comparison
bars2 = ax3b.barh(transit_modes, energy_intensity, color=colors_modes, edgecolor='black', linewidth=1.5)
ax3b.set_xlabel('Energy Intensity (MJ/passenger-km)', fontsize=11, fontweight='bold')
ax3b.set_title('(B) Energy Intensity by Transport Mode', fontsize=12, fontweight='bold', pad=15)
ax3b.grid(axis='x', alpha=0.3, linestyle='--')
ax3b.axvline(x=2.0, color='green', linestyle='--', linewidth=2, alpha=0.7, label='Efficiency Target')
ax3b.legend()

# Add value labels
for i, (bar, value) in enumerate(zip(bars2, energy_intensity)):
    ax3b.text(value + 0.1, i, f'{value}', va='center', fontweight='bold', fontsize=9)

# Chart C: Urban Density vs Transit Energy Efficiency
densities = [50, 80, 120, 150, 200, 250, 300]  # persons per hectare
efficiency = [3.5, 2.8, 2.2, 1.8, 1.5, 1.3, 1.2]  # MJ/passenger-km

ax3c.plot(densities, efficiency, marker='o', linewidth=3, markersize=10, 
          color='#2A9D8F', markerfacecolor='#E9C46A', markeredgecolor='black', markeredgewidth=2)
ax3c.fill_between(densities, efficiency, alpha=0.3, color='#2A9D8F')
ax3c.set_xlabel('Urban Density (persons/hectare)', fontsize=11, fontweight='bold')
ax3c.set_ylabel('Transit Energy Intensity (MJ/pass-km)', fontsize=11, fontweight='bold')
ax3c.set_title('(C) Urban Density vs Transit Energy Efficiency', fontsize=12, fontweight='bold', pad=15)
ax3c.grid(alpha=0.3, linestyle='--')
ax3c.set_xlim(40, 310)

# Chart D: Modal Share Impact on Urban Energy Consumption
modal_share_transit = [10, 20, 30, 40, 50, 60]  # % of trips by public transit
urban_energy_index = [100, 85, 72, 61, 52, 45]  # indexed to 100

ax3d.bar(modal_share_transit, urban_energy_index, width=7, color='#457B9D', 
         edgecolor='black', linewidth=1.5, alpha=0.8)
ax3d.set_xlabel('Public Transit Modal Share (%)', fontsize=11, fontweight='bold')
ax3d.set_ylabel('Urban Transport Energy Index', fontsize=11, fontweight='bold')
ax3d.set_title('(D) Transit Modal Share Impact on Energy Use', fontsize=12, fontweight='bold', pad=15)
ax3d.grid(axis='y', alpha=0.3, linestyle='--')
ax3d.axhline(y=50, color='green', linestyle='--', linewidth=2, alpha=0.7, label='Target Reduction')
ax3d.legend()

# Add value labels
for i, (x, y) in enumerate(zip(modal_share_transit, urban_energy_index)):
    ax3d.text(x, y + 2, f'{y}', ha='center', fontweight='bold', fontsize=9)

plt.suptitle('Figure 3: Sustainability Indicators and Performance Metrics', 
             fontsize=15, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('figure3_conceptual_framework.png', dpi=300, bbox_inches='tight')
plt.close()

print("Figure 3 created successfully")

print("\nAll figures created successfully!")
print("- Figure 1: Conceptual Framework Diagram")
print("- Figure 2: Research Process Flowchart")
print("- Figure 3: Sustainability Indicators Charts")
