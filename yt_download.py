# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:13:07 2022

@author: Aryanand
"""

from pytube import YouTube
import os

def download(link):
    count=1

    for i in links:
    
        try:
            yt=YouTube(i)
            yt.streams.filter(progressive=True,file_extension='mp4')
        
            high_res=yt.streams.get_highest_resolution()
        except:
                print("Connection Error")
  
        try:
            high_res.download(PATH)
            print(count," Completed!")
            count=count+1
        except:
            print("Downloading Error!")
            return 0
            
    return 1
         
print("Welcome to Aryanand Downloader")
#Download file on desktop
PATH=os.path.join(os.path.join(os.path.expanduser('~')), "Desktop\Aryanand Downloader") 
#Text file with Links(PATH)   
links=open('D:\\PYTHON exps\\YT DOWNLOADER\\YT LINK.txt','r')
flag=1

flag=download(links)
if flag==1:
    print("Task Completed!")
if flag==0:
    print("Task Failed! Retry?(y/n)")
    choice=input()
    if choice=='y':
        download(links)