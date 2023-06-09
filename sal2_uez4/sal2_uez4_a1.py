import re

attacker_numbers = set()
attacker_phone_number_regex = re.compile(r'^0\d{4,5}(?:[\/]{1,3}|\.)\d\d[1|4]\d{5,7}')

with open("call_log.txt", "r", encoding="utf-8") as call_log:
    for line in call_log:
        match = re.search(attacker_phone_number_regex, line)
        print(match)
        if match:
            print(f"matched: {line}")
            attacker_numbers.add(match)
        else:
             print(f"no-match: {line}")

with open("filtered_numbers.txt", "w", encoding="utf-8") as output_file:
    for number in attacker_numbers:
        output_file.write(number + "\n")

