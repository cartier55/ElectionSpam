import requests
from bs4 import BeautifulSoup


def nameGen():
    url = "https://www.fakenamegenerator.com/advanced.php?age-min=19&age-max=25"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    }

    response = requests.request("GET", url, headers=headers)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    fullName = soup.select_one('div.address > h3').text
    first = fullName.split(' ')[0]
    last = fullName.split(' ')[2]
    return {'first': first, 'last': last}
