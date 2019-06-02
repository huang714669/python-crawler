import requests,json

# r = requests.get('http://httpbin.org/get')      


'''
requests get

payload = {
    "key1": "value1",
    "key2": "value2"
}
headers = {
    'hello':'world'
}
r = requests.get('http://httpbin.org/get', params=payload,headers=headers)      
# print(r.url)
print(r.text)
'''
'''
requests post
payload = {
    'hello':'world'

}
r = requests.post('http://httpbin.org/get', params=json.dumps(payload)   
print(r.text)

'''
