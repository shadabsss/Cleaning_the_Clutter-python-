import os

#functions

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


#listing the files in directories
files = os.listdir()
files.remove("main.py")

#creating folders
createIfNotExist("Images")
createIfNotExist("Docs")
createIfNotExist("Media")
createIfNotExist("Others")

# defining values and variables 

imgExts = [".png",".jpg",".jpeg", ".apng", ".pjpeg", ".gif"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = [".txt", ".docx", ".doc", ".pdf", ".html", ".htm", ".xls", ".ppt"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = [".mp4", ".mp3", ".flv", ".mkv", ".avi", "html5", "mpeg-4"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and os.path.isfile(file):
        others.append(file)


# moving the files into folder

move("Images", images)
move("Docs", docs)
move("Media", medias)
move("Others", others)
