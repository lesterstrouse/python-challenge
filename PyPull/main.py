
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


csv_path = os.path.join("..", "election_data.csv")


# In[3]:


count = 0
total = 0
votes = dict()


# In[4]:


with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)
    #print(csv_header)
    for row in csv_reader:
        count+=1
        votes[row[2]] = votes.get(row[2],0) + 1


# In[6]:


print(votes)
print(count)

