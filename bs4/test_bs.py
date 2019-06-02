from bs4 import BeautifulSoup
import lxml
html='''
<html><head><title id='id_title' class='class_title1 class_title2'>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<div><!-- comment test --></div>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

print('title type:',type(soup.title))
print('title name:',soup.title.name)
print('title attrs:',soup.title.attrs)

print('soup.p.string type:',type(soup.p.string))
print('soup.p.string contents:',soup.p.string)

print('soup type:', type(soup))
print('soup.name:', soup.name)
print('soup.attrs:', soup.attrs)

print('soup.div.string:', soup.div.string)
print('soup.div.string type:', type(soup.div.string))
print('soup.p.string type:', type(soup.p.string))
