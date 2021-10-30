from xml.etree import ElementTree
from termcolor import colored
from os.path import isdir
from os import makedirs, rmdir
from sys import exit
from glob import glob as xmlFiles
import shutil
import argparse

# Directories
train_directory = './images/train' # It should contain the xml files with bounding boxes
test_directory = './images/test' # It should contain the xml files with bounding boxes

# Keep calm and do not touch the rest of the code :3
parser = argparse.ArgumentParser()
parser.add_argument("--move", help="Put all wrong xml and images to a wrong_data folder inside each folder", action="store_true")
args = parser.parse_args()

if not isdir(train_directory) or not isdir(test_directory):
   print(colored('[!]', 'yellow', attrs=['bold']), colored('The training or test directories do not exist'))
   exit(1)
else:
    print(colored('[Ok]', 'green'), colored('Directories exists'))

everythingWentAsExpected = True

#Add More
