# API REST didática — Flask + SQLAlchemy (ORM)

Projeto de exemplo para explicar **ORM** (Object-Relational Mapping) usando
Flask + Flask-SQLAlchemy, com uma organização simples em camadas:

```
etapa8/
├── app.py                 # ponto de entrada: cria o app, o banco e registra as rotas
├── config.py               # configurações (string de conexão do banco)
├── models/                 # ORM: uma classe Python = uma tabela no banco
│   ├── __init__.py          # instância compartilhada do SQLAlchemy (db)
│   ├── autor.py
│   ├── perfil_autor.py
│   ├── livro.py
│   └── categoria.py
├── controllers/             # regra de negócio / acesso ao banco (usa o ORM)
│   ├── autor_controller.py
│   ├── perfil_autor_controller.py
│   ├── livro_controller.py
│   └── categoria_controller.py
└── views/                   # rotas HTTP (recebem request, devolvem JSON)
    ├── autor_view.py
    ├── perfil_autor_view.py
    ├── livro_view.py
    └── categoria_view.py
```

Não usamos Blueprint de propósito, para manter o conceito de rota
(`@app.route`) o mais direto possível. Cada view importa `app` diretamente
de `app.py`.

## Modelo de dados (as 4 entidades e seus relacionamentos)

- **Autor** 1:1 **PerfilAutor** — cada autor tem no máximo um perfil (bio,
  site pessoal). A regra do 1:1 vem do `unique=True` na chave estrangeira
  `autor_id` dentro de `PerfilAutor`.
- **Autor** 1:N **Livro** — um autor pode ter vários livros; cada livro
  pertence a um único autor (`livro.autor_id`).
- **Livro** N:N **Categoria** — um livro pode ter várias categorias e uma
  categoria pode estar em vários livros. Isso é implementado com uma
  tabela de associação (`livro_categoria`), sem model próprio porque não
  guarda nenhum dado além das duas chaves estrangeiras.

## Como rodar

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python app.py
```

A API sobe em `http://127.0.0.1:5000`. Na primeira execução, o arquivo
`biblioteca.db` (SQLite) é criado automaticamente com as tabelas.

## Exemplos de requisições

Criar um autor:

```bash
curl -X POST http://127.0.0.1:5000/autores \
  -H "Content-Type: application/json" \
  -d "{\"nome\": \"Machado de Assis\", \"nacionalidade\": \"Brasileira\"}"
```

Criar o perfil (1:1) desse autor (troque `1` pelo id retornado acima):

```bash
curl -X POST http://127.0.0.1:5000/perfis \
  -H "Content-Type: application/json" \
  -d "{\"autor_id\": 1, \"biografia\": \"Escritor brasileiro...\", \"site_pessoal\": \"https://exemplo.com\"}"
```

Criar categorias:

```bash
curl -X POST http://127.0.0.1:5000/categorias -H "Content-Type: application/json" -d "{\"nome\": \"Romance\"}"
curl -X POST http://127.0.0.1:5000/categorias -H "Content-Type: application/json" -d "{\"nome\": \"Clássico\"}"
```

Criar um livro (1:N com autor, N:N com categorias — ids 1 e 2 abaixo):

```bash
curl -X POST http://127.0.0.1:5000/livros \
  -H "Content-Type: application/json" \
  -d "{\"titulo\": \"Dom Casmurro\", \"ano_publicacao\": 1899, \"autor_id\": 1, \"categoria_ids\": [1, 2]}"
```

Consultar o autor e ver, na mesma resposta, o perfil (1:1) e os livros
(1:N):

```bash
curl http://127.0.0.1:5000/autores/1
```

Consultar uma categoria e ver os livros associados (N:N):

```bash
curl http://127.0.0.1:5000/categorias/1
```

## Endpoints disponíveis

| Método | Rota                     | Ação                                  |
|--------|--------------------------|----------------------------------------|
| GET    | /autores                 | Lista autores                          |
| GET    | /autores/\<id>           | Detalha um autor (com perfil e livros) |
| POST   | /autores                 | Cria autor                             |
| PUT    | /autores/\<id>           | Atualiza autor                         |
| DELETE | /autores/\<id>           | Remove autor                           |
| GET    | /perfis/\<id>            | Detalha um perfil                      |
| POST   | /perfis                  | Cria perfil (1:1 com autor)            |
| PUT    | /perfis/\<id>            | Atualiza perfil                        |
| DELETE | /perfis/\<id>            | Remove perfil                          |
| GET    | /livros                  | Lista livros                           |
| GET    | /livros/\<id>            | Detalha um livro                       |
| POST   | /livros                  | Cria livro (1:N com autor, N:N com categorias) |
| PUT    | /livros/\<id>            | Atualiza livro                         |
| DELETE | /livros/\<id>            | Remove livro                           |
| GET    | /categorias              | Lista categorias                       |
| GET    | /categorias/\<id>        | Detalha categoria (com livros)         |
| POST   | /categorias              | Cria categoria                         |
| PUT    | /categorias/\<id>        | Atualiza categoria                     |
| DELETE | /categorias/\<id>        | Remove categoria                       |