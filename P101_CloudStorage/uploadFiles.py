import dropbox
import os
from dropbox.files import WriteMode

class TransferData (object):
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFile(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'sl.BEXjFkNBlo7GXlMcMVrsgz1Y5-5KXUSJWK94Y-aMd-PDPSn1kJN77Jln4tgMDfnIpD1mcntwlg7JwV-52HzPhy4Gw3bGc12O-o-pmhwKE2mR5JPFT1DUp2ulpwl7W5QmmDOcRkL-JIg'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer: ')
    file_to = input('Enter the full path to upload to Dropbox: ')

    transferData.uploadFile(file_from, file_to)
    print('File has been moved successfully!')

main()
