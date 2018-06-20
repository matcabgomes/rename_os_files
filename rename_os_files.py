import os

def rename_files():
    file_list = os.listdir("./secret_message/prank")
    saved_path = os.getcwd()
    print("Current Directory is "+saved_path)
    os.chdir("./secret_message/prank")
    for file_name in file_list:
        file_new_name = file_name.translate(None,"0123456789")
        print('Old name: '+ file_name)
        print('New name: '+ file_new_name)
        os.rename(file_name, file_new_name)
    os.chdir(saved_path)

rename_files()