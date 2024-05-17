import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from io import BytesIO
import os


url = "http://rsreu.ru/studentu/raspisanie-zanyatij"

# Отправляем HTTP-запрос и получаем HTML-код страницы
response = requests.get(url)
html_content = response.content

# Парсим HTML-код с помощью BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Находим все ссылки на файлы XLSX в очной форме
header = soup.find(string=lambda text: "очной формы" in text.lower())
if header:
    print(header.string+" Success")
    parent_div = header.find_parent("div")



    # Поиск всех ссылок на файлы Excel внутри найденного блока
    excel_links = parent_div.find_all("a", href=lambda href: href and "doc_download" in href and len(href) > len("/component/docman/doc_download"))
    print(f"Найдено {len(excel_links)} ссылок на файлы Excel.")
    print(excel_links)

    # Создание директории "files", если она не существует
    files_dir = os.path.join(os.getcwd(), "excel_files")
    os.makedirs(files_dir, exist_ok=True)

    # Скачивание файлов Excel
    for i, link in enumerate(excel_links, start=1):
        excel_url = link.get("href")
        full_url = requests.compat.urljoin(url, excel_url)  # Формируем полный URL
        excel_response = requests.get(full_url)

        # Проверка файла на формат .xlsx
        try:
            workbook = load_workbook(filename=BytesIO(excel_response.content))
            file_path = os.path.join(files_dir, f"table_{i}.xlsx")
            with open(file_path, "wb") as file:
                file.write(excel_response.content)
            print(f"Файл сохранен: {file_path}")
        except Exception as e:
            print(f"Файл по ссылке {full_url} не является корректным файлом .xlsx: {e}")


else:
    print("Заголовок не найден на странице.")