import csv
import numpy as np
from tqdm import tqdm
class Player:
    def __init__(self,Nome,Squadra,Ruolo,Media,Varianza):
        self.name=Nome
        self.team=Squadra
        self.role=Ruolo
        self.variance=Varianza
        self.mean=Media

def VarianceSort(ListToSort):
   NewList=[]
   for j  in range(len(ListToSort)):
        for i in range(len(ListToSort)):
            if ListToSort[0].variance>ListToSort[i].variance:
                #swap
                appoggio=ListToSort[0]
                ListToSort[0]=ListToSort[i]
                ListToSort[i]=appoggio
        NewList.append(ListToSort[0])
        ListToSort.remove(ListToSort[0])
   return NewList




def TotalSort(ListToSort):
    NewList = []
    for j in range(len(ListToSort)-1):
        for i in range(j,len(ListToSort)):
            if ListToSort[j].mean < ListToSort[i].mean:
                # swap
                appoggio = ListToSort[j]
                ListToSort[j] = ListToSort[i]
                ListToSort[i] = appoggio

        #NewList.append(ListToSort[0])
        #ListToSort.remove(ListToSort[0])
    return ListToSort


#For sort the list i need to divide it in 4 cathegories
#1) Attac ;2) Center; 3) Defense; 4) GoalKeeper

#For each cathegory i need to solve a miniMax problem
# which is to order them to have maximum mean,and minimum variance.

    # I can try to order them with maximum mean
    # then take the first value as a champion and see if it has the minimum variance
        #if yes => is ok i'll add it to the final list and remove it to the actual list
        #if no => i need to consider as champion the second element, and so on till i find the minimum

Attak=[]
Center=[]
Defense=[]
GoalKeep=[]
#loading the Listone
Listone=[]
with open('final_result.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Nomi delle colonne: {", ".join(row)}')
            line_count += 1
        else:
            Listone.append(Player(row[0],row[2],row[1],int(row[3]),int(row[4])))
            #print(f'\t{row[0]} , {row[1]} , {row[2]} , {row[3]}.')
            line_count += 1
print(f'File Risultati finali contiene {line_count} linee.')



#filling the lists
for i in range(len(Listone)):
    if Listone[i].role=="A":
        Attak.append(Listone[i])
    if Listone[i].role=="C":
        Center.append(Listone[i])
    if Listone[i].role=="D":
        Defense.append((Listone[i]))
    if Listone[i].role=="P":
        GoalKeep.append(Listone[i])

# i can eliminate the main list called Listone
# and i can iterate on roles
Roles=[Attak,Center,Defense,GoalKeep]
#alla fine del ciclo principale salvo tutto in un file csv

Ordered=[]
RolesNames=["A","C","D","P"]
#sorting the list by variance crescent order
for i in range(len(Roles)):
    Ordered.append(TotalSort(Roles[i]))
    with open('/home/giacomo/Documenti/Acr/Fanta_ACR/voti_time_serie/'+RolesNames[i]+'_ordered.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Squadra", "Ruolo","Media","Varianza"])
        for j in range(len(Ordered[i])):
            writer.writerow([Ordered[i][j].name, Ordered[i][j].team, Ordered[i][j].role,Ordered[i][j].mean,Ordered[i][j].variance])


