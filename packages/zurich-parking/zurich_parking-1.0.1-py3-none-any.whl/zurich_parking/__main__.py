import argparse
import zurich_parking
import zurich_parking.parking_helper as parking_helper
from argparse import Namespace


def main(args: Namespace):
    # Get URL from config file
    url = zurich_parking.URL

    if args.list:
        print(parking_helper.list_parkings(url))

    elif args.show:
        print(parking_helper.search_parking_spaces(url, args.show))

    elif args.version:
        print("zurich-parking version " + parking_helper.__version__)


if __name__ == "__main__":
    """Show available parkings in Zurich."""
    parser = argparse.ArgumentParser(description="Find available parking in the public parkings in Zurich.")
    parser.add_argument("-l", "--list", action="store_true", help="List all the parkings in Zurich.")
    parser.add_argument("-s", "--show", type=str, help="Show the parkings available in a specific parking.")
    parser.add_argument("-v", "--version", action="store_true", help="Get the version of parking-zurich.")

    args, unknown = parser.parse_known_args()
    main(args)
