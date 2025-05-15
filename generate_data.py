import random
import pandas as pd 
import numpy as np

id_1 = 8110 
id_2 = 8000
id_3 = 7497 
random_seed = id_1+id_2+id_3
random.seed(random_seed)
data_path="data.csv"
output_path="my_data.csv"

all_data=pd.read_csv(data_path) 
all_columns = all_data.columns.tolist()

target_column = 'smoking'  

all_columns.remove(target_column)

selected_columns = random.sample(all_columns, 10)

print(selected_columns) 
selected_columns = np.append(selected_columns, target_column)
sample_df = all_data[selected_columns].copy()
sample_df.to_csv(output_path)   
