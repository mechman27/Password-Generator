import requests
from datetime import datetime
import smtplib
import time


PASSWORD = 'derpdwarjxweyhcw'
EMAIL = "mypythontest27@gmail.com"
MY_LAT = 40.735291 # Your latitude
MY_LONG = -111.911971 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def iss_nearby():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    time_now = datetime.now()
    if time_now >= sunset or time_now <= sunrise:
        return True
    
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if iss_nearby() and is_night():
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(EMAIL, PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="Subject: Look Up\n\nThe ISS is above you in the sky")


