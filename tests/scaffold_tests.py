from nose.tools import *
from scaffold import projectfiles, projectfolders
import os
import shutil #Used for recursively deleting directories

target_dir = os.path.normpath(os.path.join(os.getcwd(),"testcruft"))

def setup():
    os.mkdir(target_dir) #Create a temporary directory that we will delete later upon test completion
    print("root test directory: {dir}".format(dir=target_dir))

def teardown():
    print("attempting to tear down {dir}".format(dir=target_dir))
    shutil.rmtree(target_dir) #Recursively deletes the directory and all of its contents

def test_create_folder_path():
    sub_dir = "magicdir"
    expected_path = os.path.join(os.path.normpath(target_dir), sub_dir)
    resultant_path = projectfolders.create_path(target_dir, sub_dir)
    assert expected_path == resultant_path
    
def test_create_folders():
    project_name = "monkey"
    projectfolders.create_folders(project_name, target_dir) #Create the project folders
    
    assert_folder_exists(target_dir, project_name) # /root/monkey exists
    project_root = os.path.join(target_dir, project_name)
    
    assert_folder_exists(project_root, "bin") # /root/monkey/bin exists
    assert_folder_exists(project_root, "tests") # /root/monkey/tests exists
    assert_folder_exists(project_root, "docs") # /root/monkey/docs exists
    assert_folder_exists(project_root, project_name) # /root/monkey/monkey exists
    
def test_create_init_files():
    project_name = "hammertime"
    projectfolders.create_folders(project_name, target_dir) #Create the project folders
    project_root = projectfolders.create_path(target_dir, project_name)
    projectfiles.write_inits(project_name, project_root)
    
    assert_file_exists(project_root, "tests", "__init__.py")
    assert_file_exists(project_root, project_name, "__init__.py")
    
def test_create_test_files():
    project_name = "balloonpants"
    projectfolders.create_folders(project_name, target_dir) #Create the project folders
    project_root = projectfolders.create_path(target_dir, project_name)
    projectfiles.write_tests(project_name, project_root)

    assert_file_exists(project_root, "tests", "{project_name}_tests.py".format(project_name=project_name))

def test_create_setup_file():
    project_name = "hipster-tears"
    projectfolders.create_folders(project_name, target_dir) #Create the project folders
    project_root = projectfolders.create_path(target_dir, project_name)
    projectfiles.write_setup(project_name, project_root)
    
    assert_file_exists(project_root, None, "setup.py")

def test_create_all_files():
    """Bring all of the individual file tests together under one roof..."""
    project_name = "mongodb-is-webscale-webscale-i-tells-ya"
    projectfolders.create_folders(project_name, target_dir) #Create the project folders
    project_root = projectfolders.create_path(target_dir, project_name)
    projectfiles.create_files(project_name, target_dir) #Oh snap, notice how we're using target_dir? This method creates a project root internally.
    
    assert_file_exists(project_root, "tests", "__init__.py")
    assert_file_exists(project_root, project_name, "__init__.py")
    assert_file_exists(project_root, "tests", "{project_name}_tests.py".format(project_name=project_name))
    assert_file_exists(project_root, None, "setup.py")

def assert_folder_exists(target_dir, sub_dir):
    """Tests to see if a particular folder exists"""
    assert os.path.exists(os.path.join(target_dir, sub_dir))
    
def assert_file_exists(target_dir, sub_dir, filename):
    """Tests to see if a particular file exists or not"""
    if sub_dir == None: #If we don't have a sub-directory
        assert os.path.exists(os.path.join(target_dir, filename))
    else:
        assert os.path.exists(os.path.join(os.path.join(target_dir, sub_dir), filename))
