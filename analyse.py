import sys

try:	
	fichier = open(sys.argv[1], "r")
except FileNotFoundError:
	print ("Ce fichier n'existe pas. Veuillez essayer avec un autre fichier")
	exit()

lignes = fichier.readlines()
fichier.close()

lignes = lignes[1:]
total = 0
nombre = 0
maximum = float("-inf")
minimum = float("inf")

for ligne in lignes:
	ligne = ligne.strip()
	parties = ligne.split(',')
	score = int(parties[1])
	total = total + score
	nombre = nombre + 1
	if score > maximum:
		maximum = score
	if score < minimum:
		minimum = score

	

print ("Moyenne :", total/nombre)
print ("Max :", maximum)
print ("Min :", minimum)
	
	
