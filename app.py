import os

# username = "JATEEN"
# password = "1234567890"

username = os.environ['MY_USER']
password = os.environ['MY_PASS']

print("Running with user: %s" % username)
print("Running with password: %s" % password)