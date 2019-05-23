# Grady McGradeface

Grady McGradeface checks a CSV file for student numbers and calculate how many passed and who failed. It supports calculation in points and percentages in addition to calculating the culmination of points or the average of percentages.

It treats cells that have a string (for example "absent") as a "non-conforming field", hence it is treated as zero-values.

A "test.csv" file has been supplied to demonstrate its use.

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

If you encounter difficulties with your CSV file, it might be in the wrong format. Note that it should be formatted as UTF-8.

Here is its help and usage text:

```text
usage: gradymcgradeface.py [-h] [-f str] [-p] [-t int] [-l float]

Grady McGradeface CLI

optional arguments:
  -h, --help            show this help message and exit
  -f str, --file str    CSV file to read from.
  -p, --percent         Treat grade value as percentages instead of points.
  -t int, --test int    Number of tests.
  -l float, --limit float
                        Number to set the grade limit to.
```

## Example usage

Options set:

* filename: test.csv
* Grade limit: 50
* Number of tests: 3

```text
./gradymcgradeface.py -f test.csv -l 50 -t 3

Non-conforming fields found:

ID: 121 -> absent
ID: 128 -> absent
ID: 129 -> absent
ID: 130 -> absent
ID: 131 -> absent
ID: 132 -> absent
ID: 17 -> absent
ID: 20 -> absent
ID: 39 -> absent
ID: 51 -> absent
ID: 6 -> absent


Students below the 50.0 points limit:

ID: 128 (points: 49.5)
ID: 129 (points: 42.0)
ID: 132 (points: 45.0)
ID: 133 (points: 23.5)
ID: 17 (points: 36.5)
ID: 20 (points: 41.5)
ID: 39 (points: 46.0)
ID: 6 (points: 38.5)


8 out of 133 students are below the limit of 50.0 points.
11 non-conforming fields found and were treated as zero-values.

The grade average was 83.06 points.
```
