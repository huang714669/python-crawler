import requests



r = requests.get('https://www.douban.com/search', params={'q':'python', 'cat':'1001'})
print('状态码：', r.status_code)
print('实际请求的RUL:', r.url)
print('页面编码：', r.encoding)
print('Cookie:\n%s' % r.cookies['bid'])
print('响应头:', r.headers)
print('页面源码byte类型:\n%s' % r.content)
print('页面源码 :', r.text)
