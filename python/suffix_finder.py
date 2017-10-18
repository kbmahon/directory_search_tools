import os


def get_file_dirs_with_suffix(directory_of_interest, suffix):
    """
    Gets all of the directories that have a file named with the given suffix
    :param directory_of_interest: string path of the directory to search
    :param suffix: string end of file name for which to look
    :return: all of the directory paths that contain a file with the suffix of interest
    """
    directory_list = set()
    # directory contents, as returned from os.walk is a tuple: (dir_name, [directories], [filenames])
    for directory_contents in os.walk(directory_of_interest):
        file_name_list = directory_contents[2]
        parent_directory = directory_contents[0]
        for file_name in file_name_list:
            if file_name.endswith(suffix):
                directory_list.add(parent_directory)

    return directory_list


def main(args):
    for dir in get_file_dirs_with_suffix(args.directory, args.suffix):
        print(dir)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Searches a directory for files ending'
                                                 ' in a given suffix.')
    parser.add_argument('suffix', type=str, help='file suffix for which to search')
    parser.add_argument('directory', type=str, help='directory in which to search')

    args = parser.parse_args()

    main(args)
