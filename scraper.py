import requests 

with open("id_list") as file:
    with open("mail_list", "w") as outfile:
        for line in file:
            inst_id = line.strip()
            email = "(bez emailu)"
            link = "https://iregistr.mpsv.cz/socreg/rozsirene_hledani_sluzby.do?si=" + inst_id
            content = requests.get(link).text.split()
            for line in content:
                if "mailto" in line:
                    email = line.split("\"")[1][7:]
            outfile.write(inst_id + " " +  email + "\n")