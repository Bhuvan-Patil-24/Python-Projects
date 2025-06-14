import os

folders = os.listdir()
for folder in folders:
    os.chdir(folder)
    filename = f"{folder.lower()[5]}"
    for i in ['py', 'js', 'c']:
        with open(f"{filename}.{i}", "w") as f:
            f.write(f"This is file {filename}.{i} in folder {folder}\n")
