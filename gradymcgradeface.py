#!/usr/bin/python3

import argparse
import csv
import sys

parser = argparse.ArgumentParser(
    description="Grady McGradeface CLI")
parser.add_argument(
    "-f", "--file", metavar="str", type=str,
    help="CSV file to read from.")
parser.add_argument(
    "-p", "--percent", action="store_true",
    help="Treat grade value as percentages instead of points.")
parser.add_argument(
    "-t", "--test", metavar="int", type=int,
    help="Number of tests.")
parser.add_argument(
    "-l", "--limit", metavar="float", type=float,
    help="Number to set the grade limit to.")
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

csv_name = args.file
grade_limit = args.limit
grade_is_percent = args.percent
number_of_tests = args.test

not_admitted = 0
total_entities = 0
cumulative_points = 0

if grade_limit is None:
    print("You have to enter a grade limit!")
    quit()
elif csv_name is None:
    print("You have to enter a CSV file to parse!")
    quit()
elif grade_is_percent and number_of_tests is None:
    print("You have to state the number of tests when calculating percentages!")
    quit()

container1 = []
d = {}
value_errors = []

with open(csv_name, "r") as file:

    csv_file = csv.reader(file)
    for line in csv_file:
        container1.append(line)

for key, value in container1:
    try:
        value = float(value)
        d.setdefault(key, []).append(value)
    except ValueError as e:
        d.setdefault(key, []).append(0)
        value_errors.append([key, value])

ordered_dict = sorted(d.items())

if value_errors != 0:
    print("\nNon-conforming fields found:\n")
    for x in sorted(value_errors):
        if x[1].isspace():
            print("ID:", x[0], "->", "N/A")
        else:
            print("ID:", x[0], "->", x[1])

print("\n")

if grade_is_percent:
    grade_limit_info = str(grade_limit) + "%"
else:
    grade_limit_info = str(grade_limit) + " points"

print(f"Students below the {grade_limit_info} limit:\n")

for id in ordered_dict:

    total_entities += 1

    try:
        x = id[1]
        x = [float(i) for i in x]
        x = sum(x)

        cumulative_points += x

        if grade_is_percent:
            x = x / number_of_tests

        if grade_is_percent:
            points_or_grade = f"{x}%"
        else:
            points_or_grade = f"points: {x}"

        if x < grade_limit:
            print(f"ID: {id[0]} ({points_or_grade})")
            not_admitted += 1

    except IndexError:
        print(f"Out of range for:\t{id[0]}")
        value_errors += 1

    except TypeError as e:
        print(
            f"TYPE ERROR for {id[0]} ({id[1]}); Someid's wrong.\n {e}")

print(f"\n\n{not_admitted} out of {total_entities} students are below the limit of {grade_limit_info}.")
print(f"{len(value_errors)} non-conforming fields found and were treated as zero-values.")

if grade_is_percent:
    print(
        f"\nThe grade average was {round(cumulative_points / total_entities, 3)}%.")
else:
    print(
        f"\nThe grade average was {round(cumulative_points / total_entities, 2)} points.")

print("\n")
