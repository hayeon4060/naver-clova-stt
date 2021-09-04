# -*- coding: utf-8 -*-
import requests
import sys
import json

file = open("result.txt", 'r', encoding='UTF8')
content = file.readlines()[0]
print(content)
start = 0
end = 1999 #만약 2천자 안되면

 
while True:
    tmp = content[:1999]
    print(tmp)
    end = tmp.rfind('.')
    print(end)
    break

# print(len(content.readlines()))


file.close()


def sum(content):

    url = 'https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize'

    data = {
      "document": {
          "title": "",
          "content": content[:2000]
      },
      "option": {
          "language": "ko",
          "model": "news",
          "tone": 2,
          "summaryCount": 3
        }
    }

    headers = {
      'X-NCP-APIGW-API-KEY-ID': 'cx49ohyd2e',
      'X-NCP-APIGW-API-KEY': 'OBo7SwStOcVy4lDt9eyMrCUzCDOcR46ruJgv8lKC',
      'Content-Type': 'application/json;utf-8'
    }

    x = requests.post(url, headers=headers,
                    data=json.dumps(data).encode('UTF-8'))

    return x.text
