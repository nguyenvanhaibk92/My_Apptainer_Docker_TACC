import json

# %%
with open('Meteorite_Landings.json') as f:
    ml_data = json.load(f)

type(ml_data)
type(ml_data['meteorite_landings'])
type(ml_data['meteorite_landings'][0])
type(ml_data['meteorite_landings'][0]['name'])

print(ml_data)
print(ml_data['meteorite_landings'])
print(ml_data['meteorite_landings'][0])
print(ml_data['meteorite_landings'][0]['name'])

# %% 
def compute_average_mass(a_list_of_dicts, a_key_string):
    total_mass = 0.
    for i in range(len(a_list_of_dicts)):
        total_mass += float(a_list_of_dicts[i][a_key_string])
    return (total_mass / len(a_list_of_dicts))


print(compute_average_mass(ml_data['meteorite_landings'], 'mass (g)'))

# %%
import json

data = {}
data['class'] = 'COE332'
data['title'] = 'Software Engineering and Design'
data['subjects'] = []
data['subjects'].append( {'unit': 1, 'topic': ['linux', 'python3', 'git']} )
data['subjects'].append( {'unit': 2, 'topic': ['json', 'csv', 'xml', 'yaml']} )

with open('class.json', 'w') as out:
    json.dump(data, out, indent=2)
# %%
