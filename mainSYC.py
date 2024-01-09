import time
import csv
import requests
from bs4 import BeautifulSoup
import json


def save_comapany(company_name, company_address, company_phone, company_email, company_info):
    json_file_name = company_name.replace(' ', '_')
    with open(f'data/{json_file_name}.json', 'w') as company_file:
        json.dump(company_address, company_phone,
                  company_email, company_info, company_file)


def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    company_name = soup.select_one('h1').text.strip()
    company_address = soup.select_one('.address').text.strip()
    company_phone = soup.select_one('.phone').text.strip()
    company_email = soup.select_one('.email').text.strip()
    rows = soup.select('.table.table-striped tr')
    company_info = {row.th.text: row.td.text for row in rows}
    save_comapany(company_name, company_address,
                  company_phone, company_email, company_info)


def main():
    start_time = time.time()

    print('Saving the output of extracted information')
    with open('urls.csv') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            scrape(row['url'])

    time_diff = time.time() - start_time
    print(f'Scrapping time: %.2f seconds' % time_diff)


main()
