import os
x=os.access('C:\\pp2\leetcode\\algorithm.study', os.F_OK)
if x:
    print('yes')
else:print('no')
