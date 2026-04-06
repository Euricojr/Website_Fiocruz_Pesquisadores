# 🏛️ Portal INSIGHT - Fiocruz

O **INSIGHT** é um laboratório interdisciplinar da Fiocruz que integra inteligência artificial, ciência de dados e epidemiologia. Este portal foi desenvolvido para ser uma vitrine dinâmica de nossas pesquisas, membros e parcerias.

---

## 🧠 Como o Site Funciona (Arquitetura)

Este é um site estático gerado com **Jekyll**. O diferencial é que ele foi projetado para ser **dirigido por dados (Data-Driven)**.

*   **Conteúdo Dinâmico**: Quase tudo o que você vê (Equipe, Projetos, Publicações) NÃO está escrito no HTML. O Jekyll lê arquivos na pasta `_data/` e renderiza as páginas automaticamente.
*   **Layouts**: Os moldes das páginas ficam em `_layouts/`. O principal é o `default.html`.
*   **Componentes**: Partes reutilizáveis (como a barra de navegação e o rodapé) ficam em `_includes/`.

---

## 🚀 Como Rodar Localmente

Para visualizar o site no seu computador antes de publicar:

### Pré-requisitos
- **Ruby** (Instalado e configurado no PATH).
- **Bundler** (`gem install bundler`).

### Passo a Passo
1.  **Instale as dependências**:
    ```powershell
    bundle install
    ```
2.  **Inicie o servidor**:
    ```powershell
    bundle exec jekyll serve
    ```
3.  **Acesse**: `http://localhost:4000`.

---

## 🌓 Design System & Temas

O site utiliza um sistema de temas dinâmico:
- **Cores**: Definidas em variáveis CSS no topo de `assets/css/main.css`.
- **Dark Mode**: Controlado via classe `.dark-mode` no `body`. A preferência do usuário é salva no `localStorage` do navegador.
- **Ícones**: Muitos ícones (incluindo o toggle de tema) usam SVGs com `fill="currentColor"`, o que permite mudar a cor via CSS rapidamente.

---

---

## 🖼️ Como Funcionam as Imagens?

Para fotos e banners nos arquivos `.yml`, você tem duas opções:

1.  **Local (Recomendado)**: Salve a imagem em `assets/img/`. No YAML, use: `image: "/assets/img/foto.jpg"`.
2.  **Externa**: Use o link direto da internet: `image: "https://site.com/foto.jpg"`.

---

## 📝 Como Atualizar o Conteúdo (`_data/`)

O portal é gerenciado editando arquivos YAML na pasta `_data/`.

### 1. Equipe (`_data/team.yml`)
Organizado por categorias. Se omitir `lattes` ou `linkedin`, o botão desaparece automaticamente.

### 2. Projetos (`_data/projects.yml`)
Gera os cards da página de projetos. Para criar um "Estudo de Caso" (detalhes):
- Crie um `.html` em `projetos/` (ex: `meu-projeto.html`).
- Use um arquivo existente como base.
- Aponte a `url` no `projects.yml` para esse arquivo.

### 3. Destaques da Home (`_data/destaques.yml`)
Controla o carrossel da página inicial.
- **Destaque Dinâmico**: Se você usar `dynamic: "latest_pub"`, o site buscará automaticamente o artigo mais recente em `publications.yml`.

---

## 🤖 Automação de Publicações

Usamos o script `atualizar_publicacoes.py` para manter a lista de artigos sempre em dia via **SerpApi**.

### Configuração
1.  Crie um arquivo `.env` na raiz (use o `.env.example` como base).
2.  Adicione sua `SERPAPI_KEY`.

### Execução
Rode o script para buscar novos artigos do Google Scholar:
```powershell
python atualizar_publicacoes.py
```
O script evita duplicatas comparando os títulos com o que já existe em `_data/publications.yml`.

---

## 🌐 Multi-idioma (Tradução)

O site possui um botão de tradução (PT/EN) na barra de navegação.
- **Funcionamento**: Utiliza o widget do Google Tradutor de forma customizada via JavaScript (`assets/js/main.js`).
- **Memória**: O idioma escolhido é salvo no navegador do usuário para que ele não precise clicar novamente ao mudar de página.

---

## 📂 Estrutura de Diretórios

- **`_data/`**: O "cérebro" do site. Altere os arquivos YAML aqui para mudar o conteúdo.
- **`_includes/`**: Componentes reutilizáveis (Navbar, Footer, Barra Social).
- **`_layouts/`**: Modelos de página (o site usa o layout `default`).
- **`assets/`**: Arquivos estáticos (CSS, imagens, JavaScript).
- **`projetos/`**: Páginas individuais com os detalhes (Estudos de Caso) de cada projeto.
- **`atualizar_publicacoes.py`**: Script Python para automação via SerpApi.

---

_Mantido pela equipe INSIGHT / Fiocruz_
