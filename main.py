import os
import json
import smtplib
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def dump_file(file: dict) -> None:
    with open("config.json", "w") as f:
        json.dump(file, f, indent=4)


def set_config() -> None:
    url: str = "https://www.editais.uff.br/editais?field_n_mero_value=&combine=&field_tipo_tid=2&field__rg_o_respons_vel_tid=&field_errata_value=All&items_per_page=50"
    minimum_url: str = "https://www.editais.uff.br"
    email: str = input("write the email to recieve the mesage:")
    app_password: str = input(
        "write the app password of the email(NOT THE REAL PASSWORD):")
    json_dict: dict = {
        "url": url,
        "minimum_url": minimum_url,
        "email": email,
        "app_password": app_password,
        "visited_scholarships": [],
        "log": []
    }
    dump_file(json_dict)


def get_json() -> dict:
    files: list = os.listdir(os.getcwd())
    if "config.json" not in files:
        set_config()
    with open("config.json", "r") as f:
        file: dict = json.load(f)
    return file


def get_html(file: dict) -> None:
    html = requests.get(file["url"])
    html.encoding = html.apparent_encoding

    soup = BeautifulSoup(html.text, "html.parser")
    last_title = soup.find(title="[body]")
    last_title_href = last_title.get('href')
    last_title = last_title.text
    if last_title not in file["visited_scholarships"]:
        file["visited_scholarships"].append(last_title)
        send_email(file, last_title, last_title_href)

    log = f"{datetime.now()}"
    file["log"].append(log)
    dump_file(file)


def send_email(file: dict, title: str, href: str) -> None:
    subject: str = "Nova oportunidade de mobilidade"
    body: str = f"Título: {title} \n\nUrl: {file["minimum_url"] + href}"
    text: str = f"subject: {subject}\n\n{body}".encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(file["email"], file["app_password"])
        smtp.sendmail(file["email"], file["email"], text)


if __name__ == "__main__":
    config: dict = get_json()
    get_html(config)
