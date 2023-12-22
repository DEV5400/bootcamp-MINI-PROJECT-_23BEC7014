import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
from math import pi
# CSV data as a string
csv_data = """ACADEMIC SATISFACTION,SOCIAL LIFE,INFRASTRUCTURE,CAREER SUPPORT,STUDENT ENGAGEMENT,HEALTH AND WELLNESS,FEEDBACK
10,10,10,10,10,10,10
8,7,8,8,9,8,8
7,8,7,6,5,7,8
7,8,7,3,6,5,3
8,8,6,7,9,9,7
9,8,7,10,9,10,10
10,6,8,5,8,6,8
4,3,2,3,4,7,
5,5,7,6,5,5,7
8,4,7,7,9,8,5
3,3,5,6,10,10,8
3,4,1,2,8,1,1
6,8,7,3,3,1,
7,8,8,8,8,8,8
10,10,10,10,10,10,10
6,7,10,5,4,8,4
6,6,7,7,5,5,6
5,4,6,5,4,5,7
1,2,4,4,4,4,4
7,7,7,8,7,9,7
4,6,4,5,5,3,3
8,8,9,8,9,8,9
6,6,5,6,7,6,6
1,1,4,1,1,1,1
2,2,5,1,1,1,1
3,7,7,5,6,8,5
4,6,3,1,8,5,1
6,5,6,7,7,8,5
4,3,5,6,6,7,3
7,9,8,7,8,8,9
8,7,9,3,8,5,7
7,2,6,7,7,7,7
6,8,8,7,7,8,8
7,8,7,9,7,10,9
8,10,7,7,8,5,7
4,4,4,4,4,5,2
5,5,8,8,10,6,7
1,1,1,1,1,1,1
6,4,7,5,7,8,2
7,6,3,4,7,3,1
1,1,1,1,1,1,1
1,1,1,4,4,1,1
8,8,10,9,9,9,
4,7,8,7,8,9,5
1,1,2,1,1,1,1
3,2,3,1,2,2,2
9,8,10,9,8,9,9
1,6,1,1,1,1,5
8,3,7,5,5,5,7
6,5,6,4,4,4,4
7,5,6,4,6,7,8
8,9,8,8,8,9,9
7,6,7,7,9,3,10
9,8,9,10,10,10,10
10,10,10,10,10,10,10
6,2,3,5,8,2,1
3,7,6,6,7,8,5
3,1,9,7,2,1,2
7,5,6,6,6,7,4
10,9,9,8,7,3,5"""

#  CSV data into a DataFrame
df = pd.read_csv(StringIO(csv_data))

# Display the DataFrame
print(df)



# Radar Chart
labels = df.columns[:-1]
num_vars = len(labels)

angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))


for i, row in df.iterrows():
    values = row.values[:-1].tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=f"Student {i + 1}")


ax.fill(angles, df.mean()[:-1].tolist() + df.mean()[:1].tolist(), alpha=0.25)


ax.set_yticklabels([])
ax.set_thetagrids([angle * 180/pi for angle in angles[:-1]], labels)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Show the radar chart
plt.title('Student Feedback Radar Chart')
plt.show()



# Total Bar Graph
total_scores = df.sum()[:-1]

fig, ax = plt.subplots(figsize=(10, 6))

total_scores.plot(kind='bar', ax=ax, color='skyblue')
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.set_ylabel('Total Score')
ax.set_title('Total Scores for Each Category')


plt.show()



# Total Line Graph
total_scores_line = df.sum(axis=1)

fig, ax = plt.subplots(figsize=(10, 6))

total_scores_line.plot(kind='line', marker='o', ax=ax, color='orange')
ax.set_xticks(range(1, len(total_scores_line) + 1))
ax.set_xlabel('Student')
ax.set_ylabel('Total Score')
ax.set_title('Total Scores Across All Categories for Each Student')


plt.show()



# Stacked Bar Plot for Total Scores
fig, ax = plt.subplots(figsize=(12, 8))

df_percentage = df.div(df.sum(axis=1), axis=0) * 100
df_percentage.plot(kind='bar', stacked=True, ax=ax)
ax.set_xticklabels(range(1, len(df) + 1), rotation=0)
ax.set_xlabel('Student')
ax.set_ylabel('Percentage Contribution to Total Score')
ax.set_title('Percentage Contribution of Each Category to Total Score for Each Student')


plt.show()



# Table for Total Scores
fig, ax = plt.subplots(figsize=(12, 8))


table_data = df.copy()
table_data['Total'] = df.sum(axis=1)
table = ax.table(cellText=table_data.values, colLabels=table_data.columns, loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Remove x and y axis labels for better presentation
ax.axis('off')


plt.show()



# Violin Plot for Total Scores
fig, ax = plt.subplots(figsize=(12, 8))

df_total = df.sum(axis=1)
ax.violinplot(dataset=df_total, vert=False)

ax.set_yticklabels([])
ax.set_xlabel('Total Score')
ax.set_title('Distribution of Total Scores Across All Students')


plt.show()



# Box Plot for Total Scores
fig, ax = plt.subplots(figsize=(12, 8))

ax.boxplot(df.sum(axis=1), vert=False)
ax.set_yticklabels([])
ax.set_xlabel('Total Score')
ax.set_title('Box Plot of Total Scores Across All Students')


plt.show()



# Scatter Plot for Total Scores
fig, ax = plt.subplots(figsize=(12, 8))

total_scores = df.sum(axis=1)
ax.scatter(range(1, len(total_scores) + 1), total_scores, color='green', s=50, alpha=0.7)
ax.set_xlabel('Student')
ax.set_ylabel('Total Score')
ax.set_title('Scatter Plot of Total Scores Across All Students')


plt.show()



# Bar Plot for Total Scores Distribution
fig, ax = plt.subplots(figsize=(12, 8))

total_scores = df.sum(axis=1)
score_counts = total_scores.value_counts().sort_index()

score_counts.plot(kind='bar', ax=ax, color='teal')
ax.set_xlabel('Total Score')
ax.set_ylabel('Number of Students')
ax.set_title('Distribution of Total Scores Across All Students')


plt.show()









