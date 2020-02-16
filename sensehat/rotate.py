#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sense_hat import SenseHat

sense = SenseHat()


# In[2]:


def normalize(g):
    color = (1 + g) * 128;
    if color < 0:
        color = 0;
    if color > 255:
        color = 255;
    return int(color)


# In[3]:


while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
  
    color = [normalize(g) for g in [x, y, z]]
    sense.clear((color))


# In[ ]:




