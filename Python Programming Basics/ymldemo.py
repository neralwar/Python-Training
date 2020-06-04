import yaml

with open('sample.yaml') as f:

    data = yaml.load(f, Loader=yaml.FullLoader)
    for sportitem in data['sports']:
        print(sportitem)

    print(data['hr'])



    
with open('sample.yml’, ‘a’) as outfile:
    yaml.dump('hr5: 100', outfile)

   

   
