import csv
import numpy as np
from tqdm import tqdm
class TimeSuccPlayer:
    def __init__(self,ruolo,nomeGioc,sq):
        self.nome=nomeGioc
        self.squadra=sq
        self.ruolo=ruolo
        self.listaSucc=[]
        self.setElementi={}
        self.listaProb=[]
        self.expected=0
        self.variance=0
    def addElem(self,number,pos):
        self.listaSucc[pos]=number

Listone=[]
with open('saving_names.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Nomi delle colonne: {", ".join(row)}')
            line_count += 1
        else:
            Listone.append(TimeSuccPlayer(row[2],row[0],row[1]))
            #print(f'\t{row[0]} , {row[1]} , {row[2]} , {row[3]}.')
            line_count += 1
print(f'File nomi contiene {line_count} linee.')

#carico i voti in ogni giocatore
with open('saving_marks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        for j in range(len(row)):
            Listone[line_count].listaSucc.append(row[j])
        Listone[line_count].setElementi=set(Listone[line_count].listaSucc)
        line_count += 1

print(f'File voti contiene {line_count} linee.')




#ogni giocatore deve avere la sua variabile aleatoria
#devo generare un set data la lista di voti

#poi per ogni giocatore devo calcolare il suo voto medio e la sua varianza

#calcolo il voto medio(valore atteso)
print("Calculating the mean for each player")
for i in tqdm(range(len(Listone))):
    Listone[i].listaSucc=[float(k) for k in Listone[i].listaSucc]
    Listone[i].expected=round(sum(Listone[i].listaSucc)/len(Listone[i].listaSucc))

#calcolo la varianza (formula se si conosce solo la media sigma^2=(max-min)^2/4)
print("Calculatin the variance for each player")
for i in tqdm(range(len(Listone))):
    Listone[i].variance=round(np.power(max(Listone[i].listaSucc)-min(Listone[i].listaSucc),2)/4)


#poi salvare giocatore,ruolo,squadra,expectedValue,variance
#giocatore ottimo se ha alto valore atteso e bassa varianza
with open('/home/giacomo/Documenti/Acr/Fanta_ACR/voti_time_serie/final_result2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Nome","Ruolo", "Squadra", "Valore_Atteso","Varianza"])

    for i in range(len(Listone)):
        writer.writerow([Listone[i].nome,Listone[i].ruolo,Listone[i].squadra,Listone[i].expected,Listone[i].variance])
