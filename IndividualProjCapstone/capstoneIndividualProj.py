import csv

with open('oui.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["Assignment"]} is the oui for {row["Organization Name"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    