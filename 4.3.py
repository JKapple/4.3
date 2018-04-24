#Average Rainfall
#By: Joe Kapple

# Declare variables to hold the total rainfall,
# monthly rainfall, average rainfall, the number
# of years, and the total number of months.
totalRainfall = 0.0
monthRainfall = 0.0
averageRainfall = 0.0
years = 0
totalMonths = 0

# Get number of years
num_years = int(input('Enter the number of years: '))

# Get rainfall by month
for year in range(num_years):
    print('For year ', year + 1, ':')
    for month in range(12):
        monthRainfall = float(input( \
            'Enter the rainfall amount for the month: '))
        # Add to total number of months
        totalMonths += 1
        # Add to total rainfall amount
        totalRainfall += monthRainfall

# Calculate the average rainfallji
averageRainfall = totalRainfall / totalMonths

print('For ', totalMonths, 'months')
print('Total rainfall: ', format(totalRainfall, '.2f'), 'inches')
print('Average monthly rainfall: ', format(averageRainfall, '.2f'), 'inches')
