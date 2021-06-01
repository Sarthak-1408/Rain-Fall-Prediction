import streamlit as st
import pandas as pd 
import pickle
from PIL import Image
import numpy as np


# Create a title
st.title("Rain Fall Prediction")


def load_model():
    result = pickle.load(open("models/xgboost_model.pkl" , "rb"))
    return result
model = load_model()

# Create a MinTemp and MaxTemp option
col1 , col2 = st.beta_columns(2)
MinTemp = float(col1.number_input("Minimum Temperature"))
MaxTemp = float(col2.number_input("Maximum Temperature"))

# Create a Rainfall and Evaporation option
col3 , col4 = st.beta_columns(2)
Rainfall = float(col3.number_input("Rainfall"))
Evaporation = float(col4.number_input("Evaporation"))

# Create a Sunshine and windGustSpeed option
col5 , col6 = st.beta_columns(2)
Sunshine = float(col5.number_input("Sunshine"))
WindGustSpeed = col6.number_input("Wind Gust Speed")

# Create a WindSpeed9am and WindSpeed3pm option
col7 , col8 = st.beta_columns(2)
WindSpeed9am = float(col7.number_input("WindSpeed 9am"))
WindSpeed3pm = col8.number_input("WindSpeed 3pm")

# Create a humidity9am and humidity3pm option
col9 , col10 = st.beta_columns(2)
Humidity9am = float(col9.number_input("Humidity 9am"))
Humidity3pm = float(col10.number_input("Humidity 3pm"))

# Create a Pressure9am and Pressure3pm option
col11 , col12 = st.beta_columns(2)
Pressure9am = float(col11.number_input("Pressure 9am"))
Pressure3pm = float(col12.number_input("Pressure 3pm"))

# Create a Cloud9am and Cloud3pm option
col13 , col14 = st.beta_columns(2)
Cloud9am = float(col13.number_input("Cloud 9am"))
Cloud3pm = float(col14.number_input("Cloud 3pm"))

# Create a RainToday and WindGustDir
col15 , col16 = st.beta_columns(2)
RainToday = col15.selectbox("Rain Today" , ["Yes" , "No"])

if RainToday == "Yes":
    RainToday = 1

else:
    RainToday = 0


WindGustDir = col16.selectbox("WindGust Direction", ['NNW', 'NW', 'WNW', 'N', 'W', 'WSW', 'NNE',
                                            'S', 'SSW', 'SW', 'SSE','NE', 'SE', 'ESE', 'ENE', 'E'])
if WindGustDir == "NNW":
    WindGustDir = 1

elif WindGustDir == "NW":
    WindGustDir = 2

elif WindGustDir == "WNW":
    WindGustDir = 3

elif WindGustDir == "N":
    WindGustDir == 4

elif WindGustDir == "W":
    WindGustDir = 5

elif WindGustDir == "WSW":
    WindGustDir = 6

elif WindGustDir == "NNE":
    WindGustDir = 7

elif WindGustDir == "S":
    WindGustDir = 8

elif WindGustDir == "SSW":
    WindGustDir = 9

elif WindGustDir == "SW":
    WindGustDir = 10

elif WindGustDir == "SSE":
    WindGustDir = 11

elif WindGustDir == "NE":
    WindGustDir = 12

elif WindGustDir == "SE":
    WindGustDir = 13

elif WindGustDir == "ESE":
    WindGustDir = 14

elif WindGustDir == "ENE":
    WindGustDir = 15

else:
    WindGustDir = 16

    

# Create a WindDir9am and WindDir3pm option
col17 , col18 = st.beta_columns(2)

WindDir9am = col17.selectbox("Wind Direction 9am" , ['NNW','N','NW','NNE','WNW','W','WSW','SW',
                                                    'SSW', 'NE','S','SSE','ENE','SE','ESE','E'])
if WindDir9am == "NNW":
    WindDir9am = 1

elif WindDir9am == "N":
    WindDir9am = 2

elif WindDir9am == "NW":
    WindDir9am = 3

elif WindDir9am == "NNE":
    WindDir9am == 4

elif WindDir9am == "WNW":
    WindDir9am = 5

elif WindDir9am == "W":
    WindDir9am = 6

elif WindDir9am == "WSW":
    WindDir9am = 7

elif WindDir9am == "SW":
    WindDir9am = 8

elif WindDir9am == "SSW":
    WindDir9am = 9

elif WindDir9am == "NE":
    WindDir9am = 10

elif WindDir9am == "S":
    WindDir9am = 11

elif WindDir9am == "SSE":
    WindDir9am = 12

elif WindDir9am == "ENE":
    WindDir9am = 13

elif WindDir9am == "SE":
    WindDir9am = 14

elif WindDir9am == "ESE":
    WindDir9am = 15

else:
    WindDir9am = 16
    
WindDir3pm = col18.selectbox("Wind Direction 3pm" , ['NW','NNW','N','WNW','W','NNE','WSW','SSW',
                                                    'S','SW','SE','NE','SSE','ENE','E','ESE'])
if WindDir3pm == "NNW":
    WindDir3pm = 1

elif WindDir3pm == "N":
    WindDir3pm = 2

elif WindDir3pm == "NW":
    WindDir3pm = 3

elif WindDir3pm == "NNE":
    WindDir3pm == 4

elif WindDir3pm == "WNW":
    WindDir3pm = 5

elif WindDir3pm == "W":
    windDir3pm = 6

elif WindDir3pm == "WSW":
    WindDir3pm = 7

elif WindDir3pm == "SW":
    WindDir3pm = 8

elif WindDir3pm == "SSW":
    WindDir3pm = 9

elif WindDir3pm == "NE":
    WindDir3pm = 10

elif WindDir3pm == "S":
    WindDir3pm= 11

elif WindDir3pm == "SSE":
    WindDir3pm = 12

elif WindDir3pm == "ENE":
    WindDir3pm = 13

elif WindDir3pm == "SE":
    WindDir3pm = 14

elif WindDir3pm == "ESE":
    WindDir3pm = 15

else:
    WindDir3pm = 16
    
# Create a Location Option
Location = st.selectbox("Location" , ['Portland', 'Cairns', 'Walpole', 'Dartmoor', 'MountGambier',
                        'NorfolkIsland', 'Albany', 'Witchcliffe', 'CoffsHarbour', 'Sydney',
                        'Darwin', 'MountGinini', 'NorahHead', 'Ballarat', 'GoldCoast',
                        'SydneyAirport', 'Hobart', 'Watsonia', 'Newcastle', 'Wollongong',
                        'Brisbane', 'Williamtown', 'Launceston', 'Adelaide', 'MelbourneAirport',
                        'Perth', 'Sale', 'Melbourne', 'Canberra', 'Albury', 'Penrith',
                        'Nuriootpa', 'BadgerysCreek', 'Tuggeranong', 'PerthAirport', 'Bendigo',
                        'Richmond', 'WaggaWagga', 'Townsville', 'PearceRAAF', 'SalmonGums',
                        'Moree', 'Cobar', 'Mildura', 'Katherine', 'AliceSprings', 'Nhil',
                        'Woomera', 'Uluru'])

if Location == "Portland":
    Location = 1

elif Location == "Cairns":
    Location = 2

elif Location == "Walpole":
    Location = 3

elif Location == "Dartmoor":
    Location = 4

elif Location == "MountGambier":
    Location = 5 

elif Location == "NorfolkIsland":
    Location = 6

elif Location == "Albany":
    Location = 7

elif Location == "Witchcliffe":
    Location = 8 

elif Location == "CoffsHarbour":
    Location = 9

elif Location == "Sydney":
    Location = 10

elif Location == "Darwin":
    Location = 11

elif Location == "MountGinini":
    Location = 12

elif Location == "NorahHead":
    Location = 13 

elif Location == "Ballarat":
    Location = 14

elif Location == "GoldCoast":
    Location = 15

elif Location == "SydneyAirport":
    Location = 16

elif Location == "Hobart":
    Location = 17

elif Location == "Watsonia":
    Location = 18

elif Location == "Newcastle":
    Location = 19

elif Location == "Wollongong":
    Location = 20

elif Location == "Brisbane":
    Location = 21

elif Location == "Williamtown":
    Location = 22

elif Location == "Launceston":
    Location = 23

elif Location == "Adelaide":
    Location = 24

elif Location == "MelbourneAirport":
    Location = 25 

elif Location == "Perth":
    Location = 26

elif Location == "Sale":
    Location = 27

elif Location == "Melbourne":
    Location = 28

elif Location == "Canberra":
    Location = 29

elif Location == "Albury":
    Location = 30 

elif Location == "Penirth":
    Location = 31

elif Location == "Nuriootpa":
    Location = 32

elif Location == "BadgerysCreek":
    Location = 33

elif Location == "Tuggeranong":
    Location = 34

elif Location == "PerthAirport":
    Location = 35

elif Location == "Bendigo":
    Location = 36

elif Location == "Richmond":
    Location = 37

elif Location == "WaggaWagga":
    Location = 38

elif Location == "Townsville":
    Location = 39

elif Location == "PearceRAAF":
    Location  = 40

elif Location == "SalmonGums":
    Location = 41

elif Location == "Moree":
    Location = 42

elif Location == "Cobar":
    Location = 43

elif Location == "Mildura":
    Location = 44

elif Location == "Katherine":
    Location = 45

elif Location == "AliceSprings":
    Location = 46

elif Location == "Nhil":
    Location = 47

elif Location == "Woomera":
    Location = 48

else:
    location = 49


# Add rainy and sunny images
sunny_image = Image.open("images/sunny.jpg")
rain_image = Image.open("images/rain.jpg")


if st.button("Submit"):
    input_lst = np.array([[Location,MinTemp,MaxTemp,Rainfall,Evaporation,Sunshine,WindGustDir,WindGustSpeed,
                WindDir9am,WindDir3pm,WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am, Pressure3pm,Cloud9am,Cloud3pm,RainToday]])

    prediction = model.predict(input_lst)
    output = prediction
    if output == 0:
        st.image(sunny_image , width = 500)
        st.success("So Sad , Tomorrow is going to be Sunny day")

    else:
        st.image(rain_image , width=500)
        st.success("Tomorrow is going to be rainy day , So enjoy yourselves with a cup of coffee")
        

# Add the Developer Profile
st.write("\n")
st.title("Developer")

col19 , col20 = st.beta_columns([1,2])

profile_image = Image.open("images/profile-pic.png")
col19.image(profile_image , width = 190)

col20.write("""
        Hey there 🖐️,
        I'm sarthak sharma, a data science student, a self-taught programmer. I was working on Data science for more than 8 months, In this period I'm learning new kinds of stuff in day-to-day life and solve many machine learning and deep learning problems. When I was in my school I don't know what is machine learning and how can we teach machines to learn something but then I just saw an Elon musk interview on youtube about AI then I got an interest in machine learning.

        Always open for new opportunities 🙋‍♂️.
""")

# Add the Social Media Handles
st.write("\n")
st.title("Social Media")

# Linkdin Prfile
st.header("Linkdin")
st.write("[Sarthak_Sharma](https://www.linkedin.com/in/sarthak-sharma-5472aa1a0/)")

# Github Profile
st.header("Github")
st.write("[Sarthak-1408](https://www.linkedin.com/in/sarthak-sharma-5472aa1a0/)")

# Instagram Profile
st.header("Instagram")
st.write("[i_sarthakofficial](https://www.instagram.com/i_sarthakofficial/)")