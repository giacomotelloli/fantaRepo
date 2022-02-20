import csv
import numpy as np

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
print(f'File contiene {line_count} linee.')

#carico i voti
with open('saving_marks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        for j in range(len(row)):
            Listone[line_count].listaSucc.append(row[j])
        Listone[line_count].setElementi=set(Listone[line_count].listaSucc)
        line_count += 1

print(f'File contiene {line_count} linee.')




#ogni giocatore deve avere la sua variabile aleatoria
#devo generare un set data la lista di voti

#poi per ogni giocatore per ogni numero nel set definire la probabilità del voto con la
#seguente formula= (numero di volte in cui il voto si ripete/lunghezza lista)
for i in range(len(Listone)):
    #ciclo per spazzolare i numeri del set
    for j in Listone[i].setElementi:
        numero=j
        countRepeat=0
        for k in range(len(Listone[i].listaSucc)):
            if Listone[i].listaSucc[k]==numero:
                countRepeat+=1

        Listone[i].listaProb.append(countRepeat/len(Listone[i].listaSucc))

    #valore atteso
    expVal=0
    count=0
    for h in Listone[i].setElementi:
        expVal=expVal+(float(h)*Listone[i].listaProb[count])
        count = count+1


    # varianza
    varianza=0
    count=0
    for r in Listone[i].setElementi:
        varianza=varianza+(pow(float(r)-expVal,2)*Listone[i].listaProb[count])
        count=count+1

    Listone[i].expected=round(expVal)
    Listone[i].variance=round(varianza)


#poi salvare giocatore,ruolo,squadra,expectedValue,variance
#giocatore ottimo se ha alto valore atteso e bassa varianza
with open('/home/giacomo/Documenti/Acr/Fanta_ACR/voti_time_serie/final_result.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Nome","Ruolo", "Squadra", "Valore_Atteso","Varianza"])

    for i in range(len(Listone)):
        writer.writerow([Listone[i].nome,Listone[i].ruolo,Listone[i].squadra,Listone[i].expected,Listone[i].variance])
