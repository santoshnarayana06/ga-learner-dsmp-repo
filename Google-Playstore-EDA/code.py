# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#Code starts here
data = pd.read_csv(path)

data['Rating'].plot(kind = 'hist')

plt.show()

data = data[data['Rating'] <=5 ]

data['Rating'].plot(kind  = 'hist')
#Code ends here


# --------------
# code starts here

total_null = data.isnull().sum()

percent_null = (total_null/data.isnull().count())

missing_data = pd.concat([total_null,percent_null], axis = 1, keys = ['Total', 'Percent'])

print(missing_data)

#DROPPING THE NULL VALUES 
data.dropna(inplace = True)

total_null_1 =  data.isnull().sum()

percent_null_1 = (total_null_1/data.isnull().count())

missing_data_1 = pd.concat([total_null_1,percent_null_1], axis = 1, keys=['Total','Percent'])

# code ends here


# --------------

#Code starts here
plt.figure(figsize =(10,10))

cat = sns.catplot(x="Category" ,y="Rating", data = data, kind = "box", height =10 )

cat.set_xticklabels(rotation = 90)

plt.title("Rating vs Category [BoxPlot]", size = 20)




#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here


data['Installs'] = data['Installs'].str.replace(',','')
data['Installs'] = data['Installs'].str.replace('+','')

data['Installs'] = data['Installs'].astype(int)

le = LabelEncoder()

data['Installs'] = le.fit_transform(data['Installs'])

sns.regplot(x = "Installs" , y = "Rating" , color = "teal", data = data)

plt.title('Rating vs Installs [regplot]', size = 20)



#Code ends here



# --------------
#Code starts here

data['Price'] = data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype(float)

plt.figure(figsize = (20,20))

sns.regplot(x = "Price", y = "Rating", color = "orange" , data = data)

plt.title('Rating vs Price', size = 20)

#Code ends here


# --------------

#Code starts here

#Finding the length of unique genres
print( len(data['Genres'].unique()) , "genres")

#Splitting the column to include only the first genre of each app
data['Genres'] = data['Genres'].str.split(';').str[0]

#Grouping Genres and Rating
gr_mean=data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()

print(gr_mean.describe())

#Sorting the grouped dataframe by Rating
gr_mean=gr_mean.sort_values('Rating')

print(gr_mean.head(1))

print(gr_mean.tail(1))

#Code ends here



# --------------

#Code starts here

#Converting the column into datetime format
data['Last Updated'] = pd.to_datetime(data['Last Updated'])

#Creating new column having `Last Updated` in days
data['Last Updated Days'] = (data['Last Updated'].max()-data['Last Updated'] ).dt.days 

#Setting the size of the figure
plt.figure(figsize = (10,10))

#Plotting a regression plot between `Rating` and `Last Updated Days`
sns.regplot(x="Last Updated Days", y="Rating", color = 'lightpink',data=data )

#Setting the title of the plot
plt.title('Rating vs Last Updated [RegPlot]',size = 20)

#Code ends here


