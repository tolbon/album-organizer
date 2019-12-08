import os
import sys
from os import listdir
from os.path import isfile, join
import datetime
import shutil
import time

cwd = os.getcwd()
print(cwd)
whereTo = sys.argv[1]
for f in listdir(cwd):
    pf = join(cwd, f)
    if isfile(pf):
        s = os.stat(pf)
        ctime = min(s.st_ctime, s.st_mtime)
        filename, file_extension = os.path.splitext(os.path.basename(pf))
        file_extension = file_extension.lower()  
        if file_extension in ['.jpg', '.jpeg', '.png', '.mov']:
            d = datetime.date.fromtimestamp(ctime)
            dirAlbums = join(whereTo, str(d.year) +'-'+ str(d.month).zfill(2))
            try:
                os.mkdir(dirAlbums)
                print(dirAlbums)
            except:
                pass
            fileToCpy = join(dirAlbums, f)
            if isfile(fileToCpy):
                fileToCpy = join(dirAlbums, filename +'_'+ str(time.time()) +''+ file_extension)
                print('file exist rename to '+ fileToCpy)
            shutil.copyfile(pf, fileToCpy)


