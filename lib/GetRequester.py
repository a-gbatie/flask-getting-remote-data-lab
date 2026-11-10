import requests
import json

class GetRequester:

  def __init__(self, url):
    self.url = url

  def get_response_body(self):
    res = requests.get(self.url) # sends GET request to API
    return res.text # grab the response body as a string

  def load_json(self):
    res = self.get_response_body() # retrieves JSON string from API
    return json.loads(res) # converts that string into Python object