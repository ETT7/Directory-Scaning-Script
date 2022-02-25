import os
import shutil
import logging
path = os.path.join(os.getcwd(),'scan')
scanFolder=[]
scanFile=[]
folderList = []
fileList = []

logging.basicConfig(filename="scaned_dirs.log", 
					format='%(message)s', 
					filemode='a+')
logger=logging.getLogger()
logger.setLevel(logging.INFO)
def main():
    for root, dirs, files in os.walk(path):
        for folder in dirs:
            scanFolder.append(os.path.join(root,folder))
        for file in files:
            scanFile.append(os.path.join(root,file))

    for name in scanFolder:
        name.replace('//', '\\')
        folderList.append(os.path.relpath(name, path))
    # print("justFolder",justFolder)
    for name in scanFile:
        name.replace('//', '\\')
        fileList.append(os.path.relpath(name, path))
    # print("justFile",justFile)


    scan(fileList, folderList)
    # print("difFolder",difFolder)

def scan(fileList, folderList):
    f= open("scaned_dirs.log","w+")
    f.write("\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓FILE LIST↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n\n")
    f.close()
    if not fileList:
        print("ファイルが存在しません")
        logger.info("0\nファイルが存在しません")
    else:
        for name in fileList:
            try:
                print("FILES :", name)
                logger.info(name)
            except OSError as e:
                pass
                print("FILE SCAN ERROR: ", e)
    
    f= open("scaned_dirs.log","a")
    f.write("\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓FOLDERS LIST↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n\n")
    f.close()

    if not folderList:
        print("フォルダが存在しません")
        logger.info("0\nフォルダが存在しません")
    else:
        for name in folderList:
            try:
                print("FOLDERS :", name)
                logger.info(name)
            except OSError as e:
                pass
                print("FOLDER SCAN ERROR: ", e)

if __name__ == "__main__":
    main()




    

    



