#!python2
# coding: utf-8

"""
AES ENCRYPT DECRYPT
Encrypts and Decrypts files using AES

TO DO DEPENDENCIES
TO DO HOW TO RUN
"""

import argparse
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = 'dev3'
__date__ = '02:17h, 08/02/2017'
__status__ = 'Production'


def main(xcrypt, password, directory):
    """
    Encrypts or Decrypts every file in a directory or just a single file
    Checks whether 'directory' is really a directory or just a file

    PARAMETERS:
        xcrypt : function
            One of two functions: encrypt or decrypt
        password : str
            Password used to encrypt or decrypt
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
        # TODO if decrypt, filter files for those with .encrypted extension
        files_to_xcrypt = filter(os.path.isfile, os.listdir(directory))
        files_to_xcrypt.sort()

        for i in files_to_xcrypt:
            xcrypt(password, i)
            # TODO write feedback stuff to screen

    # Handles single files
    elif os.path.isfile(directory):
        xcrypt(password, directory)
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

    RETURNS: bool
        True if encryption was successful
    """
    hashed_32b_password = SHA256.new(password).digest()
    iv = Random.new().read(16)
    encrypter = AES.new(key=hashed_32b_password, mode=AES.MODE_CBC, IV=iv)
    file_size = os.path.getsize(file_name)

    with open(file_name, 'rb') as file_to_encrypt:
        with open(file_name + '.encrypted', 'ab') as encrypted_file:
            encrypted_file.write(file_size + 'b')
            encrypted_file.write(iv)  # IV in the first 16 bytes after file size

            # reads 16 byte chunks until a chunk is smaller than 16, which will be padded
            file_chunk = file_to_encrypt.read(16)
            while len(file_chunk) == 16:
                encrypted_file.write(encrypter.encrypt(file_chunk))
                file_chunk = file_to_encrypt.read(16)

            # Padding the last chunk to be exactly 16 bytes
            padding = ''
            if len(file_chunk) > 0:
                padding = '0'*(16 - len(file_chunk))
                encrypted_file.write(encrypter.encrypt(file_chunk + padding))

    # Encrypted file must be equal in size to the original plus: len(file_size)+1, +16 (from IV) + len(padding)
    return os.path.getsize(file_name + '.encrypted') == int(file_size) + len(file_size) + 17 + len(padding)


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
        - file_name must have .encrypted extension

    ENSURES:
        Decryption of file_name using AES

    RETURNS: bool
        True if decryption was successful
    """

    with open(file_name, 'rb') as file_to_decrypt:
        decrypted_file_name = file_name[:len(file_name)-10]

        with open(decrypted_file_name, 'ab') as decrypted_file:
            hashed_32b_password = SHA256.new(password).digest()
            original_file_size = ''

            file_size_increment = file_to_decrypt.read(1)
            while file_size_increment != 'b':
                original_file_size += file_size_increment
                file_size_increment = file_to_decrypt.read(1)
            original_file_size = int(original_file_size)

            iv = file_to_decrypt.read(16)
            decrypter = AES.new(key=hashed_32b_password, mode=AES.MODE_CBC, IV=iv)

            file_chunk = file_to_decrypt.read(16)
            while len(file_chunk) == 16:
                decrypted_file.write(decrypter.decrypt(file_chunk))
                file_chunk = file_to_decrypt.read(16)

            # Truncate file, to eliminate padding
            file_to_decrypt.truncate(original_file_size)

        return True


if __name__ == '__main__':
    # TODO Review options and argument properties
    parser = argparse.ArgumentParser(description='Encrypt and Decrypt files using AES')

    parser.add_argument('-encrypt', help='Encrypt file or directory')
    parser.add_argument('-decrypt', help='Decrypt file or directory')
    parser.add_argument('-file', nargs='?', const=os.getcwd(), default=os.getcwd(),
                        metavar='dir', help='Directory or file path')

    parser = parser.parse_args()

    #main(parser.encrypt, parser.file)
