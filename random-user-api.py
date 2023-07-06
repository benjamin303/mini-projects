import requests

def get_user_data():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    data = response.json()

    # Extract relevant information
    user = data["results"][0]
    gender = user["gender"]
    name = user["name"]["title"] + " " + user["name"]["first"] + " " + user["name"]["last"]
    location = user["location"]["city"] + ", " + user["location"]["country"]
    email = user["email"]
    username = user["login"]["username"]
    dob = user["dob"]["date"]
    phone = user["phone"]
    picture = user["picture"]["large"]

    # Print the extracted information
    print("Gender:", gender)
    print("Name:", name)
    print("Location:", location)
    print("Email:", email)
    print("Username:", username)
    print("Date of Birth:", dob)
    print("Phone:", phone)
    print("Picture URL:", picture)

get_user_data()