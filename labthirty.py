#!/usr/bin/python3
import webbrowser

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"


def main():
    ## first I want to grab my credentials
    webbrowser.open("data:".format(NASAAPI,"r")) as mycreds
    nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=4mJpdZb7vpfGQGH2KWWXYd0QFGhpJfh4Jow1gTpL" + nasacreds.strip("\n")

    ## make a call to NASAAPI with our key
    apodresp = requests.get(NASAAPI + nasacreds)

    ## strip off json
    apod = apodresp.json()

    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])


if __name__ == "__main__":
    main()