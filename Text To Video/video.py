# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:52:53 2021

@author: STC
"""
from nltk import sent_tokenize
from gtts import gTTS
from mutagen.mp3 import MP3
from textblob import TextBlob
from selenium import webdriver
import time
import requests
import os.path
import cv2
import numpy as np
from moviepy.editor import *

doc=''' tripartite cooperation summit centuries Azerbaijan and Turkmenistan Foreign Ministers of Turkey-Azerbaijan-Turkmenistan trilateral cooperation is coming to Ankara today for meetings ANKARA Milliyet Azerbaijani Foreign Minister Ceyhun Bayramov and Turkmenistan Foreign Minister Rashid Meredov today Turkey-Azerbaijan-Turkmenistan trilateral cooperation meeting in Ankara will come to Ankara for. In a written statement made by the Foreign Bakanhğı, Turkmenistan Cabinet of Ministers and Foreign Minister Rashid Meredov, the Vice President, stated today it will organize a visit to Turkey. During the visit, bilateral talks, bilateral relations between Turkey and Turkmenistan with the recorded statement is scheduled to exchange views on regional issues, the Meredov, by President Recep Tayyip Erdogan was quoted as predicting acceptance. In a statement, visit the occasion of the Azerbaijani Foreign Minister Ceyhun Bayramov with the participation of Turkey-Azerbaijan-Turkmenistan Trilateral 5. Meeting also will be held, Foreign Bakau I Mevlut Cavusoglu also was expressed to hold bilateral meetings with Bayramov. During the meetings, it was noted that developments in relations between countries and regional issues and steps that can be taken to further improve cooperation will be discussed in bilateral and triple format. '''

#divide into sent
sentList =sent_tokenize(doc)


def create_Audio(sent,audioName):
    tts = gTTS(text=sent, lang='en')
    audioName="AudioSent"+str(i)+'.mp3'
    savePath='C:/Users/STC/Desktop/TextToSp/'+audioName
    tts.save(savePath)

def Audio_Time(audioName):
    audio = MP3("C:/Users/STC/Desktop/TextToSp/"+audioName)
    return (audio.info.length)

def KeyWords(sent):
    blob = TextBlob(sent)
    nos=blob.noun_phrases
    return(nos)
    
def search_google(search_query):
    browser = webdriver.Chrome("D:\chromDriver\chromedriver.exe")
    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
    images_url = []

    # open browser and begin search
    browser.get(search_url)
    elements = browser.find_elements_by_class_name('rg_i')
    

    count = 0
    for e in elements:
        # get images source url
        e.click()
        time.sleep(8)
        
        element = browser.find_elements_by_class_name('v4dQwb')

        # Google image web site logic
        if count == 0:
            big_img = element[0].find_element_by_class_name('n3VNCb')
        else:
           big_img = element[1].find_element_by_class_name('n3VNCb')

        images_url.append(big_img.get_attribute("src"))

        # write image to file
        reponse = requests.get(images_url[count])
        if reponse.status_code == 200:
            with open(f"search{count+1}.jpg","wb") as file:
                file.write(reponse.content)

        count += 1

        # Stop get and save after 5
        if count == 1:
            
            browser.quit()
            break
    
    return images_url



def Save_Pics(url,sentNum,wordNum):
    r = requests.get(url)
    save_path = 'C:/Users/STC/Desktop/TextToSp'
    name_of_file =  "sent"+str(sentNum)+'word'+str(wordNum)
    completeName = os.path.join(save_path, name_of_file+".jpg")
    with open(completeName, "wb") as f:
        f.write(r.content)
    return(name_of_file)
        
scenes=[]  

for i in range(len(sentList)):
    sent=sentList[i]
    audioName="AudioSent"+str(i)+'.mp3'
    create_Audio(sent,audioName)
    AduoTime= Audio_Time(audioName)
    keywords=KeyWords(sent)
    ImagesNmame=[]
    for w in range(len(keywords)):
        Imagesurl = search_google(keywords[w])
        image=Save_Pics(Imagesurl[0],i,w)
        ImagesNmame.append(image)
    sentInfo = {'sentEng':sent ,'audioName':audioName , 'AduoTime':AduoTime, 'keyWords':keywords,'ImagesNmame':ImagesNmame,}
    scenes.append(sentInfo)



clips=[]
def Create_Vid(scenes):
    filePath='C:/Users/STC/Desktop/TextToSp/'
    for i in range(len(scenes)):
        imageNames=scenes[i]['ImagesNmame']
        img=[]
        for w in range(len(imageNames)):
            completPath=filePath+imageNames[w]+'.jpg'
            img.append(cv2.imread(completPath))
        height, width, layers = img[i].shape
        size = (width,height)
        clipPath=filePath+'sent'+str(i)+'clip'+'.mp4'
        out = cv2.VideoWriter(clipPath,cv2.VideoWriter_fourcc(*'DIVX'), 1.0, size)

        sentTime=scenes[i]['AduoTime']
        
        each_image_duration = int(round(sentTime/len(img))) # in secs
        for x in range(len(img)):
            image=cv2.resize(img[x],size)
            for _ in range(each_image_duration):
                out.write(image)
        out.release()
        clips.append(clipPath)


Create_Vid(scenes)


ReadyToJoin=[]
def Add_Audio(clips,scenes):
    for i in range(len(clips)):
        filePath='C:/Users/STC/Desktop/TextToSp/'
        audioPath=filePath+scenes[i]['audioName']
            # loading video dsa gfg intro video 
        clip = VideoFileClip(clips[i]) 
          
          
        # getting only first 5 seconds 
        
          
        # loading audio file 
        audioclip = AudioFileClip(audioPath)
          
        # adding audio to the video clip 
        videoclip = clip.set_audio(audioclip) 
          
        outFile=filePath+'clib'+str(i)+'withsound'+'.mp4'
        videoclip.write_videofile(outFile)
        ReadyToJoin.append(outFile)
        
Add_Audio(clips,scenes)
    



from moviepy.editor import VideoFileClip, concatenate_videoclips
video_1 = VideoFileClip("C:/Users/STC/Desktop/TextToSp/clib0withsound.mp4")
video_2 = VideoFileClip("C:/Users/STC/Desktop/TextToSp/clib1withsound.mp4")
final_video= concatenate_videoclips([video_1, video_2])
final_video.write_videofile("C:/Users/STC/Desktop/TextToSp/finallllllll.mp4")


# Import everything needed to edit video clips 
from moviepy.editor import *
  
  
# getting subclip as video is large 
clip1 = VideoFileClip("C:/Users/STC/Desktop/TextToSp/clib0withsound.mp4") 
  
# getting subclip as video is large 
clip2 = VideoFileClip("C:/Users/STC/Desktop/TextToSp/clib1withsound.mp4")

clip3 = VideoFileClip("C:/Users/STC/Desktop/TextToSp/clib2withsound.mp4")

  
# concatinating both the clips 
final = concatenate_videoclips([clip1, clip2]) 
final.write_videofile("C:/Users/STC/Desktop/TextToSp/finallllllll.mp4")
