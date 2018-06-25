import urllib


content_stream = urllib.urlopen('http://www.baidu.com/')
content = content_stream.read()
print(content)
