
# coding: utf-8

# In[1]:


import numpy as np


# In[14]:


#1. 將下兩列 array存成npz檔


# array1 = np.array(range(30))
# 
# array2 = np.array([2,3,5])

# In[3]:


array1 = np.array(range(30))
array2 = np.array([2,3,5])


# In[50]:


np.savez("hw6",array1, array2)


# In[51]:


with open('hw6.npz', 'wb') as h:
    np.savez(h, x=array1, y=array2)


# In[15]:


#2. 讀取剛剛的npz檔，加入array3一起存成新的npz檔


# In[23]:


heyho = np.load('hw6.npz')
type(heyho)


# In[24]:


heyho.files


# In[25]:


print(heyho['x'])


# In[26]:


print(heyho['y'])


# In[28]:


array3 =  np.arange(0, 6, 1.5)


# In[44]:


array3


# In[56]:


np.savez('hw6_2',heyho['x'], heyho['y'], array3)


# In[57]:


hoho = np.load('hw6_2.npz')
type(hoho)


# In[58]:


hoho.files


# In[59]:


print(hoho['arr_0'])


# In[60]:


print(hoho['arr_2'])

