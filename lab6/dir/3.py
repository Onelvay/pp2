import os
path='C:\\pp2\\leetcode'
if os.path.exists(path):
    print("Exits\nFile name:",os.path.basename(path))
    print("Dir and files in path: ", os.listdir(path))
else: print("NO")
