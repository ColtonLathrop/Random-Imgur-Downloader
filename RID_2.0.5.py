'''
This is a script for scrapping pseudo-random images from Imgur.
Implemented is the addition of threading and functions for a GUI
'''
import random
import string
import urllib.request
import os
import binary_id as bi
import threading
import time

# Program Defaults
imgur_link = 'http://i.imgur.com/'
initial_filetype = '.jpg'
timer = True
max_threads = 150


length = int(input('Run length:'))
directory = input('Output directory:')


def swap_dir(user_dir):
    # Takes input as string and check if the directory is sub folder from where program initialized.
    # Otherwise creates the directory and navigates to it for writing.
    if os.path.exists(user_dir):
        os.chdir(user_dir)
    else:
        os.makedirs(user_dir)
        os.chdir(user_dir)


def generate_string(length):
    # Takes int and iterates over the length adding each random choice to it.
    # Returns string of img name.
    random_string = []
    for i in range(0, length):
        char = random.choice(string.ascii_letters + string.digits)
        random_string.append(char)
    return ''.join(random_string)


def convert_string(string):
    # Converts random string into a link based on input to function.
    img_name = imgur_link + string + initial_filetype
    return img_name


def download_save(web_addr, name_string):
    try:
        web_object = urllib.request.urlopen(web_addr)
    except Exception:
        return
    output_write = open(name_string, 'wb')
    output_write.write(web_object.read())
    output_write.close()
    image_type = bi.image_type(name_string)
    complete_name = name_string + '.' + str(image_type)
    if image_type is None:
        os.remove(name_string)
    else:
        try:
            os.rename(name_string, name_string + '.' + image_type)
        except FileExistsError:
            print('Encountered a duplicate of ' + name_string + ' in the current directory.')
    try:
        if os.path.getsize(complete_name) < 1 * 1024:
            os.remove(complete_name)
    except WindowsError:
        pass


def main_thread(name, length):
    # Main logic that is launched when thread is activated.
    x = generate_string(length)
    y = convert_string(x)
    download_save(y, x)


def Main():
    # Main function that creates threads limits to initialization parameter 'max_threads'.
    swap_dir(directory)
    if threading.active_count() <= max_threads:
        threading.Thread(target=main_thread, args=('threads', 5)).start()


if __name__ == '__main__':
    if timer == True:
        start = time.time()
    while True:
        if len(os.listdir(os.getcwd())) >= length:
            end = time.time()
            print(str(len(os.listdir(os.getcwd()))) + 'Images Retrieved in: ' + str(end - start))
            exit()
        Main()
