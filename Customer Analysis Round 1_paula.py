#!/usr/bin/env python
# coding: utf-8

# In[106]:


import pandas as pd


# In[107]:


file1 = pd.read_csv('file1.csv')


# In[108]:


display(file1.head())
display(file1.tail())
file1.shape


# In[109]:


file2 = pd.read_csv('file2.csv')


# In[110]:


display(file2.head())
display(file2.tail())
file2.shape


# In[111]:


file3 = pd.read_csv('file3.csv')


# In[112]:


display(file3.head())
display(file3.tail())
file3.shape


# In[113]:


#Standardize header names.
cols1 = []
for column in file1.columns:
    cols1.append(column.lower())
file1.columns = cols1


# In[114]:


column_names=file1.columns
column_names


# In[115]:


#Standardize header names
cols2 = []
for column in file2.columns:
    cols2.append(column.lower())
file2.columns = cols2


# In[116]:


column_names=file2.columns
column_names


# In[117]:


#Standardize header names
cols3 = []
for column in file3.columns:
    cols3.append(column.lower())
file3.columns = cols3
column_names=file3.columns
column_names


# In[118]:


# renaming columns
file1 = file1.rename(columns={'st':'state'})


# renaming columns
file2 = file2.rename(columns={'st':'state'})


# In[119]:


column_names=file1.columns
column_names


# In[ ]:


#Rearrange the columns 


# In[120]:


file2=file2.reindex(columns=['customer', 'state', 'gender', 'education', 'customer lifetime value',
       'income', 'monthly premium auto', 'number of open complaints',
       'policy type', 'vehicle class', 'total claim amount'])


# In[ ]:





# In[121]:


file3=file3.reindex(columns=['customer', 'state', 'gender', 'education', 'customer lifetime value',
       'income', 'monthly premium auto', 'number of open complaints',
       'policy type', 'vehicle class', 'total claim amount'])


# In[122]:


print (file1.columns)
print (file2.columns)
print (file3.columns)


# In[123]:


#Concatenate the three dataframes 
totalfile=pd.concat([file1,file2,file3])


# In[124]:


totalfile.head()


# In[125]:


totalfile.shape


# In[126]:


totalfile.dtypes #categorical are thr object datatypes one and numerical the ones with float datatype


# In[127]:


#Delete columns
totalfile = totalfile.drop(['education','number of open complaints'], axis=1)


# In[128]:


totalfile.head()


# In[131]:


# Correct the values in the column customer lifetime value.
# They are given as a percent, so multiply them by 100 and change dtype to numerical type.
#col = data['customer_lifetime_value'].str.replace('%', '') #* 100
#pd.to_numeric(data['customer_lifetime_value'], errors='coerce')

def clean_column_3(value):
    if type(value) == str and value.find('%') != -1:
        return value.replace('%', '')
    else:
        return value

#data['customer_lifetime_value'] 
totalfile['customer lifetime value'] = totalfile['customer lifetime value'].apply(clean_column_3)

display(totalfile)
#display(totalfile.tail())


# In[137]:


#drop duplicates
totalfile=totalfile.drop_duplicates()


# In[139]:


display(totalfile)


# In[ ]:





# In[146]:


#filter out the data for customers who have an income of 0 or less
totalfile=totalfile[ (totalfile['income']>0)]


# In[147]:


display(totalfile)


# In[ ]:




