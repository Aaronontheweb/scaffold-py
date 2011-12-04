"""An extremely ghetto, but functional way of creating the necessary .py files for the project setup"""
import os
import projectfolders

def create_files(project_name, root_dir):
    write_inits(project_name, root_dir)

def write_inits(project_name, root_dir):
    """Creates all of the __init__.py files necessary for the project skeleton"""
    
    #Create our file paths first...
    test_init_path = os.path.normpath(os.path.join(projectfolders.create_path(root_dir, "test"), "__init__.py"))
    project_init_path = os.path.normpath(os.path.join(projectfolders.create_path(root_dir, "project_name"), "__init__.py"))
    
    #Write the test_init file first
    test_init = open(test_init_path, 'w')
    test_init.close()
    create_file(test_init_path)
    
    #Write the NAME_init second
    project_init = open(project_init_path, 'w')
    project_init.close()
    create_file(project_init_path)
    
def create_file(path, prefix = ' ++++++'):
    print "create: %s %s" % (prefix, path)