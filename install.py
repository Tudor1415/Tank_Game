import subprocess
import sys
import os

def install(package):
    os.system("python -m pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org")
    os.system(f"python -m pip install {package} --trusted-host pypi.org --trusted-host files.pythonhosted.org")

install('numpy')
install('arcade')
install('sklearn')
