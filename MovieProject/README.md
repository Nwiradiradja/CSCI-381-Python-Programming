# Movie Project
* Python
* Jupyter Notebook
* pandas
* matplot
* Anaconda

## Tasks
* Import and Explore Data
* Perform Data Cleansing
* Using Pandas to create Histograms for Distribution Analysis
* Creating Line Charts and Bar Charts to Visulization Time
* Using Pandas to Create Scatter Plot for Correlation Analysis

## Explanation
* Firstly I want to import pandas and load the data as seenn on image 1
* After loading and importing I want to review the data by checking the dataframe. I check rows and columns by the shape and I check the data types as well as seen on image 2. I am also able to check the individual columns for each row for an example genres
* Now to perform data cleansing I want to remove 3 columns. "movie_imdb_link", "num_critic_for_reviews" and "genre". To do so I first review the data as seen on image 3. Then i perform a data.drop with the axis as 1 for columns and establishing what column I want to drop as seen on image 4. I perform the same method for the other two columns as seen on image 5
* Now I want to check the data frame shape to ensure the columns were removed. As seen before we had 14 rows, after looking at image 6 you can see the column count dropped to 11
* To change the data type I'm going to create a variable and replace the type from float64 to Int64 as seen on image 6
* As seen on image 7, at the bottom next to "dtype:" the type has change to Int64
* I also want to rename some columns, gross -> movie_income and budget -> movie_budget As seen on image 8
* Performing data analysis I'm going to use different data visualization techniques. For my first analysis I'm going to check the distribution of the duration column. Essentially how long a movie is and how many movies fall under each duration. To do so I will be using a histogram as seen on image 9, I set the histogram to a variable "ax" so I can later make the chart look more detailed with labels. I also altered the bin and the size of the figure as well as removed the default grid to make the chart easier to read
* My next analysis is very similar to the previous, how ever I will be checking the count for movies with specific scores. Only difference here is the column and the size as well as the labels as seen on image 10
* For the next analysis I will not be using a chart, however I want to find movies that have a score less than 4. To do so I set the filtered data to a variable "low_score" and I can check the Low_score dataframe shape and as you can see the number of rows dropped tremendously as seen on image 11
* Now I want to continue with the usage of histogram and use this filtering concept to find movies that are produced in the USA and their respective score, and count them. As seen on image 12, I created a condition and implemented the same concept to create a histogram which produced the chart for scores for each USA movie in our dataset
* Conducting further analysis, I want to find which years had the highest and lowest number of movies. I can use a groupby function to find it as seen on image 13, however to perform data visualization I create a lune graph as seen on image 14
* Continuing with further analysis I want to find which years movies had the highest and lowest score. I used a groupby function again to see the numbers and year but I used a bar graph for visualization as seen on image 15
* I also wanted to find the min and max for movie budget, to do so I followed the same concept as before and change the parameters for the graph as seen on image 16
* Stepping away from visual graphs, I want to switch over to correlation analysis to figure out if a correlation exist between the movie IMDB score and the income it generated. I created a variable data_corr and set the data to the variable for score and income as seen on image 17
* Now before conducting correlation analysis I want to drop non value columns as seen on image 18
* To conduct correlation analysis I use a scatter plot using the the IMDB score and the movie income as seen on image 19
* After creating a visual for the analysis I created a correlation matrix as seen on image 20. Using the correlation matrix and seeing the value of .19 or 19%, it's safe to say that the movie income and it's score has no correlation

Image 1:

Image 2:

Image 3:

Image 4:

Image 5:

Image 6:

Image 7:

Image 8:

Image 9:

Image 10:

Image 11

Image 12:

Image 13:

Image 14:

Image 15:

Image 16:

Image 17:

Image 18:

Image 19:

Image 20:
