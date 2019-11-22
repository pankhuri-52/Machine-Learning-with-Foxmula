import urllib
output=urllib.request.urlopen("https://www.google.com/")
print(output.read())
