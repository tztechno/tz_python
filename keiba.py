from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas as pd
import numpy as np
import argparse
import sys

def main(args):

    url = 'https://race.netkeiba.com/race/result.html?race_id='+args

    source = urllib.request.urlopen(url)
    soup = BeautifulSoup(source,'lxml')

    main_table=soup('table', class_="RaceTable01 RaceCommon_Table ResultRefund Table_Show_All")[0]

    head = []
    for i in range(len(main_table.find_all('th'))):
        head.append(main_table.find_all('th')[i].get_text())

    data=[]
    for d in range(len(main_table.find_all('td'))):
        data.append(main_table.find_all('td')[d].get_text())

    n=len(main_table.find_all('th'))
    data = [data[i:i+n] for i in range(0,len(data),n)]

    data_array=np.array(data)

    dataset= pd.DataFrame(data_array,columns=head)

    for col in dataset.columns:
        for i in range(len(dataset)):
            dataset.loc[i,col]=dataset.loc[i,col].replace('\n','').replace('\t','')
 
    dataset.to_csv(f'{args}.csv', index=False)
    print(f'Data exported')

    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        x = '202306050601'  
    elif len(sys.argv) == 2:
        try:
            x = str(sys.argv[1])
        except ValueError:
            print("Error: Please provide a valid integer for x.")
            sys.exit(1)
    else:
        print("Usage: python keiba.py [x]")
        sys.exit(1)

    main(x)
 
