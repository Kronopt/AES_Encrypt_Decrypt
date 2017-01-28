#!/usr/bin/env python
# coding: utf-8

"""
AES ENCRYPT DECRYPT
Encrypts and Decrypts files using AES

TO DO DEPENDENCIES
TO DO HOW TO RUN
"""

import argparse
import os
import Crypto

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = 'dev2'
__date__ = '13:55h, 28/01/2017'
__status__ = 'Production'


def main(xcrypt, directory):
    """
    Encrypts or Decrypts every file in a directory or just a single file
    Checks whether 'directory' is really a directory or just a file

    PARAMETERS:
        xcrypt : function
            One of two functions: encrypt or decrypt
        directory : str
            Represents a file path or a directory

    REQUIRES:
        xcrypt must be one of the two available functions: encrypt or decrypt

    ENSURES:
        Encrypt or Decrypt of 'directory' using AES, be it a file or a whole directory
    """

    # Handles directories
    if os.path.isdir(directory):
        # TODO add some visual feedback, like list of files to encrypt/decrypt, and show warning if there are no files
        files_to_xcrypt = filter(os.path.isfile, os.listdir(directory))
        files_to_xcrypt.sort()

        for i in files_to_xcrypt:
            xcrypt(i)
            # TODO write feedback stuff to screen

    # Handles single files
    elif os.path.isfile(directory):
        xcrypt(directory)
        # TODO write feedback stuff to screen

    else:
        print "'" + directory + "' does not exist..."

    raw_input()


def encrypt(password, file_name):
    """
    Encryption function
    Encrypts file_name using a random IV and the provided password

    PARAMETERS:
        password : str
            Password with which to encrypt file_name
        file_name : str
            Represents a file path

    REQUIRES:
        - Existing file file_name

    ENSURES:
        Encryption of file_name using AES
    """

    with open(file_name, 'rb') as file_to_encrypt:
        # TODO hash password to return a 32 byte long string (SHA-256)
        # TODO Generate a 16 byte long random IV (pycrypto own random function)
        # TODO open outfile and store the IV as the first block
        # TODO encrypt file_to_encrypt piece by piece and store it in the outfile
        # TODO at the end maybe delete the original? After checking the encrypted file?
        # TODO write feedback stuff to screen
        pass


def decrypt(password, file_name):
    """
    Decryption function
    Decrypts file_name using the provided password

    PARAMETERS:
        password : str
            Password with which to decrypt file_name
        file_name : str
            Represents a file path

    REQUIRES:
        - Existing file file_name

    ENSURES:
        Decryption of file_name using AES
    """

    with open(file_name, 'rb') as file_to_decrypt:
        # TODO hash password to return a 32 byte long string (SHA-256)
        # TODO Read the 16 byte long IV from the start of file_to_decrypt
        # TODO open outfile
        # TODO decrypt file_to_encrypt piece by piece and store it in the outfile
        # TODO at the end maybe delete the original encrypted file? After checking the decrypted file?
        # TODO write feedback stuff to screen
        pass


if __name__ == '__main__':
    # TODO Review options and argument properties
    parser = argparse.ArgumentParser(description='Encrypt and Decrypt files using AES')

    parser.add_argument('-encrypt', help='Encrypt file or directory')
    parser.add_argument('-decrypt', help='Decrypt file or directory')
    parser.add_argument('-file', nargs='?', const=os.getcwd(), default=os.getcwd(),
                        metavar='dir', help='Directory or file path')

    parser = parser.parse_args()

    main(parser.hash, parser.file)
