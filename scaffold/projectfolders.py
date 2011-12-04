"""Creates the folder skeleton for a new Python project"""
import os

def create_folders(project_name, current_directory):
    """Creates all of the requisite folders in the project skeleton"""
    root_dir = create_path(current_directory, project_name)
    
    if (os.path.exists(root_dir)): #If the path already exists, raise an error
        raise IOError(000, '%s already exists. Cannot create it.\n\nPlease try a different project name or root directory.' % root_dir)
    
    make_folder(root_dir) #Create the root directory  
    
    name_dir = create_path(root_dir, project_name)
    bin_dir = create_path(root_dir, "bin")
    tests_dir = create_path(root_dir, "tests")
    docs_dir = create_path(root_dir, "docs")
    
    make_folder(name_dir, ' +++') #Create the NAMEd directory
    make_folder(bin_dir, ' +++') #Create the bin directory
    make_folder(tests_dir, ' +++') #Create the tests directory
    make_folder(docs_dir, ' +++') #Create the docs directory
    
def make_folder(path, prefix = ''):
    """Creates the directory and prints a message letting the user know that it's been made"""
    os.mkdir(path)
    
    if(os.path.exists(path) == False): #If we were unable to make the directory for some reason...
        raise IOError(000, 'Unable to create root directory %s. Unknown error!' % path, '')
    
    print "create: %s %s" % (prefix, os.path.abspath(path))
    
def create_path(current_directory, new_folder_name):
    """Gets the absolute path of the new folder we're going to create"""
    return os.path.join(os.path.normpath(current_directory), new_folder_name)