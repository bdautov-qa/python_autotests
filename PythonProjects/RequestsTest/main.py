import requests

response = requests.post('https://pokemonbattle.me:9104/trainers/reg', json={
    "trainer_token": "0b3ec2a4d65328c7ff2f30f5deb378bf",
    "email": "bdautov91@gmail.com",
    "password": "Iloveqa1"
})

print(response.status_code)

token = '0b3ec2a4d65328c7ff2f30f5deb378bf'


response_activated = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', json = {
    "trainer_token": token
})

print(response_activated.status_code)

'''response_add_pokemon = requests.post('https://pokemonbattle.me:9104/pokemons', headers={'trainer_token' : token}, json = {
    "name": "Бубазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print(response_add_pokemon.text)

response_change_name_pokemon = requests.put('https://pokemonbattle.me:9104/pokemons', headers={'trainer_token' : token}, json = {
    "pokemon_id": "9288",
    "name": "Бумбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(response_change_name_pokemon.text)'''

response_add_pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers={'trainer_token' : token}, json = {
    "pokemon_id": "9288"
})
print(response_add_pokeball.text)