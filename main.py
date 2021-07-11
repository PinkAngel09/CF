import streamlit as st
import random

# my awesome functions
def to_celsius(fahrenheit):
    ###(32°F − 32) × 5/9 = 0°C

    '''
    (number) -> number

    Returns the number of celsius degrees equivalent to fahrenheit degreesdate.
    >>> to_celsius(32)
    0
    >>> to_celsius(212)
    100
    '''
    return (fahrenheit - 32) * (5 / 9)

def to_fahrenheit(celsius):
    ###(0°C × 9/5) + 32 = 32°F
    '''
    (number) -> number

    Returns the number of fahrenheit degrees equivalent to celsius degreesdate.
    >>> to_fahrenheit(0)
    32
    >>> to_fahrenheit(100)
    212
    '''
    return (celsius * (9 / 5)) + 32

emoji = [':heart:', ':orange_heart:', ':yellow_heart:',
         ':green_heart:', ':purple_heart:',
         ':blue_heart:', ':heartbeat:']

st.title("Celsius and Fahrenheit Conversion")
st.markdown("Author : AP")
st.markdown(f"{ random.choice(emoji)* 43}")
slide = st.slider('', min_value=-400, max_value=400, step=1, value=-40)
# st.text(slide)
cl = str(round(to_celsius(slide), 2))
fh = str(round(to_fahrenheit(slide), 2))
st.success(f"Celsius : {cl}")
st.success(f"Fahrenheit : {fh}")

st.markdown("--------")

col1, col2, col3, col4, col5, col6 = st.beta_columns(6)
with col1:
    lb = st.button('Like button')
with col2:
    db = st.button('Dislike button')
with col3:
    cb = st.button('Confusion button')
with col4:
    ab = st.button('Anger button')
with col5:
    hb = st.button('Happy button')
with col6:
    tmbb = st.button('Too many buttons button')

if lb:
    st.success('AP is awesome :heart:')
    st.balloons()
elif db:
    st.error('YOU SUCK :skull:')
elif cb:
    st.info('Huh? :confused:')
elif ab:
    st.error('*^@!$*!(!!@  :poop:')
elif hb:
    st.info('WOOWWW  :open_mouth:')
elif tmbb:
    st.info('WAYYYYYYY TOOO MANYY BUTTONS. CALM DOWN. :scream:')
else:
    lb = False


