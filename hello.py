#decorators
# create an @authenticated decorator that allows the function to run is user1 has 'valid' set to true:
user1 = {
	'name': 'sonia',
	'valid': True # changing this will either run or not the message_friends function.
}

def authenticated(fn):
	def wrapper(*args, **kwargs):
		if args[0]["valid"]:
			return fn(*args, **kwargs)
		else:
			return print("invalid user")
	return wrapper	

@authenticated
def message_friends(user):
	print("message has been sent")


message_friends(user1)