


import unittest
import requests
import json




class Test_Gtodo(unittest.TestCase):



    def test_fetcho_token(self):


        url = "http://192.168.56.150:8081/token"

        payload = json.dumps({
            "key": "matata"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)




    def test_FetchAllTodo(self):
        token = self.__fetch_token()
        print(token)

        import requests

        url = "http://192.168.56.150:8081/v1/todos"


        payload = {}
        files = {}
        headers = {
            'token': '{}'.format(token)
        }

        response = requests.request("GET", url, headers=headers, data=payload, files=files)

        print(response.text)



    def test_FetchSingleTodo(self):
        pass

    def test_AddTodo(self):
        pass

    def test_UpdateTodo(self):
        pass

    def test_DeleteTodo(self):
        pass



    def test_sd_health(self):
        pass

    def test_sd_disk(self):
        pass

    def test_sd_cpu(self):
        pass
    def test_sd_ram(self):
        pass

    def test_swagger(self):
        pass


    def __fetch_token(self):
        url = "http://192.168.56.150:8081/token"

        payload = json.dumps({
            "key": "matata"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        token_str = json.loads(response.text)
        token = token_str["data"]["token"]
        return token

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2Nzc3Mzc0NzYsImtleSI6Im1hdGF0YSIsIm5iZiI6MTY3NzczNzQ3Nn0.Jiaxy5ItrppfbQJAn24lkngI1D5-4ZQeOwpFui47A-8

if __name__ == "__main__":

    unittest.main()