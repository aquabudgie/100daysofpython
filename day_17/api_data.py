import requests
import ast

class ApiData:
    def __init__(self, url) -> None:
        self.url = url
        self.question_list = self.retrieve_data()
    
    def retrieve_data(self):
        response = requests.get(self.url)
        bytes_string = response.content
        content = bytes_string.decode("UTF-8")
        content_dict = ast.literal_eval(content)
        content_dict = self.clean_data(content_dict)
        return content_dict["results"]
    
    # Incomplete
    def clean_data(self, content_dict):
        for result in content_dict["results"]:
            print(result)
        return content_dict


data = ApiData("https://opentdb.com/api.php?amount=10&type=boolean")