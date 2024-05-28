# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Carolyn A Chew-Graham, Nav Kapur, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"C108G00","system":"readv2"},{"code":"C108800","system":"readv2"},{"code":"C109G00","system":"readv2"},{"code":"C100011","system":"readv2"},{"code":"C100112","system":"readv2"},{"code":"C109D00","system":"readv2"},{"code":"C109500","system":"readv2"},{"code":"C108E00","system":"readv2"},{"code":"C108600","system":"readv2"},{"code":"C10E.12","system":"readv2"},{"code":"C10FJ00","system":"readv2"},{"code":"66AV.00","system":"readv2"},{"code":"C109400","system":"readv2"},{"code":"C109900","system":"readv2"},{"code":"C108400","system":"readv2"},{"code":"C109.00","system":"readv2"},{"code":"C109J11","system":"readv2"},{"code":"C10E412","system":"readv2"},{"code":"C10E812","system":"readv2"},{"code":"C108500","system":"readv2"},{"code":"C109300","system":"readv2"},{"code":"C108.00","system":"readv2"},{"code":"66A5.00","system":"readv2"},{"code":"C10FJ11","system":"readv2"},{"code":"C109J00","system":"readv2"},{"code":"C109700","system":"readv2"},{"code":"C109J12","system":"readv2"},{"code":"C108.11","system":"readv2"},{"code":"E10.9","system":"readv2"},{"code":"E11.9","system":"readv2"},{"code":"E10.0","system":"readv2"},{"code":"E10.1","system":"readv2"},{"code":"E11.0","system":"readv2"},{"code":"E11.1","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulindependent-diabetes---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulindependent-diabetes---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulindependent-diabetes---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
