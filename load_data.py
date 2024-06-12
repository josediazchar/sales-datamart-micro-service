
# ### Read data and create Dataframes
import pandas as pd
import json
import glob
import os
from datetime import date, datetime
from sqlalchemy import create_engine
from config import settings


def convert_dates_to_strings(dict):
    for key, value in dict.items():
        if isinstance(value, (date, datetime)):
            dict[key] = value.isoformat()

    return dict

def load_data():
    extracted_folder_path = "./data"
    parquet_files = glob.glob(os.path.join(extracted_folder_path, '*.parquet'))

    for parquet_file in parquet_files:
        chunk_data = pd.read_parquet(parquet_file)
        # #### Clean data

        
        # remove rows with missing  for key columns
        columns_to_check = ['KeyDate', 'KeyEmployee', 'KeyProduct', 'KeyStore', 'Amount']
        cleaned_data = chunk_data.dropna(subset=columns_to_check)

        
        # parse data types for keyDate, Amount and Qty
        cleaned_data['KeyDate'] = pd.to_datetime(cleaned_data['KeyDate'])
        cleaned_data['Amount'] = pd.to_numeric(cleaned_data['Amount'], errors='coerce')
        cleaned_data['Qty'] = pd.to_numeric(cleaned_data['Qty'], errors='coerce')


        
        # Remove any row for no numeric values on the column Amount
        cleaned_data = cleaned_data.dropna(subset=['Amount'])

        
        # Remove any row for no numeric values on the column Qty
        cleaned_data = cleaned_data.dropna(subset=['Qty'])

        
        # parse to str for key columns
        cleaned_data['KeyEmployee'] = cleaned_data['KeyEmployee'].astype(str)
        cleaned_data['KeyProduct'] = cleaned_data['KeyProduct'].astype(str)
        cleaned_data['KeyStore'] = cleaned_data['KeyStore'].astype(str)



        columns_to_convert = ['Tickets', 'Products', 'Customers', 'Employees', 'Stores', 'Divisions', 'Time', 'Cedis']
        for column in columns_to_convert:
            cleaned_data[column] = cleaned_data[column].apply(lambda x: json.dumps(convert_dates_to_strings(x)) if isinstance(x, dict) else x)
        

        engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

        cleaned_data.to_sql('salesdata', con=engine, if_exists='append')
