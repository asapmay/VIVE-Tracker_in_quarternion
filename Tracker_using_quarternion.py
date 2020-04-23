# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:04:37 2020

@author: eppin
"""
import triad_openvr
import math
import numpy as np
import time
import sys

v = triad_openvr.triad_openvr()
v.print_discovered_objects()

if len(sys.argv) == 1:
    interval = 1/8
elif len(sys.argv) == 2:
    interval = 1/float(sys.argv[1])
else:
    print("Invalid number of arguments")
    interval = False
    
if interval:
    count=1
    while(True):
        try:
            start = time.time()
            txt = []       
            #第一個tracker傳值            
            for each in v.devices["tracker_1"].get_pose_quaternion():
                txt.append("%.4f"  % each)       
            for each in v.devices["tracker_2"].get_pose_quaternion():
                txt.append("%.4f"  % each)    
            for each in v.devices["tracker_3"].get_pose_quaternion():
                txt.append("%.4f"  % each)
            #print("start")
            my_json={               
                "X1_axis":txt[0],
                "Y1_axis":txt[1],
                "Z1_axis":txt[2],
                "X1_ro":txt[4]+","+txt[3],
                "Y1_ro":txt[5],
                "Z1_ro":txt[6], 
                "X2_axis":txt[7],
                "Y2_axis":txt[8],
                "Z2_axis":txt[9],
                "X2_ro":txt[11]+","+txt[10],
                "Y2_ro":txt[12],
                "Z2_ro":txt[13],
                "X3_axis":txt[14],
                "Y3_axis":txt[15],
                "Z3_axis":txt[16],
                "X3_ro":txt[18]+","+txt[17],
                "Y3_ro":txt[19],
                "Z3_ro":txt[20],
                "count":count
            }
            #print(type(txt[3]))
                      
            count+=1
            #print("\n" + txt + "T1", end="")      
            print(txt[3],txt[4],txt[5],txt[6],txt[10],txt[11],txt[12],txt[13],txt[15],txt[17],txt[18],txt[19],txt[20],txt[3]+" "+txt[10]+" "+txt[17])              
            #print(r.url)
            txt.clear()
        except:
             #print("tracker already stop")
             pass             
             
                '''
                #sleep_time = interval-(time.time()-start)
                #if sleep_time>0:
                    #time.sleep(sleep_time)
                '''
        
    
