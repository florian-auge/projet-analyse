import boto3

# utilisation du s3 d'AWS pour héberger les fichiers dans un bucket
try:										
	s3 = boto3.client('s3')						
	reponse = s3.get_object(Bucket='florian-auge-bucket', Key='scores.csv')
	lignes = reponse['Body'].read().decode('utf-8').splitlines(keepends=True)
except Exception as e:
    print("Erreur :", e)
    exit()

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
	
	
