import os;
import shutil;

from_dir = "C:/Users/sohan/OneDrive/Desktop/Python/p102"
to_dir = "C:/Users/sohan/OneDrive/Desktop/Python/p102/downloadedImage"

listOfFiles = os.listdir(from_dir)
for x in listOfFiles:
    name,ext = os.path.splitext(x)
    if ext == "":
        continue
    if ext in ['.txt','.doc','.docx','.pdf']:
        p1 = from_dir + '/' + x
        p2 = to_dir + '/' + "Document_Files"
        p3 = to_dir + '/' + "Document_Files" + '/' + x
        if os.path.exists(p2):
            print("Moving")
            shutil.move(p1,p3)
        else:
            os.makedirs(p2)
            print("Moving")
            shutil.move(p1,p3)