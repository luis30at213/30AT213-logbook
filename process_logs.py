import csv
import os

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
        rows.append(f"""
        <tr>
          <td>{row['DX']}</td>
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
