from Library import *

attribute_set = {
    'Outlook':['Sunny', 'Overcast', 'Rain'],
    'Temperature':['Hot','Mild','Cool'],
    'Humidity':['High','Normal'],
    'Wind':['Weak','Strong'],
    # 'PlayTennis':['Yes','No']
}

# print(attribute_set)

data = [
    'Dl Sunny Hot High Weak No',
    'D2 Sunny Hot High Strong No',
    'D3 Overcast Hot High Weak Yes',
    'D4 Rain Mild High Weak Yes',
    'D5 Rain Cool Normal Weak Yes',
    'D6 Rain Cool Normal Strong No',
    'D7 Overcast Cool Normal Strong Yes',
    'D8 Sunny Mild High Weak No',
    'D9 Sunny Cool Normal Weak Yes',
    'Dl0 Rain Mild Normal Weak Yes',
    'Dl1 Sunny Mild Normal Strong Yes',
    'Dl2 Overcast Mild High Strong Yes',
    'Dl3 Overcast Hot Normal Weak Yes',
    'Dl4 Rain Mild High Strong No',
    ]

data_set = []
for d in data:
    ds = d.split()
    new_data = [{}, None]
    new_data[0]['Outlook']=ds[1]
    new_data[0]['Temperature']=ds[2]
    new_data[0]['Humidity']=ds[3]
    new_data[0]['Wind']=ds[4]
    new_data[1]=True if ds[5] == 'Yes' else False
    data_set.append(new_data)

# print(data_set)
# print(calculate_entropy(data_set))


# for attr in attribute_set.keys():
#     print('{} : {}'.format(attr, calculate_information_gain(attribute_set, data_set, attr)))

attributes = [k for k in attribute_set.keys()]
id3 = ID3Node(attribute_set, attributes, data_set)
print(id3)
id3.print_all()