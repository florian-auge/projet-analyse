from flask import Flask, jsonify
import boto3

app = Flask(__name__)

@app.route('/analyse')
def analyse():

    try:
        s3 = boto3.client('s3')
        reponse = s3.get_object(Bucket='florian-auge-bucket', Key='scores.csv')
        lignes = reponse['Body'].read().decode('utf-8').splitlines(keepends=True)
    except Exception as e:
        return jsonify({"erreur": str(e)})

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

    return jsonify({
        "moyenne": total/nombre,
        "max": maximum,
        "min": minimum
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)