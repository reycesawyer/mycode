#!/usr/bin/env python3

# import additional code to complete our task - these are not commonly used so they must be imported
import shutil # tool used to help with directory movements. Stands for shell utility
import os # another tool to help interact with the OS
import getpass # tool to get username

# Get current username so I can use on different systems with different usernames
USER = getpass.getuser()


def main():
    # move into the working directory
    working_directory = f"/home/{USER}/mycode/"
    os.chdir(working_directory)

    # copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copy the entire directoryA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")

    # Tell the user the script has executed
    print("The script has finished")


if __name__ == "__main__":
    main()
