"""
Regular Expression for Extracting email ids
"""

import re

text = """
This alert service notifies trainwithshubham@gmail.com
and shubham.singh5@yahoo.com and priyanka_1@telegram.in
"""

list_of_emails = re.findall("[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",text)
print(list_of_emails)
