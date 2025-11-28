import matplotlib.pyplot as plt
import pandas as pd

# =======================
# Create the DataFrame
# =======================

data = {
    "Respondent": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],
    "Age": [16,15,17,16,18,15,17,16,15,18,16,17,15,16,18,17,15,16,17,18,15,16,17,16,15],
    "Gender": ["Female","Male","Female","Male","Female","Female","Male","Female","Male",
               "Female","Male","Female","Female","Male","Female","Male","Female","Male",
               "Female","Male","Female","Male","Female","Female","Male"],
    "Grade": [10,9,11,10,12,9,11,10,9,12,10,11,9,10,12,11,9,10,11,12,9,10,11,10,9],
    "Daily SM Hours": ["6-8 hrs","3-5 hrs","9+ hrs","3-5 hrs","6-8 hrs","9+ hrs","0-2 hrs",
                       "6-8 hrs","3-5 hrs","9+ hrs","3-5 hrs","6-8 hrs","6-8 hrs","0-2 hrs",
                       "9+ hrs","3-5 hrs","6-8 hrs","3-5 hrs","9+ hrs","6-8 hrs",
                       "3-5 hrs","0-2 hrs","6-8 hrs","9+ hrs","3-5 hrs"],
    "Main Platform": ["Facebook","TikTok","Facebook","YouTube","TikTok","Facebook","YouTube",
                      "TikTok","Facebook","Facebook","YouTube","TikTok","Facebook","YouTube",
                      "TikTok","Facebook","Facebook","YouTube","TikTok","Facebook",
                      "TikTok","YouTube","Facebook","Facebook","YouTube"],
    "Anxiety Frequency": ["Sometimes","Rarely","Often","Never","Sometimes","Often","Never","Sometimes",
                          "Rarely","Always","Rarely","Sometimes","Often","Never","Often","Sometimes",
                          "Sometimes","Rarely","Often","Sometimes","Rarely","Never","Sometimes",
                          "Always","Rarely"],
    "Depression Frequency": ["Rarely","Never","Sometimes","Never","Sometimes","Often","Never","Rarely",
                             "Rarely","Often","Never","Sometimes","Sometimes","Never","Often","Rarely",
                             "Sometimes","Never","Often","Sometimes","Rarely","Never","Sometimes",
                             "Often","Rarely"],
    "Sleep Affected": ["Yes","No","Yes","No","Yes","Yes","No","Yes","No","Yes","No","Yes","Yes","No",
                       "Yes","No","Yes","No","Yes","Yes","No","No","Yes","Yes","No"],
    "Comparison": ["Often","Sometimes","Always","Rarely","Often","Always","Never","Sometimes","Sometimes",
                   "Always","Rarely","Often","Often","Never","Always","Sometimes","Often","Rarely",
                   "Always","Sometimes","Sometimes","Never","Often","Always","Rarely"],
    "Mental Well-being": ["Fair","Good","Poor","Excellent","Fair","Poor","Excellent","Good","Good","Poor",
                          "Good","Fair","Fair","Excellent","Poor","Good","Fair","Good","Poor","Fair",
                          "Good","Excellent","Good","Poor","Good"]
}

df = pd.DataFrame(data)

# =======================
# Plot table with matplotlib
# =======================

fig, ax = plt.subplots(figsize=(20, 12))
ax.axis('off')

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc='center',
    cellLoc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.5)

plt.title("Survey Dataset Table", fontsize=18, pad=20)
plt.savefig('quanti1_table.png', dpi=300, bbox_inches='tight')