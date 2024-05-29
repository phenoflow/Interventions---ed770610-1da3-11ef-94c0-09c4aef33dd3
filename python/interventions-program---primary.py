# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Ian Buchan, Mamas A Mamas, Naveed Sattar, Darren M Ashcroft, Martin M Rutter, 2024.

import sys, csv, re

codes = [{"code":"8I81.00","system":"readv2"},{"code":"8Hj0.00","system":"readv2"},{"code":"679R.00","system":"readv2"},{"code":"9NiA.00","system":"readv2"},{"code":"9OLC.00","system":"readv2"},{"code":"8HkX.00","system":"readv2"},{"code":"9OLF.00","system":"readv2"},{"code":"8E79.00","system":"readv2"},{"code":"9NiD.00","system":"readv2"},{"code":"9OLG.00","system":"readv2"},{"code":"8Hj4.00","system":"readv2"},{"code":"9OLM.00","system":"readv2"},{"code":"9OLL.00","system":"readv2"},{"code":"Z65B.00","system":"readv2"},{"code":"9OLB.00","system":"readv2"},{"code":"8I84.00","system":"readv2"},{"code":"8Hj1.00","system":"readv2"},{"code":"8E7A.00","system":"readv2"},{"code":"8CA5200","system":"readv2"},{"code":"9NiE.00","system":"readv2"},{"code":"8Hj5.00","system":"readv2"},{"code":"9OLK.00","system":"readv2"},{"code":"8HHc.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('interventions-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["interventions-program---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["interventions-program---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["interventions-program---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
