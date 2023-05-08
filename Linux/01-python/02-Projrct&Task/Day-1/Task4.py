# define car systems and their data
systems = {
    "Engine": {
        "Fuel type": "Gasoline",
        "Cylinders": 4,
        "Horsepower": 180
    },
    "Transmission": {
        "Type": "Automatic",
        "Gears": 6,
        "Drive type": "Front-wheel drive"
    },
    "Brakes": {
        "Type": "Disc",
        "Front": "Ventilated",
        "Rear": "Solid"
    }
}

# get user input for car system
selected_system = input("Select a car system (Engine, Transmission, Brakes): ")

# check if selected system exists in the dictionary
if selected_system in systems:
    # print the data for the selected system
    print(f"{selected_system} data:")
    print(systems[selected_system])
else:
    print("Invalid system selection.")


















'''
# Set up the access token and graph API object
access_token = 'EAAHdcz0fx9kBAMyy1wFmbZCg1mZBOic3hBKR87woZCf8HzVGjyg1OCpJ4tOW8Nb2zItUIqW1VH7W32kgM5xbyqp5WwDQqf2TXXtlJhAb1ZCOqos4fR5H2mypYbdZB75Uv2YojEtresQrzUUGp8kjXOWg1W48KIrTh3k6YkNjKBlRWtMiqweqxYOELwc8tOe2jmGBKTU0iSJW0rDA1Lmj0'
fb = facebook.GraphAPI(access_token)

# Define the message and post it to Facebook
message = 'Hello, world!'
fb.put_object(parent_object='me', connection_name='feed', message=message)
'''