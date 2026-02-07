import pandas as pd
import pyspark

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
print(df)

def increment(x):
    return x + 1

df['col1'] = df['col1'].apply(increment)


'''
OR
To change all the column values in dataframe 
df = df.apply(increment)
'''

print(df)

# for big data
# Example Spark setup

sc = pyspark.SparkContext()

rdd = sc.parallelize([1, 2, 3])
print(rdd.collect())

# ----------------------------------------------------------------

# Create virtual environment 
python3 -m venv my_env

# Activate virtual environment
source my_env/bin/activate 

# Install packages to virtual environment
pip install pandas

# List packages installed in environment
pip list 

# Save installed packages to requirements file
pip freeze > requirements.txt

# Deactivate virtual environment 
deactivate

# To set up an empty environment.
source setup-env.sh

# To Upgrade to the latest version:
pip install requests --upgrade
