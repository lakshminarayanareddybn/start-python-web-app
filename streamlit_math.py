import streamlit as st
import requests

ip_address =  "127.0.0.1"
port_number = "8083"

def main():
    st.title('Addition Calculator')

    num1 = st.number_input('Enter the first number:')
    num2 = st.number_input('Enter the second number:')

    if st.sidebar.button('Add'):
        operation = "add"

    if st.sidebar.button('Subtract'):
        operation = "subtract"

    if st.sidebar.button('Multiply'):
        operation = "multiply"

    if st.sidebar.button('Divide'):
        operation = "divide"

    response = send_request(num1, num2, operation)
    if response and response.status_code == 200:
        result = response.json()
        st.success(f"Result: {result['result']}")
    else:
        st.error('Error occurred during the API call.')

def send_request(num1, num2, operation):
    url = f"http://{ip_address}:{port_number}/{operation}"
    data = {
        "num1": num1,
        "num2": num2
    }

    try:
        response = requests.post(url, json=data)
        return response
    except requests.RequestException as e:
        st.error(f"Request error: {e}")
        return None

if __name__ == '__main__':
    main()
