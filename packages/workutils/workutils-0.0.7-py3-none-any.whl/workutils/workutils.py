# coding=utf-8
"""
@File    : workutils.py
@Time    : 2024/3/9 15:50
@Author  : MengYue Sun
@Description : A tool to solve daily work
"""
import os
import argparse
import re
import chardet
from tqdm import tqdm


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


# Get the encoding format of the specified file
def get_file_encoding(file_path):
    try:
        with open(file_path, 'rb') as file:
            result = chardet.detect(file.read())
            encoding = result['encoding']
            # confidence = result['confidence']
            # return encoding, confidence
            return encoding
    except Exception as e:
        print(f"Error in get_file_encoding(file_path): {str(e)}")


def show_file_counts(file_types, total_files=0):
    """
    Print each type of file and quantity, as well as the total number of files.

    Args:
        file_types (dict): Dictionary containing file types and quantities.
        total_files (int): Total number of files.
    """
    print("=" * 50)
    print("{:<20}{}".format("Suffix", "Counts"))
    print("-" * 50)
    for file_type, count in file_types.items():
        print("{:<20}{}".format(file_type, count))
    print("-" * 50)
    print("{:<20}{}".format("Total", total_files))
    print("=" * 50)
    print()


def show_keyword_files(files, results):
    """
    Print each file name along with the keyword match count.

    Args:
        files (list): List of file paths.
        results (list): List of dictionaries containing keyword match counts for each file.
    """
    print("=" * 50)
    print("{:<20}{:<20}{}".format("Keyword", "Matches", "File Name"))
    print("-" * 50)
    for file, result in zip(files, results):
        file_name = os.path.basename(file)  # Get the file name
        for keyword, matches in result.items():
            if matches > 0:
                print("{:<20}{:<20}{}".format(keyword, matches, file_name))
    print("-" * 50)
    print("=" * 50)
    print()


def get_key_words(file_path, keywords):
    list_results = []
    dict_keyword_counts = {keyword: 0 for keyword in keywords}

    try:
        encode = get_file_encoding(file_path)
        with open(file_path, "r", encoding=encode) as file:
            for line in file:
                for keyword in keywords:
                    escaped_keyword = re.escape(keyword)
                    matches = re.finditer(escaped_keyword, line, flags=re.IGNORECASE)
                    dict_keyword_counts[keyword] += len(list(matches))
            list_results.append(dict_keyword_counts)
        return list_results, dict_keyword_counts
    except FileNotFoundError:
        print(f"Error File {file_path} not found.")
        return [], {}
    except PermissionError:
        print(f"Error No permission to read file {file_path}.")
        return [], {}
    except Exception as e:
        print(f'Error in reading file: {e}')
        return [], {}


def main():
    parser = argparse.ArgumentParser(description="A tool for daily work")
    parser.add_argument("directory", type=str, help="Folder path to analyze")
    parser.add_argument("-s", "--suffix", type=str, help="File suffix to analyze")
    parser.add_argument("-k", "--keywords", type=str,
                        help="Count Keywords in all files, such as 'key word1','key word2'")
    parser.add_argument("-a", "--all-files", action="store_true", help="Traverse all files, including hidden files")
    parser.add_argument("-o", "--output", type=str, help="File path to save the result")

    args = parser.parse_args()

    # Convert the incoming directory to an absolute path
    directory = os.path.abspath(args.directory)
    file_suffix = args.suffix
    list_keywords = [keyword.strip() for keyword in args.keywords.split(",")] if args.keywords else []

    all_files = args.all_files
    result_file = os.path.abspath(args.output) if args.output else None

    # Check if the directory exists
    if not os.path.exists(directory):
        print("The specified path does not exist.")
        return

    # Check if the specified path is a folder
    if not os.path.isdir(directory):
        print("The specified path is not a folder.")
        return

    files, types = get_files_path(directory, file_suffix, all_files)
    for file in files:
        print(file)

    # Calculate the total number of files
    total_files = len(files)

    # Print each type of file and quantity
    show_file_counts(types, total_files)

    keyword_results = []  # List to save keyword match results
    if list_keywords:  # Check if keyword parameters are passed
        with tqdm(total=total_files) as pbar:
            for file_path in files:
                results, counts = get_key_words(file_path=file_path, keywords=list_keywords)
                keyword_results.append((file_path, counts))
                pbar.update(1)

        # Print keyword match results
        show_keyword_files([os.path.basename(file[0]) for file in keyword_results],
                           [file[1] for file in keyword_results])

    if result_file:
        try:
            with open(result_file, "w") as f:
                for file in files:
                    f.write(file + "\n")
                if list_keywords:
                    f.write("\nKeyword             Matches           File Name\n")
                    f.write("-" * 50)
                    f.write("\n")
                    for file_path, counts in keyword_results:
                        file_name = os.path.basename(file_path)
                        for keyword, matches in counts.items():
                            if matches > 0:
                                f.write(f"{keyword:<20}{matches:<20}{file_name}\n")
                    f.write("-" * 50)
            print(f"The result has been saved to the {result_file} file.")
        except Exception as e:
            print(f"An error occurred while saving the result to the file: {e}")

if __name__ == "__main__":
    # Get the directory path of the current script file
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Change the working directory to the directory where the script file is located
    os.chdir(script_dir)
    main()
