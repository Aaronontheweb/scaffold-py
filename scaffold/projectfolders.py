"""Creates the folder skeleton for a new Python project"""
import os
from textwrap import dedent

def create_folders(project_name, current_directory):
    """Creates all of the requisite folders in the project skeleton"""
    root_dir = create_path(current_directory, project_name)

    if os.path.exists(root_dir) and os.listdir(root_dir):
        #If the path already exists and it is not empty, raise an error
        err_msg = '''
            {directory} already exists and it is not empty.

            Please try a different project name or root directory.
            
            '''.format(directory=root_dir)
        raise IOError(000, dedent(err_msg))
    else:
        make_folder(root_dir) #Create the root directory

    dirnames = (project_name, 'bin', 'tests', 'docs')
    
    #Create all the other directories
    for item in dirnames:
        directory = create_path(root_dir, item)
        make_folder(directory, ' +++')

def make_folder(path, prefix=''):
    """Creates the directory and prints a message to notify the user"""
    os.mkdir(path)

    if os.path.exists(path) is False: #If we were unable to make the directory for some reason...
        err_msg = 'Unable to create root directory {path_}. Unknown error!'.format(path_=path)
        raise IOError(000, err_msg, '')

    print "create: {prefix} {path_}".format(
        prefix=prefix,
        path_=os.path.abspath(path)
    )

def create_path(current_directory, new_folder_name):
    """Gets the absolute path of the new folder we're going to create"""
    current_directory = os.path.abspath(current_directory)
    return os.path.join(current_directory, new_folder_name)