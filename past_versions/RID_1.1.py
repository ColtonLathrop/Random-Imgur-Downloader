import random
import string
import urllib
import os
import imghdr

#find . -name "*.jpg"  -delete

usrInput = raw_input('desired name of output folder:')
if not os.path.exists(usrInput):
    os.makedirs(usrInput)
    os.chdir(usrInput)

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
    #removes spaces from imgSeq and joins it with .jpg 'H5gFs.jpg'
    imgName = ''.join(imgSeq)+'.jpg'
    print imgName
    #queries imgur for imgName.jpg, writes, and saves it to disk
    webImg = urllib.urlopen("http://i.imgur.com/"+imgName)
    output = open(imgName, 'wb')
    output.write(webImg.read())
    output.close()
    fileType = imghdr.what(imgName)
    if fileType is None:
        os.remove(imgName)
        continue
    print fileType
    os.rename(imgName, ''.join(imgSeq)+'.' + fileType)
    imgName = ''.join(imgSeq)+'.' + fileType
    #removes files under a certain size that signifies 'file not found'
    if os.path.getsize(imgName) < 1 * 1024:
        os.remove(imgName)
