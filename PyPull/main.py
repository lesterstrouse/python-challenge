
# coding: utf-8

# In[2]:


import os
import csv


# In[3]:


csv_path = os.path.join("..", "election_data.csv")


# In[4]:


count = 0
votes = dict()


# In[5]:


with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)
    #print(csv_header)
    for row in csv_reader:
        count+=1
        votes[row[2]] = votes.get(row[2],0) + 1


# In[7]:


winvotes = 0
for key in votes:
    pct = votes[key]/count*100
    print(f"Candidate {key} with {votes[key]} votes had {pct:.1f}% of vote")
    if votes[key] > winvotes:
        winvotes = votes[key]
        winner = key
print(f"total votes {count}")
print(f"winner {winner}")


# In[13]:


text_path = os.path.join("..", "election_summ.txt")
text_file = open(text_path,'w')
for key in votes:
    pct = votes[key]/count*100
    text_file.write(f"Candidate {key} with {votes[key]} votes had {votes[key]/count*100:.1f}% of vote\n")
text_file.write(f"total votes {count}\n")
text_file.write(f"winner {winner}\n")
text_file.close()

