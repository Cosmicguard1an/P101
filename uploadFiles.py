import dropbox
import os


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for file in files:
                local_path = os.path.join(root,file)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
                

def main():
    access_token = 'lQjkksZ-NIYAAAAAAAAAAUT4f59CtPRH6N4Wc6df3GGJKbpZ80rlF95E9apue9aT'
    file_from = input('Enter file to be uploaded: ')
    file_to = '/test_dropbox'+'/'+str(file_from)
    TransferData.upload_files(file_from,file_to)