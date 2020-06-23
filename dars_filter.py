import dars_parser
from collections import OrderedDict
import sys

# filter out classes with course numbers such as 1--
# filter out duplicates courses
def filter_classes(classes : list):
    classes = filter(lambda x: '--' not in x[1] and 'F' not in x[3], classes)
    classes = list(classes)

    classes = list(OrderedDict.fromkeys(classes))
    return classes

# create list of tuples (dept + course_num, credit_hours)
def put_into_courses(courses : list):
    list_of_courses = []
    for tup in courses:
        list_of_courses.append((tup[0] + ' ' + tup[1], float(tup[2])))
    return list_of_courses


# TODO: make a driver class and use this code
def process_pdf(filename):
    try:
        f = open(filename)
    except FileNotFoundError:
        print("Give a valid path!")
    finally:
        f.close()

    text = dars_parser.convert_pdf_text(filename)
    courses = dars_parser.get_courses_from_text(text)
    courses_num_grade_hours = dars_parser.get_courses_num_grade_and_hours(courses)

    # filter result before returning it
    courses = filter_classes(courses_num_grade_hours)
    courses = put_into_courses(courses)

    return courses

    # print(*courses, sep = '\n')
