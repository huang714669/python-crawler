from bs4 import BeautifulSoup
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''


'''
获取tag的文本内容 
如果tag只有一个 NavigableString类型子节点,那么这个tag可以使用 .string 得到子节点内容 
如果超过一个, 返回None
'''
soup = BeautifulSoup(html, 'html.parser')
print('soup.p.string:',soup.p.string)
print('soup.div.string:',soup.div.string)

'''
.strings 属性 获取所有内容, 返回一个generator(包括空白字符) 
.stripped_strings 属性 获取所有内容, 返回一个generator(去除空白字符)
'''
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'html.parser')
print('soup.p.strings:',soup.p.strings)
print('soup.p.strings list:',list(soup.p.strings))
print('----------------------------------------')
print('soup.div.strings:', soup.div.strings)
print('soup.div.strings list:', list(soup.div.strings))

html='''
<html><head></head>
<body>
<p><b>
p-content
</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'html.parser')
print('soup.p.strings:',soup.p.strings)
print('soup.p.strings list:', list(soup.p.strings))
print('----------------------------------------')
print('soup.p.stripped_strings:', soup.p.stripped_strings)
print('soup.p.stripped_strings list:', list(soup.p.stripped_strings))



'''
直接子节点

.contents 属性 将tag的子节点以列表的方式输出 
.children 属性 将tag的子节点以list_iterator的方式输出
'''
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'html.parser')
print('soup.div.contents:',soup.div.contents)
print('soup.div.contents list:', list(soup.div.contents))
print('----------------------------------------')
print('soup.div.children:', soup.div.children)
print('soup.div.children list:', list(soup.div.children))


'''
所有子孙节点

.descendants 属性 对所有子节点递归
'''
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'html.parser')
print('soup.div.contents:',soup.div.contents)
print('soup.div.contents list:', list(soup.div.contents))
print('----------------------------------------')
print('soup.div.descendants:', soup.div.descendants)
print('soup.div.descendants list:', list(soup.div.descendants))


'''
.parent 属性 获取父节点
.parents 属性 获取全部父节点
'''
print('soup.b.parent:',soup.b.parent)
print('soup.b.parent type:',type(soup.b.parent))
print('soup.b.parents:',soup.b.parents)
print('soup.b.parents type:',type(soup.b.parents))
print('-------------------------------------------')
for i in soup.b.parents:
    print('parent name:',i.name)

'''
兄弟节点

.next_sibling 属性 下一个兄弟节点 
.previous_sibling 属性 上一个兄弟节点
'''
print('soup.p.next_sibling:',repr(soup.p.next_sibling))
print('soup.p.next_sibling type:', type(soup.p.next_sibling))
print('------------------------------------------------------------------------')
print('soup.p.next_sibling.next_sibling:', soup.p.next_sibling.next_sibling)
print('soup.p.next_sibling.next_sibling type:', type(soup.p.next_sibling.next_sibling))
print('------------------------------------------------------------------------')
print('soup.p.previous_sibling:',repr(soup.p.previous_sibling))
print('soup.p.previous_sibling type:', type(soup.p.previous_sibling))
print('------------------------------------------------------------------------')
print('soup.p.previous_sibling.previous_sibling:', soup.p.previous_sibling.previous_sibling)
print('soup.p.previous_sibling.previous_sibling type:', type(soup.p.previous_sibling.previous_sibling))

'''
全部兄弟节点
.next_siblings 属性 全部的弟弟 
.previous_siblings 属性 全部的哥哥

'''
print('soup.p.next_siblings type:', type(soup.p.next_siblings))
print('soup.p.next_siblings list:', list(soup.p.next_siblings))
print('------------------------------------------------------------------------')
print('soup.p.previous_siblings type:', type(soup.p.previous_siblings))
print('soup.p.previous_siblings list:', list(soup.p.previous_siblings))


'''
前后节点

.next_element 属性 后节点 
.previous_element 属性 前节点
'''
print('soup.p.next_element :', repr(soup.p.next_element))
print('soup.p.next_element.next_element :', repr(soup.p.next_element.next_element))
print('soup.p.next_element.next_element.next_element :', repr(soup.p.next_element.next_element.next_element))
print('soup.p.next_element.next_element.next_element.next_element :', repr(soup.p.next_element.next_element.next_element.next_element))
print('------------------------------------------------------------------------')
print('soup.p.previous_element :', repr(soup.p.previous_element))
print('soup.p.previous_element.previous_element :', repr(soup.p.previous_element.previous_element))
print('soup.p.previous_element.previous_element.previous_element :', repr(soup.p.previous_element.previous_element.previous_element))
print('soup.p.previous_element.previous_element.previous_element.previous_element :', repr(soup.p.previous_element.previous_element.previous_element.previous_element))


'''
所有前后节点

.next_elements 属性 
.previous_elements 属性
'''
print('soup.p.next_elements :', type(soup.p.next_elements))
for i in  soup.p.next_elements:
    print('soup.p.next_element:',repr(i))
print('---------------------------------------------------------')
print('soup.p.previous_elements :', type(soup.p.previous_elements))
for i in  soup.p.previous_elements:
    print('soup.p.previous_element:',repr(i))

'''
搜索文档树
find_all() 当前标签的所有子节点
'''
print(soup.find_all('p'))
print(soup.find_all(re.compile('^p')))
print(soup.find_all(['p', 'div']))
print(soup.find_all(text=re.compile('content$')))
print(soup.find_all(id='panda'))
print(soup.find_all('p'))
print('-----------------------------------')
print(soup.find_all('p',limit=3))

'''
find()

find_all()返回一个列表 
find()返回第一个结果
find_parent()

在当前元素的父节点中查找,返回第一个
find_parents()

在当前元素的父节点中查找,返回list
find_next_sibling()

在当前元素的兄弟节点中查找(弟弟),返回第一个
find_next_siblings()

在当前元素的兄弟节点中查找(弟弟),返回list
find_previous_sibling()

在当前元素的兄弟节点中查找(哥哥),返回第一个
find_previous_siblings()

在当前元素的兄弟节点中查找(哥哥),返回list
find_next()

在当前元素的相邻节点中查找(向下),返回第一个
find_all_next()

在当前元素的相邻节点中查找(向下),返回list
find_previous()

在当前元素的相邻节点中查找(向上),返回第一个
find_all_previous()

在当前元素的相邻节点中查找(向上),返回list
'''


'''
CSS选择器
通过标签名查找
通过类名查找
通过 id 名查找


'''
html='''
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p class="p-class">p-content2</p>
<p class="p-class">p-content3</p>
<p class="p-class">p-content4</p>
<p>p-content5</p>
<p>p-content6</p>
<p>p-content7</p>
<panda id='panda'>panda-content</panda>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup.select('p'))
print(soup.select('.p-class'))
print(soup.select('#panda'))
print(soup.select('p #panda'))
print(soup.select('div #panda'))
print(soup.select('p[class="p-class"]'))
