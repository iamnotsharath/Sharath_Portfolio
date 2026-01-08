import requests
from bs4 import BeautifulSoup

def get_h1b_applicants():
    url = 'https://www.uscis.gov/tools/reports-and-studies/h-1b-employer-data-hub'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        data_sections = soup.find_all('div', class_='field-content')
        
        print("H1B Visa Applications Per Year:")
        for section in data_sections:
            text = section.get_text(strip=True)
            if 'FY' in text and any(char.isdigit() for char in text):
                print(text)
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    get_h1b_applicants()
    ##
