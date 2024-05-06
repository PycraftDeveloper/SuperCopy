import shutil
import os

def copy_process(to_do, source, destination):
    for element in to_do:
        try:
            mew_element = element[0].replace(source, destination)
            path = mew_element
            small_path = os.sep
            for location in path.split(os.sep)[1:-1]:
                small_path += location
                if not os.path.isdir(small_path):
                    os.mkdir(small_path)
                small_path += os.sep

            shutil.copy2(element[0], destination)
        except:
            print(f"Unable to copy: {element[0]}")