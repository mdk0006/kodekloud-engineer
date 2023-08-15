from pathlib import Path
path = Path("ecommerce/__init__.py")
print(path.exists()) # Check if it exists or not 
print(path.is_file()) # Check if the given path is file 
print(path.is_dir()) # Check if the given path is directory
print(path.name) # Name of file
print(path.stem) # name with extension
print(path.suffix) # Extension only
print(path.parent) # Gives the parent 
# Creating a new path from existing one
path2= path.with_name("file.txt") # it will not create file just make a path
print(path2.absolute())  # Getting the absolute path 
path3=path.with_suffix(".txt") # Just changing the suffix in the path
print(path3)