#!/usr/bin/env python
"""importing"""
import sys

def map_data():
    """mapperf cuntion"""
    for line in sys.stdin:
        # stripping any leading/trailing whitespace
        line = line.strip()

        # splitting the line into fields
        fields = line.split(',')

        # checking if the row is valid
        if len(fields) >= 3:
            # extract id, company, and total yearly compensation
            id_val = fields[0]
            company = fields[1]
            total_compensation = fields[2]

            # print id, companyand total yearly compensation
            print(f"{id_val}\t{company},{total_compensation}")
