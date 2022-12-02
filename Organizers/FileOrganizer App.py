from shutil import move, rmtree                 # shutil is a module designed for high-level file operations
from glob import glob                           # returns a list of all files matching a pathname pattern
import os                                       # os is a module for handling misc operating system interfaces
from pathlib import Path, WindowsPath           # Path is a method for handling file paths
import csv                                      # for handling csv file
import logging                                  # logging module
from tkinter.messagebox import askyesno, askokcancel, askyesnocancel
# print ((r'.\*.*'))

logging.basicConfig(filename='FileOrginzer.log', encoding='utf-8', format='%(asctime)s %(message)s')            

class csv_file_handling:

    def __init__ (self):
        self.newline_char = ''
        self.delemiter_char = ','
        self.quote_char='|'

    def write_pairs_to_csv (self, lists: list, file_name: str, location: str, overwrite=False) -> None:
        # lists should be structured (category, item)
        # location format: C:/parentfolder/subfolder/
        # filename format: thisfile.sufix
        if list (location) [-1] != '\\':
            file = f'{location}\\{file_name}'
        else:
            file = location + file_name
        # file format: C:/parentfolder/subfolder/thisfile.sufix

        if os.path.isdir (location) and not (os.path.isfile (file)):
            # if the location is a directory and the file path is not real,
            # create a new file in exclusive mode
            open (file, 'x')
            logging.info (f'creating {file_name}')

        elif not (os.path.isdir (location)):
            # if the directory does not exist, create the directory
            os.mkdir (location)
            logging.info (f'creating directory {location}')
            # create the file in exclusive mode
            open (file, 'x')
            logging.info (f'creating {file_name}')

        elif os.path.isfile (file) and not overwrite:
            # if the file exists and overwrite is false, end function
            logging.error (f"{file_name} is an existing file in {location}, and overwrite is disabled, so your information has not been written")
            return None

        elif os.path.isfile (file) and overwrite:
            logging.warning (f"{file_name} is an existing file in {location}, and overwrite is enabled, so {file_name} has been overwritten")

        with open (file, 'w', newline=self.newline_char) as page:
            csv_file = csv.writer (page, delimiter=self.delemiter_char, 
                            quotechar=self.quote_char, quoting=csv.QUOTE_MINIMAL)
            logging.info (f'writing to {file_name}')
            for pairs in lists:
                logging.info (f'writing {pairs}')
                csv_file.writerow (pairs)

    def get_from_csv (self, filepath: str) -> list:
        with open (filepath, 'r', newline=self.newline_char) as csv_file:
            file = csv.reader (csv_file, quotechar=self.quote_char,
                            delimiter=self.delemiter_char, quoting=csv.QUOTE_MINIMAL)
            logging.info (f'fetching info from {filepath}')
            output = []
            for row in file:
                output.append (tuple(row))
        logging.info ('information fetched')
        return output

    def print_csv_file (self, filepath: str) -> None:
        # troubleshooting function
        with open (filepath, 'r', newline=self.newline_char) as csv_file:
            output = csv.reader (csv_file, quotechar=self.quote_char,
                            delimiter=self.delemiter_char, quoting=csv.QUOTE_MINIMAL)
            blob = open ('blob.txt', 'w') # change to blob to sys.stdout for terminal output
            for row in output:
                print (row, file=blob)

class guis:

    def __init__(self) -> None:
        pass
    

class startup:

    def __init__ (self):
        logging.info ('starting new instance of FileOrganizer')
        self.extentions = [
            ('Pictures', r'.\*jpg'),
            ('Pictures', r'.\*png'),
            ('Pictures', r'.\*jfif'),
            ('Text Files', r'.\*txt'),
            ('Text Files', r'.\*pdf'),
            ('Text Files', r'.\*pdc'),
            ('Text Files', r'.\*md'),
            ('Text Files', r'.\*doc'),
            ('Text Files', r'.\*docx'),
            ('Slides', r'.\*odp'),
            ('Slides', r'.\*pptx'),
            ('Web Pictures', r'.\*webp'),
            ('ODG Files', r'.\*odg'),
            ('Movie Maker Projects', r'.\*wlmp'),
            ('ZIP files', r'.\*zip'),
            ('Excel Files', r'.\*cvs'),
            ('Raw', r'.\*cr3'),
            ('Video', r'.\*mp4'),
            ('Shortcuts', r'.\*lnk'),
            ('C++ Files', r'.\*cpp'),
            ('C++ Files', r'.\*cp'),
            ('Web Picture', r'.\*svg'),
            ('Music', r'.\*mp3'),
            ('Excel files', r'.\*xlsx'),
            ('Python programs', r'.\*py')
            ]
 
        # create defaults file with extensions listed above
        csv_file_handling().write_pairs_to_csv(self.extentions, 'defaults', (f'{os.getcwd()}\\Organizers\\'), overwrite=False)

"""
        for item in ext_list:
            print (f'{item [0]}: {glob(item[1])}', end='')
            input ()

    def make_extension_file (self):       
        os.mkdir ("./FileOrganizer Extensions")
        open ("./FileOrganizer Extensions/Default.csv", 'x')
        with open ("./FileOrganizer Extensions/Default.csv", 'a', newline='') as default_extensions:
            extend = csv.writer (default_extensions, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for items in self.extentions:
                extend.writerow (items)
"""        


if __name__ == '__main__':
    startup ()

logging.info ('all operations complete, closing FileOrganizer')