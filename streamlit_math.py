import streamlit as st
import requests

ip_address =  "lnr.pythonanywhere.com"
# port_number = "8083"

def main():
    st.title('Calculator')

    num1 = st.number_input('Enter the first number:')
    num2 = st.number_input('Enter the second number:')

    operation = None
    if st.sidebar.button('Add'):
        operation = "add"

    if st.sidebar.button('Subtract'):
        operation = "subtract"

    if st.sidebar.button('Multiply'):
        operation = "multiply"

    if st.sidebar.button('Divide'):
        operation = "divide"

    if st.sidebar.button('Table'):
        operation = "table"
        st.write("Ignoring Second number!!")
        st.subheader(f"Table for {int(num1)}")
        num2 = 0

    if operation:
        st.write(f"Calling send_request API with {num1}, {num2}, {operation}")
        response = send_request(num1, num2, operation)
        if response and response.status_code == 200:
            result = response.json()
            if isinstance(result['result'], list):
                for item in result['result']:
                    st.write(str(int(item)))
            else:
                st.success(f"Result: {result['result']}")
        else:
            st.error('Error occurred during the API call.')
    else:
        st.warning('Enter input values and select the operation')

def send_request(num1, num2, operation):
    url = f"http://{ip_address}/{operation}"
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
