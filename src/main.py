import os
import shutil
from gen_content import generate_pages_recursive

def copy_directory(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    dir_content = os.listdir(source)

    for el in dir_content:
        source_path = os.path.join(source, el)
        destination_path = os.path.join(destination, el)
        print(f"Copying {source_path} to {destination_path}")
        if os.path.isdir(source_path):
            copy_directory(source_path, destination_path)
        else:
            shutil.copy(source_path, destination_path)

def main():
    copy_directory("static", "public")
    generate_pages_recursive("src/content", "src/template.html", "public")

main()            