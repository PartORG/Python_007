import sys
import logging

from handler import Handler
from aiohttp import web
# import File_system.file_system as fs

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

    # Handler
    handler = Handler()

    # Server creation
    app = web.Application()
    app.add_routes([
        web.get("/files/list", handler.get_file_list(file_path)),
        web.get("/files", handler.get_file_data(file_path)),
        web.post("/files", handler.create_file(file_path)),
        web.delete("/files/{file_name}", handler.delete_file(file_path)),
        web.post("/change_file_dir", handler.change_work_dir(file_path))
    ])

    web.run_app(app, port=9000)
    # command = ''
    #
    # while command != 'q':
    #     command = input(
    #         '''What command to perform:
    #         * create file (C)
    #         * delete file (D)
    #         * list files in provided folder (L)
    #         * read file or directory (R)
    #         * show metadata of file (M)
    #         * quit (Q)\n\n''').strip().lower()
    #
    #     if command == 'c':
    #         text = input('Enter a text to be stored in new file:\n')
    #         fs.create(file_path, text)
    #     elif command == 'l':
    #         fs.read(file_path)
    #     elif command == 'r':
    #         file_name = input('Enter a file name to read:\n')
    #         fs.read(file_path, file_name)
    #     elif command == 'd':
    #         file_name = input('Enter a file name to delete:\n')
    #         fs.delete(file_path, file_name)
    #     elif command == 'm':
    #         file_name = input('Enter a file name to get metadata:\n')
    #         fs.get_metadata(file_path, file_name)
    #     elif command == 'q':
    #         logging.info("...closing app.")
    #     else:
    #         logging.info("wrong command. Try again.")
    #
    # logging.info("Bye! Thank you for using this app.")


if __name__ == '__main__':
    main()
