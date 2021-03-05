# py weather

import streamlit as st
import configparser
from include.st_wp_functions import (
    set_page_config,
    get_zipcode,
    get_location,
    remove_streamlit_menu,
)

# load in config.ini and set defaults
config = configparser.ConfigParser()
config.read("config.ini")
set_page_config(config["DEFAULT"]["app_name"], config["DEFAULT"]["favicon"])
remove_streamlit_menu(config["DEFAULT"]["remove_streamlit_menu"])
debug_log = config["DEFAULT"]["enable_debug_logging"]

# page title standup
st.title(config["DEFAULT"]["app_name"] + " " + config["DEFAULT"]["favicon"])
st.write("Location access will be requested or specify your location")

# this function powers custom JS to gather location & show data
get_location(debug_log)

# Manual Selection
if st.button("Specify Location"):
    get_zipcode(debug_log)
