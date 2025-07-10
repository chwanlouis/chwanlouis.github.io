




import json


class AWSQuiz(object):
    @staticmethod
    def print_question(data: dict) -> None:
        return




if __name__ == "__main__":
    file_name = "jsons\\qdb.json"
    with open(file_name, encoding="utf-8") as file:
        qdb = json.load(file)
    print(qdb[0]["question"])
