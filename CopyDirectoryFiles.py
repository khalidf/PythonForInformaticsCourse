#Find files in directory and subdirectory and copy to same structure on different server

import shutil
import os
source = os.listdir('\\\INX-SRV-SFTP\sftp\sftpIBReports')
#destination = "/tmp/newfolder/"
print source
for files in source:
    if files.startswith('20160412_') and files[9].isalpha() and files.endswith('.csv') :
        #shutil.copy(files,destination)
        #and files.[9].isalpha() 
        print files