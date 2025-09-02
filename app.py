from flask import Flask, request, jsonify, Response
import dicttoxml

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"id": 2, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954}
]

@app.route('/livros', methods=['GET'])
def get_livros():
    accept = request.headers.get("Accept")

    if accept == "application/xml":
        xml = dicttoxml.dicttoxml(livros, custom_root="livros", attr_type=False)
        return Response(xml, mimetype="application/xml")
    else:
        return jsonify(livros)

@app.route('/livros', methods=['POST'])
def add_livro():
    novo = request.get_json()
    novo["id"] = len(livros) + 1
    livros.append(novo)
    return jsonify(novo), 201

if __name__ == "__main__":
    app.run(debug=True)
