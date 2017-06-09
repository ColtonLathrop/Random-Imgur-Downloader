import random
import string
import urllib
import os
import imghdr

#find . -name "*.jpg"  -delete
skipCreate = 0
usrFileinput = raw_input('desired name of output folder:')
#checks if the directory exists/ if it does it created a new directory
if os.path.exists(usrFileinput):
    os.chdir(usrFileinput)
    print 'rebatching into' + os.path.abspath(os.getcwd())
    skipCreate += 1
#checks to see if os.path.exists found a directory and runs
if not skipCreate == 1:
    os.makedirs(usrFileinput)
    os.chdir(usrFileinput)

loop = int(1.00)
usrRunsize = int(raw_input('desired batch size:'))
txtDoc = open(usrFileinput + ".txt", "a")
docSkip = 1

while loop <= usrRunsize:
    #this generates the strings as either a random character (cap sens)
    u = random.choice(string.letters+string.digits)
    v = random.choice(string.letters+string.digits)
    w = random.choice(string.letters+string.digits)
    x = random.choice(string.letters+string.digits)
    y = random.choice(string.letters+string.digits)
    z = random.choice(string.letters+string.digits)
    imgSeq = [u,v,w,x,y]
    loop += 1.00
    docSkip = 0
    #removes spaces from imgSeq and joins it with .jpg 'H5gFs.jpg'
    imgName = ''.join(imgSeq)+'.jpg'
    #queries imgur for imgName.jpg, writes, and saves it to disk
    webImg = urllib.urlopen("http://i.imgur.com/"+imgName)
    output = open(imgName, 'wb')
    output.write(webImg.read())
    output.close()
    fileType = imghdr.what(imgName)
    if fileType is None:
        os.remove(imgName)
        loop -= 1.00
        continue
    os.rename(imgName, ''.join(imgSeq)+'.' + fileType)
    imgName = ''.join(imgSeq)+'.' + fileType
    #removes files under a certain size that signifies 'file not found'
    if os.path.getsize(imgName) < 1 * 1024:
        os.remove(imgName)
        loop -= 1.00
        docSkip = 1
    print '{0:.0f}%'.format(loop / usrRunsize * 100)
    if docSkip == 0:
        txtDoc.write("\n" + str(imgName))
    if loop > usrRunsize:
        break
