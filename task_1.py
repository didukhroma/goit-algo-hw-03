import sys
import shutil
from pathlib import Path

def parse_args_and_return_folders_path():
    '''
    Parse arguments and return folders path
    '''
    args = sys.argv[1:]

    if len(args) == 0:
        print('Please add at least one argument')
        return None
    
    try:
        path_to_folder = Path(args[0])
        if not path_to_folder.exists():
            print(f'Path {path_to_folder} does not exist')
            return None
        if len(args) > 1:
            path_to_new_folder = Path(args[1])

            if not path_to_new_folder.exists():
                print(f"Destination folder {path_to_new_folder} does not exist, create dist in the source folder")
                path_to_new_folder = Path(path_to_folder / 'dist')
        else:
            path_to_new_folder = Path(path_to_folder / 'dist')
        return path_to_folder, path_to_new_folder    
    except Exception as e:
        print(f"Error parsing arguments: {e}")
        return None

 

def read_folder_and_copy_files(path_to_folder,path_to_new_folder):
    '''
    Read folder and copy files
    '''
    folders_name = []
    try:
        for file in path_to_folder.iterdir():
            try:
                if file.is_file():
                    if not file.suffix:
                        continue
                    # create subfolders
                    if file.suffix.lower() not in folders_name:
                        folders_name.append(file.suffix.lower())
                        Path(path_to_new_folder / file.suffix.lower()).mkdir(parents=True, exist_ok=True)               
                    #copy files
                    shutil.copy(file, path_to_new_folder / file.suffix.lower() / file.name)
                #recursion read folder    
                elif file.is_dir():
                    read_folder_and_copy_files(file,path_to_new_folder)
            except PermissionError:
                print(f"Permission denied for file {file}")
            except FileNotFoundError:
                print(f"File {file} not found")    
            except Exception as e:
                print(f"Error copying file {file}: {e}")
    except Exception as e:
        print(f"Error reading folder {path_to_folder}: {e}")

def main():
    '''
    Main function
    '''
    folders_path = parse_args_and_return_folders_path()
    if not folders_path:
        return    
    path_to_folder, path_to_new_folder = folders_path
    try:
        read_folder_and_copy_files(path_to_folder, path_to_new_folder)
        print("Operation completed successfully")
    except Exception as e:
        print(f"Operation failed: {e}")
    

if __name__ == '__main__':
    main()