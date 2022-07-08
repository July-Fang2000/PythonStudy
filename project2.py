import os

def rename_file():
    file_list = os.listdir("/Users/alvin/Documents/pythonStudy_project2/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Dirctory is "+ saved_path)
    os.chdir("/Users/alvin/Documents/pythonStudy_project2/prank")
    for file_name in file_list:
        translation_table = file_name.maketrans("0123456789", "          ", "0123456789")
        os.rename(file_name,file_name.translate(translation_table))
    os.chdir(saved_path)
rename_file()