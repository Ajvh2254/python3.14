import json

json_list = [] # store the converted json for each line
csv_file = open('csv_files.txt', 'r')

for line in csv_file.readlines():
    club, city, county = line.strip().split(',')
    data = {
        'club': club,
        'city': city,
        'country': county
    }
    json_list.append(data)

csv_file.close()

json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file) # writes json data to a file
json_file.close()
