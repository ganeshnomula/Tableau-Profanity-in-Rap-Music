# Tableau-Profanity-in-Rap-Music
This project is about visualizing profanity in Rap music with data available from 1985 to 2013

# Introduction
As we all know, a common ingredient in many rap lyrics is shameless profanity. No word is off limits. With f-bombs and assorted slurs streaming through popular music, it’s no shock that some people are up in arms against rap. Is it appropriate for them to be spitting profanity-laced lyrics to the world? 

The present condition of rap music today is something that is talked about in music and cinema industry. Many individuals including myself strongly believe that rap music has been deteriorating slowly since last 10 years. That is because the present rap/hip-hop artists depend exclusively on beat and not on great verses or meaningful lyrics. Which seems to be the loss of creative craftsmanship. In my view, the lyrics supported today have next to zero word play, and the level of vocabulary has been seriously dropped down and improper music language is eventually making it's way to common conversational language.

The dataset I have chosen for the project contains a comprehensive list of 14 most used profane words in different albums and songs by different artists from 1985 to 2013. Dataset has 2297 rows and 19 columns.

The Primary Objective is to extract a story out of the dataset to help music industry to understand about the insane rise of profane lanugage in the songs.The story contains descriptive analysis using various statistical visualizations of variables in the dataset. The following table gives metadata.

| __Column Name__  | __Description__ |
| ------------- | ------------- |
| Year  | Year of the Album/Song released from 1985-2013|
| Album  | Name of the Album  |
| Artist  | Name of the Artist  |
| Song  | Name of the Song  |
| F\*ck  | Number of times F\*ck is used |
| Sh\*t  | Number of times Sh\*t is used|
| B\*tch  | Number of times B\*tch is used |
| P\*ssy  | Number of times P\*ssy is used|
| Ho€  | Number of times Ho€ is used |
| N-Word  | Number of times N-Word is used|
| Homophobic | Number of times Homophobic is used |
| G-Damn  | Number of times G-Damn is used|
| Skeet  | Number of times Skeet is used |
| Tits  | Number of times Tits is used|
| C\*nt  | Number of times C\*nt is used |
| Ass  | Number of times Ass is used|
| Total  | Combined total of Number of times all the profane words used |
| City  | City Origin of Rapper/ Hip-Hop Band |
| State  | State Origin of Rapper/ Hip-Hop Band |

# Exploratory Analysis
As a avid music listener,I want to leverage opportunity in this class to be a great narrator of the data related to music. So, I decided I would analyze a music data for my project. To my surprise, I found this dataset through the list of datasets provided in class and it aligns perfectly well with my area of interest. The dataset comprised of many numerical variables along with three Designator variables and one Quantitative variable. The dataset is perfectly organized it has neither a null value nor any missing data. 

Although The dataset is already comprehensive I want to add an additional column showing the location of the Arist/Band is from. For this I want to use Python to scrape the locations of different artists or add the manually through a Google Search. By adding loation column I'm assuming to analyze about how a culture in a particular state can impact rappers. During this exploratory analysis I will try different combinations of variables to determine most and least profane artists along with many other insights.

The dataset will enable me to create interactive dashboards at the same time answering different cases/queries.
* Preliminary analysis should be done to find the frequency of profane words in folk songs in comparision with hip-hop.
* Further analysis involves finding the most profane word along with top artists using them.
* Detailed analysis should be done to find the sudden rise in use of profane words in the given 33 year range.
* Locating the artists on a Map and finding where more profane artists are from.

All the above mentioned are my primary targets to derive from the dataset. I will add few more insights along the way into dashboards creation.

# Explanatory Analysis
### Audience
The analysis of my data would be in general for anyone who intersts/loves music, rap songs and hip-hop bands.

### Relationship to the Audience
My role is assumed to be a Business Intelligence Analyst for Music Censorboard.

### Expectation from Audience
Through my analysis and data story, I'm expecting:
* To create a little concern in my audience over the music industry.
* Songwriters would minimize or avoid profane language rather be more meaningful. 

### Usage of my data to convey the point
Data wouldn’t make sense by just looking at it. Data has plenty of information to be conveyed once it is put into the right form.
I will be using the data in my dataset to state the rise of profane language in music industry and present that data visually my audience and bringing out a new perspective to my audience thus helping them to understand how profane language has taken a new default position.

# Resources
* http://www.besttickets.com/blog/wp-content/uploads/2013/12/Rap-Profanity-Data-Collective.csv - Profanity in Rap music from 1985 – 2013 Dataset
* https://nycdatascience.com/blog/student-works/analyzing-evolution-rap-music-1989-2016/
* http://lab.musixmatch.com/profanity_genres/#analysis
* https://consequenceofsound.net/2014/04/well-hot-damn-heres-a-breakdown-of-raps-most-profane-artists/
* https://www.besttickets.com/blog/rap-profanity/
