from bs4 import BeautifulSoup
import httpx

async def get_prayer_time(region):
    response = httpx.get(f"https://namozvaqti.uz/shahar/{region}")
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    times = []
    for i in soup.find_all('p', {'class':'time'}):
        times.append(i.text)
    return times



