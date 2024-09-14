# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

# Print out the number of rows and columns
print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

print("Literacy among women is a catalyst for empowerment and social changes. However, it has been a major issue over centuries, as women in several countries do not have access to this basic requirement. India and Pakistan are two such countries that have had a fluctuating relationship with women education over the past few years. Since they are neighboring countries, they may share a similar trend. ")

input("Press enter to keep reading")

print("Women in India and Pakistan living in poor households are less likely to receive education. According to some sources, women education has said to have progressed over the years. Increase in %of literate women has proved to be proportionate to the economic development of a country.")

print("Approximately 5-10% of households in India are below the poverty line while approximately 20% of households in Pakistan are below the poverty line. This could be a leading reason for the condition of lack of literacy in women. Another factor could be the education systems. Indian education system is highly ranked. One of Pakistan’s critical problems is their lack of good schools and colleges.")

input("Press enter to see the visuals")

print("Close the plot window to see the inference.")

# create a scatter plot
countryOneBool = lwd["country_name"]=='India'
countryTwoBool = lwd["country_name"]=='Pakistan'
countryOneData = lwd.loc[countryOneBool]
countryTwoData = lwd.loc[countryTwoBool]
      # 
plt.scatter(x = "year", y = "ED_litt_p", data= countryOneData, c = 'orange')
plt.scatter(x = "year", y = "ED_litt_p", data= countryTwoData, c = 'green')

plt.title("Literacy in Women over the Years")
plt.xlabel("Year")
plt.ylabel("% women who are literate")

plt.show()

print("The results give rise to the following questions:\nHas the major issue of women’s education been subsiding over the years or is it getting worse?\nIs quality of education offered by the country the driving force to this trend?\nHow is the trend going to be in the coming years at this rate?")