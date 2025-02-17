# TherapyHub 

**TherapyHub** é um sistema web full-stack para gerenciamento de consultas terapêuticas. Ele permite que profissionais de saúde registrem pacientes, acompanhem seu humor ao longo do tempo e visualizem estatísticas interativas.

## Tecnologias Utilizadas

- **Django** (Backend)
- **PostgreSQL / SQLite** (Banco de Dados)
- **HTML, CSS, JavaScript** (Frontend)
- **Chart.js** (Gráficos e Visualizações)
- **Bootstrap** (Estilização)

## Funcionalidades

✅ Cadastro e gerenciamento de pacientes\
✅ Registro e visualização de consultas\
✅ Acompanhamento do humor dos pacientes por gráficos\
✅ Contabilização de visualizações nas consultas

## 📎 Estrutura do Projeto

```
TherapyHub/  
├── core/          # Configurações principais do Django  
├── consultas/     # Aplicação para gerenciamento de consultas  
├── pacientes/    # Aplicação para cadastro de pacientes  
├── templates/    # Templates HTML  
├── static/       # Arquivos CSS, JS e imagens  
├── db.sqlite3    # Banco de dados (caso use SQLite)  
└── manage.py    # Arquivo principal para rodar o Django  
``` 

## 🛠 Como Rodar o Projeto?

### 1⃣ Clone o Repositório

```sh
git clone https://github.com/SEU-USUARIO/TherapyHub.git
cd TherapyHub
```

### 2⃣ Crie um Ambiente Virtual

```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3⃣ Instale as Dependências

```sh
pip install -r requirements.txt
```

### 4⃣ Execute as Migrações e Rode o Servidor

```sh
python manage.py migrate
python manage.py runserver
```

O sistema estará disponível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 🚀

## Contribuição

Sinta-se à vontade para abrir issues e enviar pull requests com melhorias!
