
import re, requests

base_url = 'http://127.0.0.1:5000/'

def scrape_links(url): return re.findall(r'href="([a-z]+\.html)"', requests.get(url).text)
    

def visit_all_pages():
    links = ['index.html']
    result = []
    while links:
        next = links.pop()
        if next not in result:
            result.append(next)
            links.extend(scrape_links(f'{base_url}{next}'))
        
    return sorted(result)

print('\n'.join(visit_all_pages()))