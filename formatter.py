import csv
from scrapper import scrape_problems
import csv

problems = scrape_problems()

filename = "problemstatements.csv"
with open(filename, "w", newline="") as f:
    w = csv.DictWriter(f, ["id", "code", "institution", "problem_statement"])
    w.writeheader()
    for problem in problems:
        w.writerow(problem)
