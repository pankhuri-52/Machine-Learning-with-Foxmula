import urllib
output=urllib.request.urlopen("https://www.google.com/")
try:
    output=urllib.request.urlopen("https://www.google.com/search?q=python")
    print(output.read())
except Exception as e:
    print(str(e))

#=================================================================
import urllib
try:
    headers={}
    headers['User-Agent']="Chrome/24.0.1312.25"
    output=urllib.request.Request("https://www.google.com/search?q=python",headers=headers)
    res=urllib.request.urlopen(output)
    print(res.read())
    print(output.read())
except Exception as e:
    print(str(e))
 
#=============================================================

"""Regular Expressions"""
import re   
data="""Anshu is 19 years old, Deepak is 40 years old, John is 120 years old,
Shruti is 3000 years old, georgia is 12 years old."""
ages=re.findall(r'\d{1,3}',data)
letters=re.findall(r'\w',data) #it will separate the letters in the names as individual letters
names=re.findall(r'[A-Z][a-z]*',data) #* means repition of small case alphabets
print(names)

#==============================================================

