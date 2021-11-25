#!/usr/bin/env python
# coding: utf-8

# Revision

# In[1]:


# Add elements of 2 lists
ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
ls3 = []
for i in range(len(ls1)):
    ls3.append(ls1[i] + ls2[i])
    
ls3


# In[2]:


# Simple Calculator
operation = input('Enter the operation: ')
op1 = float(input('Enter 1st operand: '))
op2 = float(input('Enter 2nd operand: '))

if operation == "+":
    print(op1 + op2)
elif operation == "-":
    print(op1 - op2)
elif operation == "*":
    print(op1 * op)
elif operation == "/":
    if op2 == 0:
        print('Cannot Divide by Zero')
    else:
        print(op1 / op2)
else:
    print('Invalid Operation')


# In[3]:


# Bubble Sort
list = [4,8,1,5,2,7,9,3]

def bsort(list):
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            if list[i]>list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

print(bsort(list))


# Program 1
# 

# In[4]:


# Mean, Median, Mode
data = [115.3, 195.5, 120.5, 110.2, 90.4, 105.6, 110.9, 116.3, 122.3, 125.4]
mean = 0.0
median = 0
mode = 0

sort_data = bsort(data)
long = len(data)

for i in data:
    mean = sum(data) / long
    
if long % 2 == 0:
    median = (data[(long//2) - 1] + data[long//2]) / 2
else:
    median = data[long//2]

mode_dict = {}

for i in data:
    if not i in mode_dict:
        mode_dict[i] = 1
    else:
        mode_dict[i] += 1 

maxi = 0

for i in mode_dict:
    if mode_dict[i] > maxi:
        maxi = mode_dict[i]
        mode = i
        
print('Mean:', mean)
print('Median:', median)
print('Mode:', mode)


# In[5]:


# Standard Deviation
temp = 0

for i in range(0, long):
    temp = temp + ((data[i] - mean) ** 2)

variance = temp / long
sd = (variance) ** (1/2)

print('Variance:', variance)
print('Standard Deviation:', sd)


# In[6]:


# Validation
import numpy as np
from scipy import stats


# In[7]:


print(np.mean(data))
print(np.median(data))
print(stats.mode(data).mode[0],'-->',stats.mode(data).count[0], 'times')
print(np.var(data))
print(np.std(data))


# In[8]:


# Min-Max Normalisation
minimum = data[0]
maximum = data[0]

for i in range(0, long):
    if data[i] > maximum:
        maximum = data[i]
    if data[i] < minimum:
        minimum = data[i]

min_max_normal = []
for i in range(0, long):
    min_max_normal.append((data[i] - minimum) / (maximum - minimum))

print('Min Max Normalisation:\n', min_max_normal)


# In[9]:


# Standardisation
standard = []
for i in range(0, long):
    standard.append((data[i] - mean) / sd)
    
print('Standardisation:\n', standard)


# In[ ]:




