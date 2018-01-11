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
$  python3 coursera.py 
Не указан аргумент - имя директории.
Excel-файл будет записан в локальную директорию

Какое количество тренингов с сайта www.coursera.orgследует рассмотреть ?
всего их 2602 (укажите целое число от 1 до 2602)
4

Имя файла, куда нужно будет сохранить информацию ? : 
workbook4

Данные о тренингах Coursera записаны в файл ./workbook4.xlsx
```

## 5.Какие функции могут быть переиспользованы в вашем коде
Функция `get_full_courses_list` формирует полный список всех треннигов предлагаемых [www.coursera.org](https://www.coursera.org)
Функция `get_input_data` запрашивает данные от пользователя и вызывает функцию `get_full_courses_list` тем самым обеспечивая программу необходимыми для работы данными
Функция `choose_random_courses`  делает случайную выборку и формирует список url- страниц для тренингов, для которых  в последствии будет идти сбор интересующей информации
Функция `write_courses_info_to_xlsx`  записывает всю собранную о случайных курсах информацию в excel-файл


Импортировать и использовать функции коди можно  следующим образом:  
```python
from coursera import get_full_courses_list
from coursera import choose_random_courses
from coursera import write_courses_info_to_xlsx


full_courses_list = get_full_courses_list()
courses_links_list = choose_random_courses(
    amount_of_courses,
    full_courses_list
)
trending_repos_info_list = get_open_issues(trending_repos_list)
courses_info = get_courses_info(courses_links_list)
write_courses_info_to_xlsx(courses_info, excel_workbook_file_path)

```

## 6. Цели
Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
