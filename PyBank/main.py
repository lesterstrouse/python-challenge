
# coding: utf-8

# In[11]:


import os
import csv


# In[19]:


count = 0
total = 0
gincrease = 0
gdecrease = 0


# In[12]:


csv_path = os.path.join("..", "budget_data.csv")


# In[26]:


with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)
    #print(csv_header)
    for row in csv_reader:
        count+=1
        amt=int(row[1])
        total+=amt
        if amt > gincrease:
            gincrease = amt
        elif amt < gdecrease:
            gdecrease = amt


# In[28]:


print(f"no of months {count}")
print(f"total increase/decrease {total}")
print(f"average increase/decrease {total/count}")
print(f"greatest increase {gincrease}")
print(f"greatest decrease {gdecrease}")

