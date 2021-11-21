from shutil import move, copy
#from glob import glob
import os

information = """---
you are using Copy_Pictures.py
to copy a list of pictures, select the copy option by entering 'c' into the menu
to move a list of pictures, select the move option by entering 'm' into the menu
to do anything else, use a different program
---
first, some vocabulary
file path - the path of filename to the file refered to, exsample: 'D:\\Users\\junio\\OneDrive\\Pictures\\Dancing'
default - the value which the program will use if you press enter without typing in another value
file name - the name of a file without the file path
---
use

first enter the file path of the parent file of the file you want to copy to
the easiest way to do this is to right-click the file name at the top of file gui and select 'copy address as text', then paste the address into this program

next enter the file name of the destination file
this can be an already existing file or a new file

next enter the file path to the filename which you wish to copy
again, the easiest way to do this is to copy the address

next enter the file extension
examples of file extensions are: jpg, png, cr3, txt, pdf

next enter any text which is shown before the image number
example: image_

next enter any text which comes after the file number
example: _

finally, enter the image number of the filename you wish to move or copy

"""

def message (pre, line):
    print ('\n' + str(pre))
    return input (line)


menu = {'info':['i','(i)','info'],
        'move':['m','(m)','move'],
        'copy':['c','(c)','copy']}

esc = False

while esc == False:
    select = input (str('---menu---\nmove (m), copy (c), info (i): ')).lower()
    if select in menu['info']:
        print (information)
    elif select in menu['copy']:
        select = 'copy'
        esc = True
    elif select in 'move':
        select = 'move'
        esc = True
    else:
        print ('that option is not available, please try again')

destination_path = message ("please enter file path for destination file without destination file name (default .\\)",'destination path: ')
folder = str(message ("please enter destination file name (default 'new file')",'destination file name: '))
print ('\n---\nthe following entries are about the filename to be copied')
file_path = message ("please enter file path to filename to be copied (default .\\)",'file path: ')
try:
    num_extension = message ("please enter how many different file extensions you are going to move (default 1)", "number of extensions: ")
    if num_extension == '':
        num_extension = 1
    else:
        num_extension = int (num_extension)
except ValueError:
    print ("input must be int, setting extension number to default")
    num_extension = 1
if num_extension > 1:
    extension = []
    for x in range (1, num_extension + 1):
        extend = message (f"please enter the file extension number {x}",'extension: ')
        if extend == '':
            extend = '.jpg'
        elif extend [0] != '.':
            ex = list (extend)
            ex.insert(0, '.')
            extend = ''
            for x in ex:
                extend += x
        extension.append(extend)

elif num_extension < 1:
    print ('number of extensions must be non-negative int, setting extension number to default')
    num_extension = 1

elif num_extension == 1:
    extension = message ("please enter the file extension (default .jpg)",'extension: ')
    if extension == '':
        extension = '.jpg'
    elif extension [0] != '.':
        ex = list (extension)
        ex.insert(0, '.')
        extension = ''
        for x in ex:
            extension += x

prefix = str(message ("please enter the file prefix (default None)",'prefix: '))
sufix = str(message ("please enter sufix which does not include the file extension (default None)",'sufix: '))

if destination_path == '':
    destination_path = '\\.'
elif destination_path [-1] != '\\':
    destination_path += '\\'
if file_path == '':
    file_path = '\\.'
elif file_path [-1] != '\\':
    file_path += '\\'
if folder == '':
    folder = 'new file'
try:
    os.mkdir(destination_path + folder)
    print ('\nfile does not exist, making new file...\n')
except FileExistsError:
    print ('\nfound', destination_path + folder)
#print (extension)

pics = []
number = ' '
#print (folder)
print ('\npress enter to end sequence')
while number != '':
    number = input ('picture number: ')
    if num_extension == 1:
        filename = '.\\' + prefix + number + sufix + extension
    else:
        filename = []
        for x in range (0, len (extension)):
            filename.append('.\\' + prefix + number + sufix + extension[x])
    if num_extension == 1:
        try:
            if select == 'move':
                move (file_path + filename, destination_path + folder)
            elif select == 'copy':
                copy (file_path + filename, destination_path + folder)
            print ('adding', filename, 'to', folder + '...')
        except:
            print ('could not locate', filename, 'in', file_path)
    else:
        for file in filename:
            try:
                if select == 'move':
                    move (file_path + file, destination_path + folder)
                elif select == 'copy':
                    copy (file_path + file, destination_path + folder)
                print ('adding', file, 'to', folder + '...')
            except:
                print ('could not locate', file, 'in', file_path)
        
input ('\nfile transfer complete, press enter to terminate program')