import asyncio
import time
import csv
import aiohttp
import json
from bs4 import BeautifulSoup


async def save_company(company_name, company_address, company_phone, company_email):
    json_file_name = company_name.replace(' ', '_')
    with open(f'data/{json_file_name}.json', 'w') as company_file:
        json.dump(company_address, company_phone, company_email, company_file)


async def scrape(url, session):
    async with session.get(url) as resp:
        body = await resp.text()
        soup = BeautifulSoup(body, 'html.parser')
        company_name = soup.select_one('.company-name').text.strip()
        company_address = soup.select_one('.company-address').text.strip()
        company_phone = soup.select_one('.company-phone').text.strip()
        company_email = soup.select_one('.company-email').text.strip()
        await save_company(company_name, company_address, company_phone, company_email)


async def main():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        with open('urls.csv') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                task = asyncio.create_task(scrape(row['url'], session))
                tasks.append(task)

        print('Saving the output of extracted information')
        await asyncio.gather(*tasks)

        time_diff = time.time() - start_time
        print(f'Scraping time: %.2f seconds' % time_diff)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
