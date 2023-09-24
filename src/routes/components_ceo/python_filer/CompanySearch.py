import json
from bs4 import BeautifulSoup



data = """2020 Bulkers	OSE: 2020	Shipping	2347,00
ABG Sundal Collier Holding	OSE: ABG	Finans	1 845,50
ABL Group	OSE: ABL	Konsulent	1739
Adevinta	OSE: ADE	Kommunikasjon	100 537,38
AF Gruppen	OSE: AFG	Industri	18 376,58
AGILYX	OSE: AGLX	Teknologi	2560
Airthings	OSE: AIRX	Teknologi	563,766
Akastor	OSE: AKAST	Finans	3502,00
Aker	OSE: AKER	Finans	28 415,12
Aker BP	OSE: AKRBP	Energi	61 116,32
Aker Horizons	OSE: AKH	Energi	7800,00
Aker Solutions	OSE: AKSO	Energi	3 959,49
American Shipping Company	OSE: AMSC	Industri	1 603,31
Asetek	OSE: ASTK	IT	1 631,84
Atea	OSE: ATEA	IT	11 525,19
Avance Gas Holding	OSE: AGAS	Energi	1 348,24
Axactor	OSE: ACR	Finans	1 268,10
B2Holding	OSE: B2H	Finans	1 902,09
Bakkafrost	OSE: BAKKA	Konsumvarer	32 601,16
BerGenBio	OSE: BGBIO	Helsevern	2 739,96
Bonheur	OSE: BONHR	Industri	9 101,83
Bouvet	OSE: BOUV	IT	5 350,26
BW LPG	OSE: BWLPG	Energi	5 145,48
BW Offshore Limited	OSE: BWO	Energi	5 655,42
Crayon Group Holding	OSE: CRAYN	IT	5 767,37
DNB	OSE: DNB	Finans	216 213,29
DNO	OSE: DNO	Energi	5 579,48
Elkem	OSE: ELK	Materialer	10 004,35
Entra	OSE: ENTRA	Eiendom	23 317,60
Equinor	OSE: EQNR	Energi	432 629,47
Europris	OSE: EPR	Forbruksvarer	7 375,61
Fjord1	OSE: FJORD	Industri	4 525,16
Fjordkraft Holding	OSE: ELMRA	Forsyning	8 481,94
Frontline	OSE: FRO	Energi	14 312,92
Gaming Innovation Group	OSE: GIG	Forbruksvarer	642,88
Gjensidige Forsikring	OSE: GJF	Finans	93 197,91
Golden Ocean Group	OSE: GOGL	Industri	5 000,39
Grieg Seafood	OSE: GSF	Konsumvarer	10 159,89
Hexagon Composites	OSE: HEX	Industri	8 587,95
IDEX Biometrics	OSE: IDEX	IT	1 264,10
Kitron	OSE: KIT	IT	2 686,56
Kongsberg Automotive	OSE: KOA	Forbruksvarer	1 569,27
Kongsberg Gruppen	OSE: KOG	Industri	24 766,13
Lerøy Seafood Group	OSE: LSG	Konsumvarer	31 417,31
Medistim	OSE: MEDI	Helsevern	4 277,20
Mowi	OSE: MOWI	Konsumvarer	84 702,80
MPC Container Ships	OSE: MPCC	Industri	1 018,89
Nel	OSE: NEL	Industri	26 156,95
Nordic Nanovector	OSE: NANOV	Helsevern	1 467,47
Nordic Semiconductor	OSE: NOD	IT	15 852,00
Norsk Hydro	OSE: NHY	Materialer	52 047,77
Norwegian Air Shuttle	OSE: NAS	Industri	8 104,34
Norwegian Finans Holding	OSE: NOFI	Finans	12 517,88
Olav Thon Eiendomsselskap	OSE: OLT	Eiendom	15 906,16
Orkla	OSE: ORK	Konsumvarer	89 527,37
PCI Biotech Holding	OSE: PCIB	Helsevern	1 745,91
PGS	OSE: PGS	Energi	1 239,44
Photocure	OSE: PHO	Helsevern	1 930,68
SalMar	OSE: SALM	Konsumvarer	48 737,51
SATS	OSE: SATS	Forbruksvarer	3 521,15
Scatec Solar	OSE: SCATC	Forsyning	21 584,51
Schibsted ser. A	OSE: SCHA	Kommunikasjon	34 565,80
Schibsted ser. B	OSE: SCHB	Kommunikasjon	38 704,48
SpareBank 1 SR-Bank	OSE: SRBANK	Finans	18 374,58
Stolt-Nielsen	OSE: SNI	Industri	4 372,89
Storebrand	OSE: STB	Finans	23 098,42
Subsea 7	OSE: SUBC	Energi	20 282,00
Telenor	OSE: TEL	Kommunikasjon	197 113,66
TGS-NOPEC Geophysical Company	OSE: TGS	Energi	15 618,82
TietoEVRY	OSE: TIETOO	IT	31 709,91
Tomra Systems	OSE: TOM	Industri	55 106,51
Veidekke	OSE: VEI	Industri	16 626,61
Wallenius Wilhelmsen	OSE: WAWI	Industri	5 701,12
XXL	OSE: XXL	Forbruksvarer	5 498,07
Yara International	OSE: YAR	Materialer	101 970,69"""
lines = data.split('\n')
company_names = []

for line in lines:
    company_name = line.split("\t")
    company_names.append(company_name[0])
    
def save_company_names_to_json():
    data = {'Company': company_names}
    json_file_path = 'company_names.json'

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)

save_company_names_to_json()
