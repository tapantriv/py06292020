import requests
Mars= "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY"
def main():
    thisday= input("what dy you wanna see?")
    newMars= requests.get(f"{Mars}&sol={thisday[0]['photos']}")
    uri= newMars.json()
    print(uri)
main()