'''
This is a script for scrapping pseudo-random images from Imgur.
Implemented is the addition of threading and functions for a GUI
'''
import random
import string
import urllib
import os
import imghdr
import threading

length = 5
directory = 'test'
name = 'threads'
def swap_dir(user_dir):
    if os.path.exists(user_dir):
        os.chdir(user_dir)
    else:
        os.makedirs(user_dir)
        os.chdir(user_dir)

def generate_string(length):
    random_string = []
    for i in xrange(0, length):
        char = random.choice(string.letters + string.digits)
        random_string.append(char)
    return ''.join(random_string)

def convert_string(string):
    img_name = 'http://i.imgur.com/' + string + '.jpg'
    return img_name

def download_save(web_addr, name_string):
    try:
        web_object = urllib.urlopen(web_addr)
    except Exception:
        return
    output_write = open(name_string, 'wb')
    output_write.write(web_object.read())
    output_write.close()
    image_type = imghdr.what(name_string)
    complete_name = name_string + '.' + str(image_type)
    if image_type is None:
        os.remove(name_string)
    else:
        os.rename(name_string, name_string + '.' + image_type)
    try:
        if os.path.getsize(complete_name) < 1 * 1024:
            os.remove(complete_name)
    except WindowsError:
        pass

def function_thread(name, length):
    x = generate_string(length)
    y = convert_string(x)
    download_save(y, x)

def Main():
    thread1 = threading.Thread(target=function_thread, args=(name, 5))
    thread2 = threading.Thread(target=function_thread, args=(name, 5))
    thread3 = threading.Thread(target=function_thread, args=(name, 5))
    thread4 = threading.Thread(target=function_thread, args=(name, 5))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    print threading.active_count()


if __name__ == '__main__':
    swap_dir(directory)
    while True:
        Main()
