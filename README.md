# PyWeatherApp
A weather web application based on Streamlit &amp; OpenWeatherMap 
You will need an open weather map API key, found here - https://openweathermap.org/

# Quick Setup
1 - Install API key in config.ini \
2 - install requirements.txt if needed \
3 - Start the app with "streamlit run main.py" 

# Configuration
Here is what you can change in config.ini

[DEFAULT]
app_name // Name of app displayed on webpage\
favicon // emoji for favicon and appended to app name\
remove_streamlit_menu // streamlit has a menu that is unused in this app, by default this is removed\
enable_verbose_logging // raw api data will be displayed on page with response

[OPENWEATHERMAP]
api_key // api key for our open weather map account\
temp_units // unit of measurements for weather data. Default is imperial. Other options include "metric"
