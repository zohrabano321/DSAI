#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
pil_img = Image.open("D:\Python\download.jpg")


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
gb=np.array(pil_img)
plt.imshow(gb)


# In[3]:


gb.shape


# In[27]:


plt.imshow(gb[20:80, 150:200,:])


# In[28]:


gb[100,100]


# In[29]:


plt.imshow(gb[:,:,0])


# In[5]:


plt.figure(figsize=(5,5))


# In[9]:


A=gb


# In[10]:


id(A) == id(gb)


# In[11]:


B = gb.copy()
id(B)==id(gb)


# In[12]:


gb[:,:,] = 0


# In[14]:


plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(gb)
plt.title("Ghizer")
plt.subplot(122)
plt.imshow(A)
plt.title("Gilgit")
plt.show()


# In[16]:


plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(gb)
plt.title("Ghizer")
plt.subplot(122)
plt.imshow(B)
plt.title("Gilgit")
plt.show()


# In[17]:


#flipping
image = Image.open("D:\data science\download.jpg")
plt.figure(figsize=(6,6))
plt.imshow(image)
plt.show()


# In[18]:


array = np.array(image)
width, height, C = array.shape
print('width', width ,'height and Channel', height, C)


# In[24]:


array_flip = np.zeros((width, height, C), dtype=np.uint8)


# In[25]:


for i,row in enumerate(array):
    array_flip[width - 1 - i, :, :] = row
  


# In[26]:


array_flip


# In[27]:


from PIL import ImageOps


# In[28]:


im_flip = ImageOps.flip(image)
plt.figure(figsize=(5,5))
plt.imshow(im_flip)
plt.show()


# In[29]:


im_mirror = ImageOps.mirror(image)
plt.figure(figsize=(5,5))
plt.imshow(im_mirror)
plt.show()


# In[30]:


im_flip = image.transpose(1)
plt.imshow(im_flip)
plt.show()


# In[31]:


flip = {"FLIP_LEFT_RIGHT": Image.FLIP_LEFT_RIGHT,
        "FLIP_TOP_BOTTOM": Image.FLIP_TOP_BOTTOM,
        "ROTATE_90": Image.ROTATE_90,
        "ROTATE_180": Image.ROTATE_180,
        "ROTATE_270": Image.ROTATE_270,
        "TRANSPOSE": Image.TRANSPOSE,
        "TRANSVERSE": Image.TRANSVERSE}


# In[32]:


flip["FLIP_LEFT_RIGHT"]


# In[33]:


for key, values in flip.items():
    plt.figure(figsize=(10,10))
    plt.subplot(1,2,1)
    plt.imshow(image)
    plt.title("orignal")
    plt.subplot(1,2,2)
    plt.imshow(image.transpose(values))
    plt.title(key)
    plt.show()


# In[34]:


upper = 50
lower = 100
crop_top = array[upper: lower,:,:]
plt.figure(figsize=(5,5))
plt.imshow(crop_top)
plt.show()


# In[35]:


left = 50
right = 100
crop_horizontal = crop_top[: ,left:right,:]
plt.figure(figsize=(5,5))
plt.imshow(crop_horizontal)
plt.show()


# In[37]:


image = Image.open("D:\data science\download.jpg")
crop_image = image.crop((left, upper, right, lower))
plt.figure(figsize=(5,5))
plt.imshow(crop_image)
plt.show()


# In[38]:


crop_image = crop_image.transpose(Image.FLIP_LEFT_RIGHT)
crop_image


# In[ ]:




