import random
import string
import urllib


loop = 1
while True:
    #this generates the strings as either a random character (cap sens)
    u = random.choice(string.letters+string.digits)
    v = random.choice(string.letters+string.digits)
    w = random.choice(string.letters+string.digits)
    x = random.choice(string.letters+string.digits)
    y = random.choice(string.letters+string.digits)
    z = random.choice(string.letters+string.digits)
    imgSeq = [u,v,w,x,y]
    #this removes the spaces that occur in lists that separate our random character
    imgName = ''.join(imgSeq)+'.jpg'
    print imgName
    #opens the url writes the data to the jpg
    webImg = urllib.urlopen("http://i.imgur.com/"+imgName)
    output = open(imgName, 'wb')
    output.write(webImg.read())
    output.close()
