def bank(greetings: str) -> None:
	if greetings == "hello":
		print("$0")
	elif greetings[0] == "h":
		print("$20")
	else:
		print("$100")

greetings = input("Input Greeting: ").lower().split()[0].replace(",","")
bank(greetings)