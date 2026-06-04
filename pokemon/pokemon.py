import requests

def get_pokemon(name):
     try:
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        answer = requests.get(url)

        if answer.status_code == 200:
         return answer.json()
        
        return None
        
     except requests.exceptions.RequestException:
        return None
    
def show_pokemon(data):
    print("\nName:", data["name"])
    print(f"Type: {', '.join(t['type']['name'] for t in data['types'])}")
    print(f"Skills: {", ".join(s["ability"]["name"] for s in data["abilities"])}")
    print("Base Experience:", data["base_experience"])
    print("Height:", data["height"])
    print("Weight", data["weight"])

def main():
    pokemon = input("Enter name of pokemon: ").lower()

    data = get_pokemon(pokemon)

    if data:
        show_pokemon(data)
    else:
        print("Pokemon not found or server unavaible")

if __name__ == "__main__":
    main()