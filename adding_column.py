import pandas as pd


df = pd.read_csv('Final_Dataset.csv', header=0, encoding='unicode_escape')


occurences_artists = df.Artist.value_counts()  # counts number of times the artist name has appeared

# print('Before: ', df.Artist.unique())
# print('Before: ', occurences_artists)

def artist_location(artist_name, artist_city, artist_state):
    df.loc[df.Artist == artist_name, 'City'] = artist_city
    df.loc[df.Artist == artist_name, 'State'] = artist_state


artist_location('LL Cool J', 'Bay Shore', 'New York')
artist_location('Run DMC', 'New York', 'New York')
artist_location('Too $hort', 'Los Angeles', 'California')
artist_location('World Class Wreckin Cru', 'Compton', 'California')
artist_location('2 Live Crew', 'Miami', 'Florida')
artist_location('Afrika Bambaataa', 'The Bronx', 'New York')
artist_location('Beastie Boys', 'New York', 'New York')
artist_location('Boogie Down', 'The Bronx', 'New York')
artist_location('Dana Dane', 'Fort Greene', 'New York')
artist_location('NWA', 'Los Angeles', 'California')
artist_location('Public Enemy', 'Long Island', 'New York')
artist_location('Eazy-E', 'Compton', 'California')
artist_location('Slick Rick', 'The Bronx', 'New York')
artist_location('De La Soul', 'Long Island', 'New York')
artist_location('EPMD', 'Brentwood', 'New York')
artist_location('Ghetto Boys', 'Houston', 'Texas')
artist_location('Kool G Rap', 'Jamaica', 'New York')
artist_location('A Tribe Called Quest', 'St. Albans', 'New York')
artist_location('Brand Nubian', 'New Rochelle', 'New York')
artist_location('Gang Starr', 'Brooklyn', 'New York')
artist_location('Ice Cube', 'Baldwin Hills', 'California')
artist_location('Main Source', 'New York', 'New York')
artist_location('Diamond D', 'The Bronx', 'New York')
artist_location('Dr. Dre', 'Compton', 'California')
artist_location('Pete Rock & CL Smooth', 'Mount Vernon', 'New York')
artist_location('Redman', 'Newark', 'New Jersey')
artist_location('KRS1', 'The Bronx', 'New York')
artist_location('Snoop Dogg', 'Long Beach', 'California')
artist_location('Wu-Tang Clan', 'Staten Island', 'New York')
artist_location('Common', 'Chicago', 'Illinois')
artist_location('Jeru The Damaja', 'Brooklyn', 'New York')
artist_location('Nas', 'Brooklyn', 'New York')
artist_location('Notorious B.I.G.', 'Brooklyn', 'New York')
artist_location('Scarface', 'Houston', 'Texas')
artist_location('Goodie Mob', 'Atlanta', 'Georgia')
artist_location('Mobb Deep', 'Queens', 'New York')
artist_location('Raekwon', 'Staten Island', 'New York')
artist_location('The Roots', 'Philadephia', 'Pensylvania')
artist_location('Tupac', 'Harlem', 'New York')
artist_location('Fugees', 'South Orange', 'New Jersey')
artist_location('Jay-Z', 'Brooklyn', 'New York')
artist_location('Outkast', 'Atlanta', 'Georgia')
artist_location('Busta Rhymes', 'Brooklyn', 'New York')
artist_location('O.C.', 'Brooklyn', 'New York')
artist_location('Big Pun', 'The Bronx', 'New York')
artist_location('Juvenile', 'New Orleans', 'Louisiana')
artist_location('Eminem', 'St. Joseph', 'Missouri')
artist_location('Mos Def', 'Brooklyn', 'New York')
artist_location('Ludacris', 'Atlanta', 'Georgia')
artist_location('Nelly', 'Austin', 'Texas')
artist_location('Ja Rule', 'Queens', 'New York')
artist_location('50 Cent', 'Jamaica', 'New York')
artist_location('Chingy', 'St. Louis', 'Missouri')
artist_location('T.I.', 'Atlanta', 'Georgia')
artist_location('D12', 'Detroit', 'Michigan')
artist_location('Kanye West', 'Atlanta', 'Georgia')
artist_location('Madvillain', 'Long Beach', 'California')
artist_location('The Game', 'Compton', 'California')
artist_location('Clipse', 'Virginia Beach', 'Virginia')
artist_location('Ghostface Killah', 'Staten Island', 'New York')
artist_location('Lupe Fiasco', 'Chicago', 'Illinois')
artist_location('UGK', 'Port Arthur', 'Texas')
artist_location('Bun B', 'Port Arthur', 'Texas')
artist_location("Lil' Wayne", 'New Orleans', 'Louisiana')
artist_location('Big Boi', 'Savannah', 'Georgia')
artist_location('Drake', 'Ontario', 'Canada')
artist_location('Rick Ross', 'Carol City', 'Florida')
artist_location('J. Cole', 'Fayetteville', 'North Carolina')
artist_location('Jay-Z + Kanye', 'Brooklyn/Atlanta', 'New York/Georgia')
artist_location('Kendrick Lamar', 'Compton', 'California')
artist_location('Macklemore & Ryan Lewis', 'Seattle', 'Washington')
artist_location('Schoolboy Q', 'Los Angeles', 'California')
artist_location('Pusha T', 'New York', 'New York')


print(df.State.unique())
print(df.State.value_counts())

print(df.head())

# Exporting Excel File for Tableau
export_excel = df.to_excel('Profane_Music_Dataset_Final.xlsx', index=False)











