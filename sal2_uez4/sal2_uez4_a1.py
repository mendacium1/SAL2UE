"""
sal2_uez3_a1.py
(c) S2210239021, Jakob Mayr
Exercise sheet 4

This python program reads in telephone numbers from a log-file called "call_log.txt". It than
filters out numbers from "attackers" by a given ruleset using a regex. The attack numbers are then
written into the file "attacker_numbers.txt".
"""
import re

# Set to store attacker phone numbers (no dublicates)
attacker_numbers = set()

# Regular expression pattern to match attacker phone numbers
# Explanation:
# \b - word boundary anchor (so that match does not occur in larger word)
# 0 - String begins with 0
# (\d{4,5}) - 4 or 5 digits long area code (brackets for "area"-group)
# (?:[\/]{1,3}|\.) - Non-capturing group that looks for "/", "//", "///" or a ".". This represents
# the seperator between area-code and number
# (\d\d[1|4]\d{5,7}) - Group that checks the number. (2 digits followed by 1 or 3 in the thir
# place and 5-7 digits at the end - total length 8-10)
attacker_phone_number_regex = re.compile(r'\b0(\d{4,5})(?:[\/]{1,3}|\.)(\d\d[1|4]\d{5,7})\b')

# Open the call log file to read in phone numbers
with open("call_log.txt", "r", encoding="utf-8") as call_log:
    # Iterate over each line in the call log (each number)
    for line in call_log:
        # Search for a match using the regular expression
        match = re.search(attacker_phone_number_regex, line)
        if match:
            # Extract the area code and number from the match
            area_code = match.group(1)
            number = match.group(2)
            formatted_number = f"{area_code}/{number}"
            # Add the formatted number to the set of attacker numbers
            attacker_numbers.add(formatted_number)

# Open a file to write the attacker numbers
with open("attacker_numbers.txt", "w", encoding="utf-8") as output_file:
    # Write each attacker number to the file (should be 1863 numbers)
    for number in attacker_numbers:
        output_file.write(number + "\n")

