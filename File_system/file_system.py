# Set of main functions for File System App
import os
import logging

import Utils.utils as utils

from Crypto import BaseCipher, AES_cipher, RSA_cipher

logging.basicConfig(level=logging.INFO)


def create(file_path, text):
    """
    Create a new text file in provided path with randomly generated name.

    Input: file_path - path where to store file.
           text - Data to store in file.
    Output: - None -
    """

    file_name = os.path.join(file_path, utils.generate_random_name())
    with open(file_name, "at") as f:
        f.write(text)
    logging.info("file created: %s" % file_name)
    logging.info("-" * 20)
    return True


def delete(file_path, file_name=None):
    """
    Delete provided file from provided path.

    Input: file_path - path to the file.
           file_name - name of a file to delete.
    Output: - None -
    """

    if file_name is not None:
        data = os.path.join(file_path, file_name)
        if os.path.exists(data):
            if os.path.isfile(data):
                os.remove(data)
                logging.info("file deleted")
                logging.info("-" * 20)
                return 0
        else:
            logging.error("File does not exist.\nNothing was deleted.")
            return -1
    else:
        if os.path.isdir(file_path):
            os.rmdir(file_path)
            logging.info("folder deleted")
            logging.info("-" * 20)
            return 0


def read(file_path, file_name=None):
    """
    Display a content of a provided file in provided path.
    If file name was not provided, function displays a list of all files in provided path.

    Input: file_path - folder path.
           file_name - name of a file to read.
    Output: File content in CLI or list of files in CLI.
    """

    if file_name is not None:
        data = os.path.join(file_path, file_name)
        if os.path.isfile(data):
            with open(data, "r") as f:
                file_data = f.read()
            logging.info("File content:\n %s" % file_data)
            logging.info("-" * 20)
            return file_data
        else:
            logging.error("File does not exist.")
            return -1
    else:
        if os.path.isdir(file_path):
            files_list = os.listdir(file_path)
            logging.info("list of files:\n")
            for file in files_list:
                logging.info("%s" % file)
            logging.info("-" * 20)
            return files_list


def get_metadata(file_path, file_name=None):
    """
    Display a metadata of a provided file from provided folder path.

    Input: file_path - path to the file.
           file_name - name of a file to get metadata for.
    Output: Display metadata of file in CLI.
    """

    if file_name is not None:
        data = os.path.join(file_path, file_name)
        if os.path.exists(data):
            metadata = convert_stat_to_dict(os.stat(data))
            logging.info("Metadata of file:\n")
            for k, v in metadata.iteritems():
                logging.info("\t\t%s: \t%s" % (k, v))
            logging.info("-" * 20)
            return metadata
        else:
            logging.error("File does not exist.")
            return -1
    else:
        logging.error("File name was not provided.")
        return -1


def convert_stat_to_dict(data):
    """
    Convert nt.stat_result object to dictionary.

    Input: data - nt.stat_result object
    Output: dictionary of converted data.
    """
    try:
        converted_data = {k: getattr(data, k) for k in dir(data) if k.startswith('st_')}
        return converted_data
    except Exception as er:
        logging.error(er)
        return -1
