import urllib.request


content_stream = urllib.request.urlopen('http://www.baidu.com/')
content = content_stream.read()
print(content)
