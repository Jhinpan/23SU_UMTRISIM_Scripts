import requests

# # Set up the parameters for the Overpass API query
# params = {
#     'data': '''
#         [out:xml];
#         (
#             node(42.21139,-83.78454,42.2425,-83.3264);
#             <;
#         );
#         out body;
#     '''
# }

# # Send the request to the Overpass API
# response = requests.get(
#     'http://overpass-api.de/api/interpreter', params=params)

# # Write the response to a .osm file
# with open('filtered_data.osm', 'w') as file:
#     file.write(response.text)

# Set up the parameters for the Overpass API query
params = {
    'data': '''
        [out:xml];
        way(42.21139,-83.78454,42.2425,-83.3264)["ref"="I 94"];
        (._;>;);
        out body;
    '''
}

# Send the request to the Overpass API
response = requests.get(
    'http://overpass-api.de/api/interpreter', params=params)

# Write the response to a .osm file
with open('filtered_data.osm', 'w') as file:
    file.write(response.text)
