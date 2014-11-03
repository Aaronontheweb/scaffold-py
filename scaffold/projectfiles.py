"""An extremely ghetto (but functional) way to create the necessary .py files for the scaffold"""
import os
from scaffold import projectfolders
from textwrap import dedent
import subprocess

def create_files(project_name, root_dir):
    """Creates all files necessary for a project skeleton"""
    root_dir = projectfolders.create_path(root_dir, project_name) #Modify the root
    
    write_setup(project_name, root_dir)
    write_inits(project_name, root_dir)
    write_tests(project_name, root_dir)

def write_setup(project_name, root_dir):
    """Writes a default setup.py file"""
    #Get the path for setup.py
    setup_path = get_file_path(root_dir, None, "setup.py") 
    setup_content = get_setup_text(project_name)
    with open(setup_path, 'w') as setup_file:
        setup_file.write(setup_content)
    print_file(setup_path, " +++")
    
def write_tests(project_name, root_dir):
    """Writes tests/PROJECT_NAME_tests.py file to disk"""
    #Get the path for setup.py
    filename = "{project_name}_tests.py".format(project_name=project_name)
    test_path = get_file_path(root_dir, "tests", filename) 
    test_content = get_test_text(project_name)
    with open(test_path, 'w') as test_file:
        test_file.write(test_content)
    print_file(test_path)

def write_inits(project_name, root_dir):
    """Creates all __init__.py files necessary for the project skeleton"""
    
    #Create our file paths first...
    init_paths = {
        'test': get_file_path(root_dir, "tests", "__init__.py"),
        'project': get_file_path(root_dir, project_name, "__init__.py")
    }
    
    #Write the test_init file first
    test_init = open(init_paths['test'], 'w')
    test_init.close()
    print_file(init_paths['test'])
    
    #Write the NAME_init second
    project_init = open(init_paths['project'], 'w')
    project_init.close()
    print_file(init_paths['project'])
    
def print_file(path, prefix=' ++++++'):
    print(
    "create: {prefix} {path_}".format(
        prefix=prefix,
        path_=os.path.abspath(path))
    )

def get_file_path(root_dir, sub_dir, filename):
    if sub_dir == None: #In case we're writing directly to the root directory
        return os.path.normpath(os.path.join(root_dir, filename))
    
    #Otherwise, build out the appropriate path for the subdirectory
    path_ = projectfolders.create_path(root_dir, sub_dir)
    filepath = os.path.join(path_, filename)
    return os.path.normpath(filepath)

def get_setup_text(project_name):
    #This is quite ghetto, and can probably be improved
    setup_text = """
        try:
            from setuptools import setup
        except ImportError:
            from distutils.core import setup

        config = {{
            'description': 'My Project',
            'author': '{author}',
            'url': 'URL to get it at.',
            'download_url': 'Where to download it.',
            'author_email': '{author_email}',
            'version': '0.1',
            'install_requires': ['nose'],
            'packages': ['{project}'],
            'scripts': [],
            'name': '{project}'
        }}

        setup(**config)

    """.format(
            project = project_name, 
            author = get_user_name_from_git() or "My Name", 
            author_email = get_user_email_from_git() or "My email.")

    return dedent(setup_text)

def get_test_text(project_name):
    #Again, quite ghetto and can probably be improved, but it works
    test_text = """
        from nose.tools import *
        import {PROJECT}

        def setup():
            print("SETUP!")

        def teardown():
            print("TEAR DOWN!")

        def test_basic():
            print("I RAN!")
    """.format(PROJECT=project_name)
    
    return dedent(test_text)

def get_user_name_from_git():
    try:
        git_process = subprocess.Popen(['git', 'config', 'user.name'], stdout=subprocess.PIPE
                                                                     , stderr=subprocess.PIPE)
        user_name, err = git_process.communicate()
        return user_name.rstrip()
    except OSError:
        return None

def get_user_email_from_git():
    try:
        git_process = subprocess.Popen(['git', 'config', 'user.email'], stdout=subprocess.PIPE
                                                                      , stderr=subprocess.PIPE)
        user_email, err = git_process.communicate()
        return user_email.rstrip()
    except OSError:
        return None
