import json
import random
from shapely.geometry import Point, Polygon
from faker import Faker

fake = Faker()

def generate_kingdom_name():
    kingdom_adjective = fake.word().capitalize()
    kingdom_noun = fake.word().capitalize()
    return f"The Kingdom of {kingdom_adjective} {kingdom_noun}"

def generate_king_name():
    first_name = fake.first_name_male()
    last_name = fake.last_name()
    return f"{first_name} {last_name}"

def generate_random_point():
    lon = random.uniform(-180, 180)
    lat = random.uniform(-90, 90)
    return Point(lon, lat)

def polygon_to_geojson(polygon):
    geojson = {
        "type": "Polygon",
        "coordinates": [
            [list(coord) for coord in polygon.exterior.coords]
        ]
    }
    return geojson

def generate_random_polygon(num_points=5):
    points = [generate_random_point() for _ in range(num_points)]
    # Ensure the first and last points are the same to close the polygon
    points.append(points[0])
    polygon = Polygon([[point.x, point.y] for point in points])
    return polygon_to_geojson(polygon)
