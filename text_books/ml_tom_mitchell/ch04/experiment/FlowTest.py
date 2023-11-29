from Library import Data, Network

'''
Definition)
    - Data : 8 digit binary, only one digit with one and zero for others.

'''
# Parameter Settings
possible_dataset = []
for i in range(8):
    temp_data = Data(8)
    temp_x = [0 for _ in range(8)]
    temp_x[i] = 1
    temp_data._x = temp_x
    possible_dataset.append(temp_data)
for d in possible_dataset:
    print(d)


training_data_set = []

N = Network(8, 3)
print(N)