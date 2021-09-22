from gtts import gTTS
import os

from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest

from nltk import tokenize
from operator import itemgetter
import math

# change to voice 

def create_Audio(sent):
    document=""" HDP'li Taşdemir'e soruşturma açıldı NAMIK DURUKAN Ankara İçişleri Bakanı Süleyman Soylu'nun "Gara'ya giden milletvekili" olarak ismini açıkladığı HDP Ağrı Milletvekili Dirayet Dilan Taşdemir hakkında "silahlı terör örgütü üyesi olmak" suçundan soruşturma başlatıldı. İçişleri Bakanı Soylu önceki akşam bir televizyon programına katıldı. Soylu programda 2017'de terör örgütüne katılan ve bir süre önce güvenlik güçlerine teslim olan bir teröristin, "Gara'dan birisiyle arabaya biniyorlar. Yanındaki diyor ki 'Bunu tanıdın mı?', 'Hayır tanımadım' deyince bu Dirayet Dilan Taşdemir, HDP Ağrı Milletvekili diyor" şeklindeki ifadesini anlattı. Ankara Cumhuriyet Başsavcılığı Soylu'nun açıklamalarını Dirayet Dilan Taşdemir BULDAN: SALI DAHA FAZLASINI AÇIKLAYACAĞIM HDP Eş Genel Başkanı Pervin Buldan İse Twitter'dan yaptığı açıklamada "İçişleri Bakanı'mn katıldığı programda gösterdiği resimlerin tamamı çözüm sürecinde Erdoğan'ın bilgisi ve onayı ile gittiğimiz Kandil fotoğraflarıdır. Ben salı günü grup toplantımızda daha fazlasını açıklayacağım" ifadelerini kullandı. ihbar ederek Taşdemir hakkında soruşturma başlattığım duyurdu. Açıklamada 20 Şubat'ta ulusal bir televizyon kanalındaki programda, Taşdemir'in PKK/KCK silahlı terör örgütü mensuplarının bulunduğu ve Türk Silahlı Kuvvetleri tarafından operasyon yapılan Irak'ın Gara bölgesine gittiğinin açıklandığı kaydedildi. Söz konusu açıklama ihbar kabul edilerek Taşdemir hakkında, 5237 sayılı Türk Ceza Kanunu'nun 314/2 maddesi kapsamında "silahlı terör örgütü üyesi olmak" suçundan soruşturma başlatıldığı kaydedildi. 'Külliyen yalan' HDP Ağrı Milletvekili Dilan Dirayet Taşdemir de Twitter hesabından, "Bunun kocaman bir yalan ve iftira olduğunu göstereceğiz" mesajını paylaştı. Taşdemir, Milliyet'e yaptığı açıklamada ise, şöyle konuştu: "Tamamıyla yalan. Partimizi hedefe koyan bir açıklama. Operasyonun siyasi sorumluluğunu üstünden atmak için hedef şaşırtamaya yöneliktir. Külliyen yalan. Dedikodu ve şovla algı yönetmeye yöneliktir. Detaylı bir açıklama yapacağız. Tamamıyla iftira ve hayal ürünü." HDP'li Taşdemir'e soruşturma açı İd! kaüld^ Soylu programda 2017'de terör örgütüne katılan ve bir sü- ihbar ederek Taşdemir hakkında Taşdemir hakkında, 5237 sayılı ceğiz" mesajını paylaştı. Taşdemir re önce güvenlik güçlerine tes- soruşturma başlattığım duyurdu. Türk Ceza Kanunu'nun 314/2 Milliyet'e yaptığı açıklamada ise lim olan bir teröristin, "Gara'dan Açıklamada 20 Şubat'ta ulusal bir maddesi kapsamında "silahlı terör şöyle konuştu: "Tamamıyla yalan birisiyle arabaya biniyorlar. Ya- televizyon kanalındaki program- örgütü üyesi olmak" suçundan so- Partimizi hedefe koyan bir açıkla- nındaki diyor ki 'Bunu tanıdın da, Taşdemir'in PKK/KCK silahlı ruşturma başlatıldığı kaydedildi. ma. Operasyonun siyasi sorumlu- mı?', 'Hayır tanımadım' deyince terör örgütü mensuplarının bu- ır"iı« "I > luğunu üstünden atmak için hede] bu Dirayet Dilan Taşdemir, HDP lunduğu ve Türk Silahlı Kuvvet- JvUlliyen yalan şaşırtamaya yöneliktir. Külliyen Ağrı Milletvekili diyor" şeklindeki leri tarafından operasyon yapılan HDP Ağrı Milletvekili Dilan yalan. Dedikodu ve şovla algı yö- ifadesini anlattı. Irak'ın Gara bölgesine gittiğinin Dirayet Taşdemir de Twitter he- netmeye yöneliktir. Detaylı biı Ankara Cumhuriyet Başsav- açıklandığı kaydedildi. Söz konu- sabmdan, "Bunun kocaman bir açıklama yapacağız. Tamamıyla cılıeı Soylu'nun açıklamalarını su açıklama ihbar kabul edilerek yalan ve iftira olduğunu göstere- iftira ve hayal ürünü." """
    tts = gTTS(text=sent, lang='tr')
    tts.save("news2.mp3")


# search words
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('turkish') 

document=""" HDP'li Taşdemir'e soruşturma açıldı NAMIK DURUKAN Ankara İçişleri Bakanı Süleyman Soylu'nun "Gara'ya giden milletvekili" olarak ismini açıkladığı HDP Ağrı Milletvekili Dirayet Dilan Taşdemir hakkında "silahlı terör örgütü üyesi olmak" suçundan soruşturma başlatıldı. İçişleri Bakanı Soylu önceki akşam bir televizyon programına katıldı. Soylu programda 2017'de terör örgütüne katılan ve bir süre önce güvenlik güçlerine teslim olan bir teröristin, "Gara'dan birisiyle arabaya biniyorlar. Yanındaki diyor ki 'Bunu tanıdın mı?', 'Hayır tanımadım' deyince bu Dirayet Dilan Taşdemir, HDP Ağrı Milletvekili diyor" şeklindeki ifadesini anlattı. Ankara Cumhuriyet Başsavcılığı Soylu'nun açıklamalarını Dirayet Dilan Taşdemir BULDAN: SALI DAHA FAZLASINI AÇIKLAYACAĞIM HDP Eş Genel Başkanı Pervin Buldan İse Twitter'dan yaptığı açıklamada "İçişleri Bakanı'mn katıldığı programda gösterdiği resimlerin tamamı çözüm sürecinde Erdoğan'ın bilgisi ve onayı ile gittiğimiz Kandil fotoğraflarıdır. Ben salı günü grup toplantımızda daha fazlasını açıklayacağım" ifadelerini kullandı. ihbar ederek Taşdemir hakkında soruşturma başlattığım duyurdu. Açıklamada 20 Şubat'ta ulusal bir televizyon kanalındaki programda, Taşdemir'in PKK/KCK silahlı terör örgütü mensuplarının bulunduğu ve Türk Silahlı Kuvvetleri tarafından operasyon yapılan Irak'ın Gara bölgesine gittiğinin açıklandığı kaydedildi. Söz konusu açıklama ihbar kabul edilerek Taşdemir hakkında, 5237 sayılı Türk Ceza Kanunu'nun 314/2 maddesi kapsamında "silahlı terör örgütü üyesi olmak" suçundan soruşturma başlatıldığı kaydedildi. 'Külliyen yalan' HDP Ağrı Milletvekili Dilan Dirayet Taşdemir de Twitter hesabından, "Bunun kocaman bir yalan ve iftira olduğunu göstereceğiz" mesajını paylaştı. Taşdemir, Milliyet'e yaptığı açıklamada ise, şöyle konuştu: "Tamamıyla yalan. Partimizi hedefe koyan bir açıklama. Operasyonun siyasi sorumluluğunu üstünden atmak için hedef şaşırtamaya yöneliktir. Külliyen yalan. Dedikodu ve şovla algı yönetmeye yöneliktir. Detaylı bir açıklama yapacağız. Tamamıyla iftira ve hayal ürünü." HDP'li Taşdemir'e soruşturma açı İd! kaüld^ Soylu programda 2017'de terör örgütüne katılan ve bir sü- ihbar ederek Taşdemir hakkında Taşdemir hakkında, 5237 sayılı ceğiz" mesajını paylaştı. Taşdemir re önce güvenlik güçlerine tes- soruşturma başlattığım duyurdu. Türk Ceza Kanunu'nun 314/2 Milliyet'e yaptığı açıklamada ise lim olan bir teröristin, "Gara'dan Açıklamada 20 Şubat'ta ulusal bir maddesi kapsamında "silahlı terör şöyle konuştu: "Tamamıyla yalan birisiyle arabaya biniyorlar. Ya- televizyon kanalındaki program- örgütü üyesi olmak" suçundan so- Partimizi hedefe koyan bir açıkla- nındaki diyor ki 'Bunu tanıdın da, Taşdemir'in PKK/KCK silahlı ruşturma başlatıldığı kaydedildi. ma. Operasyonun siyasi sorumlu- mı?', 'Hayır tanımadım' deyince terör örgütü mensuplarının bu- ır"iı« "I > luğunu üstünden atmak için hede] bu Dirayet Dilan Taşdemir, HDP lunduğu ve Türk Silahlı Kuvvet- JvUlliyen yalan şaşırtamaya yöneliktir. Külliyen Ağrı Milletvekili diyor" şeklindeki leri tarafından operasyon yapılan HDP Ağrı Milletvekili Dilan yalan. Dedikodu ve şovla algı yö- ifadesini anlattı. Irak'ın Gara bölgesine gittiğinin Dirayet Taşdemir de Twitter he- netmeye yöneliktir. Detaylı biı Ankara Cumhuriyet Başsav- açıklandığı kaydedildi. Söz konu- sabmdan, "Bunun kocaman bir açıklama yapacağız. Tamamıyla cılıeı Soylu'nun açıklamalarını su açıklama ihbar kabul edilerek yalan ve iftira olduğunu göstere- iftira ve hayal ürünü." """

doc='''An investigation was launched against HDP's Taşdemir NAMIK DURUKAN An investigation was launched against HDP Ağrı Deputy Dirayet Dilan Taşdemir, whose name was announced by Ankara Minister of Interior Süleyman Soylu as "the deputy who went to Gara", on charges of "being a member of an armed terrorist organization". Interior Minister Soylu attended a television program the previous evening. In the Soylu program, a terrorist who joined the terrorist organization in 2017 and surrendered to the security forces a while ago, "They are getting into the car with someone from Gara. When he says 'Do you recognize this?', 'No, I do not', this is Dirayet Dilan Taşdemir, HDP Agri MP. he says "he told his expression as. Ankara Chief Public Prosecutor's Office Soylu's statements Dirayet Dilan Taşdemir BULDAN: I WILL EXPLAIN MORE ON TUESDAY HDP Co-Chair Pervin Buldan said on Twitter, "All of the pictures shown in the program attended by the Minister of Interior are Kandil photographs that we went with Erdogan's knowledge and approval during the solution process. "I'll explain more in our group meeting on Tuesday." he announced that I started an investigation against Taşdemir. In the statement, it was recorded that on February 20, in a program on a national television channel, it was announced that Taşdemir had gone to the Gara region of Iraq where PKK / KCK armed terrorist organization members were present and were operated by the Turkish Armed Forces. The statement in question was accepted as a notice and it was noted that an investigation was initiated against Taşdemir for "being a member of an armed terrorist organization" within the scope of Article 314/2 of the Turkish Penal Code No. 5237. HDP Ağrı Deputy Dilan Dirayet Taşdemir shared the message, "We will show that this is a huge lie and slander" on his Twitter account. In his statement to Milliyet, Taşdemir said: "It is completely a lie. A statement that puts our party on the target. The target is to confuse the political responsibility of the operation. The complex is a lie. It is aimed at managing the perception with gossip and show. We will make a detailed explanation. figment." An investigation is opened against HDP's Taşdemir! In the program, kaüld ^ Soylu, who joined the terrorist organization in 2017 and shared a report about Taşdemir, “We will be sentenced to death, numbered 5237”. In his statement, a terrorist who is limed, "Gara'dan statement under a national clause on February 20" said: "They get into the car with someone who is completely lying. Or, as a result of the crime of being a member of the program-organization on the television channel, he says in a statement that puts our party as a target, 'When you recognized this, it was noted that Taşdemir was initiated a PKK / KCK armed investigation. Is it politically responsible for the operation?', 'No The aim of this Dirayet Dilan Taşdemir, HDP, and the Turkish Armed Forces - Jvulliyen is to confuse the lie. Deputy Dilan is a lie. He explained his perception direction through gossip and show. Dirayet Taşdemir, who went to the Gara region of Iraq, is also directed to Twitter. It was noted that a detailed Ankara Chief Public Prosecutor was announced. From the subject, he said, "We will make a huge statement. It is completely a product of slander and imagination to show that it is a lie and slander by accepting the explanation of Soylu's statements."'''
from textblob import TextBlob
def Words(sent):
    blob = TextBlob(doc)
    nos=blob.noun_phrases

from selenium import webdriver
import time, requests

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
        time.sleep(1)
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
        if count == 5:
            browser.quit()
            break
   
    return images_url

items = search_google('taşdemir namik durukan')




# save 

import requests
import os.path

def Save_Pics(url):
 
    r = requests.get(url)
    i=1
    save_path = 'C:/Users/STC/Desktop/TextToSp'
    
    name_of_file =  "news"+str(i+1)
    
    completeName = os.path.join(save_path, name_of_file+".jpg")      
    
    
    with open(completeName, "wb") as f:
        f.write(r.content)
    
Save_Pics('https://i2.milimaj.com/i/milliyet/75/0x0/6032cdff55428521c00bb464.jpg')  



from mutagen.mp3 import MP3
def Audio_Time(url):
    audio = MP3("C:/Users/STC/Desktop/TextToSp/news2.mp3")
    print(audio.info.length)

