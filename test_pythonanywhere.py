import requests

def send_numbers_to_url(num1, num2):
    url = "http://lnr.pythonanywhere.com/add"
    payload = {"num1": num1, "num2": num2}

    try:
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            print("Numbers sent successfully!")
        else:
            print(f"Failed to send numbers. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
    return response

if __name__ == "__main__":
    num1 = 42
    num2 = 7
    response = send_numbers_to_url(num1, num2)
    print(response.content)
