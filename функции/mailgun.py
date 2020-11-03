import requests
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxd47ce8b5d237498e8e9c4575b76de136.mailgun.org/messages",
		auth=("api", "0ca6d751555536777235b571c180ff16-9b1bf5d3-01ef434a"),
		data={"from": "nazikkydyralieva@gmail.com",
			"to": ["maximneveraa@gmail.com",],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})
send_simple_message()