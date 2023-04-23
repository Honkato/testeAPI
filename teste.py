from flask import Flask, jsonify, request
import json

app = Flask('_name_')


# with open('data.json', 'r') as arquivo:
#     livros = json.load(arquivo)


livros = [
  {
    "_id": {
      "$oid": "642a14682f362b1354778e32"
    },
    "quantidade": 2,
    "cor": "vermelho"
  },
  {
    "_id": {
      "$oid": "642b55fdf87413a323baffa8"
    },
    "quantidade": 2,
    "cor": "azul"
  }
]

@app.route('/livros', methods=['GET'])
def obter_livro():
    return jsonify(livros)

app.run(host='teste-api-biblioteca.onrender.com',debug=True)
