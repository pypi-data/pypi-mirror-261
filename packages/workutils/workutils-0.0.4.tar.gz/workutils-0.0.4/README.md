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
usage: workutils [-h] [-s SUFFIX] [-k KEYWORDS] [-a] [-o OUTPUT] directory

A tool for daily work

positional arguments:
  directory             Folder path to analyze

options:
  -h, --help            show this help message and exit
  -s SUFFIX, --suffix SUFFIX
                        File suffix to analyze
  -k KEYWORDS, --keywords KEYWORDS
                        Count Keywords in all files, such as keyword1,keyword2,keyword3
  -a, --all-files       Traverse all files, including hidden files
  -o OUTPUT, --output OUTPUT
                        File path to save the result

```

## Examples

1. Select the folder path to analyze

```shell
$ workutils ../
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
$
```

2. Select the folder path and specify the files with a certain suffix to analyze.

```shell
$ workutils ../ -s py
E:\workutils\workutils\workutils.py
E:\workutils\workutils\__init__.py
========================================
Suffix    Counts
----------------------------------------
.py       2
----------------------------------------
Total     2
========================================
$ 
```

3. Traverse all files, including hidden files

```shell
$ workutils ../ -a   
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
PS $ 

```

4. Input result file path to save the result

```shell
$ workutils ../ -s py -o result.txt
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
$ 
```

result.txt
```text
E:\workutils\workutils\workutils.py
E:\workutils\workutils\__init__.py

```

5. Find keywords and count occurrences in all files

```shell
$ workutils ./ -s log -k AS0100504GN_2 -o a.txt
E:\workutils\workutils\1111.log
E:\workutils\workutils\a\a.log
E:\workutils\workutils\b\test.log
E:\workutils\workutils\c\c.log
==================================================
Suffix              Counts
--------------------------------------------------
.log                4
--------------------------------------------------
Total               4
==================================================

==================================================
Keyword             File Name           Matches
--------------------------------------------------
AS0100504GN_2       1111.log            2
AS0100504GN_2       test.log            2
AS0100504GN_2       c.log               2
--------------------------------------------------
==================================================

The result has been saved to the E:\workutils\workutils\a.txt file.
$ 
```