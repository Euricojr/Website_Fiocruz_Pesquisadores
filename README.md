# 🏛️ Portal INSIGHT - Fiocruz

Este repositório contém o código-fonte do portal do **INSIGHT**, um laboratório interdisciplinar que integra inteligência artificial, ciência de dados e epidemiologia. O site é estático e gerado com **Jekyll**, focado em facilitar a gestão de conteúdo sem necessidade de conhecimentos profundos em programação.

A maior parte do conteúdo (Projetos, Equipe, Publicações e Destaques) é gerada automaticamente através de listas de arquivos de dados do tipo YAML (`.yml`).

---

## 🚀 Como Rodar Localmente

Siga estes passos para visualizar o site no seu computador antes de publicar alterações na web:

### Pré-requisitos
- **Ruby** (Instalado e configurado no PATH)
- **Jekyll** e **Bundler** (Instalados via terminal: `gem install jekyll bundler`)

### Passo a Passo
1. **Instale as dependências** (apenas na primeira vez):
   ```bash
   bundle install
   ```
2. **Inicie o servidor local**:
   ```bash
   bundle exec jekyll serve
   ```
3. **Acesse no navegador**: Abra `http://localhost:4000` para ver o site ao vivo.

---

## 🖼️ Como Funcionam as Imagens no Site?

Você tem sempre duas opções para colocar fotos e banners nos arquivos `.yml`:

1. **Local (Recomendado):** Salve a imagem dentro da pasta `assets/img/` do projeto. No arquivo YAML, escreva apenas o caminho:
   `image: "/assets/img/foto.jpg"`
2. **Externa (Link da internet):** Clique com o botão direito numa imagem online, copie o endereço e cole no YAML:
   `image: "https://site.com/foto.jpg"`

*(Se o arquivo YAML não possuir um campo preenchido para lattes ou linkedin, o botão correspondente será **ocultado** automaticamente para manter o design limpo).*

---

## 📝 Como Atualizar o Conteúdo (Arquivos de Dados)

Você gerencia o portal editando arquivos simples de texto na pasta `_data/`. O site lê esses arquivos e desenha os cartões e banners sozinho.

### 1. Equipe (`_data/team.yml`)
A página de **Equipe** lê os dados deste arquivo, que é dividido por categorias ("Liderança Científica", "Membros", etc.).

**Modelo de adição:**
```yaml
- category: "NOME DA CATEGORIA"
  members:
    - name: "Nome do Membro"
      role: "Cargo (ex: Voluntário)"
      institution: "Faculdade / Instituição"
      image: "/assets/img/foto.jpg"
      linkedin: "https://www.linkedin.com/..."
      lattes: "https://lattes.cnpq.br/..."
```

### 2. Projetos (`_data/projects.yml`)
A página de **Projetos** carrega uma grade de cartões.
**Modelo de adição:**
```yaml
- title: "Nome do Projeto"
  image: "/assets/img/banner-projeto.jpg" 
  description: "Descrição curta com resumo da pesquisa."
  tags:
    - "Epidemiologia"
    - "IA"
  url: "/projetos/nome-do-projeto.html" # Link interno para o Estudo de Caso
  external: false
```
**Criando um Estudo de Caso Premium para o Projeto:**
Para que o botão "Ver Detalhes" do projeto funcione, crie um novo arquivo de texto dentro da pasta `projetos/` (ex: `nome-do-projeto.html`). Copie o HTML de uma página existente (como `arboili.html`), altere os textos da "Ficha Técnica" e da "Descrição Completa", e pronto! O design de portal premium fará o resto.

### 3. Banner Destaques da Home (`_data/destaques.yml`)
O carrossel gigante rotativo da página inicial (`index.html`) puxa as informações deste arquivo. O ideal é ter de 3 a 5 banners rodando.

**Modelo de adição:**
```yaml
- title: "Título Gigante do Banner"
  category: "LABEL EM CIMA DO TÍTULO"
  description: "Texto de apoio embaixo do título."
  image: "https://...link-da-imagem" # A foto que vai ficar de fundo
  url: "/projetos/meu-projeto.html" # Para onde o botão "Saiba Mais" vai levar
```

### 4. Publicações (`_data/publications.yml`)
A página de **Publicações** exibe os artigos do laboratório e pode ser preenchida de duas formas:

#### Opção A: Atualização Automática (Recomendada via Botência-Python)
Temos um bot (`atualizar_publicacoes.py`) que vasculha o Google Scholar e insere novos artigos automaticamente.
1. Configure sua chave da SerpApi no arquivo `.env`.
2. Rode `python atualizar_publicacoes.py`.
*(Lembre-se de configurar o parâmetro `limite: 15` dentro do script para que a API não gaste todo o seu saldo do Scholar baixando o histórico que já existe na página).*

#### Opção B: Atualização Manual
Basta colar um novo bloco de texto no topo de `_data/publications.yml`:
```yaml
- year: 2026
  category: artigos
  title: "Avanços em Inteligência na Epidemiologia"
  authors: "Silva, A., Almeida, A."
  venue: "Revista Saúde Pública"
  link_text: "Ler Artigo →"
  link_url: "https://doi.org/10.1234/..."
```

---

## 📂 Estrutura de Diretórios Resumida

- **`_data/`**: Contém o cérebro dinâmico (Projetos, Equipe, Publicações, Destaques da Home).
- **`_includes/`**: Componentes soltos que se repetem no site (Ex: navbar, footer).
- **`_layouts/`**: Os moldes Mestre (O `default.html` é o que abraça todas as páginas do site).
- **`assets/img/`**: A pasta raiz onde você deve salvar as fotos e logos.
- **`projetos/`**: Pasta onde você codifica os textos detalhados (os Estudo de Caso) de cada projeto.

---

_Mantido pela equipe INSIGHT / Fiocruz_
