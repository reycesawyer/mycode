#!/usr/bin/env python3

# import additional code to complete our task - these are not commonly used so they must be imported
import shutil # tool used to help with directory movements. Stands for shell utility
import os # another tool to help interact with the OS
import getpass # tool to get username

# Get current username so I can use on different systems with different usernames
USER = getpass.getuser()

def main():
    # Specify working directory
    workingdir = f"/home/{USER}/mycode/"
    os.chdir(workingdir)
    
    # Move file1 to a folder2
    shutil.move('raynor.obj', 'ceph_storage/')
    
    # Have the user give a new name for kerrigan.obj
    newname = input("What do you want the new name to be for kerrigan.obj? ")

    # Rename the file. Works like mv in linux
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + newname)

if __name__ == "__main__":   
    main()
