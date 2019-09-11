import http.client
import requests
import json
import urllib
import shutil

##########################################################
#INITIATING THE REQUESTING
originalurl = "https://api.pexels.com/v1/search?"
querystring = {"query": "face",
               "per_page": "40"}
headers = {
    'Authorization': "APIKEY"
}

response = requests.request(
    "GET", originalurl, headers=headers, params=querystring).json()

next_page = response['next_page']
############################################################
#MAIN FUNCTION IN WHILE TRUE LOOP
while True:
    if response['next_page']:
        try:
            querystring = {"query": "face",
                           "per_page": "40"}
            headers = {
                'Authorization': "APIKEY"
            }

            response = requests.request(
                "GET", originalurl, headers=headers, params=querystring).json()

            originalurl = response['next_page']
            for i in range(40):
                try:
                    url = response['photos'][i]['src']['tiny']
                    print(url)
                    photo_id =response['photos'][i]['id']
                    r = requests.get(url, stream=True)
                    if r.status_code == 200:
                        with open(str(photo_id)+".jpg", 'wb') as f:
                            r.raw.decode_content = True
                            shutil.copyfileobj(r.raw, f)
                except:
                    print('NONE')
        except:
            print('Error While Requesting Data :( ')

############################################################
#IMAGE FORMATS
'''
original	   The size of the original image is given with the attributes width and height.
large	       This image has a maximum width of 940px and a maximum height of 650px. It has the aspect ratio of the original image.
large2x	       This image has a maximum width of 1880px and a maximum height of 1300px. It has the aspect ratio of the original image.
medium	       This image has a height of 350px and a flexible width. It has the aspect ratio of the original image.
small	       This image has a height of 130px and a flexible width. It has the aspect ratio of the original image.
portrait	   This image has a width of 800px and a height of 1200px.
landscape	   This image has a width of 1200px and height of 627px.
tiny	       This image has a width of 280px and height of 200px.
'''
##############################################################
