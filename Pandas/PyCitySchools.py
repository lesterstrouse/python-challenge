
# coding: utf-8

# # PyCity Schools Analysis
# 
# * As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending per student actually (\$645-675) underperformed compared to schools with smaller budgets (<\$585 per student).
# 
# * As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).
# 
# * As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school. 
# ---

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "../../../schools_complete.csv"
student_data_to_load = "../../../students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single datase
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[3]:


student_data.head()


# In[4]:


school_data.head()


# In[5]:


student_count = school_data_complete['student_name'].count()
school_count = school_data_complete['school_name'].value_counts().count()
total_budget = school_data['budget'].sum()
ave_math = student_data['reading_score'].mean()
ave_read = student_data['math_score'].mean()
over_pass = (ave_math + ave_read)/2
student_passr = student_data.loc[(student_data['reading_score']>69)]['student_name'].count()
student_passm = student_data.loc[(student_data['math_score']>69)]['student_name'].count()
stu_passm_pct = int(student_passm) /int(student_count) * 100
stu_passr_pct = student_passr / student_count * 100                               
record=[{'no students':student_count,'no schools':school_count,'tot budget':total_budget,'ave math':ave_math,'ave read':ave_read,         'overall pass':over_pass,'student pass pct math':stu_passm_pct,'student pass pct reading':stu_passr_pct}]
school_df = pd.DataFrame(record)
school_df


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[6]:


#sch_count_df = pd.DataFrame(school_data_complete['school_name'].value_counts())
sch_group_df = school_data_complete.groupby(['school_name'])
school_type = school_data.set_index("school_name")["type"]
Student_count = sch_group_df['student_name'].count()
school_budget = school_data.set_index("school_name")['budget']
ave_math = sch_group_df['math_score'].mean()
ave_read = sch_group_df['reading_score'].mean()
PerStudent_budg = school_budget/Student_count


# In[10]:


#ave_total = (ave_math + ave_read)/2
passr=school_data_complete.loc[(school_data_complete['reading_score']>69)].groupby('school_name')['student_name'].count().values
passm=school_data_complete.loc[(school_data_complete['math_score']>69)].groupby('school_name')['student_name'].count().values#


# In[21]:


school_dct_sch = {'Type':school_type,'Total Students':Student_count,                'Budget':school_budget,'PerStudent Budget':PerStudent_budg,                 'Average Math Score':ave_math,'Average Reading Score':ave_read,                'Pass Read Cnt':passr,'Pass Math Cnt':passm}
school_df_sch = pd.DataFrame(school_dct_sch)
school_df_sch['Pass Math Pct'] = school_df_sch['Pass Math Cnt']/school_df_sch['Total Students'] * 100
school_df_sch['Pass Read Pct'] = school_df_sch['Pass Read Cnt']/school_df_sch['Total Students'] * 100
school_df_sch['Overall Pass Pct'] = (school_df_sch['Pass Read Pct'] +  school_df_sch['Pass Math Pct'])/2
school_df_ave = school_df_sch.sort_values(by = ['Overall Pass Pct'],ascending=False)
school_df_ave.head()


# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[22]:


school_df_ave.tail()


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[15]:





# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[16]:





# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[17]:


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


# In[18]:





# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[ ]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[19]:





# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[20]:




