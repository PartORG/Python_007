import sys
import os
import file_system as fs


def main():
    # do smth
    arguments = sys.argv

    print "Passed arguments: ", arguments
    print "CWD: ", os.getcwd()

    file_path = arguments[1]
    command = ''

    while command != 'q':
        command = raw_input('What command to perform:\n\n'
                        '* create file (C)\n'
                        '* delete file (D)\n'
                        '* read file or directory (R)\n'
                        '* show metadata of file (M)\n'
                        '* quit (Q)\n\n').lower()
        if command == 'c':
            text = raw_input('Enter a text to be stored in new file:\n')
            fs.create(file_path, text)
        elif command == 'r':
            fs.read(file_path)
        elif command == 'd':
            fs.delete(file_path)
        elif command == 'm':
            fs.get_metadata(file_path)
        else:
            print "wrong command. Try again."

    print "Bye! Thank you for using this app."


if __name__ == '__main__':
    main()
