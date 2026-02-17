import requests
import yaml
import time
import random
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# --- CONFIGURAÇÕES ---
API_KEY = os.getenv("SERPAPI_KEY")
AUTHOR_ID = "EnBKFUAAAAAJ"

if not API_KEY or API_KEY == "SUA_CHAVE_AQUI":
    print("Erro: API_KEY não configurada. Edite o arquivo .env e adicione sua chave do SerpApi.")
    exit(1)

print(f"Iniciando extração do autor {AUTHOR_ID} via SerpApi...")
print("Atenção: Isso consome 1 crédito da API por artigo para buscar o link direto da revista.\n")

todas_publicacoes = []
start = 0
num_por_pagina = 100

while True:
    print(f"Buscando lista de artigos a partir da posição {start}...")
    url_lista = f"https://serpapi.com/search.json?engine=google_scholar_author&author_id={AUTHOR_ID}&api_key={API_KEY}&hl=pt-br&start={start}&num={num_por_pagina}"

    try:
        response = requests.get(url_lista)
        response.raise_for_status()
        data = response.json()
        
        artigos = data.get("articles", [])
        if not artigos:
            print("Fim da lista de artigos.")
            break
            
        for artigo in artigos:
            titulo_artigo = artigo.get('title', 'Sem Título')
            citation_id = artigo.get('citation_id', '')
            
            print(f"Processando: {titulo_artigo[:40]}...")
            
            # Link padrão (Scholar) caso não ache o da revista
            link_direto = artigo.get('link', '#') 
            
            # --- BUSCA DO LINK DIRETO DO PAPER (Springer, Nature, etc) ---
            # Faz uma chamada extra para pegar o link "Source" ou "Title Link" do detalhe
            if citation_id:
                # Nota: view_op=view_citation retorna detalhes específicos
                url_citacao = f"https://serpapi.com/search.json?engine=google_scholar_author&view_op=view_citation&citation_id={citation_id}&api_key={API_KEY}"
                try:
                    res_cit = requests.get(url_citacao)
                    if res_cit.status_code == 200:
                        data_cit = res_cit.json()
                        citation = data_cit.get("citation", {})
                        
                        # Tenta pegar o link do título (geralmente vai para a editora)
                        if "link" in citation:
                             link_direto = citation["link"]
                        
                        # Se não, tenta recursos (PDFs)
                        elif citation.get("resources"):
                            link_direto = citation["resources"][0].get("link", link_direto)
                            
                except Exception as e:
                    print(f"  -> Aviso: Erro ao buscar detalhe da citação ({e}). Mantendo link padrão.")
            
            # Define a categoria dinamicamente
            # Exemplo simples baseado no título, pode ser refinado
            categoria = 'preprints' if 'preprint' in titulo_artigo.lower() else 'artigos'
            
            # Formata Venue/Journal
            # SerpApi retorna 'publication' como "Nature ..., 2020" string
            venue_full = artigo.get('publication', 'Google Scholar')
            venue_parts = venue_full.split(',')
            venue_name = venue_parts[0] if venue_parts else venue_full
            
            # Monta a estrutura EXATA exigida pelo layout do site
            pub_dict = {
                'year': artigo.get('year', 'N/A'),
                'category': categoria,
                'title': titulo_artigo,
                'authors': artigo.get('authors', 'Alexandra e colaboradores'),
                'venue': venue_name,
                'venue_type': 'Artigo' if categoria == 'artigos' else 'Preprint', # Campo auxiliar para o layout
                'image': f"https://picsum.photos/80/110?random={random.randint(1, 100)}",
                'link_text': "Ler Artigo",
                'link_url': link_direto
            }
            todas_publicacoes.append(pub_dict)
            
            # Pausa curta para ser gentil com a API
            time.sleep(0.1) 
            
        start += num_por_pagina
        
    except Exception as e:
        print(f"❌ Erro na extração da lista: {e}")
        break

# Salva no formato e arquivo corretos
if todas_publicacoes:
    try:
        OUTPUT_FILE = '_data/publications.yml'
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(todas_publicacoes, f, allow_unicode=True, sort_keys=False)
        print(f"\n✨ SUCESSO! {len(todas_publicacoes)} artigos formatados e salvos em {OUTPUT_FILE}")
    except Exception as e:
        print(f"\n❌ Erro ao salvar o arquivo YAML: {e}")
else:
    print("\n⚠️ Nenhum artigo encontrado.")
