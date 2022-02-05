from bs4 import BeautifulSoup
import requests


def scrape_problems():
    url = "https://sih.gov.in/sih2022PS"
    req = requests.get(url)
    # print(req.content)

    soup = BeautifulSoup(req.text, "html.parser")
    # print(soup.prettify())

    content = soup.find("table", {"id": "dataTablePS"})
    # print(content)
    table = content.find("tbody")

    problems = []
    for row in table.findChildren("tr", recursive=False):
        data = []
        for table_data in row.find_all("td"):
            data.append(table_data.text.strip().replace("\n", "").replace("  ", ""))

        desc = row.find("table", {"id": "settings"}).find("tr").find("td").text.strip()

        problem_dict = {
            "id": data[0],
            "institution": data[1],
            "problem_statement": desc,
            "code": data[10],
        }
        problems.append(problem_dict)

    return problems
