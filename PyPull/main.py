
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


csv_path = os.path.join("..", "election_data.csv")


# In[3]:


count = 0
votes = dict()


# In[4]:


with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)
    #print(csv_header)
    for row in csv_reader:
        count+=1
        votes[row[2]] = votes.get(row[2],0) + 1


# In[42]:


winvotes = 0
for key in votes:
    pct = votes[key]/count*100
    print(f"{key},{votes[key]},{pct:.1f}")
    if votes[key] > winvotes:
        winvotes = votes[key]
        winner = key
print(f"total votes {count}")
print(f"winner {winner}")

