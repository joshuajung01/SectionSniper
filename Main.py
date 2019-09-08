# HowdyHack 2019
import json
from typing import Dict, List
from Data_Functions import find_avai_class

import requests

# Get all terms: https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/classSearch/getTerms?dataType=json&offset=1&max=500
from requests import Response


class CourseData:
    def __init__(self, crn, name, title):
        self.crn = crn
        self.name = name
        self.title = title

    def print_data(self):
        print("CRN:", self.crn)
        print("Name:", self.name)
        print("Title:", self.title)


def request_terms() -> List[Dict[str, str]]:
    """Performs a GET request for all terms in TAMU history"""
    url = "https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/classSearch/getTerms?dataType=json&offset=1&max=500"
    response: Response = requests.get(url)
    return json.loads(response.content)


def request_sections(dept: str, course_num: str, cookies):
    url = f"https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_subjectcoursecombo={dept+course_num}&txt_term=201931&pageOffset=0&pageMaxSize=500&sortColumn=subjectDescription&sortDirection=asc"
    response = requests.get(url, cookies=cookies)
    return json.loads(response.content)


def post_term(term_code: str):
    """Makes a POST request to set the desired term for consequent requests. Returns cookies"""
    url = "https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/term/search?mode=courseSearch"
    body = {
        "dataType": "json",
        "term": term_code
    }
    response: Response = requests.post(url, data=body)
    return response.cookies


def main():
    terms = request_terms()
    term_code = terms[0]["code"]
    term_cookies = post_term(term_code)

    data = request_sections(dept,course_num,term_cookies)
    availible_classes = find_avai_class(data, dept, course_num)
    print(availible_classes)


if __name__ == '__main__':
    main()
