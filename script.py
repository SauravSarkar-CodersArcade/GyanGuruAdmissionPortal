# # script.py
# import os
#
# def print_structure(startpath='.', ignore_dirs=None):
#     if ignore_dirs is None:
#         ignore_dirs = []
#
#     for root, dirs, files in os.walk(startpath):
#         # Skip ignored directories
#         dirs[:] = [d for d in dirs if d not in ignore_dirs]
#
#         level = root.replace(startpath, '').count(os.sep)
#         indent = '    ' * level
#         print(f"{indent}{os.path.basename(root)}/")
#         subindent = '    ' * (level + 1)
#         for f in files:
#             print(f"{subindent}{f}")
#
# if __name__ == "__main__":
#     print("Project Folder Structure (ignoring venv, .idea/):\n")
#     print_structure(ignore_dirs=['venv', '.idea'])

# import os, sys
#
#
# def print_structure(startpath='.', ignore_dirs=None):
#     if ignore_dirs is None:
#         ignore_dirs = []
#
#     for root, dirs, files in os.walk(startpath):
#         dirs[:] = [d for d in dirs if d not in ignore_dirs]
#         level = root.replace(startpath, '').count(os.sep)
#         indent = '    ' * level
#         print(f"{indent}{os.path.basename(root)}/")
#         subindent = '    ' * (level + 1)
#         for f in files:
#             print(f"{subindent}{f}")
#
#
# if __name__ == "__main__":
#     path = sys.argv[1] if len(sys.argv) > 1 else '.'
#     print(f"Project Folder Structure of {path} (ignoring venv, .idea/):\n")
#     print_structure(startpath=path, ignore_dirs=['venv', '.idea'])

import os, sys

def print_structure(startpath='.', ignore_dirs=None, ignore_ext=None):
    if ignore_dirs is None:
        ignore_dirs = []
    if ignore_ext is None:
        ignore_ext = []

    for root, dirs, files in os.walk(startpath):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        level = root.replace(startpath, '').count(os.sep)
        indent = '    ' * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = '    ' * (level + 1)

        for f in files:
            if any(f.endswith(ext) for ext in ignore_ext):
                continue
            print(f"{subindent}{f}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(f"Project Folder Structure of {path}:\n")
    print_structure(
        startpath=path,
        ignore_dirs=['venv', '.idea', '.git', '.vscode'],
        ignore_ext=['.exe', '.class']  # skip compiled files
    )
