import requests
from tqdm import tqdm
# This program will download files of the marks of every day of the specified season
# that belongs to the Serie A championship, from the website fantacalcio.it
numero2020="1621839592000"
numero2019="-5"

url1="http://www.fantacalcio.it/Servizi/Excel.ashx?type=1&g="
url2="&t=1621839592000&s=" #stagione 2020-21
url3="&t=1644243601000&s=" #stagione 2021-22



#Ask for season ex: 2020-21
print("-----------------------")
print(" Download Season Marks ")
print("-----------------------")

season=input("Write here the season (ex:2020-21):")

for i in tqdm(range(1,39)):
    finalUrl=url1+str(i)+url3+season
    r = requests.get(finalUrl, allow_redirects=True)
    open(season+'/Voti_Fantacalcio_Stagione_'+season+'_Giornata_'+str(i)+'.xlsx', 'wb').write(r.content)
print("FINISHED !!")