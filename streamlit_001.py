import streamlit as st
import requests
import json

st.title("Hello Streamlit")
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data ={
    "operation":"+",
    "values":[
        3,
        4,
        5,
        6
    ]
}
response = requests.post("http://127.0.0.1:8082/math", data=json.dumps(data), headers=headers, timeout=20)
print(response.content)
st.write(response.content)
