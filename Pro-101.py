import dropbox
import os
from dropbox import files
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,"rb")as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode("overwrite"))

def main():
    access_token = 'sl.AxpSUvclL7pqEC8Q7qRO9MOdwNts8tRnxafnntgFcFqhOdtomL2Lx1Cp0veQDQZIJ1_w2RoSOz2AbYLAQMeRk7irhvn3V1o9aZ3hlDt7acC9id67zZ-3hRze7sI9YBScXuJiiSs'
    transferData = TransferData(access_token)

    file_from = str(input("enter the folder path to transfer"))
    file_to = input("enter the full path")

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
