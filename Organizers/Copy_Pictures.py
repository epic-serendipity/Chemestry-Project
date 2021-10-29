from shutil import move, copy
#from glob import glob
import os

information = """---
you are using Copy_Pictures.py
to copy a list of pictures, select the copy option by entering 'c' into the menu
to move a list of pictures, select the move option by entering 'm' into the menu
to do anything else, use a different program
---
first enter the file path of the parent file of the file you want to copy to
the easiest way to do this is to right-click the file name at the top of file gui and select 'copy address as text', then paste the address into this program

next enter the file name of the destination file
this can be an already existing file or a new file

next enter the file path to the files which you wish to copy
again, the easiest way to do this is to copy the address

next enter the file extension
examples of file extensions are: jpg, png, cr3, txt, pdf

next enter any text which is shown before the image number
example: image_

next enter any text which comes after the file number
example: _

finally, enter the image number of the files you wish to move or copy

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
print ('\n---\nthe following entries are about the files to be copied')
file_path = message ("please enter file path to files to be copied (default .\\)",'file path: ')
extension = message ("please enter the file extension (default .jpg)",'extension: ')
prefix = str(message ("please enter the file prefix (default None)",'prefix: '))
sufix = str(message ("please enter sufix (default None)",'sufix: '))

if extension == '':
    extension = '.jpg'
elif extension [0] != '.':
    ex = list (extension)
    ex.insert(0, '.')
    extension = ''
    for x in ex:
        extension += x
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

#print (extension)

pics = []
number = ' '
#print (folder)
print ('\npress enter to end sequence')
while number != '':
    number = input ('picture number: ')
    if number == '' and len (pics) >= 1:
        try:
            os.mkdir(destination_path + folder)
            print ('\nfile does not exist, making new file...\n')
        except FileExistsError:
            print ('\nfound', destination_path + folder)
        for files in pics:
            try:
                if select == 'move':
                    move (file_path + files, destination_path + folder)
                elif select == 'copy':
                    copy (file_path + files, destination_path + folder)
                print ('adding', files, 'to', folder + '...')
            except:
                print ('could not locate', files, 'in', file_path)
    elif number != '':
        filename = '.\\' + prefix + number + sufix + extension
        pics.append(filename)
input ('\nfile transfer complete, press enter to terminate program')