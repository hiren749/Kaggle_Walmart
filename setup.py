import os
from zipfile import ZipFile
from kaggle.api.kaggle_api_extended import KaggleApi


# Folders for Repos
if not os.path.isdir('./data'):
    os.mkdir('./data')
if not os.path.isdir('./code'):
    os.mkdir('./code')
if not os.path.isdir('./figures'):
    os.mkdir('./figures')
if not os.path.isdir('./sub'):
    os.mkdir('./sub')



api = KaggleApi()
api.authenticate()
comp = 'walmart-recruiting-store-sales-forecasting'
api.competition_download_files(comp, path = './data')

# Extract competition files
zf = ZipFile('./data/'+comp+'.zip', 'r')
zf.extractall('./data/')
os.remove('./data/walmart-recruiting-store-sales-forecasting.zip')

os.chdir('./data')
for file in os.listdir():
    print(file)
    if file.endswith('zip'):
        with ZipFile(file, 'r') as zipObj:
            zipObj.extractall()
        os.remove(file)
