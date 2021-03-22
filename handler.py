import json

from aiohttp import web
from File_system import file_system as fs


class Handler:
    def __init__(self):
        pass

    async def get_file_list(self, file_path):
        files = await fs.read(file_path)

        return web.json_response(data={
            "status": 'success',
            "data": files
        })

    async def get_file_data(self, request, file_path):
        pass

    async def create_file(self, request, file_path):
        pass

    async def delete_file(self, request, file_path):
        pass

    async def change_work_dir(self, request: web.Request, file_path):
        pass
