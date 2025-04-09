import re
import json

log_file = "/tmp/timestamp.log"
output_file = "error_logs.json"

error_entries = []

with open(log_file, "r") as file:
    for line in file:
        match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - ERROR - (.+)", line)
        if match:
            timestamp = match.group(1)
            message = match.group(2)
            error_entries.append({"timestamp": timestamp, "error": message})

with open(output_file, "w") as json_file:
    json.dump(error_entries, json_file, indent=4)

print("Error logs extracted to", output_file)
