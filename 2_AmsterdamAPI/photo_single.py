import requests
# documentation: http://docs.python-requests.org/en/master/

## request data
    # request data from the amsterdam panorama API
    # (url: https://api.data.amsterdam.nl/panorama/recente_opnames/2016/)
    # HINT: use the `get` function of the `requests` module
response = .....?
## We are going to create a python dictionary from the response
# To do this we use the .json method of the response object.
# json is a general web data sharing format and is structured 
# the exact same way a Python dictionary is (probably not by coincidence).
# Therefore we can use it to create a python dictionary.
response_dict = response.json()

## retrieve the image url
    # retrieve the url from the response dictionary
    # HINT: explore the dictionary using the variable explorer
    # available in spyder.
    # HINT: how do we get a value out of a dictionary?
url = response_dict['results'].....?
## request the image
    # use the image url to get the image
    # HINT: remember how we used the `requests` module to retrieve data from an url?
image_response = .....?

# The response we get through the requests module contains
# data and functions (like header information and for exmample the .json method we used before)
# That we do not need now. To get the actual data of the image (in bytes)
# we specify we want to content like so:
image = image_response.content

## save the image to the hard disk
    # save the image to the data/ directory
    # use the filename as defined in the response dictionary
filename = response_dict['results'].......?
    # HINT: remember how we wrote data to a file?
    # To write bytes to a file instead of text, use 'wb' instead of just 'w'
    # when opening the file.
output_file = open(filename, 'wb')
output_file.write(......?)
output_file.close()
