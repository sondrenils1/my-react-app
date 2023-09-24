import json
from pygoogle_image import image as pi

# Specify the path to your JSON file
json_file_path = "Ceo_list.json"

# Open and read the JSON file
#with open(json_file_path, "r") as json_file:
   # data = json.load(json_file)

data = [
    {
        "company": "2020 BULKERS",
        "name": "Herman Bilung"
    },
    {
        "company": "ABG SUNDAL COLLIER HOLDING",
        "name": "Jonas Str\u00f6m"
    },
    {
        "company": "ABL GROUP",
        "name": "Reuben Segal"
    },
    {
        "company": "ADEVINTA",
        "name": "Antoine Jouteau"
    },
    {
        "company": "AF GRUPPEN",
        "name": "Amund T\u00f8ftum"
    },
    {
        "company": "AGILYX",
        "name": "Tim Stedman"
    },
    {
        "company": "AIRTHINGS",
        "name": "\u00d8yvind Birkenes"
    },
    {
        "company": "AKASTOR",
        "name": "Karl Erik Kjelstad"
    },
    {
        "company": "AKER",
        "name": "\u00d8yvind Eriksen"
    },
    {
        "company": "AKER BP",
        "name": "Karl Johnny Hersvik"
    },
    {
        "company": "AKER HORIZONS",
        "name": "Kristian R\u00f8kke"
    },
    {
        "company": "AKER SOLUTIONS",
        "name": "Kjetel Digre"
    },
    {
        "company": "AMSC ASA",
        "name": "P\u00e5l Lothe Magnussen"
    },
    {
        "company": "ASETEK",
        "name": "Andr\u00e9 Eriksen"
    },
    {
        "company": "ATEA",
        "name": "Steinar S\u00f8nsteby"
    },
    {
        "company": "AVANCE GAS HOLDING",
        "name": "\u00d8ystein Kalleklev"
    },
    {
        "company": "AXACTOR",
        "name": "Johnny Tsolis"
    },
    {
        "company": "B2HOLDING",
        "name": "Erik Just Johnsen"
    },
    {
        "company": "BAKKAFROST",
        "name": "Regin Jacobsen"
    },
    {
        "company": "BERGENBIO",
        "name": "Martin Olin"
    },
    {
        "company": "BONHEUR",
        "name": "Anette Olsen"
    },
    {
        "company": "BOUVET",
        "name": "Per Gunnar Tronsli"
    },
    {
        "company": "BW LPG",
        "name": "Anders Onarheim"
    },
    {
        "company": "BW OFFSHORE LIMITED",
        "name": "Marco Beenen"
    },
    {
        "company": "CRAYON GROUP HOLDING",
        "name": "Melissa Mulholland"
    },
    {
        "company": "DNB BANK",
        "name": "Kjerstin Braathen"
    },
    {
        "company": "DNO",
        "name": "Bj\u00f8rn Dale"
    },
    {
        "company": "ELKEM",
        "name": "Helge Aasen"
    },
    {
        "company": "ENTRA",
        "name": "Sonja Horn"
    },
    {
        "company": "EQUINOR",
        "name": "Anders Opedal"
    },
    {
        "company": "EUROPRIS",
        "name": "Espen Eldal"
    },
    {
        "company": "FRONTLINE",
        "name": "Lars Barstad"
    },
    {
        "company": "GAMING INNOVATION GROUP",
        "name": "Richard Brown"
    },
    {
        "company": "GJENSIDIGE FORSIKRING",
        "name": "Geir Holmgren"
    },
    {
        "company": "GOLDEN OCEAN GROUP",
        "name": "Ulrik Uhrenfeldt Andersen"
    },
    {
        "company": "GRIEG SEAFOOD",
        "name": "Andreas Kvame"
    },
    {
        "company": "HEXAGON COMPOSITES",
        "name": "Jon Erik Engeset"
    },
    {
        "company": "IDEX BIOMETRICS",
        "name": "Vincent Graziani"
    },
    {
        "company": "KITRON",
        "name": "Peter Nilsson"
    },
    {
        "company": "KONGSBERG AUTOMOTIVE",
        "name": "Linda Nyquist-Evenrud (tf)"
    },
    {
        "company": "KONGSBERG GRUPPEN",
        "name": "Geir H\u00e5\u00f8y"
    },
    {
        "company": "MEDISTIM",
        "name": "Kari Eian Krogstad"
    },
    {
        "company": "MOWI",
        "name": "Ivan Vindheim"
    },
    {
        "company": "MPC CONTAINER SHIPS",
        "name": "Constantin Baack"
    },
    {
        "company": "NEL",
        "name": "H\u00e5kon Volldal"
    },
    {
        "company": "NORDIC SEMICONDUCTOR",
        "name": "Svenn-Tore Larsen"
    },
    {
        "company": "NORSK HYDRO",
        "name": "Hilde Merete Aasheim"
    },
    {
        "company": "NORWEGIAN AIR SHUTTLE",
        "name": "Geir Karlsen"
    },
    {
        "company": "OLAV THON EIENDOMSSELSKAP",
        "name": "Dag Tangevald-Jensen"
    },
    {
        "company": "ORKLA",
        "name": "Nils Selte"
    },
    {
        "company": "PCI BIOTECH HOLDING",
        "name": "Per Walday"
    },
    {
        "company": "PGS",
        "name": "Rune Olav Pedersen"
    },
    {
        "company": "PHOTOCURE",
        "name": "Daniel Schneider"
    },
    {
        "company": "SALMAR",
        "name": "Frode Arntsen"
    },
    {
        "company": "SATS",
        "name": "Sondre Gravir"
    },
    {
        "company": "SPAREBANK 1 SR-BANK",
        "name": "Benedicte Schilbred Fasmer"
    },
    {
        "company": "STOLT-NIELSEN",
        "name": "Niels G. Stolt-Nielsen"
    },
    {
        "company": "STOREBRAND",
        "name": "Odd Arild Grefstad"
    },
    {
        "company": "SUBSEA 7",
        "name": "John Evans"
    },
    {
        "company": "TELENOR",
        "name": "Sigve Brekke"
    },
    {
        "company": "TGS",
        "name": "Kristian Johansen"
    },
    {
        "company": "TIETOEVRY",
        "name": "Kimmo Alkio"
    },
    {
        "company": "TOMRA SYSTEMS",
        "name": "Tove Andersen"
    },
    {
        "company": "VEIDEKKE",
        "name": "Jimmy Bengtsson"
    },
    {
        "company": "WALLENIUS WILHELMSEN",
        "name": "Lasse Kristoffersen"
    },
    {
        "company": "XXL",
        "name": "P\u00e5l Wibe"
    },
    {
        "company": "YARA INTERNATIONAL",
        "name": "Svein Tore Holsether"
    }
]

#for i in data:
    #keywords = i["name"] + " " + i["company"].lower()
    #pi.download(keywords=keywords, limit=3)

pi.download(keywords="August Wille Vaage", limit=10)