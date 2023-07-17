import streamlit as st
import requests
import json

st.title("Hello Streamlit")

st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
response = requests.get("http://127.0.0.1:8083/hello")
st.write(str(response.content))

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
