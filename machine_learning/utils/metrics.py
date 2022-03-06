# Import needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read data in the csv file
# df = pd.read_csv('../data/data.csv')

df = pd.read_csv('../machine_learning/data/data_ROS_2.csv')
print(df.head(10))
print(df.shape)
print("\n")
df.info()

# Check null values
print("\n")
print(df.isnull().sum())    # check null values
print(df['target'].value_counts())   # target value counts
print(df['target'].value_counts() / df.shape[0] * 100)  # Percentage of patients have and do not have heart disease

# Create a pie plot to display the percentage of the positive and negative heart disease
print("\n")
labels = ['yes', 'No']
values = df['target'].value_counts().values
plt.pie(values, labels=labels, autopct='%1.0f%%')
plt.title('Heart Disease')
plt.show()

# Create a pie plot to display the percentage of the positive and negative heart disease count plot
sns.countplot(x="target", data=df)
plt.show()

# Correlation map
plt.figure(figsize=(15, 15))
sns.heatmap(df.corr(), annot=True, cmap="Blues")
plt.show()

# Display age distribution
df['age'].plot(kind='hist', title='Age Distribution')
plt.show()

# Get min, max and average of the age
print("\n")
print('Min age: ', min(df['age']))
print('Max age: ', max(df['age']))
print('Average age: ', df['age'].mean())

# Display age distribution based on heart disease
sns.distplot(df[df['target'] == 1]['age'], label='Do not have heart disease')
sns.distplot(df[df['target'] == 2]['age'], label='Have heart disease')
plt.xlabel('Frequency')
plt.ylabel('Age')
plt.title('Age Distribution based on Heart Disease')
plt.legend()
plt.show()

# Get min, max and average of the age of the people do not have heart disease
print("\nGet min, max and average of the age of the people do not have heart disease\n")
print('Min age of people who do not have heart disease: ', min(df[df['target'] == 1]['age']))
print('Max age of people who do not have heart disease: ', max(df[df['target'] == 1]['age']))
print('Average age of people who do not have heart disease: ', df[df['target'] == 1]['age'].mean())

# Get min, max and average of the age of the people have heart disease
print("\nGet min, max and average of the age of the people have heart disease\n")
print('Min age of people who have heart disease: ', min(df[df['target'] == 2]['age']))
print('Max age of people who have heart disease: ', max(df[df['target'] == 2]['age']))
print('Average age of people who have heart disease: ', df[df['target'] == 2]['age'].mean())

# Number of males and females
F = df[df['sex'] == 0].count()['target']
M = df[df['sex'] == 1].count()['target']
# Create a plot
figure, ax = plt.subplots(figsize=(6, 4))
ax.bar(x=['Female', 'Male'], height=[F, M])
plt.xlabel('Gender')
plt.title('Number of Males and Females in the dataset')
plt.show()

# Display chest pain types in bar chart
df.groupby(df['cp']).count()['target'].plot(kind='bar', title='Chest Pain Types', figsize=(8, 6))
plt.xlabel('Chest Pain Types')
plt.xticks(np.arange(4), ('typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'), rotation=0)
plt.show()

# Display chest pain types based on the target
pd.crosstab(df.cp, df.target).plot(kind="bar", figsize=(8, 6))
plt.title('Heart Disease Frequency According to Chest Pain Type')
plt.xlabel('Chest Pain Type')
plt.xticks(np.arange(4), ('typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'), rotation=0)
plt.ylabel('Frequency')
plt.show()

# Display blood pressure distribution
df['trestbps'].plot(kind='hist', title='Blood Pressure in mm Hg', figsize=(8, 6))
plt.show()

# Display blood pressure distribution based on heart disease
fig, (axis1, axis2) = plt.subplots(1, 2, figsize=(25, 5))
ax = sns.distplot(df[df['target'] == 1]['trestbps'], label='Do not have heart disease', ax=axis1)
ax.set(xlabel='People Do Not Have Heart Disease')
ax = sns.distplot(df[df['target'] == 2]['trestbps'], label='Have heart disease', ax=axis2)
ax.set(xlabel='People Have Heart Disease')
plt.show()

# Get min, max and average of the  blood pressure of the people do not have heart disease
print("\n")
print('Min blood pressure of people who do not have heart disease: ', min(df[df['target'] == 1]['trestbps']))
print('Max blood pressure of people who do not have heart disease: ', max(df[df['target'] == 1]['trestbps']))
print('Average blood pressure of people who do not have heart disease: ', df[df['target'] == 1]['trestbps'].mean())

# Get min, max and average of the blood pressure of the people have heart disease
print("\n")
print('Min blood pressure of people who have heart disease: ', min(df[df['target'] == 2]['trestbps']))
print('Max blood pressure of people who have heart disease: ', max(df[df['target'] == 2]['trestbps']))
print('Average blood pressure of people who have heart disease: ', df[df['target'] == 2]['trestbps'].mean())

# Display Cholesterol distribution
df['chol'].plot(kind='hist', title='Serum Cholestoral in mg/dl', figsize=(8, 6))
plt.show()

# Display Cholesterol distribution based on heart disease
fig2, (axis1, axis2) = plt.subplots(1, 2, figsize=(25, 5))
ax = sns.distplot(df[df['target'] == 1]['chol'], label='Do not have heart disease', ax=axis1)
ax.set(xlabel='People Do Not Have Heart Disease')
ax = sns.distplot(df[df['target'] == 2]['chol'], label='Have heart disease', ax=axis2)
ax.set(xlabel='People Have Heart Disease')
plt.show()

# Get min, max and average of the Cholestoral of the people do not have heart diseas
print('Min cholestoral of people who do not have heart disease: ', min(df[df['target'] == 1]['chol']))
print('Max cholestoral of people who do not have heart disease: ', max(df[df['target'] == 1]['chol']))
print('Average cholestoral of people who do not have heart disease: ', df[df['target'] == 1]['chol'].mean())

# Get min, max and average of the Cholestoral of the people have heart diseas
print('Min cholestoral of people who have heart disease: ', min(df[df['target'] == 2]['chol']))
print('Max cholestoral of people who have heart disease: ', max(df[df['target'] == 2]['chol']))
print('Average cholestorale of people who have heart disease: ', df[df['target'] == 2]['chol'].mean())

# Display fasting blood sugar in bar chart
df.groupby(df['fbs']).count()['target'].plot(kind='bar', title='Fasting Blood Sugar', figsize=(8, 6))
plt.xticks(np.arange(2), ('fbs < 120 mg/dl', 'fbs > 120 mg/dl'), rotation=0)
plt.show()

# Display fasting blood sugar based on the target
pd.crosstab(df.fbs, df.target).plot(kind="bar", figsize=(8, 6))
plt.title('Heart Disease Frequency According to Fasting Blood Sugar')
plt.xlabel('Fasting Blood Sugar')
plt.xticks(np.arange(2), ('fbs < 120 mg/dl', 'fbs > 120 mg/dl'), rotation=0)
plt.ylabel('Frequency')
plt.show()

# Display electrocardiographic results in bar chart
df.groupby(df['restecg']).count()['target'].plot(kind='bar', title='Resting Electrocardiographic Results',
                                                 figsize=(8, 6))
plt.xticks(np.arange(3), ('normal', 'ST-T wave abnormality', 'probable or left ventricular hypertrophy'))
plt.show()

# Display resting electrocardiographic results based on the target
pd.crosstab(df.restecg, df.target).plot(kind="bar", figsize=(8, 6))
plt.title('Heart Disease Frequency According to Resting Electrocardiographic Results')
plt.xticks(np.arange(3), ('normal', 'ST-T wave abnormality', 'probable or left ventricular hypertrophy'))
plt.xlabel('Resting Electrocardiographic Results')
plt.ylabel('Frequency')
plt.show()

# Display maximum heart rate distribution
df['thalach'].plot(kind='hist', title='Maximum Heart Rate Achieved', figsize=(8, 6))
plt.show()

# Display maximum heart rate distribution based on heart disease
fig3, (axis1, axis2) = plt.subplots(1, 2, figsize=(25, 5))
ax = sns.distplot(df[df['target'] == 1]['thalach'], label='Do not have heart disease', ax=axis1)
ax.set(xlabel='People Do Not Have Heart Disease')
ax = sns.distplot(df[df['target'] == 2]['thalach'], label='Have heart disease', ax=axis2)
ax.set(xlabel='People Have Heart Disease')
plt.show()

# Get min, max and average of the maximum heart rate of the people do not have heart disease
print("\n")
print('Min resting blood pressure of people who do not have heart disease: ', min(df[df['target'] == 1]['thalach']))
print('Max resting blood pressure of people who do not have heart disease: ', max(df[df['target'] == 1]['thalach']))
print('Average resting blood pressure of people who do not have heart disease: ',
      df[df['target'] == 1]['thalach'].mean())

# Get min, max and average of the maximum heart rate of the people have heart disease
print("\n")
print('Min maximum heart rate  of people who have heart disease: ', min(df[df['target'] == 2]['thalach']))
print('Max maximum heart rate people who have heart disease: ', max(df[df['target'] == 2]['thalach']))
print('Average maximum heart rate of people who have heart disease: ', df[df['target'] == 2]['thalach'].mean())

# Display exercise induced angina in bar chart
df.groupby(df['exang']).count()['target'].plot(kind='bar', title='Exercise Induced Angina', figsize=(8, 6))
plt.xticks(np.arange(2), ('No', 'Yes'), rotation=0)
plt.show()

# Display exercise induced angina based on the target
pd.crosstab(df.exang, df.target).plot(kind="bar", figsize=(8, 6))
plt.title('Heart Disease Frequency According to Exercise Induced Angina')
plt.xlabel('Exercise Induced Angina')
plt.xticks(np.arange(2), ('No', 'Yes'), rotation=0)
plt.ylabel('Frequency')
plt.show()

# Display ST depression induced by exercise relative to rest distribution
df['oldpeak'].plot(kind='hist', title='ST Depression Induced by Exercise Relative to Rest', figsize=(8, 6))
plt.show()

# Display ST depression distribution based on heart disease
fig4, (axis1, axis2) = plt.subplots(1, 2, figsize=(25, 5))
ax = sns.distplot(df[df['target'] == 1]['oldpeak'], label='Do not have heart disease', ax=axis1)
ax.set(xlabel='People Do Not Have Heart Disease')
ax = sns.distplot(df[df['target'] == 2]['oldpeak'], label='Have heart disease', ax=axis2)
ax.set(xlabel='People Have Heart Disease')
plt.show()

# Get min, max and average of the ST depression  of the people have heart disease
print("\n")
print('Min ST depression of people who do not have heart disease: ', min(df[df['target'] == 1]['oldpeak']))
print('Max ST depression of people who do not have heart disease: ', max(df[df['target'] == 1]['oldpeak']))
print('Average ST depression of people who do not have heart disease: ', df[df['target'] == 1]['oldpeak'].mean())

# Get min, max and average of the ST depression of the people have heart disease
print("\n")
print('Min ST depression of people who have heart disease: ', min(df[df['target'] == 2]['oldpeak']))
print('Max ST depression of people who have heart disease: ', max(df[df['target'] == 2]['oldpeak']))
print('Average ST depression of people not have heart disease: ', df[df['target'] == 2]['oldpeak'].mean())

# Display slope of the peak exercise ST segment in bar chart
df.groupby(df['slope']).count()['target'].plot(kind='bar', title='Slope of the Peak Exercise ST Segment', figsize=(8, 6))
plt.xticks(np.arange(3), ('upsloping', 'flat', 'downsloping'), rotation=0)
plt.show()

# Display slope of the peak exercise ST segment based on the target
pd.crosstab(df.slope, df.target).plot(kind="bar", figsize=(8, 6))
plt.title('Heart Disease Frequency According to Slope of the Peak Exercise ST Segment')
plt.xlabel('Slope')
plt.xticks(np.arange(3), ('upsloping', 'flat', 'downsloping'), rotation=0)
plt.ylabel('Frequency')
plt.show()

# Display number of major vessels in bar chart
df.groupby(df['ca']).count()['target'].plot(kind='bar', title='Number of Major Vessels Colored by Flourosopy', figsize=(8, 6))
plt.show()

# Display number of vessels based on the target
pd.crosstab(df.ca, df.target).plot(kind="bar", figsize=(8, 6))
plt.title('Heart Disease Frequency According to Number of Major Vessels Colored by Flourosopy')
plt.xlabel('number of vessels')
plt.xticks(rotation=0)
plt.ylabel('Frequency')
plt.show()

# Display thalassemia in bar chart
df.groupby(df['thal']).count()['target'].plot(kind='bar', title='Thalassemia')
plt.xticks(np.arange(3), ('normal', 'fixed defect', 'reversible defect'), rotation=0)
plt.show()

# heart disease frequency according to thalassemia
pd.crosstab(df.thal, df.target).plot(kind="bar", figsize=(8, 6))
plt.title('Heart Disease Frequency According to Thalassemia')
plt.xlabel('Thalassemia')
plt.xticks(np.arange(3), ('normal', 'fixed defect', 'reversible defect'), rotation=0)
plt.ylabel('Frequency')
plt.show()

# The correlation between heart disease, cp and exang
g = sns.factorplot("cp", col="exang", col_wrap=3, data=df[df['target'] == 1], kind="count")
plt.xticks(np.arange(4), ('typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'), rotation=0)
g.fig.suptitle('People without Heart Disease', y=1.1)
plt.show()

g = sns.factorplot("cp", col = "exang", col_wrap = 3, data = df[df['target'] == 2], kind = "count")
plt.xticks(np.arange(4), ('typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'), rotation = 0)
g.fig.suptitle('People with Heart Disease', y = 1.1)
plt.show()

# The correlation between oldpeak, slope and target
sns.catplot(x="slope", y="oldpeak", hue="target", data=df)
plt.title('The correlation between oldpeak and slope')
plt.xticks(np.arange(3), ('upsloping', 'flat', 'downsloping'), rotation=0)
plt.show()

# The correlation between ca and age
g = sns.catplot(x='ca', y='age', hue='target', data=df, kind="swarm")
g.fig.suptitle('The correlation between number of major vessels colored by flourosopy and age', y=1.1)
plt.show()

# The correlation between age and thalach
sns.relplot(x='age', y='thalach', data=df, hue='target', legend="full")
plt.title('The correlation between age and heart rate')
plt.show()
