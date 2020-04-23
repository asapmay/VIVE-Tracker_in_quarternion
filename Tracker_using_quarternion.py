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
import requests

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
            r=requests.get('https://t4e5p5wd2a.execute-api.ap-northeast-1.amazonaws.com/First/data',params=my_json)
            #r=requests.get('https://dnhe9i3f3m.execute-api.ap-southeast-2.amazonaws.com/First/trackervalue',params=my_json)
            #r=requests.get('https://az5hn67fc3.execute-api.us-east-1.amazonaws.com/First/trackervalue',params=my_json)
            print(txt[3],txt[4],txt[5],txt[6],txt[10],txt[11],txt[12],txt[13],txt[15],txt[17],txt[18],txt[19],txt[20],txt[3]+" "+txt[10]+" "+txt[17])
    
            
            #print(r.url)
            txt.clear()
        except:
             #print("tracker already stop")
             pass             
             '''
             以下加2個tracker        
             '''
             '''
             for each in v.devices["tracker_2"].get_pose_euler():
                 txt2.append("%.4f"  % each)
            my_json={
                "X_axis":txt2[0],
                "Y_axis":txt2[1],
                "Z_axis":txt2[2],
                "X_ro":txt2[3],
                "Y_ro":txt2[4],
                "Z_ro":txt2[5],
                "type":"T2"
            }
                #print("\n" + txt + "T1", end="")
                r2=requests.get('https://j3snu0fq7e.execute-api.ap-northeast-1.amazonaws.com/TrackerTest1/get-tracker-data',params=my_json)
                print(my_json)
                print(r2.url)
                #print("\n" + txt2 + "T2", end="")
            
                
                
                
                for each in v.devices["tracker_3"].get_pose_euler():
                    txt3.append("%.4f"  % each)
                my_json={
                    "X_axis":txt3[0],
                    "Y_axis":txt3[1],
                    "Z_axis":txt3[2],
                    "X_ro":txt3[3],
                    "Y_ro":txt3[4],
                    "Z_ro":txt3[5],
                    "type":"T3"
                }
                #print("\n" + txt + "T1", end="")
                r=requests.get('https://j3snu0fq7e.execute-api.ap-northeast-1.amazonaws.com/TrackerTest1/get-tracker-data',params=my_json)
                print(my_json)
                print(r.url)
                txt3.clear()
                #print("\n" + txt3 + "T3", end="")
                
                print()
                '''
                #sleep_time = interval-(time.time()-start)
                #if sleep_time>0:
                    #time.sleep(sleep_time)
        
        
    
