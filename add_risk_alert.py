import csv

def calculate_risk(signal):
    signal = float(signal)
    if signal > 1.2:
        return "🚩 High Risk"
    elif signal > 0.7:
        return "⚠️ Moderate Risk"
    else:
        return "OK: Cleared (Low)"

with open("scan_results.csv", "r", encoding="utf-8") as infile, \
     open("cleaned_scan_results.csv", "w", newline="", encoding="utf-8") as cleanfile, \
     open("skipped_rows_log.csv", "w", newline="", encoding="utf-8") as logfile:

    reader = csv.reader(infile)
    clean_writer = csv.writer(cleanfile)
    log_writer = csv.writer(logfile)

    header = next(reader)
    header_with_risk = header + ["Risk Alert"]
    
    # Write headers to both files
    clean_writer.writerow(header_with_risk)
    log_writer.writerow(header + ["Reason Skipped"])

    for row in reader:
        try:
            if row[3].strip() == "":
                row.append("Missing Signal Score")
                log_writer.writerow(row)
                continue
            risk = calculate_risk(row[3])
            row.append(risk)
            clean_writer.writerow(row)
        except ValueError:
            row.append("Invalid Signal Format")
            log_writer.writerow(row)
