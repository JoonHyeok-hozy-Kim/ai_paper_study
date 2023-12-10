* [Back to Dive into Deep Learning](../../main.md)

# 2.2 Data Processing

## 2.2.1 Reading the Dataset
#### Tech) Using pandas for csv file 
1. Create a csv file.
   ```python
   import os

   os.makedirs(os.path.join('..', 'data'), exist_ok=True)
   data_file = os.path.join('..', 'data', 'house_tiny.csv')
   with open(data_file, 'w') as f:
        f.write('''NumRooms,RoofType,Price
        NA,NA,127500
        2,NA,106000
        4,Slate,178100
        NA,NA,140000''')
   ```

2. Import pandas and load the dataset.
   ```python
   import pandas as pd
   data = pd.read_csv(data_file)
   print(data)
   ```
   ![](images/001.png)

<br>

#### Tech) Dealing with missing values.
In the previous example, the variable RoofType had two values, either "Slate" or NaN (not a number).    
- There are two heuristics to deal with NaN values.
  1. Discard the row or the column
  2. One Hot Encoding
     - i.e.) Change the variable in to binary variables.   
       |Before|After|
       |:----:|:---:|
       |RoofType = {Slate, NaN}| RoofType_Slate={True, False} <br> RoofType_Nan={True, False} |

- How to perform One hot encoding in pandas
  ```python
  inputs, target = data.iloc[:, 0:2], data.iloc[:, 2]
  inputs = pd.get_dummies(inputs, dummy_na=True)
  print(inputs)
  ```











<br>

* [Back to Dive into Deep Learning](../../main.md)