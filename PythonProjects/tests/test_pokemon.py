import requests
import pytest


URL ='https://api.pokemonbattle.me/v2'
HEADERS ={'Content-Type': 'application/json'}
TOKEN = 'fd19e76bf151fa41fd1b53db660e364f'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {"level": 5})
    assert response.status_code == 200


def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id": 559})
    assert response.json()['data'][0]['city'] == 'Лес'

CASES = [
  {'city', 'Лес'},
  {'trainer_name', 'Годзилла'}  
]

@pytest.mark.parametrize('key,value', CASES)

def test_parametrize_body(key,value):
   response = requests.get(url = f'{URL}/trainers', params = {"trainer_id": 559}) 
   assert response.json()['data'][0][key] == value