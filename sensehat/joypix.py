#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sense_hat import SenseHat
sense = SenseHat()


# In[2]:


sense.show_message('kevin')


# In[5]:


sense.clear(0, 0, 0)
x, y = 0, 0
while True:
  for event in sense.stick.get_events():
    if event.action == 'released':
      continue
    if event.direction == 'up':
      y = y - 1
    if event.direction == 'down':
      y = y + 1
    if event.direction == 'left':
      x = x - 1
    if event.direction == 'right':
      x = x + 1
    x = x % 8
    y = y % 8
    sense.set_pixel(x, y, 0, 80, 0)
        


# In[ ]:




