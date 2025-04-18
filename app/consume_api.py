import request
import json

response = request.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

for data in response.json()['items']:
    if data['answer_count'] == 1:
        print(data['title'])
        print(data['link'])
    else:
        print('skipped')
    print()    