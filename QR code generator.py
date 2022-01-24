import pyqrcode,png
str="https://share.streamlit.io/nikhileshshah01/weather-forecasting/main/weather.py"
url=pyqrcode.create(str)
url.svg("weatherapp.svg",scale=8)
url.png("weatherapp.png",scale=6)
