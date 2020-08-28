'''
A simple Command-Line interface to traverse folders in a directory.
'''
# IDEAS #
# 1. View file/folder size, date created/modified
# 2. Sort file/folder by date modified/created
# 3. Read the contents of file if possible [read functionality].
# 4. Create a text file in the current directory, [open vi]
# 5. Create a folder in the current directory
# 5. View size of the current folder.
# 6. Delete a file/folder [DANGEROUS]
# 7. Show current folder after selection.

# Directory traversal CLI
import os

USER_START_PROMPT_MSG = ('Enter the name of a directory. (q: quit)\n')
USER_OPTION_PROMPT_MSG = ('Please provide which folder to list. '
                    '(q: quit, b: go back, 0: back to start)\t')

ALLOWED_OPTS = ('q', 'b', '0')

def evaluate_option(opt):
    pass

def is_valid(opt):
    if opt in ALLOWED_OPTS:
        return(True)
    else:
        return(False)


def prompt_user():
    opt = input(USER_OPTION_PROMPT_MSG)
    return(opt)

def get_dir_struct(thedir)-> tuple:
    '''
    Returns the directory structure, number of folders,
    and number of files in the directory as a tuple
    '''
    entries = os.listdir(thedir)
    dir_struct = {'files':[], 'folders': []}

    # NOTE: Avoiding two for loops by checking in one loop
    # NOTE: Although here a lst comprehension will work,
    #       because only two options, isfile implies not isdir
    # TODO: Do using next(os.walk)
    #       First entry will give
    #       dirpath, dirnames, filenames
    #       current folder, folders, files
    num_folders = 0
    num_files = 0
    for e in entries:
        f = os.path.join(thedir, e)
        if os.path.isfile(f):
            dir_struct['files'].append(e)
            num_files += 1
        elif os.path.isdir:
            dir_struct['folders'].append(e)
            num_folders += 1

    return(dir_struct, num_folders, num_files)

def print_dir_struct(dir_struct)-> None:
    print('files: ', dir_struct.get('files', []))
    print('folders:', ('[]' if not dir_struct['folders'] else ''))
    for i, folder in enumerate(dir_struct['folders']):
        print(f'\t{i+1}. {folder}')

    return(None)


def main():
    dir_is_valid = False
    while True:
        start_dir = input(USER_START_PROMPT_MSG)
        if os.path.isdir(start_dir):
            dir_is_valid = True
            break
        elif start_dir == 'q':
            break


    if dir_is_valid:
        curdir = start_dir
        curdirpath, curdirname = os.path.split(start_dir)
        show_dir_struct = True
        while True:
            if show_dir_struct:
                dir_struct, num_folders, num_files = get_dir_struct(curdir)
                print_dir_struct(dir_struct)

            opt = prompt_user()
            if opt == 'q':
                break
            elif opt == 'b':
                # go back one dir
                show_dir_struct = True
                curdir = os.path.dirname(curdir)
            elif opt == '0':
                # go back to start
                show_dir_struct = True
                curdir = start_dir
            else:
                try:
                    if 1 <= int(opt) < num_folders:
                        curdirpath = curdir
                        curdirname = dir_struct['folders'][int(opt)-1]
                        curdir = os.path.join(curdirpath, curdirname)
                        show_dir_struct = True
                    else:
                        print('Please enter a valid folder number')
                except ValueError:
                    print('Please enter a valid option.')



if __name__ == "__main__":
    main()