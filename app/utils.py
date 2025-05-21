import pandas as pd

def load_data():
    benin = pd.read_csv('notebooks/benin_clean.csv')
    sierra_leone = pd.read_csv('notebooks/sierraleone_clean.csv')
    togo = pd.read_csv('notebooks/togo_clean.csv')
    
    benin['Country'] = 'Benin'
    sierra_leone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'
    
    return pd.concat([benin, sierra_leone, togo], ignore_index=True)
