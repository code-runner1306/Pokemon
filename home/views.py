from django.shortcuts import render, redirect
import requests,json
# Create your views here.
def home(request):
    try:
        if request.method =='POST': 
            Pokemon = request.POST.get("name")
            shiny = request.POST.get('poke')
            print(shiny)
            api_name = "https://pokeapi.co/api/v2"
            url = api_name + f"/pokemon/{Pokemon.lower()}"
            pokeinfo={}
            # Make the API request
            info = requests.get(url)

            if info.status_code == 200:
                # Load the response as JSON (only call json.loads once)
                info = info.json()
                pokeinfo = {
                    'name': info['name'].title(),
                    'abilities': [{
                        'ability_name': ability['ability']['name'].title(),
                        'is_hidden': ability['is_hidden']
                    } for ability in info['abilities']],
                    'moveset': [{
                        'move': moves['move']['name'].title(),
                        'level_learned_at': moves['version_group_details'][len(moves['version_group_details'])-1]['level_learned_at']
                    }for moves in info['moves']],
                    'typing': [{
                        'type':types['type']['name'].title()
                    }for types in info["types"]]
                }
                pokeinfo['moveset'].sort(key=lambda move: move['level_learned_at'] if move['level_learned_at'] is not None else float('inf'))
            else:
                print("Error: Could not retrieve data from the API.")  
            is_shiny = shiny == 'Shiny'
            return render(request, "index.html",{"pokeinfo":pokeinfo, 'Shiny':is_shiny})    
    except Exception as e:
        print("Error Occured " + e.str())
        return redirect('/')
    return render(request, "index.html")