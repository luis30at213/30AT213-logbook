import csv
import os
import re

## Array with divisions and their flags
divisions = {
    1: "it", 2: "us", 3: "br", 4: "ar", 5: "ve", 6: "co",
    8: "pe", 9: "ca", 10: "mx", 11: "pr", 12: "uy", 13: "de",
    14: "fr", 15: "ch", 16: "be", 17: "us", 18: "gr", 19: "nl",
    20: "no", 21: "se", 22: "gf", 23: "jm", 24: "pa", 25: "jp",
    26: "gb", 27: "is", 28: "hn", 29: "ie", 30: "es", 31: "pt",
    32: "cl", 33: "us", 34: "es", 35: "at", 36: "sm", 37: "do",
    38: "gl", 39: "ao", 40: "li", 41: "nz", 42: "lr", 43: "au",
    44: "za", 45: "rs", 46: "de", 47: "dk", 48: "sa", 49: "es",
    50: "ru", 51: "ad", 52: "fo", 53: "sv", 54: "lu", 55: "gi",
    56: "fi", 57: "in", 112: "lb", 330: "sk"
}

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input and output file paths
input_file = os.path.join(script_dir, "my_logs.csv")
template_file = os.path.join(script_dir, "templates", "logbook.html")
output_file = os.path.join(script_dir, "logbook.html")

# Read the CSV file and transform the data
with open(input_file, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = []
    for row in csv_reader:
        # Extract the first 1 or 2 digits from the DX field
        match = re.match(r"(\d{1,3})", row['DX'])
        division_number = int(match.group(1)) if match else None
        country_code = divisions.get(division_number, 'unknown')
        flag_cell = f'<img src="images/flags/{country_code}.png" width="40" height="30" alt="{country_code}">' if country_code != 'unknown' else ''
        rows.append(f"""
        <tr>
          <td>{row['DX']}</td>
          <td>{flag_cell}</td>
          <td>{row['DATE']}</td>
          <td>{row['UTC']}</td>
          <td>{row['FREQUENCY']}</td>
          <td>{row['MODE']}</td>
          <td>{row['RST'].replace('/', '')}</td>
        </tr>
        """)

# Read the template_logbook.html file
with open(template_file, mode='r', encoding='utf-8') as html_file:
    template_content = html_file.read()

# Replace {LOGBOOK} with the transformed rows
updated_content = template_content.replace("{LOGBOOK}", "\n".join(rows))

# Write the updated content to logbook.html
with open(output_file, mode='w', encoding='utf-8') as html_file:
    html_file.write(updated_content)
