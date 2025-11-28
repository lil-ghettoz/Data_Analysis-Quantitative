import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Table 1: Sustainability Indicators by Transport Mode
data_table1 = {
    'Transport Mode': ['Bus (Diesel)', 'Bus (CNG)', 'Bus (Electric)', 'Light Rail Transit', 
                       'Metro/Subway', 'Commuter Rail', 'Private Car (Gasoline)', 'Private Car (Electric)'],
    'Energy Intensity\n(MJ/pass-km)': [2.8, 2.4, 1.2, 1.5, 1.3, 1.8, 4.2, 2.1],
    'CO₂ Emissions\n(g/pass-km)': [95, 78, 35, 45, 40, 55, 180, 65],
    'Passenger Capacity\n(persons)': [60, 60, 80, 200, 300, 400, 5, 5],
    'Operating Cost\n($/km)': [4.5, 4.8, 3.2, 8.5, 12.0, 10.5, 0.8, 0.6],
    'Sustainability\nScore (0-100)': [55, 62, 85, 78, 82, 70, 25, 58]
}

df_table1 = pd.DataFrame(data_table1)

# Create figure for Table 1
fig1, ax1 = plt.subplots(figsize=(14, 6))
ax1.axis('tight')
ax1.axis('off')

# Create table
table1 = ax1.table(cellText=df_table1.values, colLabels=df_table1.columns,
                   cellLoc='center', loc='center', 
                   colWidths=[0.18, 0.15, 0.15, 0.15, 0.15, 0.15])

table1.auto_set_font_size(False)
table1.set_fontsize(9)
table1.scale(1, 2.2)

# Style header
for i in range(len(df_table1.columns)):
    cell = table1[(0, i)]
    cell.set_facecolor('#2A9D8F')
    cell.set_text_props(weight='bold', color='white', fontsize=10)

# Style rows with alternating colors
for i in range(1, len(df_table1) + 1):
    for j in range(len(df_table1.columns)):
        cell = table1[(i, j)]
        if i % 2 == 0:
            cell.set_facecolor('#F0F0F0')
        else:
            cell.set_facecolor('white')
        
        # Highlight best values in each column
        if j == 1:  # Energy Intensity
            if df_table1.iloc[i-1, j] == df_table1.iloc[:, j].min():
                cell.set_facecolor('#C8E6C9')
        elif j == 2:  # CO2 Emissions
            if df_table1.iloc[i-1, j] == df_table1.iloc[:, j].min():
                cell.set_facecolor('#C8E6C9')
        elif j == 5:  # Sustainability Score
            if df_table1.iloc[i-1, j] == df_table1.iloc[:, j].max():
                cell.set_facecolor('#C8E6C9')

plt.title('Table 1: Comparative Sustainability Indicators by Transport Mode', 
          fontsize=13, fontweight='bold', pad=20)
plt.savefig('table1_conceptual_framework.png', dpi=300, bbox_inches='tight')
plt.close()

print("Table 1 created successfully")

# Table 2: Urban Form and Transit Energy Relationships
data_table2 = {
    'City Type': ['Auto-Oriented\n(Low Density)', 'Suburban\n(Medium Density)', 
                  'Transit-Oriented\n(High Density)', 'Compact Urban\n(Very High Density)'],
    'Population Density\n(persons/hectare)': [20, 60, 120, 200],
    'Job Density\n(jobs/hectare)': [15, 45, 90, 150],
    'Transit Modal Share\n(%)': [8, 18, 35, 55],
    'Per Capita Transit Energy\n(MJ/person/year)': [450, 820, 1200, 1450],
    'Per Capita Auto Energy\n(MJ/person/year)': [8500, 5200, 2800, 1200],
    'Total Transport Energy\n(MJ/person/year)': [8950, 6020, 4000, 2650],
    'Energy Efficiency\nIndex': [1.0, 1.49, 2.24, 3.38]
}

df_table2 = pd.DataFrame(data_table2)

# Create figure for Table 2
fig2, ax2 = plt.subplots(figsize=(15, 5))
ax2.axis('tight')
ax2.axis('off')

# Create table
table2 = ax2.table(cellText=df_table2.values, colLabels=df_table2.columns,
                   cellLoc='center', loc='center',
                   colWidths=[0.14, 0.12, 0.10, 0.12, 0.13, 0.13, 0.13, 0.10])

table2.auto_set_font_size(False)
table2.set_fontsize(8.5)
table2.scale(1, 2.5)

# Style header
for i in range(len(df_table2.columns)):
    cell = table2[(0, i)]
    cell.set_facecolor('#457B9D')
    cell.set_text_props(weight='bold', color='white', fontsize=9)

# Style rows
for i in range(1, len(df_table2) + 1):
    for j in range(len(df_table2.columns)):
        cell = table2[(i, j)]
        if i % 2 == 0:
            cell.set_facecolor('#E8F4F8')
        else:
            cell.set_facecolor('white')
        
        # Highlight efficiency improvements
        if j == 7:  # Energy Efficiency Index
            value = df_table2.iloc[i-1, j]
            if value > 2.5:
                cell.set_facecolor('#C8E6C9')
            elif value > 1.5:
                cell.set_facecolor('#FFF9C4')

plt.title('Table 2: Urban Form Characteristics and Transit Energy Relationships', 
          fontsize=13, fontweight='bold', pad=20)
plt.savefig('table2_conceptual_framework.png', dpi=300, bbox_inches='tight')
plt.close()

print("Table 2 created successfully")

# Table 3: Data Collection Sources and Methods
data_table3 = {
    'Data Category': ['Transit Operations', 'Energy Consumption', 'Urban Form', 
                      'Ridership Patterns', 'Environmental Impact', 'Socioeconomic'],
    'Primary Sources': [
        'Transit agency records,\nGPS tracking systems',
        'Utility bills, smart meters,\nenergy management systems',
        'GIS databases, satellite imagery,\ncensus data',
        'Automated fare collection,\npassenger surveys',
        'Air quality monitors,\nemissions databases',
        'Census data, household surveys,\nemployment statistics'
    ],
    'Secondary Sources': [
        'Government reports,\nindustry publications',
        'National energy databases,\nIEA statistics',
        'Urban planning documents,\nland use maps',
        'Academic studies,\ntransit reports',
        'EPA databases,\nclimate reports',
        'Statistical yearbooks,\nWorld Bank data'
    ],
    'Collection Method': [
        'Digital records extraction,\nAPI integration',
        'Direct measurement,\nautomated logging',
        'Spatial analysis,\nremote sensing',
        'Electronic data capture,\nfield surveys',
        'Sensor networks,\nmodeling software',
        'Database queries,\nsurvey instruments'
    ],
    'Temporal Coverage': [
        '12-24 months',
        '12-36 months',
        'Current + 5-year trends',
        '12-24 months',
        '12-36 months',
        'Latest census + updates'
    ],
    'Data Quality': [
        'High',
        'High',
        'Medium-High',
        'High',
        'Medium',
        'Medium-High'
    ]
}

df_table3 = pd.DataFrame(data_table3)

# Create figure for Table 3
fig3, ax3 = plt.subplots(figsize=(16, 7))
ax3.axis('tight')
ax3.axis('off')

# Create table
table3 = ax3.table(cellText=df_table3.values, colLabels=df_table3.columns,
                   cellLoc='left', loc='center',
                   colWidths=[0.13, 0.20, 0.20, 0.20, 0.13, 0.10])

table3.auto_set_font_size(False)
table3.set_fontsize(8)
table3.scale(1, 2.8)

# Style header
for i in range(len(df_table3.columns)):
    cell = table3[(0, i)]
    cell.set_facecolor('#E9C46A')
    cell.set_text_props(weight='bold', color='black', fontsize=9)
    cell.set_text_props(ha='center')

# Style rows
for i in range(1, len(df_table3) + 1):
    for j in range(len(df_table3.columns)):
        cell = table3[(i, j)]
        if i % 2 == 0:
            cell.set_facecolor('#FFF8E1')
        else:
            cell.set_facecolor('white')
        
        # Center first column
        if j == 0:
            cell.set_text_props(ha='center', weight='bold')
        
        # Highlight data quality
        if j == 5:
            cell.set_text_props(ha='center')
            if df_table3.iloc[i-1, j] == 'High':
                cell.set_facecolor('#C8E6C9')
            elif df_table3.iloc[i-1, j] == 'Medium-High':
                cell.set_facecolor('#FFF9C4')

plt.title('Table 3: Data Collection Sources and Methodological Framework', 
          fontsize=13, fontweight='bold', pad=20)
plt.savefig('table3_conceptual_framework.png', dpi=300, bbox_inches='tight')
plt.close()

print("Table 3 created successfully")

# Table 4: Variables and Measurement Framework
data_table4 = {
    'Variable Type': ['Dependent Variables', '', '', 'Independent Variables', '', '', 
                      'Moderating Variables', '', 'Control Variables', ''],
    'Variable Name': [
        'Energy Consumption per Passenger-km',
        'GHG Emissions per Passenger-km',
        'Overall Sustainability Score',
        'Population Density',
        'Transit Service Frequency',
        'Fleet Technology Type',
        'Urban Form Configuration',
        'Policy Framework Strength',
        'Climate Zone',
        'Economic Development Level'
    ],
    'Measurement Unit': [
        'MJ/passenger-km',
        'g CO₂e/passenger-km',
        'Index (0-100)',
        'Persons/hectare',
        'Vehicles/hour',
        'Categorical',
        'Categorical',
        'Index (0-10)',
        'Categorical',
        'GDP per capita (USD)'
    ],
    'Data Source': [
        'Transit agency records',
        'Emissions calculation model',
        'Multi-indicator aggregation',
        'Census data, GIS analysis',
        'Transit schedules',
        'Fleet inventory',
        'Urban planning documents',
        'Policy document analysis',
        'Climate databases',
        'Economic statistics'
    ],
    'Expected Relationship': [
        'Outcome measure',
        'Outcome measure',
        'Outcome measure',
        'Negative (↓ energy)',
        'Negative (↓ energy)',
        'Varies by type',
        'Moderates density effect',
        'Moderates policy impact',
        'Controls for climate',
        'Controls for development'
    ]
}

df_table4 = pd.DataFrame(data_table4)

# Create figure for Table 4
fig4, ax4 = plt.subplots(figsize=(16, 8))
ax4.axis('tight')
ax4.axis('off')

# Create table
table4 = ax4.table(cellText=df_table4.values, colLabels=df_table4.columns,
                   cellLoc='left', loc='center',
                   colWidths=[0.16, 0.24, 0.18, 0.20, 0.22])

table4.auto_set_font_size(False)
table4.set_fontsize(8.5)
table4.scale(1, 2.5)

# Style header
for i in range(len(df_table4.columns)):
    cell = table4[(0, i)]
    cell.set_facecolor('#F4A261')
    cell.set_text_props(weight='bold', color='black', fontsize=10)
    cell.set_text_props(ha='center')

# Style rows
variable_colors = {
    'Dependent Variables': '#E3F2FD',
    'Independent Variables': '#F3E5F5',
    'Moderating Variables': '#FFF3E0',
    'Control Variables': '#E8F5E9'
}

current_type = None
for i in range(1, len(df_table4) + 1):
    var_type = df_table4.iloc[i-1, 0]
    if var_type != '':
        current_type = var_type
    
    for j in range(len(df_table4.columns)):
        cell = table4[(i, j)]
        if current_type in variable_colors:
            cell.set_facecolor(variable_colors[current_type])
        
        # Bold variable type
        if j == 0 and var_type != '':
            cell.set_text_props(weight='bold', ha='center')

plt.title('Table 4: Research Variables and Measurement Framework', 
          fontsize=13, fontweight='bold', pad=20)
plt.savefig('table4_conceptual_framework.png', dpi=300, bbox_inches='tight')
plt.close()

print("Table 4 created successfully")

print("\nAll tables created successfully!")
print("- Table 1: Comparative Sustainability Indicators")
print("- Table 2: Urban Form and Energy Relationships")
print("- Table 3: Data Collection Sources")
print("- Table 4: Research Variables Framework")
