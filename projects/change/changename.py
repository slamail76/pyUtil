#This program change original name with a random name
import os, random, sys, string


path = "aaa"

files = os.listdir(path)
print(files)
"""
for namefile in files:
    rand = str("".join(random.sample(string.ascii_lowercase + string.digits, 6)))
    mynamefile= namefile[:-4]
    mynamefile = mynamefile.replace(" ", "")
    mynamefile = mynamefile.replace("attestato-", "")
    change=mynamefile+"_"+rand+".pdf"
    path1="C:/Users/stefano/PycharmProjects/pyUtil/projects/change/aaa"
     #print(path1)
    #print(change)
    os.chdir(path1)
    os.rename(namefile,change)
"""
#fine