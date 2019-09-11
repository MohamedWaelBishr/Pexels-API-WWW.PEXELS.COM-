import http.client
import requests
import json
import urllib
import shutil

############################################################
#MAIN FUNCTION IN WHILE TRUE LOOP
originalurl = "https://api.pexels.com/videos/search?"
try:
    querystring = {"query": "face",
                   "per_page": "40"}
    headers = {
        'Authorization': "APIKEY"
    }

    response = requests.request(
        "GET", originalurl, headers=headers, params=querystring).json()
    if(response['videos'][0]['video_files'][0]['quality']== 'hd'):
        for i in range(40):
            try:
                if(response['videos'][i]['video_files'][0]['quality']== 'hd'):
                    url = response['videos'][i]['video_files'][0]['link']
                    print(url)
                    photo_id =response['videos'][i]['id']
                    urllib.request.urlretrieve(url,str(photo_id)+'.mp4')
                    print(str(photo_id)+' ------> Done')
                elif(response['videos'][i]['video_files'][1]['quality']== 'hd'):
                    url = response['videos'][i]['video_files'][1]['link']
                    print(url)
                    photo_id =response['videos'][i]['id']
                    urllib.request.urlretrieve(url,str(photo_id)+'.mp4')
                    print(str(photo_id)+' ------> Done')
                elif(response['videos'][i]['video_files'][2]['quality']== 'hd'):
                    url = response['videos'][i]['video_files'][2]['link']
                    print(url)
                    photo_id =response['videos'][i]['id']
                    urllib.request.urlretrieve(url,str(photo_id)+'.mp4')
                    print(str(photo_id)+' ------> Done')
                else:
                    continue
            except:
                print('NONE')
except:
    print('Error While Requesting Data :( ')
