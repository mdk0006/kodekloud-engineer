from pathlib import Path as path
dir_path = path("dir_1")

# Content of the above folder
print("The files and folder of the directory")
for p in dir_path.iterdir():
    print(p)

paths = [p for p in dir_path.iterdir()]  # List comprehensions
# Posix or Windows Path
print(paths)
# print(paths[0])

only_dir_paths = [p for p in dir_path.iterdir() if p.is_dir()] # CAN NOT be use for searching the pattern
for i in only_dir_paths:
    print(i)

# Recursive search
py_files = [p for p in dir_path.rglob("*.py")]# Recursive search 
print(py_files)
