import requests

def pokemon():
    pkm = str(input("Enter name of the Pokemon: ")).lower()

    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{pkm}"
        answer = requests.get(url)

        if answer.status_code == 200:
            poke = answer.json()
            print("\nName:", poke["name"])
            print(f"Type: {', '.join(t['type']['name'] for t in poke['types'])}")
            print(f"Skills: {", ".join(s["ability"]["name"] for s in poke["abilities"])}")
            print("Base Experience:", poke["base_experience"])
            print("Height:", poke["height"])
            print("Weight", poke["weight"])
        else:
            print("Pokemon not found")
    except requests.exceptions.RequestException:
        print("The server could be not acessed")
    return pokemon

if __name__ == "__main__":
    pokemon()