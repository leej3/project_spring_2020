
from pathlib import Path
import os
import shutil 

def create_package_dir(package_name='BIOF309_RDK'):
    """ This function creates a new directory within the current directory using the passed input string 
    package_name. If a directory with the same name as package_name already exists, it deletes the old 
    directory."""
    
    start_dir = Path.cwd()
    print(f"Starting in {start_dir}")

    if start_dir.name == package_name:
        os.chdir(start_dir.parent)
        package_dir = start_dir
    else:
        package_dir = start_dir / package_name
    
    if package_dir.exists():
        print("Removing old directory...")
        shutil.rmtree(package_dir)

    print(f"Creating {package_dir}...")
    package_dir.mkdir()
    print(f"The current working directory is now {package_dir}")
    os.chdir(package_dir)
    
def create_package_str(package_name='EHT_RDK'):
    """ This function creates a new package structure within the current directory. It creates a new directory
    to house code, with the passed input string package_name, as well as blank files for 'init.py' within the 
    new directory, setup.py, License and Readme files."""
    
    Path('tests').mkdir()
    python_dir = Path(package_name)
    python_dir.mkdir()
    (python_dir / '__init__.py').touch()
    Path('setup.py').touch()
    Path('LICENSE').touch()
    Path('README.md').touch()
