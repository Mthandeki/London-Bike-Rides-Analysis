# Import pandas as a library
import pandas 

#Import zipfile library (used to extract the file downloaded from kaggle)
import zipfile

#Import kaggle library (used to download data from kaggle)
import kaggle

#donwload the dataset from kaggle using the Kaggle API
# !kaggle datasets download -d hmavrodiev/london-bike-sharing-dataset

# extract the file from the zip file
zipfile_name = 'London_Bike_dataset.zip'
with zipfile.ZipFile(zipfile_name, 'r') as file:
    file.extractall()

# read in csv file as a pandas dataframe
bikes = pd.read_csv("london_merged.csv")

# explore the data
bikes.shape     
