import os
path='C:\\pp2\\lab6_mine\\test_case\\for_del.txt'
if os.access(path,os.F_OK):
    os.remove('for_del.txt')
    print('File deleted')
else:
    print('File do not exits')
