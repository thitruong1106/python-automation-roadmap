import json 

pokemon = [{
    'name': 'Chrizard',
    'set': 'base set',
    'rarity':'reverse holo', 
    'valued_usd':350,
    'graded': True
},
{
    'name': 'Piplup',
    'set': 'base set',
    'rarity':'reverse holo', 
    'valued_usd':350,
    'graded': False
},
{
    'name': 'Snorlax',
    'set': 'base set',
    'rarity':'SIR', 
    'valued_usd':400,
    'graded': False
}
]

#Create and save to json file 
with open('card.json', 'w') as f:
    json.dump(pokemon,f,indent=4)

print('✅ Saved card to json')


#reading json_file 
with open('card.json', 'r') as f:
    data = json.load(f)

#for each card in data 
suggestions = []
for card in data: 
    print("card name:", card['name'])

    if card['valued_usd'] > 100 and not card ['graded']:
        suggestions.append({
            "name": card['name'],
            "set": card['set'],
            "value": card['valued_usd']
        })
    else:
        print(f"{card['name']} is already graded")

#save suggestion to a new file 
with open("grading_sugestion.json", 'w') as f:
    json.dump(suggestions, f, indent=4)

print("saved to grading suggestion to grading_suggestion.json")