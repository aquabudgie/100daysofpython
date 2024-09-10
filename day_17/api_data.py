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
        return content_dict["results"]