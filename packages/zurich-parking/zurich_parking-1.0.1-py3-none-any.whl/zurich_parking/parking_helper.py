import feedparser
import json

from zurich_parking.parking import Parking


def list_parkings(url: str) -> str:
    parkings = _parse_feed(url)
    parking_names = []
    for parking in parkings:
        parking_names.append(parking.name)
    return json.dumps(parking_names)

def search_parking_spaces(url: str, parking_name: str):
    parkings = _parse_feed(url)
    parking = _find_parking(parkings, parking_name)
    return parking

def _parse_feed(url: str) -> list:
    feed = feedparser.parse(url)
    parkings = list()

    for entry in feed["entries"]:
        parkings.append(Parking(
            name = entry["title"].split('/')[0].strip(),
            spaces = _extract_spaces(entry["summary"].split('/')[1].strip()),
            open = _extract_open(entry["summary"].split('/')[0].strip())
        ))
    return parkings

def _find_parking(parkings: list, search: str) -> Parking:
    for parking in parkings:
        if parking.name.lower().find(search.lower()) > -1:
            return(json.dumps(parking.__dict__))
    return 'Parking ' + search + ' not found in Zurich.'

def _extract_spaces(spaces_str: str) -> int:
    try: 
        return int(spaces_str) 
    except: 
        return 0

def _extract_open(open_str: str) -> bool:
    if open_str.lower() == 'open':
        return True
    return False


