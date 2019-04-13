import pandas as pd


df = pd.read_csv('Final_Dataset.csv', header=0, encoding='unicode_escape')

occurences_artists = df.Artist.value_counts()


for row in df.Artist:
    if row == 'LL Cool J':
        df['Location'] =

print(occurences_artists['LL Cool J'])



# print(df.Artist)
# # if df['Artist'] == 'LL Cool J':
#     print('Success')

