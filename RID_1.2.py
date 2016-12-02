import random
import string
import urllib
import os
import imghdr
import urwid

def menu_button(caption, callback):
    button = urwid.Button(caption)
    urwid.connect_signal(button, 'click', callback)
    return urwid.AttrMap(button, None, focus_map='reversed')

def sub_menu(caption, choices):
    contents = menu(caption, choices)
    def open_menu(button):
        return top.open_box(contents)
    return menu_button([caption, u'...'], open_menu)

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    body.extend(choices)
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def startloop(button):
    response = urwid.Text([u'You chose ', button.label, u'\n'])
    done = menu_button(u'Ok', exit_program)
    top.open_box(urwid.Filler(urwid.Pile([response, done])))

def file_name(button):
    file_input = urwid.Edit("")
    menu_button(u'ok', exit_program)

def back_program(button):
    raise urwid.connect_signal(button, 'esc', callback)

def exit_program(button):
    raise urwid.ExitMainLoop()

def start_downloader(button):
    usrInput = file_input
    if not os.path.exists(usrInput):
        os.makedirs(usrInput)
        os.chdir(usrInput)
    loop = 1
    number_images = 500
    while True:
        #this generates the strings as either a random character (cap sens)
        u = random.choice(string.letters+string.digits)
        v = random.choice(string.letters+string.digits)
        w = random.choice(string.letters+string.digits)
        x = random.choice(string.letters+string.digits)
        y = random.choice(string.letters+string.digits)
        z = random.choice(string.letters+string.digits)
        imgSeq6 = [u,v,w,x,y,z]
        imgSeq = [u,v,w,x,y]
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
            continue
        os.rename(imgName, ''.join(imgSeq)+'.' + fileType)
        imgName = ''.join(imgSeq)+'.' + fileType
        loop += 1
        #removes files under a certain size that signifies 'file not found'
        if os.path.getsize(imgName) < 1 * 1024:
            os.remove(imgName)
            loop -= 1
        if loop >= number_images:
            break
menu_top = menu(u'Random Imgur Downloader', [
    menu_button(u'Run', start_downloader),
    sub_menu(u'Settings', [
        menu_button(u'Number of Images', startloop),
        menu_button(u'Image Type', startloop),
        menu_button(u'Folder Name', file_name),
        menu_button(u'Url Type', startloop),
    ]),
    menu_button(u'Exit', exit_program),
])

class CascadingBoxes(urwid.WidgetPlaceholder):
    max_box_levels = 4

    def __init__(self, box):
        super(CascadingBoxes, self).__init__(urwid.SolidFill(u'/'))
        self.box_level = 0
        self.open_box(box)

    def open_box(self, box):
        self.original_widget = urwid.Overlay(urwid.LineBox(box),
            self.original_widget,
            align='center', width=('relative', 80),
            valign='middle', height=('relative', 80),
            min_width=24, min_height=8,
            left=self.box_level * 3,
            right=(self.max_box_levels - self.box_level - 1) * 3,
            top=self.box_level * 2,
            bottom=(self.max_box_levels - self.box_level - 1) * 2)
        self.box_level += 1

    def keypress(self, size, key):
        if key == 'esc' and self.box_level > 1:
            self.original_widget = self.original_widget[0]
            self.box_level -= 1
        else:
            return super(CascadingBoxes, self).keypress(size, key)

top = CascadingBoxes(menu_top)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
