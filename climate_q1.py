import matplotlib.pyplot as plt
import sqlite3

# Connect to the database
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

# Fetch data from the database and populate lists
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")
data = cursor.fetchall()
Year, CO2, Temperature = zip(*data)  # Unzip the data into separate lists


# Create a figure with two subplots (2 rows, 1 column)
fig, (ax1, ax2) = plt.subplots(2, 1)

# Plot CO2 data in the first subplot
ax1.plot(Year, CO2, 'b--')
ax1.set_title("Climate Data")
ax1.set_ylabel("[CO2]")
ax1.set_xlabel("Year (decade)")

# Plot Temperature data in the second subplot
ax2.plot(Year, Temperature, 'r*-')
ax2.set_ylabel("Temp (C)")
ax2.set_xlabel("Year (decade)")

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()

# Save the figure
fig.savefig("co2_temp_1.png")

# Close the database connection
conn.close()
