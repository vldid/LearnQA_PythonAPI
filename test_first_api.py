import pytest
import requests

class TestFirstAPI:
    names = [
        {"Vitalii"},
        {"Arseniy"},
        {""}
    ]
    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "http://playground.learnqa.ru/api/hello"
        data = {'name':name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is not field 'answer' in the response"

        expected_response_text = f"Hello, {name}"
        actual_resposne_text = response_dict["answer"]
        assert actual_resposne_text == expected_response_text, "Actual text in the response is not correct"