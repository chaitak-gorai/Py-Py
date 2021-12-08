from bs4 import BeautifulSoup
import requests
import os

main_doc = requests.get('https://aclanthology.org/venues/ijcnlp/')
soup = BeautifulSoup(main_doc.text, 'html.parser')
total_conferences_in_2021 = len(soup.find(class_='row').find_all('a', class_='align-middle'))
# (soup1.find_all('a', class_='badge badge-primary align-middle mr-1')
conferences_in_2021 = []

for i in range(0, total_conferences_in_2021):
    conferences_in_2021.append('https://aclanthology.org/'+soup.find(class_='row').find_all('a', class_='align-middle')[i].get('href'))

document_number = 0
for i in range(0, total_conferences_in_2021):
    conference = requests.get(conferences_in_2021[i])
    soup_new = BeautifulSoup(conference.text, 'html.parser')
    total_pdfs_in_the_conference = len(soup_new.find_all('a', class_='badge badge-primary align-middle mr-1'))
    for j in range(0, total_pdfs_in_the_conference):
        url = (soup_new.find_all('a', class_='badge badge-primary align-middle mr-1')[j].get('href'))
        response = requests.get(url)
        file_path = os.path.join("C:\PDF", f"Document{document_number + 1}.pdf")
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Document{document_number + 1} is downloaded.")
        document_number += 1