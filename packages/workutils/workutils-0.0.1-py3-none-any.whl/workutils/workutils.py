# coding=utf-8
"""
@File    : workutils.py
@Time    : 2024/3/9 15:50
@Author  : MengYue Sun
@Description : A tool to solve daily work
"""
import os
import argparse


def get_files_path(folder_path, file_suffix=None, all_files=False):
    """
    Get all files including paths in the specified folder, default all files, only process specified suffix files after passing parameters

    Args:
        folder_path: Folder path
        file_suffix: File suffix, default None means all files
        all_files: Whether to traverse all files, including hidden files, default is False

    Returns:
        List containing all file paths
    """

    log_files = []  # Used to store all file paths
    file_types = {}  # Used to count file types and quantities

    try:
        for root, dirs, files in os.walk(folder_path):
            if not all_files:
                # Check whether the -a parameter is passed, if not, remove hidden folders
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                files = [f for f in files if not f.startswith('.')]

            for file in files:
                if file_suffix is None or file.lower().endswith(f".{file_suffix}"):
                    # If no suffix is specified or the file suffix matches the specified suffix, process the file
                    file_path = os.path.join(root, file)
                    log_files.append(file_path)

                    # Get file type
                    file_extension = os.path.splitext(file)[1].lower()
                    if file_extension not in file_types:
                        file_types[file_extension] = 1
                    else:
                        file_types[file_extension] += 1

        # Return a list containing all file paths, file types, and quantities
        return log_files, file_types
    except Exception as e:
        print(
            f'Error in get_files_path(folder_path, file_suffix="{file_suffix}", all_files={all_files}):{str(e)}'
        )


def show_file_counts(file_types, total_files):
    """
    Print each type of file and quantity, as well as the total number of files.

    Args:
        file_types (dict): Dictionary containing file types and quantities.
        total_files (int): Total number of files.
    """
    print("=" * 40)
    print("{:<10}{}".format("Suffix", "Counts"))
    print("-" * 40)
    for file_type, count in file_types.items():
        print("{:<10}{}".format(file_type, count))
    print("-" * 40)
    print("{:<10}{}".format("Total", total_files))
    print("=" * 40)


def main():
    parser = argparse.ArgumentParser(description="A toolkit for daily work")
    parser.add_argument("directory", type=str, help="Folder path to analyze")
    parser.add_argument("-s", "--suffix", type=str, help="File suffix to analyze")
    parser.add_argument("-a", "--all-files", action="store_true", help="Traverse all files, including hidden files")
    parser.add_argument("-o", "--output", type=str, help="File path to save the result")

    args = parser.parse_args()

    directory = os.path.abspath(args.directory)  # Convert the incoming directory to an absolute path
    file_suffix = args.suffix
    all_files = args.all_files
    result_file = os.path.abspath(args.output) if args.output else None

    if not os.path.isdir(directory):
        print("The specified path does not exist or is not a folder.")
        return

    files, types = get_files_path(directory, file_suffix, all_files)
    for file in files:
        print(file)

    # Calculate the total number of files
    total_files = len(files)

    # Print each type of file and quantity
    show_file_counts(types, total_files)

    if result_file:
        try:
            with open(result_file, "w") as f:
                for file in files:
                    f.write(file + "\n")
            print(f"The result has been saved to the {result_file} file.")
        except Exception as e:
            print(f"An error occurred while saving the result to the file: {e}")


if __name__ == "__main__":
    main()
