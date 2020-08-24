import os


def run():
    path = home_path
    while True:
        try:
            print('\n------------------------')
            view_option = int(input('Enter\n1: all files\n2: folders only\n3: files only\n: '))
            print('------------------------\n')
        except ValueError:
            print('Please Enter a numeric value')
            print('------------------------\n')
            continue
        home = None
        folder = False
        if view_option == 1:
            home = [x for x in sorted(os.listdir(path))]
        elif view_option == 2:
            folder = True
            home = [x for x in sorted(os.listdir(path)) if x[0] != '.' and os.path.isdir(os.path.join(path, x))]
        elif view_option == 3:
            home = [x for x in sorted(os.listdir(path)) if x[0] != '.' and os.path.isfile(os.path.join(path, x))]
            folder = False
        directory_list = dict()
        print(f'Directory list of \'{path}\'')
        if home:
            for i, data in enumerate(home):
                directory_list[i + 1] = data
                print(f'{i + 1}: {data}')
            try:
                print('\n------------------------')
                choice = int(input('Enter \n1: Go further\n2: Clean Up\n: '))
                print('------------------------\n')
            except ValueError:
                print('Please Enter a numeric value')
                print('------------------------\n')
                continue
            if choice == 1:
                try:
                    print('\n-----------------------------------------')
                    folder_index = int(input('Enter srno. to enter the folder\n: '))
                    print('------------------------\n')
                except ValueError:
                    print('Please Enter a numeric value')
                    print('-----------------------------------------\n')
                    continue
                if folder:
                    path = os.path.join(path, directory_list[folder_index])
                    print(f'{directory_list[folder_index]} selected, path: {path}')
                else:
                    print(f'Cannot go inside {directory_list[folder_index]} because it is not a folder.')
            elif choice == 2:
                clean_up(path)
                break
            else:
                print('Invalid Choice entered.')


def clean_up(path):
    global FOLDERS, EXT_IMG, EXT_DOCS, EXT_MEDIA, EXT_ZIPS, EXT_TORRENTS, EXT_PROGRAMS_PACKAGES, FOLDERS
    print(FOLDERS)
    message = 'Enter srno. for folders to create\n' + ''.join(
        f'{i + 1}: {name}\n' for i, name in enumerate(FOLDERS)) + \
              '8: All' + \
              'Note: Files belonging to other than selected folders will be moved to \'Others\' folder' \
              '\n: '
    choices = [int(x) for x in input(message).split(' ')]
    if 8 in choices:
        choices.extend([1, 2, 3, 4, 5, 6, 7])
        choices = list(set(choices))
    print(f'cleaning up directory: {path}')
    all_files = os.listdir(path)
    for file in all_files:
        if os.path.isfile(os.path.join(path, file)):
            if file.lower().endswith(tuple(EXT_ZIPS)) and 1 in choices:
                folder = FOLDERS[0]
            elif file.lower().endswith(tuple(EXT_DOCS)) and 2 in choices:
                folder = FOLDERS[1]
            elif file.lower().endswith(tuple(EXT_IMG)) and 3 in choices:
                folder = FOLDERS[2]
            elif file.lower().endswith(tuple(EXT_PROGRAMS_PACKAGES)) and 4 in choices:
                folder = FOLDERS[3]
            elif file.lower().endswith(tuple(EXT_MEDIA)) and 5 in choices:
                folder = FOLDERS[4]
            elif file.lower().endswith(tuple(EXT_TORRENTS)) and 6 in choices:
                folder = FOLDERS[5]
            else:
                folder = FOLDERS[6]
            move_files(path, file, folder)


def move_files(path, file_name, folder):
    try:
        os.mkdir(os.path.join(path, folder))
    except FileExistsError:
        pass
    current_path = os.path.join(path, file_name)
    new_path = os.path.join(path, folder + '/' + file_name)
    print(f'moving {file_name} from {current_path} --> {new_path}')
    try:
        os.replace(current_path, new_path)
    except OSError:
        pass


FOLDERS = ['-Zips', '-Documents', '-Images', '-Programs & Packages', '-Media', '-Torrents',
           '-Other']
EXT_ZIPS = ['.zip', '.gz', '.tar', '.pkg', '.rar', '.7z', '.z', '.tar.gz', '.rpm']
EXT_PROGRAMS_PACKAGES = ['.csv', '.html', '.css', '.deb', '.exe', '.sh', '.json', '.c', '.cpp', '.py', '.java', '.js',
                         '.php']
EXT_IMG = ['.jpeg', '.jpg', '.png', '.gif', '.webp', '.svg', '.tif', '.tiff', '.bmp']
EXT_MEDIA = ['.mp3', '.mp4', '.mpa', '.wav', '.wma', '.mkv', '.3gp', '.avi', '.flv', '.mov', '.mpg', '.mpeg']
EXT_DOCS = ['.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wpd', '.ods', '.xls', '.xlsm', '.xlsx']
EXT_TORRENTS = ['.torrent']

if __name__ == '__main__':
    home_path = '/home/hp'
    run()
