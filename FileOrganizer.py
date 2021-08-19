from shutil import move
from glob import glob
import os

print (glob(r'.\*.*'))
files = [('Pictures', glob(r'.\*jpg')),
         ('Pictures', glob(r'.\*png')),
         ('Pictures', glob(r'.\*jfif')),
         ('Text Files', glob(r'.\*txt')),
         ('Text Files', glob(r'.\*pdf')),
         ('Text Files', glob(r'.\*pdc')),
         ('Text Files', glob(r'.\*md')),
         ('Text Files', glob(r'.\*doc')),
         ('Text Files', glob(r'.\*docx')),
         ('Slides', glob(r'.\*odp')),
         ('Slides', glob(r'.\*pptx')),
         ('Web Pictures', glob(r'.\*webp')),
         ('ODG Files', glob(r'.\*odg')),
         ('Movie Maker Projects', glob(r'.\*wlmp')),
         ('ZIP files', glob(r'.\*zip')),
         ('Excel Files', glob(r'.\*cvs')),
         ('Raw', glob(r'.\*cr3')),
         ('Video', glob(r'.\*mp4')),
         ('Shortcuts', glob(r'.\*lnk')),
         ('C++ Files', glob(r'.\*cpp')),
         ('C++ Files', glob(r'.\*cp')),
         ('Web Picture', glob(r'.\*svg')),
         ('Music', glob(r'.\*mp3'))]
for x in files:
    counter = 0
    file_path = '.\\' + x[0]
    if (len(x[1]) > 0) and not(os.access(file_path, os.R_OK)):
        print ('file does not exist')
        os.mkdir(file_path)
    while counter < len (x[1]):
        file = x[1][counter]
        print (file)
        print (file_path)
        move (file, file_path + file.removeprefix('.'))
        counter += 1
