import requests

URL ='https://api.pokemonbattle.me/v2'
HEADERS ={'Content-Type': 'application/json'}
TOKEN = 'fd19e76bf151fa41fd1b53db660e364f'
trainer_id:559

body = {
    "trainer_token": TOKEN,
    "email": "linar301@yandex.ru",
    "password": "Rapid301Pokemon"
}

body_confirm = {
    "trainer_token": TOKEN
}

body_pokemons = {
    "name": "generate",
    "photo": "generate"
}

body_pokemons_put = {
    "pokemon_id": "id_покемона",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_pokemons_post = {
    "pokemon_id": "9"
}

response = requests.post(url = f'{URL}/trainers/reg', headers = HEADERS, json = body)
print(response.text)

response_confirm = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADERS, json = body_confirm)
print(response_confirm.text)

response_pokemons = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body_pokemons)
print(response_pokemons.text)

response_pokemons_put = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_pokemons_put)
print(response_pokemons_put.text)

response_pokemons_post = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_pokemons_post)
print(response_pokemons_post.text)