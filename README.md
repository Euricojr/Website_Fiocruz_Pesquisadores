# Guia de Execução Local - Fiocruz Website & Admin

Este repositório contém dois componentes principais:

1. **Backend & Painel Admin** (`insight-admin`): API FastAPI e interface administrativa.
2. **Frontend** (`Website_Fiocruz_Pesquisadores`): Site público gerado com Jekyll.

---

## 🛠️ Configuração Inicial (Primeira vez)

Se for a primeira vez rodando o projeto, você precisará criar um usuário administrador:

1. Ative o `venv` e entre na pasta `insight-admin`.
2. Rode o script de criação:
   ```powershell
   python create_admin.py
   ```
3. Siga as instruções no terminal para definir seu email e senha.

---

## 🚀 Como Rodar o Backend (API e Admin)

O backend gerencia os dados e serve a interface de administração.

1. **Ative o Ambiente Virtual** (na raiz do projeto):

   ```powershell
   .\venv\Scripts\activate
   ```

2. **Entre na pasta do backend**:

   ```powershell
   cd insight-admin
   ```

3. **Inicie o servidor**:

   ```powershell
   python -m uvicorn main:app --reload

   ```

4. **Acesse nos links abaixo**:
   - **Painel Administrativo:** [http://127.0.0.1:8000/static/admin/index.html](http://127.0.0.1:8000/static/admin/index.html)
   - **Documentação API (Swagger):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🌐 Como Rodar o Frontend (Site Público)

O site público é gerado estaticamente via Jekyll.

1. **Abra um novo terminal** e entre na pasta que contém o site Jekyll e o `Gemfile`:

   ```powershell
   2x cd Website_Fiocruz_Pesquisadores
   ```

   > Se você estiver no caminho `...\Insight\Website_Fiocruz_Pesquisadores`, este comando abre a subpasta que contém o `Gemfile` do site.

2. **Instale as dependências** (caso ainda não tenha feito):

   ```powershell
   bundle install
   ```

3. **Inicie o Jekyll**:

   ```powershell
   bundle exec jekyll serve
   ```

4. **Acesse no link abaixo**:
   - **Site:** [http://127.0.0.1:4000](http://127.0.0.1:4000)

---

## 🛠️ Notas Adicionais

- **Ambiente Python**: Se as dependências não estiverem instaladas no `venv`, rode `pip install -r requirements.txt` dentro da pasta `insight-admin`.
- **Dependências Ruby**: Se o Jekyll não rodar, use `bundle install` na pasta `Website_Fiocruz_Pesquisadores`.
- **Sincronização**: O Admin atualiza arquivos YAML dentro da pasta do frontend. Certifique-se de que o servidor do backend está rodando para que as alterações no painel reflitam no site.
