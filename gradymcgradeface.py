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
	"-e", "--errors", action="store_true",
	help="Treat value errors or index error as a condition for failing.")
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
args=parser.parse_args()

csv_name = args.file
error_fail_true = args.errors
grade_limit = args.limit
grade_is_percent = args.percent
number_of_tests = args.test

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

with open(csv_name, "r") as file:

	csv_file = csv.reader(file)
	for line in csv_file:
		container1.append(line)

for key, value in container1:
	d.setdefault(key, []).append(value)

sorted(d.items())
ordered_dict = d.items()

not_admitted = 0
value_errors = 0
total_entities = 0

print("\n")

if grade_is_percent:
	print(f"Limit set to {grade_limit}% \n")
else:
	print(f"Limit set to {grade_limit} \n")

for thing in ordered_dict:

	total_entities += 1

	try:
		x = thing[1]

		x = [float(i) for i in x]
		
		x = sum(x)

		if grade_is_percent:
			x = x / number_of_tests

		if grade_is_percent:
			points_or_grade = f"{x}%"
		else:
			points_or_grade = f"points: {x}"

		if x < grade_limit:
			print(f"Not admitted:		{thing[0]} ({points_or_grade})")
			not_admitted += 1
	except IndexError:
		print(f"Out of range for:	{thing[0]}")
		value_errors += 1
	except ValueError:
		print(f"Value error for:	{thing[0]}")
		value_errors += 1
	except TypeError as e:
		print(f"TYPE ERROR for {thing[0]} ({thing[1]}; Something's wrong.\n {e}")

print("\n")

if error_fail_true:
	print(f"{not_admitted + value_errors} out of {total_entities} students are not admitted to the final.")
	print(f"of which {value_errors} had value errors or were out of range.")
else:
	print(f"{not_admitted} out of {total_entities} students are not admitted to the final.")
	print(f"{value_errors} had value errors or were out of range and thus not counted.")

print("\n")