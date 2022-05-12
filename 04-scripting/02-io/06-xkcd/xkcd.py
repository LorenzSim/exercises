import json
import sys
import urllib.request

import cv2

number = sys.argv[1]
url = f'https://xkcd.com/{number}/info.0.json'

with urllib.request.urlopen(url) as input:
    data = json.loads(input)
    picture_url = data['img']
    
    with urllib.request.urlopen(picture_url) as input_picture:
        img = cv2.imread(input_picture, cv2.IMREAD_ANYCOLOR)
        while True:
            cv2.imshow("test", img)
            cv2.waitKey(0)
            sys.exit()
        cv2.destroyAllWindows()


    
