import csv, requests 

with open("PSSvsichni.tsv","r") as file, open("PSSemaily.tsv", "w", newline="") as outfile:
    tsvlines = []
    inst_ids = set()
    maildict = {}

    tsvin = csv.reader(file, delimiter="\t")
    for row in tsvin:
        inst_ids.add(row[1])
        tsvlines.append(row)

    for counter,inst_id in enumerate(inst_ids):
        email = "(bez emailu)"
        link = "https://iregistr.mpsv.cz/socreg/rozsirene_hledani_sluzby.do?si=" + inst_id
        content = requests.get(link).text.split()
        for line in content:
            if "mailto" in line:
                email = line.split("\"")[1][7:]
        print(str(counter+1) + "/" + str(len(inst_ids)) + ": " + inst_id + " " + email)
        maildict[inst_id] = email
    print(maildict)

    for line in tsvlines:
        if line[1] in maildict:
            line.append(maildict[line[1]])
    
    tsvout = csv.writer(outfile, delimiter="\t")

    for line in tsvlines:
        tsvout.writerow(line)