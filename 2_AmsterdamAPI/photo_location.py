import requests
# documentation: http://docs.python-requests.org/en/master/
import fiona
from fiona.crs import from_epsg
# documentation: http://toblerity.org/fiona/manual.html


## request a photo from a certain location
    # choose a location (for example of your house, or near the university)
    # and find out the latitude and longitude.
    # use this latitude and longitude to request a photo.
    # save the photo the the hard disk, like we did before.
    # HINT: look at https://api.data.amsterdam.nl/panorama/opnamelocatie/
    # for accpeted parameters
    # HINT: look in the `requests` module documentation how to add parameters
    # to a request


## create a shapefile with the location of the photo using fiona
    # first define the coordinate reference system (CRS)
    # using the `from_epsg` function imported from `fiona.crs`.
    # HINT: the correct epsg code can be found using Google.
    # which coordinate reference system are we dealing with?
crs = 
    # Then define the schema. The schema defines how the shapefile
    # is structured. It defines the type of geometry and the
    # properties of each entry.
    # HINT: look in the `fiona` documentation
    # HINT: think of what properties we should save with the points
schema = 

    # Open a shapefile using fiona
    # HINT: use fiona.open(..)
    # HINT: pass in the schema and crs we created
shp_filepath = 'data\\photo_location.shp'
with fiona.open(shp_filepath, 'w', 'ESRI Shapefile',
                schema=schema, crs=crs) as shp:
    # write the point to the shapefile
    # HINT: pass in the geometry found in the response dictionary
    # HINT: pass in the properties found in the response dictionary
    # corresponding to the schema we defined
