from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from .forms import SearchForm
import requests
from bs4 import BeautifulSoup
import urllib.parse
from django.conf import settings

@login_required
def scraper_home(request):
    """Página principal del scraper con formulario de búsqueda"""
    form = SearchForm()
    return render(request, 'scraper/home.html', {'form': form})

@login_required
def scraper_run(request):
    """Ejecuta el scraping basado en la palabra clave del usuario"""
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            
            # Realizar scraping en Wikipedia
            resultados = scrape_wikipedia(keyword)
            
            # Enviar resultados por email
            if resultados:
                send_scraper_email(request.user.email, keyword, resultados)
            
            context = {
                'keyword': keyword,
                'resultados': resultados,
                'email_enviado': True if resultados else False
            }
            return render(request, 'scraper/result.html', context)
    
    return redirect('scraper_home')


def scrape_wikipedia(keyword):
    """
    Scrapea Wikipedia buscando artículos relacionados con la palabra clave
    """
    try:
        # Codificar la palabra clave para la URL
        encoded_keyword = urllib.parse.quote(keyword)
        url = f"https://es.wikipedia.org/wiki/{encoded_keyword}"
        
        # Hacer request
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parsear HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        resultados = []
        
        # Obtener el título
        title_tag = soup.find('h1', class_='firstHeading')
        if title_tag:
            title = title_tag.get_text()
        else:
            title = keyword
        
        # Obtener párrafos del contenido
        content_div = soup.find('div', class_='mw-parser-output')
        if content_div:
            paragraphs = content_div.find_all('p', limit=5)
            
            for i, p in enumerate(paragraphs, 1):
                text = p.get_text().strip()
                if len(text) > 50:  # Solo párrafos con contenido significativo
                    resultados.append({
                        'numero': i,
                        'titulo': f"Párrafo {i}",
                        'contenido': text[:300] + '...' if len(text) > 300 else text,
                        'fuente': url
                    })
        
        # Si no hay resultados, intentar buscar en la página de búsqueda
        if not resultados:
            search_url = f"https://es.wikipedia.org/w/index.php?search={encoded_keyword}"
            response = requests.get(search_url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            search_results = soup.find_all('div', class_='mw-search-result-heading', limit=5)
            for i, result in enumerate(search_results, 1):
                link = result.find('a')
                if link:
                    resultados.append({
                        'numero': i,
                        'titulo': link.get_text(),
                        'contenido': f"Artículo encontrado en Wikipedia",
                        'fuente': f"https://es.wikipedia.org{link['href']}"
                    })
        
        return resultados if resultados else []
        
    except Exception as e:
        print(f"Error en scraping: {e}")
        return []


def send_scraper_email(user_email, keyword, resultados):
    """
    Envía los resultados del scraping por email
    """
    try:
        # Crear contenido del email
        body = f"Resultados del scraping para: {keyword}\n\n"
        body += "=" * 60 + "\n\n"
        
        for res in resultados:
            body += f"{res['numero']}. {res['titulo']}\n"
            body += f"   {res['contenido']}\n"
            body += f"   Fuente: {res['fuente']}\n\n"
        
        # Enviar email
        email = EmailMessage(
            subject=f"Resultados de Scraping: {keyword}",
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user_email],
        )
        email.send(fail_silently=False)
        return True
    except Exception as e:
        print(f"Error enviando email: {e}")
        return False
