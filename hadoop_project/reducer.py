#!/usr/bin/python3
"""importing"""
import sys

def reducer():
    """reducer function"""
    top_salaries = []

    for line in sys.stdin:
        line = line.strip()
        id_val, rest = line.split('\t', 1)
        company, salary = rest.split(',', 1)
        salary = float(salary)

        # adding the current record to the list and keep it sorted by salary
        top_salaries.append((id_val, salary, company))
        top_salaries = sorted(top_salaries, key=lambda x: x[1], reverse=True)[:10]

    # printign the top 10 salaries
    print("id\tSalary\tcompany")
    for id_val, salary, company in top_salaries:
        print(f"{id_val}\t{salary}\t{company}")
