#!python2
# coding: utf-8

"""
INSTALL DEPENDENCIES
Installs module dependencies for AES_Encrypt_Decrypt.py

HOW TO RUN:
    - Directly, by double clicking the script.
"""

import subprocess
import sys

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '1.0'
__date__ = '23:52h, 28/02/2017'


def install_dependencies():
    dependencies = ["pycrypto"]
    python_exe = sys.executable  # location of python executable, avoids dependency on windows PATH

    try:
        # check if pip is installed
        subprocess.check_output([python_exe, "-m", "pip", "--version"])

    except subprocess.CalledProcessError:
        print
        print "Pip is the recommended tool for installing Python packages, and usually comes bundled with python."
        print "Without pip, dependencies are much harder to install..."
        print
        raw_input("Press any key to exit")
        sys.exit()

    print "pycrypto needs Microsoft Visual C++ 9.0, make sure you install it first: http://aka.ms/vcpython27"
    raw_input("Press any key to continue...")

    print
    print "Installing dependencies for AES_Encrypt_Decrypt.py"

    # Install dependencies
    subprocess.call([python_exe, "-m", "pip", "install"] + dependencies)

    print
    raw_input("Press any key to exit")

if __name__ == '__main__':
    install_dependencies()
