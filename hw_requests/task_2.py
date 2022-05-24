import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    
    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()
    
    def upload(self, filename):
        disk_file_path = '/new_txt'
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл добавлен!')
        


if __name__ == '__main__':
    path_to_file = input('file_path')
    token = input('token')
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
    