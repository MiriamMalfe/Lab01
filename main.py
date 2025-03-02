#la prima riga contiene il testo della domanda
#la seconda riga contiene un numero intero positivo, che indica il livello di difficoltà della domanda
#la terza riga contiene la risposta corretta
#la quarta, quinta e sesta riga contengono le risposte errate
import random

domande = open("domande.txt", "r")
punti = open("punti.txt", "r")

class domanda:
    def __init__(self, testo, difficolta, rispostaCorretta, rispostaSbagliata1, rispostaSbagliata2, rispostaSbagliata3):
        self.testo = testo
        self.difficolta = difficolta
        self.rispostaCorretta = rispostaCorretta
        self.rispostaSbagliata1 = rispostaSbagliata1
        self.rispostaSbagliata2 = rispostaSbagliata2
        self.rispostaSbagliata3 = rispostaSbagliata3

    def __str__(self):
        print(f"{self.testo} {self.difficolta} {self.rispostaCorretta} {self.rispostaSbagliata1} {self.rispostaSbagliata2} {self.rispostaSbagliata3}")


stringa = ""
i=1
d = ""
liv = 0
rGiusta = ""
r1 = ""
r2 = ""
r3 = ""

listaDomande = []

#oltre al ciclo per creare la domanda, trovo il livello massimo della difficolta
max = 0

for line in domande:
    line = line.strip("\n")
    if i==1:
        d = line
    if i==2:
        liv = int(line)
        if liv > max:
            max = liv
    if i==3:
        rGiusta = line
    if i==4:
        r1=line
    if i==5:
        r2 = line
    if i ==6:
        r3 = line
        dom = domanda(d, liv, rGiusta, r1, r2, r3)
        listaDomande.append(dom)
    if i==7:
        i = 0

    i = i +1

#creo un array per contare quante domande ho per ogni livello
#creo una nuova variabile --> è una specie di array dove [casella dell'array -> None significa vuota]*(indica il numero delle caselle)
#questo array avrà in ogni casella un numero int che rappresenta il numero tot di domande di quel livello
variabileArray = [0] * (max+1)   #uso max+1 perche se il livello massimo è 5 io devo contare anche la casella del livello 0

i=0
while i< (max+1):
    for doma in listaDomande:
        if doma.difficolta == i:
            #aggiorno il valore dell'array contatore
            variabileArray[i] = variabileArray[i]+1
    i=i+1


livelloAttuale = 0
risposta = 0   #è una variabile booleana dove se l'utente risponde correttamente assume valore 0, altrimenti assume qualsiasi altro valore che non sia zero
c = 1 #variabile per numero delle domande nel livello in cui mi trovo

while risposta == 0 and livelloAttuale <= max :
    print("il livello di difficoltà attuale è "+ str(livelloAttuale))
    nRandom = random.randint(1, variabileArray[livelloAttuale])
    for doman in listaDomande:
        if doman.difficolta == livelloAttuale:
            if nRandom == c: #controllo se è la domanda nella posizione che mi interessa
                print(doman.testo+"\n"+ doman.rispostaCorretta+"\n"+doman.rispostaSbagliata1+"\n"+doman.rispostaSbagliata2+"\n"+doman.rispostaSbagliata3 )
                c=1
                inserimento = input("inserire la risposta: ")
                if inserimento == doman.rispostaCorretta:
                    livelloAttuale = (livelloAttuale+1)
                    print("La risposta è corretta")
                else:
                    print("Risposta errata")
                    risposta = 1 #il gioco termina quando sbaglia la domanda
                break  #interrompo ciclo quando termina il gioco nel ciclo in cui gli pongo la domanda (non dovendone fasre altre perchè ha perso non mi interessa più scorrere le domande)
            else:
                c = c+1













