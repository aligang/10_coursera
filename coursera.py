#!/usr/bin/env python3


import random
import requests
import bs4
import re
import openpyxl
import os
import sys
from lxml import objectify


def get_full_courses_list():
    url = "https://www.coursera.org/sitemap~www~courses.xml"
    coursera_courses_response = requests.get(url)
    coursera_courses_xml_as_bytecode = coursera_courses_response.content
    urlset_xml_root_object = objectify.fromstring(
        coursera_courses_xml_as_bytecode
    )
    full_courses_list = [
        url_object.loc.text
        for url_object in urlset_xml_root_object.iterchildren()
    ]
    return full_courses_list


def choose_random_courses(amount_of_courses, full_courses_list):
    courses_links_list = random.sample(
        full_courses_list,
        amount_of_courses
    )
    return courses_links_list


def get_courses_info(courses_links_list):
    courses_info = [("url", "language", "date", "duration(weeks)")]
    for course_link in courses_links_list:
        course_page_info_response = requests.get(course_link)
        course_page_info = course_page_info_response.text
        html_dom = bs4.BeautifulSoup(course_page_info, 'html.parser')
        language_html = html_dom.find(
            "div",
            class_="rc-Language"
        )
        start_date_html = html_dom.find(
            "div",
            class_="startdate rc-StartDateString caption-text"
        )
        duration_html = html_dom.find(
            "div",
            class_="rc-WeekView"
        )
        language = language_html.text
        start_date = start_date_html.text
        if duration_html:
            duration = len(duration_html)
        else:
            duration = "N/A"
        courses_info.append((course_link, language, start_date, duration))
    return courses_info


def write_courses_info_to_xlsx(courses_info, excel_workbook_file_path):
    excel_workbook = openpyxl.Workbook()
    work_sheet = excel_workbook.active
    work_sheet.title = "coursera_offers"
    for row in courses_info:
        work_sheet.append(row)
    if re.search("\.xlsx$", excel_workbook_file_path):
        excel_workbook_file_path_with_extension = excel_workbook_file_path
    else:
        excel_workbook_file_path_with_extension = "{}.xlsx".format(
            excel_workbook_file_path
        )
    excel_workbook.save(excel_workbook_file_path_with_extension)
    print(
        "\n"
        "Данные о тренингах Coursera записаны в файл {}".format(
            excel_workbook_file_path_with_extension
        )
    )


def get_input_data():
    full_courses_list = get_full_courses_list()
    total_amount_of_courses = len(full_courses_list)
    amount_of_courses_as_string = input(
        "Какое количество тренингов с сайта www.coursera.org"
        "следует рассмотреть ?"
        "\n"
        "всего их {} (укажите целое число от 1 до {})"
        "\n".format(
            total_amount_of_courses,
            total_amount_of_courses
        )
    )
    excel_workbook_name = input(
        "\n"
        "Имя файла, куда нужно будет сохранить информацию ? : "
        "\n"
    )
    return amount_of_courses_as_string, total_amount_of_courses, \
        excel_workbook_name, full_courses_list


if __name__ == '__main__':
    if len(sys.argv) < 2:
        directory_path = "./"
        print(
            "Не указан аргумент - имя директории."
            "\n"
            "Excel-файл будет записан в локальную директорию"
            "\n"
        )
    else:
        directory_path = sys.argv[1]
    if not os.path.exists(directory_path):
        sys.exit(
            "Такая директория не существует"
            "\n"
            "Перезапустите код, указав корректную директорию "
            "или не указывайте совсем"
            )
    (amount_of_courses_as_string, total_amount_of_courses,
     excel_workbook_name, full_courses_list) = get_input_data()
    if not re.search("^\d+$", amount_of_courses_as_string):
        sys.exit(
            "Неверно указан формат начальных данных"
            "\n"
            "Количество рассматриваемых курсов должно быть "
            "в формате целого положительного числа"
        )
    amount_of_courses = int(amount_of_courses_as_string)
    if amount_of_courses > total_amount_of_courses:
        sys.exit(
            "Неверно указан формат начальных данных"
            "\n"
            "Количество рассматриваемых курсов не может"
            "быть больше имеющегося количества курсов"
        )
    courses_links_list = choose_random_courses(
        amount_of_courses,
        full_courses_list
    )
    courses_info = get_courses_info(courses_links_list)
    excel_workbook_file_path = directory_path + excel_workbook_name
    write_courses_info_to_xlsx(courses_info, excel_workbook_file_path)
