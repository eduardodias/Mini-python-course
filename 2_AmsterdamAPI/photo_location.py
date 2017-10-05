import requests
# documentation: http://docs.python-requests.org/en/master/
import fiona
from fiona.crs import from_epsg
# documentation: http://toblerity.org/fiona/manual.html


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

# Lookup the image url in the response dictionary
# as you have done in the previous exercise.
# Get the image in the same way as in the previous exercise
url = .....?
image_response = .......?
image = ......?

# Save the image to the hard disk. Again, look in the previous
# exercise how you did it.
filename = .......?
output_file = open(......?)
output_file.write(......?)
output_file.close()


## We are going to create a shapefile with the location of the photo using fiona
# first we need to define the coordinate reference system (CRS) and
# define how the shapefile is structured.
# The CRS we define using the from_epsg function provided by fiona. This 
# function sets the CRS using an EPSG code, which can be found online.
# In our case we are using WSG84. Lookup the EPSG code for WSG84 and
# enter it.
crs = from_epsg(.....?)
# Then we define the schema. The schema defines how the shapefile
# is structured. It defines the type of geometry and the
# properties of each entry.
# The geometry we need now is a Point. The properties we save with
# each point are the path to the image and the time the photo has
# been taken.
schema = {'geometry': 'Point',
          'properties': {'Path': 'str',
                         'DateTime': 'str'}}
# Next we open a shapefile using fiona and we pass in the schema and 
# CRS as we defined. 
shp = fiona.open('photo_location.shp', 'w', 'ESRI Shapefile', schema=schema, crs=crs)
# Now we write the data to the shapefile
# The coordinates are located in the response dictionary.
# You can use the variable explorer to see what's going on
# in the response dictionary.
shp.write({'geometry': response_dict['geometrie'],
           'properties': {'Path': 'file://' + 'C:/asdfasdf/asdfasdf......?' + filename,
                          'DateTime': response_dict['timestamp']}})
# Lastly we close the shapefile
shp.close()
