#!/usr/bin/env python
# coding: utf-8

# # SPYPY

# ##### https://www.spectralpython.net/fileio.html
# ##### https://www.spectralpython.net/class_func_ref.html?highlight=file%20type

# ## Other capabilities to look into

# * Class labeling
# * Viewing Hypercube (requires wxpython that has had errors installing)

# In[1]:


#import needed libraries
import numpy as np
import matplotlib.pyplot as plt #required for platting
from spectral import * #library for working with hyperspectral data
import spectral.io.aviris as aviris #required for displaying spectrum


# ## Opening Imaging

# In[2]:


img = open_image('/Users/dk/Desktop/MSI_Data/FF_Symeon-f77v_shot03_refl.hdr')


# To open the file you need to open the header file?

# ## Getting Image Data

# In[3]:


#SpyPy does not fully open files due to the file size, unless special commands are used
img.__class__


# In[4]:


#prints the general sata information
print(img)


# Prints information instead of the image since SpyPy does not pull all information into the memory unless specifed. Typically it access the data through the original file to save memeory.

# In[5]:


#(rows, columns, bands)
img.shape


# The SpyPy informations says array starts at 0. So the true number present is +1 of the number returned. Though, this appears to be starting at 1, at least for the bands. The header for this file shows there are 15 total bands.

# ## Selecting Portions of Image

# ### Single Pixel

# In[6]:


#selecting a single pixel (row, column)
pixel = img[50,100]


# In[7]:


#display number of bands at that pixel
pixel.shape


# In[8]:


print(pixel)


# Remeber that SpyPy says the array starts at 0. Verify this is the case since there appears to be a discrepancy with the bands at least.

# Since a pixel is a 1x1 rowxcolun, the shape of a single pixel becomes the number of bands.

# In[9]:


#similar to above, accesses a single pixel
pixel2 = img.read_pixel(50,100)


# In[10]:


pixel2.shape


# In[11]:


print(pixel2)


# ### Single Band Across the Whole Image

# In[12]:


# [:,:,#] where the ":" refers to all rows/columns present
band6 = img[:,:,5]


# Remeber that SpyPy says the array starts at 0. So, to get band 6 you have to call band 5.

# In[13]:


#display the number of rows/columns for a specific band
band6.shape


# Should match the size of the image if not cropping was completed.

# In[14]:


#Reads a single band into an array; similar to method above without maintaining the 3rd deminsion
band7 = img.read_band(6)


# In[15]:


#display the number of rows/columns for a specific band
band7.shape


# ### Multiple Bands Across the Whole Image

# In[16]:


#Reads multiple bands into a 3D array; requires a [LIST] of intergers tp be made
band_set = [1,2,3,4]
band_set = img.read_bands(band_set)


# In[17]:


band_set.shape


# In[18]:


#Reads multiple bands into a 3D array; requires a [LIST] of intergers tp be made
band_set2 = [1,2,3]
band_set2 = img.read_bands(band_set2)


# In[19]:


band_set2.shape


# ## Viewing the Image

# ### Displaying 3 bands as RGB

# In[20]:


#produce image (R, G, B) from the image file
#header file lists bands (7, 5, 3) as the default bands but the band array begins at 0, 
#shifting default bands down by 1
view = imshow(img, (6, 4, 2))


# In[21]:


print(view)


# In[22]:


#produce image (R, G, B) from the image file 
#displaying flourescent bands as false color
#note band array starts at 0, so band numbers are adjusted down 1 from the header file
view2 = imshow(img, (12, 13, 14))


# In[23]:


print(view2)


# ### Create an overlay and display over image

# In[24]:


#designate the band that is meant to be an overlay
#this can be used to overlay graound truth over the image
ol = img.read_band(14)


# In[25]:


view3 = imshow(classes = ol)


# In[26]:


#all of the following must be in the same cell to display properly in Jupyter Notebook
view4 = imshow(img, (6, 4, 2), classes = ol)
#sets the overlay on the image
view4.set_display_mode('overlay')
#sets the overlay level of transparancy, with 0 being fully transparent and 1 being fully opaque
#0.5 is default
view4.class_alpha = 0.5


# In[27]:


#all of the following must be in the same cell to display properly in Jupyter Notebook
view5 = imshow(img, (6, 4, 2), classes = ol)
#sets the overlay on the image
view5.set_display_mode('overlay')
#sets the overlay level of transparancy, with 0 being fully transparent and 1 being fully opaque
#0.5 is default
view5.class_alpha = 0.3





