import os

nums_dirs = 0
nums_files = 0

try:
    for root, dirs, files in os.walk(r"C:\GitHub\Note-Taking"):
        print("directory {}".format(root))
        if '.git' in dirs:
            dirs.remove('.git')
        for directory in dirs:
            nums_dirs += 1
            print("<DIR>\t{}".format(directory))
        for file in files:
            nums_files += 1
            print("\t{}".format(file))
    print('dirs:{}---files:{}'.format(nums_dirs, nums_files))
except OSError as ex:
    print(ex)