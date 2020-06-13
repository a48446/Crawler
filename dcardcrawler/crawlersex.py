import requests
import json
import os

def Data_to_Dcard(infor_json,index):
    Dcard_Json = {
        'id': 0,
        'title': 'title',
        'gender': 'M',
        'topics': [],
        'url':'',
        'likeCount':0,
        'commentCount':0,
        'media':[],
        'mediaCount':0
    }

    Dcard_Json['id']            = int(infor_json['id'])
    Dcard_Json['title']         = str(infor_json['title'])
    Dcard_Json['gender']        = str(infor_json['gender'])
    Dcard_Json['topics']        = infor_json['topics']
    Dcard_Json['url']           = 'https://www.dcard.tw/f/'+ forums +'/p/' + str(infor_json['id'])
    Dcard_Json['likeCount']     = int(infor_json['likeCount'])
    Dcard_Json['commentCount']  = int(infor_json['commentCount'])
    Dcard_Json['media']         = infor_json['media']
    Dcard_Json['mediaCount']    = int(len(infor_json['media']))

    print( "{:3d} 編號：{}｜網址：{}｜性別：{}｜讚數：{:5d}｜圖片數量：{}｜標題：{}".format(         
        index + 1,
        str(infor_json['id']),
        str(Dcard_Json['url']),
        str(Dcard_Json['gender']),
        Dcard_Json['likeCount'],
        Dcard_Json['mediaCount'],
        str(Dcard_Json['title'])
        ))
    
    return Dcard_Json

def Data_inject(datas):
    Dcard_infors = []
    for index,data in enumerate(datas):
        Dcard_infors.append([])
        Dcard_infors[index] = Data_to_Dcard(data,index)
    return Dcard_infors

def Compute_sex(datas):
    Male = 0        #男
    Male_l = 0      #男
    Male_p = 0      #男

    Female = 0      #女
    Female_l = 0    #女
    Female_p = 0    #女
    for sex in datas:
        if sex['gender'] == 'M':
            Male += 1
            Male_l += sex['likeCount']
            Male_p += sex['mediaCount']
        elif sex['gender'] == 'F':
            Female += 1
            Female_l += sex['likeCount']
            Female_p += sex['mediaCount']

    done = [[Male,Male_l,Male_p],[Female,Female_l,Female_p]]

    print("男性=>發文篇數：{:2d}｜讚數：{:2d}｜圖片數：{:2d}\n女性=>發文篇數：{:2d}｜讚數：{:2d}｜圖片數：{:2d}\n".format(
        done[0][0],done[0][1],done[0][2],
        done[1][0],done[1][1],done[1][2]
        ))
    return done

def download_image(datas):
    folder_path ='./dcard/' + forums + '/'

    if (os.path.exists(folder_path) == False): 
        os.makedirs(folder_path)               

    for images in datas:
        if images['mediaCount'] > 0:
            for index,image_url in enumerate(images['media']):
                image = requests.get(str(image_url['url']))    
                img_name = folder_path + str(images['title']).replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('<','').replace('>','').replace('|','') + '/' 
                if (os.path.exists(img_name) == False):        
                    os.makedirs(img_name)                      
                with open(img_name + str(index + 1) + '.png','wb') as file:
                    file.write(image.content)
                    file.flush()
                file.close()                                   
                print("Download：{}，The number {} of photo ，Remaining {} photo need download".format(images['title'],index + 1,images['mediaCount'] - index - 1))
            print("########## Complete",images['title'],"##########\n")
    print("Photo download completed..")

Dcard_Api = {
    'popular': 'false', # 熱門
    'limit': '100'       # 顯示文章篇數，最多100篇
}

url = 'https://www.dcard.tw/_api/forums/'
forums = 'sex'

Dcard = requests.get(url + forums + '/posts?', params=Dcard_Api)
Dcard_to_Json = json.loads(Dcard.text)
Dcard_format = Data_inject(Dcard_to_Json)

print("data analyzing")
Compute_sex(Dcard_format)

print('media download')
download_image(Dcard_format)