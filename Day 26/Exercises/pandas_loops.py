import pandas as pd
musicians_dict={'name':['John','Paul','George', 'Ringo', 'The Beatles'],'score': [93,96, 99, 95, 99]}

musicians_df = pd.DataFrame(musicians_dict)


for (index, row) in musicians_df.iterrows():
    if row['name'] == 'The Beatles':
        print('This was a full band')
    print(row)
    print(row['name'])