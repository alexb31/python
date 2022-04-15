import os
from datetime import datetime

# os.chdir("/Users/alexandre.bornstein/Desktop/Lab/")
# os.makedirs('toto/sub')
# os.removedirs('toto/sub')

# os.rename('loop.py', 'loop2.py')

# mod_time = os.stat('loop.py').st_mtime
# print(datetime.fromtimestamp(mod_time))

# print(os.listdir())

# for dirpath, dirname, filename in os.walk(os.getcwd()):
#   print('Current Path:', dirpath)
#   print('Current Name:', dirname)
#   print('Current file name:', filename)
#   print()

# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)

# print(os.environ.get("HOME"))
print(os.path.dirname('/tmp/test.txt'))