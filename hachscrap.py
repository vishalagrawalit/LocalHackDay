import requests
import json

data = {}


param = { '/?username':'harkirat155','api_key':'63b3040dd99d6820d23626e658843d9042ca638a'}


resp = requests.get('https://clist.by/api/v1/contest/', 
                    params=param)

print(resp)

if resp.status_code != 200:
    # This means something went wrong.
#    raise ApiError('GET /api/v1/contest {}'.format(resp.status_code))
    print('error')


for con in resp.json():
    print('{} {}'.format(con['id'], con['summary']))



with open("data_file.json", "w") as write_file:
    json.dump(resp, write_file)


