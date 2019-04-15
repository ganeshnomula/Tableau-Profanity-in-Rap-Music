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
artist_location('Big Pun', 'Bronx', 'New York')
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

# Exporting CSV
export_csv = df.to_csv('Profane_Music_Dataset_Final.csv')

"""'LL Cool J' 'Run DMC' 'Too $hort' 'World Class Wreckin Cru' '2 Live Crew'
 'Afrika Bambaataa' 'Beastie Boys' 'Boogie Down' 'Dana Dane' 'NWA'
 'Public Enemy' 'Eazy-E' 'Slick Rick' 'De La Soul' 'EPMD' 'Ghetto Boys'
 'Kool G Rap' 'A Tribe Called Quest' 'Brand Nubian' 'Gang Starr'
 'Ice Cube' 'Main Source' 'Diamond D' 'Dr. Dre' 'Pete Rock & CL Smooth'
 'Redman' 'KRS1' 'Snoop Dogg' 'Wu-Tang Clan' 'Common' 'Jeru The Damaja'
 'Nas' 'Notorious B.I.G.' 'Scarface' 'Goodie Mob' 'Mobb Deep' 'Raekwon'
 'The Roots' 'Tupac' 'Fugees' 'Jay-Z' 'Outkast' 'Busta Rhymes' 'O.C.'
 'Big Pun' 'Juvenile' 'Eminem' 'Mos Def' 'Ludacris' 'Nelly' 'Ja Rule'
 '50 Cent' 'Chingy' 'T.I.' 'D12' 'Kanye West' 'Madvillain' 'The Game'
 'Clipse' 'Ghostface Killah' 'Lupe Fiasco' 'UGK' 'Bun B' "Lil' Wayne"
 'Big Boi' 'Drake' 'Rick Ross' 'J. Cole' 'Jay-Z + Kanye' 'Kendrick Lamar'
 'Macklemore & Ryan Lewis' 'Schoolboy Q' 'Pusha T']
Jay-Z                      165
Eminem                     160
Kanye West                  92
Outkast                     86
Nas                         78
50 Cent                     75
T.I.                        71
Tupac                       71
De La Soul                  61
A Tribe Called Quest        58
Drake                       51
Raekwon                     44
Wu-Tang Clan                43
Common                      42
The Roots                   42
Notorious B.I.G.            42
Public Enemy                42
NWA                         38
Gang Starr                  37
Dr. Dre                     37
Lil' Wayne                  37
Snoop Dogg                  37
Ice Cube                    34
UGK                         34
Goodie Mob                  34
Kendrick Lamar              33
Mos Def                     32
Rick Ross                   29
Ludacris                    28
Kool G Rap                  26
                          ... 
J. Cole                     17
Pete Rock & CL Smooth       17
The Game                    17
Lupe Fiasco                 17
Big Boi                     16
Jay-Z + Kanye               16
Ja Rule                     16
Juvenile                    16
Brand Nubian                15
Nelly                       15
Mobb Deep                   15
KRS1                        14
Fugees                      14
O.C.                        14
Redman                      14
Chingy                      14
Diamond D                   13
Pusha T                     12
EPMD                        12
Eazy-E                      12
Slick Rick                  12
Clipse                      12
Jeru The Damaja             11
Scarface                    10
Main Source                 10
Ghetto Boys                 10
2 Live Crew                  6
Dana Dane                    5
Afrika Bambaataa             4
World Class Wreckin Cru      2"""











