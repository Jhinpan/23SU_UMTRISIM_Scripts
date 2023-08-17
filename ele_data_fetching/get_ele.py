import requests
from xml.etree import ElementTree
import matplotlib.pyplot as plt


def get_elevation(lat, long, units="Meters"):
    url = f"https://nationalmap.gov/epqs/pqs.php?x={long}&y={lat}&units={units}&output=xml"
    response = requests.get(url)
    tree = ElementTree.fromstring(response.content)
    elevation_element = tree.find(".//elevation")

    # Check if the elevation element was found
    if elevation_element is None:
        print(f"No elevation data found for coordinates ({lat}, {long})")
        return None

    return float(elevation_element.text)


# Replace these with a list of coordinates along your route
coordinates = [(42.2808, -83.7430), (42.3314, -83.0458)]  # example coordinates

elevations = [get_elevation(lat, long) for lat, long in coordinates]

# Plot the elevations
plt.plot(range(len(elevations)), elevations)
# plt.title("Elevation along I-94 from Ann Arbor to Detroit")
# plt.xlabel("Point along route")
# plt.ylabel("Elevation (meters)")

# Save the plot as a .tif file
plt.savefig("elevation_map.tif")
