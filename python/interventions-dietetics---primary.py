# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Ian Buchan, Mamas A Mamas, Naveed Sattar, Darren M Ashcroft, Martin M Rutter, 2024.

import sys, csv, re

codes = [{"code":"66AY.00","system":"readv2"},{"code":"13A4.00","system":"readv2"},{"code":"8CA4200","system":"readv2"},{"code":"9NJ6.00","system":"readv2"},{"code":"ZA11925","system":"readv2"},{"code":"13B..00","system":"readv2"},{"code":"8CA4700","system":"readv2"},{"code":"1F11.00","system":"readv2"},{"code":"13B1.00","system":"readv2"},{"code":"ZC2..12","system":"readv2"},{"code":"8CA4600","system":"readv2"},{"code":"ZC2..11","system":"readv2"},{"code":"8CA4.00","system":"readv2"},{"code":"8CE4.00","system":"readv2"},{"code":"8B5A.00","system":"readv2"},{"code":"8CA4z00","system":"readv2"},{"code":"8CA4100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('interventions-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["interventions-dietetics---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["interventions-dietetics---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["interventions-dietetics---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
