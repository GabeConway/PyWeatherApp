# these are the functions for streamlit webpage generation

import openweathermapy.core as owm
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import pandas as pd
import configparser

# Load in config and set open weather api defaults
config = configparser.ConfigParser()
config.read("config.ini")
settings = {
    "APIKEY": config["OPENWEATHERMAP"]["api_key"],
    "units": config["OPENWEATHERMAP"]["temp_units"],
}


def remove_streamlit_menu(enabled):
    # this disables the streamlit menu
    if enabled == "1":
        hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def set_page_config(title, pageicon):
    st.set_page_config(page_title=title, page_icon=pageicon, layout="centered")


def get_location(verbose_log):
    loc_button = Button(label="Get Location")
    loc_button.js_on_event(
        "button_click",
        CustomJS(
            code="""
        navigator.geolocation.getCurrentPosition(
            (loc) => {
                document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
            }
        )
        """
        ),
    )
    result = streamlit_bokeh_events(
        loc_button,
        events="GET_LOCATION",
        key="get_location",
        refresh_on_update=False,
        override_height=75,
        debounce_time=0,
    )
    if result:
        if "GET_LOCATION" in result:
            raw = result.get("GET_LOCATION")
            location = (raw["lat"], raw["lon"])
            data = owm.get_current(location, **settings)
            weather_data_gen(data, verbose_log)


def get_zipcode(verbose_log):
    city = st.text_input("or enter your zip code (US Only) ")
    if city:
        data = owm.get_current(zip=city, **settings)
        weather_data_gen(data, verbose_log)


def weather_data_gen(data, verbose_log):
    locname = "your location: " + data["name"] + "," + data["sys"]["country"]
    currentcondition = "current condition: " + data["weather"][0]["description"]
    st.subheader(currentcondition)
    st.write(locname)
    st.write(f"Results in {settings.get('units')}")
    st.table(pd.DataFrame(data["main"], index=["result"]))
    if verbose_log == "1":
        st.write("RAW data")
        st.json(data)
