# coding : utf-8

### BOUJOUR FÉLIX
### TOUT D'ABORD, METS UN .py À LA FIN DE SCRIPTS PLEEEZ

import csv, json
import requests

fichier = "lobby.csv"

url = "http://jhroy.ca/uqam/lobby.json"

entetes = {
     "User-Agent":"Félix Pedneault - 514/778-4207 : requête envoyée dans le cadre d'un cours de journalisme pour un reportage numérique",
     "From":"felix.pedneault21@gmail.com"}

req = requests.get(url, headers=entetes)
print(req)

n = 0
registre = list(range(344458,438004))

for climat in registre:
    infos = []
    n += 1
    
    if req.status_code != 200: ### FAIRE CETTE VÉRIFICATION AVANT LA BOUCLE!
        print("Échec")
    else:
        sujet = req.json() ### CETTE TRANSFORMATION-LÀ AUSSI DOIT ÊTRE FAITE AVANT LA BOUCLE

        climat = sujet["client_org_corp_num"] ### ÇA BLOQUE ICI PCQ TA VARIABLE "SUJET" CONTIENT TOUT LE JSON
        ligne1 = sujet["fr_client_org_corp_nm"]["en_client_org_corp_nm"]["date_comm"][0]["objet"]["objet_autre"][1]["institution"][2]
        print(climat, ligne1)

        if sujet ["objet"] == "limat":
            print("objet") 
    
        infos.append(n)
        infos.append(climat)
        infos.append(ligne1)
        print(infos)

        dead = open(fichier,"a")
        obies = csv.writer(dead)
        obies.writerow(infos)
