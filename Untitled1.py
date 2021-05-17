#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd

data = pd.read_csv('simpsons.csv')

data = data.drop('Unnamed: 0', axis=1)
x = data.drop('gender', axis=1)
y = data['gender']

print(x)
print(y)


# In[9]:


from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier(criterion = 'entropy')#criterion=기준
dtc.fit(x,y)#x=training data, y=answer


# In[10]:


from sklearn import tree

tree.plot_tree(dtc, feature_names=['hair_length', 'weight','age'])


# In[11]:


from sklearn import tree

tree.plot_tree(dtc,feature_names=x.columns)


# In[12]:


from sklearn.tree import export_graphviz

export_graphviz(dtz,
               out_file='dicision_tree.dot',
               feature_names = x.columns,
               rounded = True)


# In[ ]:




