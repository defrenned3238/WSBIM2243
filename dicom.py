# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:10:13 2021

@author: Gauthier_Rotsart
"""


import pydicom
import matplotlib as plt
ds = pydicom.read_file("C:/Users/Gauthier_Rotsart/Downloads/data/IM-0001-0001-0001.dcm")
arr = ds.pixel_array
plt.pyplot.imshow(arr)
