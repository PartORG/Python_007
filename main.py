import sys
import File_system.file_system as fs
import logging

logging.basicConfig(level=logging.INFO)


def main():
    """
    Main function of a File System project.
    It shows a menu in console with discribed functionality.

    Input: it takes Path as CLI parameter.
    Output: - None -
    """
    arguments = sys.argv
    file_path = arguments[1]
    command = ''

    while command != 'q':
        command = input(
            '''What command to perform:
            * create file (C)
            * delete file (D)
            * list files in provided folder (L)
            * read file or directory (R)
            * show metadata of file (M)
            * quit (Q)\n\n''').strip().lower()

        if command == 'c':
            text = input('Enter a text to be stored in new file:\n')
            fs.create(file_path, text)
        elif command == 'l':
            fs.read(file_path)
        elif command == 'r':
            file_name = input('Enter a file name to read:\n')
            fs.read(file_path, file_name)
        elif command == 'd':
            file_name = input('Enter a file name to delete:\n')
            fs.delete(file_path, file_name)
        elif command == 'm':
            file_name = input('Enter a file name to get metadata:\n')
            fs.get_metadata(file_path, file_name)
        elif command == 'q':
            logging.info("...closing app.")
        else:
            logging.info("wrong command. Try again.")

    logging.info("Bye! Thank you for using this app.")


if __name__ == '__main__':
    main()
