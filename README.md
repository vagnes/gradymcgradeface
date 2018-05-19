# Grady McGradeface

Grady McGradeface checks a CSV file for student numbers and calculate how many passed and who failed. It supports calculation in points and percentages.

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

## Example usage

Options set:

* filename: test.csv
* Value errors and index errors are treated as failing condition.
* Grade limit: 70
* Number of tests: 3

```text
./gradymcgradeface.py -f test.csv -e -l 70 -t 3


Limit set to 70.0

Not admitted:           4 (points: 64.0)
Value error for:        6
Value error for:        17
Value error for:        20
Not admitted:           25 (points: 64.0)
Value error for:        39
Value error for:        51
Value error for:        121
Value error for:        128
Value error for:        129
Value error for:        130
Value error for:        131
Value error for:        132
Not admitted:           133 (points: 23.5)


14 out of 133 students are not admitted to the final.
of which 11 had value errors or were out of range.

The grade average was 79.16 points.
```