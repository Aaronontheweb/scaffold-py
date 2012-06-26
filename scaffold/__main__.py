"""Creates a project skeleton for a new python project, per the recommended steps
in Learn Python the Hard Way Exercise #46 (http://learnpythonthehardway.org/book/ex46.html)"""

import argparse
import projectfolders
import projectfiles
import os

parser = argparse.ArgumentParser(description='Scaffolding tool for simple Python projects', epilog='Report any issues to [Github url]')
parser.add_argument('-p','--project',required=True, nargs=1, help='The name of the project to create')
parser.add_argument('-d','--dir',required=False, nargs=1, help='The directory in which to create the project (creates in current directory by default)')

args = parser.parse_args() #Unpack the commandline arguments

cur_dir = os.getcwd() #Get the current working directory as our default root project directory

if(args.dir != None): #If the user set an explicit output directory
    cur_dir = args.dir[0]

try:
    projectfolders.create_folders(args.project[0], cur_dir) #Creates all of the project folders we need
    projectfiles.create_files(args.project[0], cur_dir) #Creates all of the project files we need
except IOError as (errno, strerror):
    print strerror


