# workutils
A tool to solve daily work

## Installation
You can install, upgrade, uninstall workutils with these commands(without $):
```shell
$ pip install workutils
$ pip install --upgrade workutils
$ pip unstall workutils
```

## Help

```shell
$ workutils -h
usage: workutils [-h] [-s SUFFIX] [-a] [-o OUTPUT] directory

A toolkit for daily work

positional arguments:
  directory             Folder path to analyze

options:
  -h, --help            show this help message and exit
  -s SUFFIX, --suffix SUFFIX
                        File suffix to analyze
  -a, --all-files       Traverse all files, including hidden files
  -o OUTPUT, --output OUTPUT
                        File path to save the result

```

## Examples

1. Select the folder path to analyze

```shell
E:\workutils\workutils> workutils ../
E:\workutils\a.txt
E:\workutils\LICENSE
E:\workutils\README.md
E:\workutils\workutils\workutils.py
E:\workutils\workutils\__init__.py
========================================
Suffix    Counts
----------------------------------------
.txt      1
          1
.md       1
.py       2
----------------------------------------
Total     5
========================================
E:\workutils\workutils>
```

2. Select the folder path and specify the files with a certain suffix to analyze.

```shell
E:\workutils\workutils> workutils ../ -s py
E:\workutils\workutils\workutils.py
E:\workutils\workutils\__init__.py
========================================
Suffix    Counts
----------------------------------------
.py       2
----------------------------------------
Total     2
========================================
E:\workutils\workutils> 
```

3. Traverse all files, including hidden files

```shell
E:\workutils\workutils> workutils ../ -a   
E:\workutils\a.txt
E:\workutils\LICENSE
E:\workutils\README.md
E:\workutils\.git\config
...
E:\workutils\.git\refs\remotes\origin\HEAD
E:\workutils\workutils\workutils.py
E:\workutils\workutils\__init__.py
========================================
Suffix    Counts
----------------------------------------
.txt      1
          15
.md       1
.sample   13
.idx      1
.pack     1
.py       2
----------------------------------------
Total     34
========================================
PS E:\workutils\workutils> 

```

4. Input result file path to save the result

```shell
E:\workutils\workutils> workutils ../ -s py -o result.txt
E:\workutils\workutils\workutils.py
E:\workutils\workutils\__init__.py
========================================
Suffix    Counts
----------------------------------------
.py       2
----------------------------------------
Total     2
========================================
The result has been saved to the E:\workutils\workutils\result.txt file.
E:\workutils\workutils> 
```

result.txt
```text
E:\workutils\workutils\workutils.py
E:\workutils\workutils\__init__.py

```