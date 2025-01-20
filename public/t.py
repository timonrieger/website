import os

def replace_underscore(path):
    for root, files in os.walk(path):
        print(root)
        print(files)
        for file in files:
            if '_' in file:
                new_file = file.replace('_', '-')
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} to {new_path}')

# specify the path here
replace_underscore('posts/')