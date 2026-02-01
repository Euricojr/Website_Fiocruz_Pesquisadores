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

## 📝 Como Atualizar o Conteúdo (Importante)

**Boas notícias:** Você NÃO precisa editar arquivos HTML complicados para adicionar novos conteúdos. Tudo é gerenciado através da pasta `_data/`.

### 1. Adicionar Novos Projetos

Edite o arquivo: `_data/projects.yml`

Para adicionar um novo projeto, basta copiar a estrutura abaixo e colar no final do arquivo:

```yaml
- title: "Nome do Novo Projeto"
  description: "Uma breve descrição dos objetivos e impacto do projeto."
  image: "/assets/img/nome-da-imagem.jpg" # Salve a imagem na pasta assets/img
  tags:
    - "Inovação"
    - "Saúde Pública"
```

### 2. Adicionar Membros da Equipe

Edite o arquivo: `_data/team.yml`

Os membros são organizados por categorias (Liderança, Membros Principais, etc.). Encontre a categoria certa e adicione um novo item na lista `members`:

```yaml
- name: "Dra. Maria Exemplo"
  role: "Pesquisadora Sênior"
  affiliation: "Fiocruz / ENSP"
  image: "https://link-da-foto-ou-caminho-local.jpg"
  links:
    lattes: "http://lattes.cnpq.br/..."
    linkedin: "https://linkedin.com/in/..."
```

### 3. Adicionar Publicações

Edite o arquivo: `_data/publications.yml`

Adicione novas publicações no topo da lista para que apareçam primeiro:

```yaml
- year: 2025
  category: artigos # Opções: artigos, preprints, relatorios
  title: "Título do Artigo Científico"
  authors: "Silva, A., Souza, B."
  venue: "Nome da Revista ou Journal"
  link_text: "Ler Artigo →"
  link_url: "https://doi.org/..."
```

---

## 📂 Estrutura de Pastas

Aqui está um resumo rápido de onde as coisas estão:

- **`_data/`**: 🧠 **O Cérebro.** Aqui ficam os arquivos `.yml` com todo o texto e informações do site.
- **`_includes/`**: 🧩 **Peças soltas.** Contém componentes reutilizáveis, como a barra de navegação (`navbar.html`).
- **`_layouts/`**: 🏗️ **A Base.** O arquivo `default.html` define a estrutura padrão (cabeçalho, corpo) de todas as páginas.
- **`assets/`**: 🎨 **Recursos Visuais.** Contém as pastas `css` (estilos), `js` (scripts) e `img` (imagens).
- **`*.html`** (Raiz): As páginas principais do site (`index.html`, `projetos.html`, etc). Elas apenas "chamam" os dados.

---

## 🛠️ Tecnologias Usadas

- **Jekyll**: Gerador de sites estáticos.
- **Liquid**: Linguagem de template usada para criar a lógica (loops, condições).
- **Ruby**: Linguagem base do Jekyll.
- **HTML5 / CSS3**: Estrutura e estilo visual do site.

---

_Mantido pela equipe de desenvolvimento e pesquisa da Fiocruz._
