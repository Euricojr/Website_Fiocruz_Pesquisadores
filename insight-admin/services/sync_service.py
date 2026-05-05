
import os
import requests
import yaml
import time
import random
from dotenv import load_dotenv
from services.yaml_service import get_file_path, read_yaml, write_yaml

load_dotenv()

API_KEY = os.getenv("SERPAPI_KEY")

# Researchers to sync
PESQUISADORES = [
    {"nome": "Alexandra Almeida", "id": "EnBKFUAAAAAJ", "limite": 5},
    {"nome": "Francisco Bastos", "id": "dzP4uYEAAAAJ", "limite": 5}
]

def sync_publications():
    """
    Syncs publications from Google Scholar via SerpApi.
    Avoids duplicates by checking titles.
    Returns: dict with status and details.
    """
    if not API_KEY:
        return {"success": False, "message": "SERPAPI_KEY not configured in .env"}

    all_fetched = []
    
    for researcher in PESQUISADORES:
        author_id = researcher["id"]
        limite = researcher["limite"]
        nome = researcher["nome"]
        
        # SerpApi parameters: sort by pubdate to get latest
        url = f"https://serpapi.com/search.json?engine=google_scholar_author&author_id={author_id}&api_key={API_KEY}&hl=pt-br&sort=pubdate&num={limite}"
        
        try:
            response = requests.get(url)
            if response.status_code != 200:
                continue
                
            data = response.json()
            articles = data.get("articles", [])
            
            for art in articles:
                title = art.get('title', 'Sem Título')
                
                # Basic parsing like in the original script
                categoria = 'preprints' if 'preprint' in title.lower() else 'artigos'
                venue_full = art.get('publication', 'Google Scholar')
                venue_name = venue_full.split(',')[0] if ',' in venue_full else venue_full
                
                pub_dict = {
                    'year': art.get('year', 'N/A'),
                    'category': categoria,
                    'title': title,
                    'authors': art.get('authors', f'{nome} e colaboradores'),
                    'venue': venue_name,
                    'venue_type': 'Artigo' if categoria == 'artigos' else 'Preprint',
                    'image': f"https://picsum.photos/80/110?random={random.randint(1, 100)}",
                    'link_text': "Ler Artigo",
                    'link_url': art.get('link', '#')
                }
                all_fetched.append(pub_dict)
                
            time.sleep(0.5) # Avoid hitting API too hard
            
        except Exception as e:
            print(f"Error syncing {nome}: {e}")
            continue

    if not all_fetched:
        return {"success": False, "message": "No new publications found or API error."}

    # Load existing to avoid duplicates
    existing_pubs = read_yaml("publications.yml")
    existing_titles = {str(p.get('title', '')).strip().lower() for p in existing_pubs}
    
    new_to_add = []
    for pub in all_fetched:
        if str(pub.get('title', '')).strip().lower() not in existing_titles:
            new_to_add.append(pub)
            existing_titles.add(str(pub.get('title', '')).strip().lower())

    if new_to_add:
        # Prepend new publications to the list (so they appear at the top)
        updated_pubs = new_to_add + existing_pubs
        write_yaml("publications.yml", updated_pubs)
        return {"success": True, "new_count": len(new_to_add), "total_count": len(updated_pubs)}
    
    return {"success": True, "new_count": 0, "message": "All publications are already up to date."}
