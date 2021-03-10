import os


def create(file_name, text):
    print "called create function"
    if os.path.exists(file_name):
        with open(file_name, "at") as f:
            f.write(text)
    else:
        with open(file_name, "wt") as f:
            f.write(text)
    print "file created"
    print "-" * 20


def delete(file_name):
    print "called delete function"
    if os.path.exists(file_name):
        if os.path.isdir(file_name):
            os.remove(file_name)
            print "file deleted"
            print "-" * 20

        if os.path.isfile(file_name):
            os.rmdir(file_name)
            print "folder deleted"
            print "-" * 20
    else:
        print "File does not exist.\nNothing was deleted."


def read(file_name=os.getcwd()):
    print "called read function"
    if os.path.exists(file_name):
        if os.path.isdir(file_name):
            files_list = os.listdir(file_name)
            print "list of files:\n", files_list
            print "-" * 20

        if os.path.isfile(file_name):
            with open(file_name, "r") as f:
                file_data = f.read()
            print "File content:\n", file_data
            print "-" * 20
    else:
        print "File does not exist."


def get_metadata(file_name):
    print "called get_metadata function"
    if os.path.exists(file_name):
        metadata = os.stat(file_name)
        print "Metadata of file:"
        print metadata
        print "-" * 20
    else:
        print "File does not exist."
