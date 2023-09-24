import json
import requests
from bs4 import BeautifulSoup
import re

from html_content1 import liste1 
from html_content2 import liste2
from html_content3 import liste3
from html_content4 import liste4
from company_names import Company as companies




"""url = "https://www.nordnet.no/market/stocks?exchangeCountry=NO"

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    with open("html_content1.txt", "w", encoding="utf-8") as file:
        file.write(html_content)
    print("HTML content saved to html_content.txt")
else:
    print("Failed to retrieve HTML content")"""



input_text = liste1 + liste2 + liste3 + liste4
#print(input_text)
whole_dict = []

#print(companies)
for i in companies:
#i = input("Enter a company name: ").upper()
    try: 
        i = i.upper()
        print(i)
        search_index = input_text.upper().find(i)
        print(search_index)


        if search_index != -1:
            start_index = input_text.rfind("{\"instrument_id\":", 0, search_index)
            end_index = input_text.find("}", search_index) + 1
            if start_index != -1 and end_index != -1:
                company_info = input_text[start_index:end_index]
                company_info= json.loads(company_info)
                #print(company_info)
                info = [company_info["instrument_id"], company_info["name"]]
                
            else:
                print("Company information not found.")
        else:
            print("Company not found.")

        print(info)

        if (i=="AKER" and company_info["name"] == "AKER BP"):
            info[1] = "AKER"
            info[0] = "16105613"

        url = "https://www.nordnet.no/market/stocks"
        ny_url = url + "/" + str(info[0]) + "-" + info[1].lower() + "?details"
        print(ny_url)

        if i == "LERØY SEAFOOD GROUP":
            ny_url = "https://www.nordnet.no/market/stocks/16105604-le-ro-y-seafood-group"
            
        response = requests.get(ny_url)
        soup = BeautifulSoup(response.content, "html.parser")
        soup = soup.text
        #print(soup)
        print(i)
        if i.endswith("ASA") and i != "AMSC ASA":
            i = i[:-4]
        if i.endswith("AS"):
            i = i[:-3]
        new_name = i.lower().capitalize() + "CEO"
        print(new_name)
        indeks = soup.upper().index(new_name.upper())
        nye = soup[indeks:]
        tyve = soup[indeks:indeks+70]
        print(tyve)
        """pattern = fr'e.'
        print(pattern)
        match = re.search(pattern, soup, re.IGNORECASE)
        print(match)

        tekst = match.group()
        print(tekst)"""

        pattern = r'(?<=CEO).*?(?=E-post)'

        match = re.search(pattern, tyve)

        ceo_info = match.group(0).strip()
        print(ceo_info)
        mini_dict = {}
        mini_dict["company"] = i
        mini_dict["name"] = ceo_info
        print(mini_dict)
        whole_dict.append(mini_dict)
    except Exception:
        continue
print(whole_dict)

json_file_path = "Ceo_list.json"

# Write the list of dictionaries to the JSON file
with open(json_file_path, "w") as json_file:
    json.dump(whole_dict, json_file , indent=4)

