import json
import requests as req
print(json.loads(req.get('https://www.boredapi.com/api/activity'))['activity'])
