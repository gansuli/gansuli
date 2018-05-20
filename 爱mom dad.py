# -*- coding: utf-8 -*-
"""
Created on Sun May 20 19:45:41 2018

@author: asus
"""
print('\n'.join([''.join([('Love dad'[(x-y)%8]
if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 
else' ')
for x in range(-30,30)])
for y in range(15,-15,-1)]))
