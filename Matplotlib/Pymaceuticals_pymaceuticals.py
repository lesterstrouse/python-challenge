
# coding: utf-8

# In[2]:


# Dependencies and Setup
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats 
# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
mouse_drug_data_to_load = "../../../mouse_drug_data.csv"
clinical_trial_data_to_load = "../../../clinicaltrial_data.csv"
 
# Read the Mouse and Drug Data and the Clinical Trial Data
mouse_drug_data = pd.read_csv(mouse_drug_data_to_load)
clinical_trial_data = pd.read_csv(clinical_trial_data_to_load)
# Combine the data into a single dataset
mouse_clin_data = pd.merge(clinical_trial_data,mouse_drug_data,how ='outer',on = ['Mouse ID','Mouse ID'])

# Display the data table for preview

mouse_clin_data.head()


# ## Tumor Response to Treatment

# In[3]:


# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 
mouse_clin_grp = mouse_clin_data.groupby(['Drug','Timepoint']).mean()
# Convert to DataFrame
mouse_clin_grp.reset_index(inplace=True)
mouse_clin_grp_df = pd.DataFrame(mouse_clin_grp)
# Preview DataFram
mouse_clin_grp_df.head()


# In[4]:


mouse_clin_grp_final = mouse_clin_grp_df.drop(columns =['Metastatic Sites'])
mouse_clin_grp_final.head()


# In[5]:


# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
mouse_clin_sem = mouse_clin_data.groupby(['Drug','Timepoint'])['Tumor Volume (mm3)'].sem()
# Convert to DataFrame
mouse_clin_sem_reset = mouse_clin_sem.reset_index()
mouse_clin_sem_df = pd.DataFrame(mouse_clin_sem_reset)
# Preview DataFrames
mouse_clin_sem_df.head()


# In[6]:


# Minor Data Munging to Re-Format the Data Frames
mc_sem_df = mouse_clin_sem_df.pivot(columns="Drug",index='Timepoint')
# Preview that Reformatting worked
mc_sem_df.head()


# In[7]:


mc_grp_final_df = mouse_clin_grp_final.pivot(columns='Drug',index='Timepoint')
mc_grp_final_df.head()


# In[20]:


# Generate the Plot (with Error Bars)
#x_lim = 50
#y_lim = 80
#x_axis = np.arange(0,x_lim,10)
#plt.title('Tumor Response to Treatment')
#plt.xlim = (0,x_lim)
#plt.ylim = (30,y_lim)
mc_grp_final_df.plot(grid=True,title="Tumor Response to Treatment",figsize=(15,5))
# Save the Figure
plt.savefig('tumorplot.png')


# In[9]:


# Show the Figure
#plt.show()


# ## Metastatic Response to Treatment

# In[10]:


# Store the Mean Met. Site Data Grouped by Drug and Timepoint 
mc_grpm = mouse_clin_grp_df.drop(columns =['Tumor Volume (mm3)'])
mc_grpm.head()
# Convert to DataFrame

# Preview DataFrame


# In[11]:


# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint 
mc_semm = mouse_clin_data.groupby(['Drug','Timepoint'])['Metastatic Sites'].sem()
# Preview DataFrames
mc_semm_reset = mc_semm.reset_index()
# Convert to DataFrame
mc_semm_df = pd.DataFrame(mc_semm_reset)
# Preview DataFrame
mc_semm_df.head()


# In[12]:


# Minor Data Munging to Re-Format the Data Frames
mc_grpm_df = mc_grpm.pivot(columns='Drug',index='Timepoint')
# Preview that Reformatting worked
mc_grpm_df.head()


# In[18]:


# Generate the Plot (with Error Bars)
mc_grpm_df.plot(grid=True,figsize =(10,5),title='Metastatic Spread During Treatment')
# Save the Figure
plt.savefig('metaplot.png')
# Show the Figure


# In[9]:





# ## Survival Rates

# In[14]:


# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)
mouse_clin_grp_cnt = mouse_clin_data.groupby(['Drug','Timepoint'])['Mouse ID'].count()
# Convert to DataFrame
mc_grp_cnt = mouse_clin_grp_cnt.reset_index()
mc_grp_cnt_df = pd.DataFrame(mc_grp_cnt)
# Preview DataFrame
mc_grp_cnt_df.head()


# In[10]:





# In[15]:


# Minor Data Munging to Re-Format the Data Frames
mc_grp_cnt_pivot = mc_grp_cnt_df.pivot(columns='Drug',index='Timepoint')
# Preview the Data Frame
mc_grp_cnt_pivot


# In[11]:





# In[21]:


# Generate the Plot (Accounting for percentages)
mc_grp_cnt_pivot.plot(grid=True,figsize=(10,5),title='Survival During Treatment')
# Save the Figure
plt.savefig('mousecnt.png')
# Show the Figure
#plt.show()


# In[12]:





# ## Summary Bar Graph

# In[17]:


# Calculate the percent changes for each drug
#print(type(mouse_clin_grp_final))
mc_grp_tumor = mouse_clin_grp_final['Tumor Volume (mm3)'].pct_change()
# Display the data to confirm
mouse_clin_grp_final['Pct Chg'] = mc_grp_tumor#mouse_clin_grp_final['Tumor Volume (mm3)'].pct_change
mouse_clin_grp_final.head()


# In[ ]:


# Store all Relevant Percent Changes into a Tuple


# Splice the data between passing and failing drugs


# Orient widths. Add labels, tick marks, etc. 


# Use functions to label the percentages of changes


# Call functions to implement the function calls


# Save the Figure


# Show the Figure
fig.show()


# In[14]:




