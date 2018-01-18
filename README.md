## 1.Что это такое ?

Этот код позволяет сформировать список из набора случайных тренингов с сайта [www.coursera.org](https://www.coursera.org)  и записать его в excel-файл

## 2.Системные требования
Для работы с программой понадобится Python3.5 (который скорее всего у вас уже установлен, если Вы используете Linux)  
Также может понадобиться установить модули `requests`, `openpyxl`, `beautifulsoup4`, `lxml` сделать это можно выполнив  :
```bash
$ pip3 install -r requirements.txt
```

## 3.Где можно скачать  
Можно форкнуть здесь - [тренинги с курсеры](https://github.com/aligang/10_coursera)  
и затем скачать 
```bash
$ git clone https://github.com/<юзернейм-аккаунта-на-гите>/10_coursera
```

## 4.Как этим пользоваться...  
*a.Данный код может быть исползован как самостоятельная программа,*  

```bash
$  python3 coursera.py --amount 7 --directory 123 --filename file_with_courses

Данные о тренингах Coursera записаны в файл 123/file_with_courses.xlsx

```

## 5.Какие функции могут быть переиспользованы в вашем коде
Функция `fetch_get_response` формирует http-get вызов и возваращет содержимое пейлоуда
Функция `extract_full_courses_list` парсит список курсов в формате xml  и формирует список курсов в формате string
Функция `create_cli_parser` запрашивает данные от пользователя  тем самым обеспечивая программу необходимыми для работы данными
Функция `choose_random_courses` делает случайную выборку и формирует список url- страниц для тренингов, для которых  в последствии будет идти сбор интересующей информации                 
Функция `get_courses_data` формирует список ключевых параметров cтраниц тренингов -   использует адреса url страниц тренингов, получаемых от `choose_courses`, отправляет запросы  на эти адреса (переисопльзуюя функцию `fetch_get_response`), а полученную HTM-структуру парсит, вызывая функцию `gather_data_from_html_page` 
Функция `gather_data_from_html_page` собиратает ключевыю информаций с HTML-страниц
Функция `put_courses_data_to_excel_workbook` конвертирует информацию, полученную от функции  `fetch_get_response` в формат excel-объекта
Функция `write_excel_workbook_to_file` записывает excel-объект в excel-файл


Импортировать и использовать функции коди можно  следующим образом:  
```python
from coursera import fetch_get_responce
from coursera import choose_courses
from coursera import get_courses_data
from coursera import grab_data_from_html_page
from coursera import put_courses_data_to_excel_workbook


full_courses_list = extract_full_courses_list(
    full_courses_list_as_xml
)
some_courses_links = choose_courses(
    amount_of_courses,
    full_courses_list
)
courses_data = get_courses_data(some_courses_links)
excel_workbook_file_path = os.path.join(
    path_to_directory,
    file_name
)
excel_workbook = put_courses_data_to_excel_workbook(
    courses_data
)
excel_workbook.save(excel_workbook_file_path_with_extension)


```

## 6. Цели
Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
