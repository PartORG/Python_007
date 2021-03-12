# Set of main functions for File System App
import os
import utils


def create(file_path, text):
    """
    This function creates a new text file in provided path with randomly generated name.

    Input: file_path - path where to store file.
           text - Data to store in file.
    Output: - None -
    """
    print "called create function"
    file_name = os.path.join(file_path, utils.generate_random_name())
    with open(file_name, "at") as f:
        f.write(text)
    print "file created"
    print "-" * 20


def delete(file_path, file_name=None):
    """
    This function deletes provided file from provided path.

    Input: file_path - path to the file.
           file_name - name of a file to delete.
    Output: - None -
    """
    print "called delete function"
    if file_name is not None:
        data = os.path.join(file_path, file_name)
        if os.path.exists(data):
            if os.path.isfile(data):
                os.remove(data)
                print "file deleted"
                print "-" * 20
        else:
            print "File does not exist.\nNothing was deleted."
    else:
        if os.path.isdir(file_path):
            os.rmdir(file_path)
            print "folder deleted"
            print "-" * 20


def read(file_path, file_name=None):
    """
    This function displays a content of a provided file in provided path.
    If file name was not provided, function displays a list of all files in provided path.

    Input: file_path - folder path.
           file_name - name of a file to read.
    Output: File content in CLI or list of files in CLI.
    """
    print "called read function"
    if file_name is not None:
        data = os.path.join(file_path, file_name)
        if os.path.exists(data):
            if os.path.isfile(data):
                with open(data, "r") as f:
                    file_data = f.read()
                print "File content:\n", file_data
                print "-" * 20
        else:
            print "File does not exist."
    else:
        if os.path.isdir(file_path):
            files_list = os.listdir(file_path)
            print "list of files:\n", files_list
            print "-" * 20


def get_metadata(file_path, file_name=None):
    """
    This function displays a metadata of a provided file from provided folder path.

    Input: file_path - path to the file.
           file_name - name of a file to get metadata for.
    Output: Display metadata of file in CLI.
    """

    print "called get_metadata function"
    if file_name is not None:
        data = os.path.join(file_path, file_name)
        if os.path.exists(data):
            metadata = os.stat(data)
            print "Metadata of file:"
            print metadata
            print "-" * 20
        else:
            print "File does not exist."
    else:
        print "File name was not provided."
