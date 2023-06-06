import re

attacker_numbers = set()

with open("call_log.txt", "r", encoding="utf-8") as call_log:
    for line in call_log:
        match = re.search(r'\b0(\d{4,5})[./]{1,3}(?:1|4)(\d{7,9})\b', line)
        if match:
            area_code = match.group(1)
            number = match.group(2)
            formatted_number = f"{area_code}/{number}"
            attacker_numbers.add(formatted_number)

with open("filtered_numbers.txt", "w", encoding="utf-8") as output_file:
    for number in attacker_numbers:
        output_file.write(number + "\n")
