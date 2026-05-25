import argparse
import os
import glob
import shutil

parser = argparse.ArgumentParser(description="files organiser")
parser.add_argument("fold_name",help="The gold fold")
args = parser.parse_args()



#images/（jpg, png, jpeg）
image_files = []
for ext in ['*.jpg', '*.jpeg', '*.png']:
    image_files.extend(glob.glob(f"**/{ext}", recursive=True))
    

if image_files:
    folder_name = "images"
    os.makedirs(folder_name, exist_ok=True)
    for file in image_files:
        shutil.move(file, folder_name)

#docs/（pdf, docx, md, txt）
docs_files = []
for ext in ['*.pdf', '*.docx', '*.md','*.txt']:
    docs_files.extend(glob.glob(f"**/{ext}", recursive=True))
    

if docs_files:
    folder_name = "docs"
    os.makedirs(folder_name, exist_ok=True)
    for file in docs_files:
        shutil.move(file, folder_name)



#code/（py, ipynb, cpp, etc）
code_files = []
for ext in ['*.py', '*.ipynb', '*.cpp','*.etc']:
    code_files = [].extend(glob.glob(f"**/{ext}", recursive=True))
    

if code_files :
    folder_name = "codes"
    os.makedirs(folder_name, exist_ok=True)
    for file in code_files:
        shutil.move(file, folder_name)


#data/（csv, json, xlsx）
data_files = []
for ext in ['*.csv', '*.json', '*.xlsx']:
    data_files.extend(glob.glob(f"**/{ext}", recursive=True))
    

if data_files:
    folder_name = "datas"
    os.makedirs(folder_name, exist_ok=True)
    for file in data_files:
        shutil.move(file, folder_name)



#others/
other_files = []
for ext in ['*.*']:
    image_files.extend(glob.glob(f"**/{ext}", recursive=True))
    

if other_files:
    folder_name = "others"
    os.makedirs(folder_name, exist_ok=True)
    for file in other_files:
        shutil.move(file, folder_name)

images_n = len(image_files)
docs_n = len(docs_files)
code_n = len(code_files)
data_n = len(data_files)
others_n = len(other_files)

print("moved "+images_n+" images")
print("moved "+docs_n+" docs")
print("moved "+code_n+" code files")
print("moved "+data_n+" data files")
print("moved "+others_n+" others")

