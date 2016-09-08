# we import the Twilio client from the dependency we just installed
from twilio.rest import TwilioRestClient

# the following line needs your Twilio Account SID and Auth Token
client = TwilioRestClient("ACa6f87a924f011ea4ee6b1c649a2d0224", "e0a0236184ddcec0206f1dc0e77a219a")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+918743038740", from_="+12015604580", body="Hello from Python!")

