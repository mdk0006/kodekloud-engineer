# ? Check if the path exists in the current directory or not
from pathlib import Path as path


def main():
    # Getting the folder name
    folder = get_name()
    # Checking if the folder exists or not
    check_create(folder)


def get_name():
    """Getting the name for the directory to check"""
    name_of_dir = input("Name of the directory you want to check? \n")
    folder = path(name_of_dir)
    return folder


def check_create(folder):
    """Check if the directory exists and then make or change """
    if folder.exists():
        print('The given folder is present')
        change = input(
            "Do you want to change its name or remove it? \n c for change r for remove \n")
        if change == 'c':
            new_name = input("\nEnter a new Name: ")
            folder.rename(new_name)
            print("The folder name has been changed")
        elif change == 'r':
            folder.rmdir()
            print("The folder has been removed")
        else:
            pass
    else:
        print('The given folder is not present')
        make = input('Do you want to create one? y for yes \n')
        if make == "y":
            folder.mkdir()
            print("The folder has been created")
        else:
            print("No folder will be created")


if __name__ == "__main__":
    main()
