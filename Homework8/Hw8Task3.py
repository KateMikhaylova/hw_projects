import requests
import time


class Stackoverflow:

    def __init__(self, tag):
        self.tag = str(tag)

    def get_two_days_question_list(self):
        question_list = []
        time_now = int(time.time())
        time_two_days_ago = time_now - 172800
        counter = 1
        while True:
            params = {'page': str(counter), 'pagesize': '100', 'fromdate': str(time_two_days_ago),
                      'todate': str(time_now), 'order': 'desc', 'sort': 'creation', 'tagged': self.tag,
                      'site': 'stackoverflow'}
            url = 'https://api.stackexchange.com/2.3/questions?'
            response = requests.get(url, params=params)
            info = response.json()
            for element in info['items']:
                question_list.append(element['title'])
            if not info['has_more']:
                break
            counter += 1
            time.sleep(1)
        return question_list


if __name__ == '__main__':
    python = Stackoverflow('Python')
    questions = python.get_two_days_question_list()
    print(len(questions))
    for question in questions:
        print(question)
