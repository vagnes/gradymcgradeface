# Grady McGradeface

Grady McGradeface checks a CSV file for student numbers and calculate how many failed and who. It supports calculation in points and percentages.

It treats cells that have a string (for example "absent") as errors that you can set as a failing condition as well.

A "test.csv" file has been supplied to demontstrate its use.

The script calculates all test results that student number has. Thus, to calculate more than one test, just append it to your CSV file, like so:

```text
1,39.5
2,27
3,28
(...)
1,40
2,28
3,22.5
(...)
1,14
2,20
3,'absent'
(...)
```

Here is its help and usage text:

```text
usage: gradymcgradeface.py [-h] [-f str] [-e] [-p] [-t int] [-l float]

Grady McGradeface CLI

optional arguments:
  -h, --help            show this help message and exit
  -f str, --file str    CSV file to read from.
  -e, --errors          Treat value errors or index error as a condition for
                        failing.
  -p, --percent         Treat grade value as percentages instead of points.
  -t int, --test int    Number of tests.
  -l float, --limit float
                        Number to set the grade limit to.
```
