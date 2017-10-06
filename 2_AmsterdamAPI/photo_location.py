import requests
# documentation: http://docs.python-requests.org/en/master/

## request a photo from a certain location
# choose a location (for example of your house, or near the university),
# make sure it's on a road and find out the latitude and longitude.
# use this latitude and longitude to request a photo.
# save the photo the the hard disk, like we did before.
# HINT: look at https://api.data.amsterdam.nl/panorama/opnamelocatie/
# for accepted parameters
# HINT: look in the `requests` module documentation how to add parameters
# to a request
loc = {.....?}
response = requests.get(.....?, params=.....?)
response_dict = response.json()

# Lookup the image url, time, and coordiantes in the response 
# dictionary as you have done in the previous exercise.
url = .....?
time = .....?
latitude = .....?
longitude = .....?

# Save the url along with the coordinates to a csv file.
csv_file = open("photo_location.csv", "w")
# Write the column names in the first line
csv_file.write("url,lat,lon,time\n")
# Write the data to the csv file
csv_file.write(url + "," + str(latitude) + "," + str(longitude) + "," + time + "\n"))
csv_file.close()
