# sqlalchemy-challenge
SQL Alchemy Homework

![surfs-up](https://user-images.githubusercontent.com/85430216/167292209-56a1ca00-5c2b-46eb-87c7-40ce48218928.png)


## Instructions

I have decided to treat myself to a long holiday vacation in Honolulu, Hawaii! To help with my trip planning, I have done some climate analysis on the area. The following sections outline the steps I took to accomplish this task.

### Part 1: Climate Analysis and Exploration

In this section I used Python and SQLAlchemy, ORM queries, Pandas, and Matplotlib to perform basic climate analysis and data exploration of my climate database. 

* I created a folder called Hawaii within the sqlalchemey-challenge repo

* I used the starter code to create a notebook called climate_analysis.ipynb to complete my climate analysis and data exploration.

* I used SQLAlchemy’s `create_engine` to connect to the hawaii.sqlite SQLite database in the Resources folder of the sqlalchemey-challenge repo.

* I used SQLAlchemy’s `automap_base()` to reflect my tables into classes and save a reference to those classes called `Station` and `Measurement`.

* I linked Python to the database by creating a SQLAlchemy session and closed out the session at the end of my notebook.


#### Precipitation Analysis

To perform an analysis of precipitation in the area, i have done the following:

#### Find the most recent date in the data set.
most_recent_date = session.query(func.max(Measurement.date)).first()

The most recent date is '2017-08-23'

#### Calculate the date one year from the last date in data set.
previous_year = dt.date(2017,8,23) - dt.timedelta(days=365)

#### Perform a query to retrieve the data and precipitation scores
result = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date>=previous_year).all()

#### Save the query results as a Pandas DataFrame and set the index to the date column
df1 = pd.DataFrame(result,columns=['date', 'precipitation'])

#### Sort the dataframe by date
df1 = df1.sort_values('date')

#### Use Pandas Plotting with Matplotlib to plot the data

df1.plot(x='date', y = 'precipitation', rot = 90, fontsize = 10)
plt.title("Last 12 months of precipitation data", fontsize=15)
plt.xlabel('Date', fontsize = 10)
plt.ylabel('Inches', fontsize= 10)
plt.legend(loc ="upper right", fontsize=10)
plt.tight_layout
plt.rcParams["figure.figsize"] = (20,20)
plt.savefig("Homework_Images/Last 12 months of precipitation data.png")
plt.show()

![Last 12 months of precipitation data](https://user-images.githubusercontent.com/85430216/167317977-c1cd74d1-9b3e-4255-84a0-5f0932a6634b.png)

#### Use Pandas to calcualte the summary statistics for the precipitation data
df1.describe()

![Summary_statistics](https://user-images.githubusercontent.com/85430216/167318036-ef57c763-1f09-43ab-a099-ffc1c775365c.PNG)


#### Station Analysis

To perform an analysis of stations in the area, i have done the following:

* Design a query to calculate the total number of stations in the dataset.

* Design a query to find the most active stations (the stations with the most rows).

    * List the stations and observation counts in descending order.

    * Which station id has the highest number of observations?

    * Using the most active station id, calculate the lowest, highest, and average temperatures.

    * **Hint:** You will need to use functions such as `func.min`, `func.max`, `func.avg`, and `func.count` in your queries.

* Design a query to retrieve the previous 12 months of temperature observation data (TOBS).

    * Filter by the station with the highest number of observations.

    * Query the previous 12 months of temperature observation data for this station.

    * Plot the results as a histogram with `bins=12`, as shown in the following image:

    ![station-histogram](Images/station-histogram.png)

* Close out the session.

- - -

### Part 2: Climate App

Design a Flask API based on the queries developed in the Climate Anaysis.

Using Flask to create the routes foloowing routes:

* `/`

    * Homepage.

    * List all available routes.

* `/api/v1.0/precipitation`

    * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

    * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

    * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

    * Query the dates and temperature observations of the most active station for the previous year of data.

    * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

    * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.

    * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than or equal to the start date.

    * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates from the start date through the end date (inclusive).


## Rubric

[Unit 10 Homework Rubric](https://docs.google.com/document/d/1gT29iMF3avSvJruKpcHY4qovP5QitgXePqtjC6XESI0/edit?usp=sharing)

- - -

## References

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, [https://doi.org/10.1175/JTECH-D-11-00103.1](https://doi.org/10.1175/JTECH-D-11-00103.1)

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
