import sys
import requests
import json
import os
import wget

def text_cleanup(text):
    new =""
    for i in text:
        if i not in'\?.!/;:"':
            new += i
    return new
 
print("crawler start")
 
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'
}

# 利用get取得API資料  
url = "https://www.dcard.tw/_api/forums/pet/posts?popular=true"

reqs = requests.get(url, headers=header)
#if print 503  = 錯誤 // 200 =正常
 
if(int(reqs.status_code)==200):
    print("Dcardsever status:Connect ing")
else:
    print("Dcardsever status:Connect error")
    os.system("pause")
    os._exit()
 
reqsjson = json.loads(reqs.text)
total_num = len(reqsjson)

#print (total_num) #共30篇
 
for i in range(0,total_num):
 
    title = reqsjson[i]["title"]
    title = text_cleanup(title)
 
    media_num = len(reqsjson[i]['media']) #判斷這文章圖的數量
    print( title+"檢查有沒有圖檔")
    if media_num != 0:
 
        path =  title                     #資料夾名字用標題命名
        print("status:have pictures")
        if not os.path.isdir(path):       #檢查是否已經有了
            os.mkdir(path)                #沒有的用標題建立資料夾
 
        for i_m in range(0, media_num):
            image_url = reqsjson[i]['media'][i_m]['url']
 
            filepath =  title + '/' + str(i_m) + '.jpg'
            if not os.path.isfile(filepath): #檢查是否下載過圖片，沒有就下載
                wget.download(image_url, filepath)
               
    else:
        print("status:no pictures")
 
 
 
 
print("crawler end")