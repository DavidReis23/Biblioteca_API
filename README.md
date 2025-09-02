# 📚 Biblioteca API

API REST simples feita em **Python (Flask)** para gerenciar uma lista de livros.  
Permite retornar dados em **JSON** ou **XML**, dependendo do cabeçalho `Accept`.

🚀 Tecnologias usadas
- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [dicttoxml](https://pypi.org/project/dicttoxml/)

⚙️ Como rodar o projeto

1. Clone este repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/seu-usuario/biblioteca_api.git
   cd biblioteca_api

🔹 1. Instalar HTTPie

No PowerShell (com seu venv ativado, de preferência):
pip install httpie

🔹 2. Testar o GET /livros (JSON padrão)
http GET http://127.0.0.1:5000/livros

🔹 3. Testar o GET /livros (em XML)
http GET http://127.0.0.1:5000/livros Accept:application/xml

🔹 4. Testar o POST /livros (adicionar um novo livro)
http POST http://127.0.0.1:5000/livros titulo="Harry Potter" autor="J.K. Rowling" ano:=1997

🔹 5. Conferir se o livro foi adicionado
http GET http://127.0.0.1:5000/livros

⚡ Com esses 4 comandos você já consegue:

* Ver JSON
* Ver XML
* Adicionar um livro
* Confirmar se ele foi salvo
