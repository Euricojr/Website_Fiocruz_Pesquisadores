# 🏛️ Portal de Pesquisadores da Fiocruz

Este repositório contém o código-fonte do site estático gerado com **Jekyll**, desenvolvido para divulgar os projetos de pesquisa, a equipe e as publicações científicas da Fiocruz.

O foco deste projeto foi manter o design visual original intacto enquanto tornamos a gestão de conteúdo fácil e dinâmica através de arquivos de dados (YAML).

---

## 🚀 Como Rodar Localmente

Siga estes passos para visualizar o site no seu computador antes de fazer alterações.

### Pré-requisitos

- **Ruby** (Instalado e configurado no PATH)
- **Jekyll** e **Bundler** (`gem install jekyll bundler`)

### Passo a Passo

1.  **Instale as dependências** (apenas na primeira vez):

    ```bash
    bundle install
    ```

2.  **Inicie o servidor local**:

    ```bash
    bundle exec jekyll serve
    ```

3.  **Acesse no navegador**:
    Abra `http://localhost:4000` para ver o site.

---

## 📝 Como Atualizar o Conteúdo

Você pode gerenciar a maior parte do conteúdo do site editando arquivos simples na pasta `_data/`. Não é necessário mexer nos arquivos HTML para estas alterações.

### 1. Projetos (`projects.html`)

Arquivo: `_data/projects.yml`

Adicione novos projetos copiando o bloco abaixo:

```yaml
- title: "Nome do Novo Projeto"
  image: "https://link-da-imagem.com/foto.jpg" # URL externa ou caminho local (/assets/img/...)
  description: "Descrição breve do projeto."
  tags:
    - "Tag 1"
    - "Tag 2"
```

### 2. Equipe (`equipe.html`)

Arquivo: `_data/team.yml`

Os membros são divididos por categorias (`Liderança`, `Membros Principais`, etc.). Adicione um novo membro na lista `members`:

```yaml
members:
  - name: "Nome do Pesquisador"
    role: "Cargo / Função"
    affiliation: "Fiocruz / Unidade"
    image: "https://link-da-foto.jpg"
    links:
      lattes: "http://lattes.cnpq.br/..."
      linkedin: "https://linkedin.com/in/..."
```

### 3. Publicações (`publicacoes.html`)

Arquivo: `_data/publications.yml`

As publicações são exibidas em ordem. Adicione novas no topo da lista:

```yaml
- year: 2025
  category: artigos # Opções: artigos, preprints, relatorios
  title: "Título da Publicação"
  authors: "Sobrenome, N., Silva, A."
  venue: "Nome da Revista ou Journal"
  image: "https://link-da-capa-revista.jpg" # Opcional
  link_text: "Ler Artigo →"
  link_url: "https://doi.org/..."
```

### 4. Dashboards & Ferramentas (`dashboards.html`)

Arquivo: `_data/dashboards.yml`

Para adicionar paineis (PowerBI, Shiny, etc):

```yaml
- title: "Nome do Dashboard"
  description: "Descrição do que a ferramenta faz."
  tool: "PowerBI" # Ex: R Shiny, Tableau, PowerBI
  image: "https://link-do-preview.jpg"
  url: "https://link-para-acessar.com"
  featured: false # Deixe true se quiser destaque (se implementado)
```

---

## 📄 Páginas Estáticas

Algumas páginas possuem conteúdo fixo que não muda com frequência. Para alterá-las, você deve editar o arquivo HTML diretamente:

- **Sobre (`sobre.html`)**: Texto institucional e imagem de topo. Edite o texto dentro das tags `<p class="about-text">`.
- **Colabore (`colabore.html`)**: Informações sobre parcerias e contatos. Edite os textos dentro dos cartões `.collab-card`.

---

## 📂 Estrutura de Arquivos

- **`_data/`**: Contém os arquivos YAML com o conteúdo dinâmico (Projetos, Equipe, Publicações, Dashboards).
- **`_includes/`**: Componentes reutilizáveis (Ex: `navbar.html`).
- **`_layouts/`**: Modelos de página (Ex: `default.html`).
- **`assets/`**: Imagens, CSS e Scripts.
- **Páginas Principais**:
  - `index.html` (Home)
  - `projetos.html`
  - `equipe.html` (Lê de team.yml)
  - `publicacoes.html` (Lê de publications.yml)
  - `dashboards.html` (Lê de dashboards.yml)
  - `sobre.html`
  - `colabore.html`

---

## 🛠️ Tecnologias

- **Jekyll**: Gerador de site estático.
- **Liquid**: Linguagem de templates.
- **HTML5 / CSS3**: Estrutura e Estilização.
- **Font Awesome**: Ícones.

---

_Mantido pela equipe de desenvolvimento e pesquisa da Fiocruz._
