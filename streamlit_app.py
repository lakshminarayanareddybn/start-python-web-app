import inspect
import streamlit as st

st.set_page_config(page_title="My Streamlit App")

# "with" notation
demo_option = None
with st.sidebar:
    demo_option = st.radio("Select the demo",
    ('Checkbox', 'Button', 'Radio', 'Selectbox', 'Multiselect', 'Slider', 'SelectSlider'))

    # if genre == 'Comedy':
    #     st.write('You selected comedy.')
    # else:
    #     st.write("You didn\'t select comedy.")


def demo_checkbox(st):
    st.header("Checkbox Sample!")

    # check box
    agree = st.checkbox('I agree')

    if agree:
        st.write('Great!')

def display_code(st, code):
    st.text_area("Code", code, height=400)

def demo_button(st):
    st.header("Button Sample!")
    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')

def demo_radio(st):
    st.header("Radio Sample!")
    genre = st.radio(
        "What\'s your favorite movie genre",
        ('Comedy', 'Drama', 'Documentary'))

    if genre == 'Comedy':
        st.write('You selected comedy.')
    else:
        st.write("You didn\'t select comedy.")
    
def demo_selectbox(st):
    st.header("Selectbox Sample!")

    option = st.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', option)

def demo_multiselect(st):
    st.header("Multiselect Sample!")

    options = st.multiselect(
        'What are your favorite colors',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])

    st.write('You selected:', options)

def demo_slider(st):
    st.header("Slider Sample!")

    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')

    st.header("Range slider Sample!")

    values = st.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0))
    st.write('Values:', values)

    st.header("Rangetime slider Sample!")
    from datetime import time

    appointment = st.slider(
        "Schedule your appointment:",
        value=(time(11, 30), time(12, 45)))
    st.write("You're scheduled for:", appointment)

    st.header("Datetime slider Sample!")
    from datetime import datetime

    start_time = st.slider(
        "When do you start?",
        value=datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm")
    st.write("Start time:", start_time)

def demo_select_slider(st):
    st.header("Select slider Sample!")

    color = st.select_slider(
        'Select a color of the rainbow',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
    st.write('My favorite color is', color)
    
    st.divider()

    st.header("Range Select slider Sample!")

    start_color, end_color = st.select_slider('Select a range of color wavelength',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
        value=('red', 'blue'))
    st.write('You selected wavelengths between', start_color, 'and', end_color)
    
if demo_option == 'Checkbox':
    demo_checkbox(st)
    display_code(st, str(inspect.getsource(demo_checkbox)))

if demo_option == 'Button':
    demo_button(st)
    display_code(st, str(inspect.getsource(demo_button)))

if demo_option == 'Radio':
    demo_radio(st)
    display_code(st, str(inspect.getsource(demo_radio)))
        
if demo_option == 'Selectbox':
    demo_selectbox(st)
    display_code(st, str(inspect.getsource(demo_selectbox)))

if demo_option == 'Multiselect':
    demo_multiselect(st)
    display_code(st, str(inspect.getsource(demo_multiselect)))

if demo_option == 'Slider':
    demo_slider(st)
    display_code(st, str(inspect.getsource(demo_slider)))

if demo_option == 'SelectSlider':
    demo_select_slider(st)
    display_code(st, str(inspect.getsource(demo_select_slider)))

st.header("Get data from Hari-ji website Sample!")
import requests
st.write(requests.get(url="http://hariharigg.pythonanywhere.com/?celsius=15"))