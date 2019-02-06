import json
import time
from websocket import create_connection

ws = create_connection("ws://10.42.0.96:10100", subprotocols=["data-transfer-nortek"])
print("Connecting to DVL1000 via websocket...")
result = ws.recv()
print("Status: '%s'" % result)

try:
	while True:
		result = ws.recv()
		#print("Received '%s'" % result)

		#Parsing json
		theData = json.loads(result)
		
		#Alternating data each time data is recieved. Each with unique ID(4123 and 8219) and dataset. Using IF to sort this out
		#8219 seem to have additional information like Status, Speed of Sound, Temperature
		#More data if more modes of tracking is turned on IDs 4125 and 8221 belongs to Water Tracking mode.
		#IDs 4123 and 8219 belongs to Bottom Track mode.
		'''
		if theData["id"] == 4123:
			print("id: " + str(theData["id"]) + " Mode: " + theData["name"] + " time: " + theData["timeStampStr"])

			#Pressure
			print(theData["frames"][0]["inputs"][0]["name"] + "(" + str(theData["frames"][0]["inputs"][0]["min"]) + " - " + str(theData["frames"][0]["inputs"][0]["max"]) + ")" + ": " + str(theData["frames"][0]["inputs"][0]["lines"][0]["data"][0]) + " " + theData["frames"][0]["inputs"][0]["units"])
		'''	
		if theData["id"] == 8219:
			#Parsing Variables
			BottomID = theData["id"]
			BottomMode = theData["name"]
			BottomTime = theData["timeStampStr"]
			BottomStatus = theData["frames"][1]["inputs"][0]["lines"][0]["data"][0]
			
			#Speed of Sound variables
			BottomSpeedOfSoundMin = theData["frames"][2]["inputs"][0]["min"]
			BottomSpeedOfSoundMax = theData["frames"][2]["inputs"][0]["max"]
			BottomSpeedOfSoundUnit = theData["frames"][2]["inputs"][0]["units"]
			BottomSpeedOfSoundData = theData["frames"][2]["inputs"][0]["lines"][0]["data"][0]
			
			#Temperature varliables
			BottomTempMin = theData["frames"][3]["inputs"][0]["min"]
			BottomTempMax = theData["frames"][3]["inputs"][0]["max"]
			BottomTempUnit = theData["frames"][3]["inputs"][0]["units"]
			BottomTempData = theData["frames"][3]["inputs"][0]["lines"][0]["data"][0]
			
			#Pressure variables
			BottomPressureName = theData["frames"][4]["inputs"][0]["name"]
			BottomPressureMin = theData["frames"][4]["inputs"][0]["min"]
			BottomPressureMax = theData["frames"][4]["inputs"][0]["max"]
			BottomPressureData = theData["frames"][4]["inputs"][0]["lines"][0]["data"][0]
			BottomPressureUnit = theData["frames"][4]["inputs"][0]["units"]
			
			#Print Data---------
			print("id: " + str(BottomID) + ". Mode: " + BottomMode + ". Status: " + BottomStatus + ". Time: " + BottomTime)
			
			#Speed of sound
			print("Speed of Sound(" + str(BottomSpeedOfSoundMin) + " - " + str(BottomSpeedOfSoundMax) + "): " + str(BottomSpeedOfSoundData) + " " + BottomSpeedOfSoundUnit)
			
			#Temperature
			print("Temperature(" + str(BottomTempMin) + " - " + str(BottomTempMax) + "): " + str(BottomTempData) + " " + BottomTempUnit)
			
			#Pressure
			print(BottomPressureName + "(" + str(BottomPressureMin) + " - " + str(BottomPressureMax) + ")" + ": " + str(BottomPressureData) + " " + BottomPressureUnit)

		
		time.sleep(0.005)
except KeyboardInterrupt:
    pass


ws.close()
import json
import time
from websocket import create_connection

ws = create_connection("ws://10.42.0.96:10100", subprotocols=["data-transfer-nortek"])
print("Connecting to DVL1000 via websocket...")
result = ws.recv()
print("Status: '%s'" % result)

try:
	while True:
		result = ws.recv()
		#print("Received '%s'" % result)

		#Parsing json
		theData = json.loads(result)
		
		#Alternating data each time data is recieved. Each with unique ID(4123 and 8219) and dataset. Using IF to sort this out
		#8219 seem to have additional information like Status, Speed of Sound, Temperature
		#More data if more modes of tracking is turned on IDs 4125 and 8221 belongs to Water Tracking mode.
		#IDs 4123 and 8219 belongs to Bottom Track mode.
		'''
		if theData["id"] == 4123:
			print("id: " + str(theData["id"]) + " Mode: " + theData["name"] + " time: " + theData["timeStampStr"])

			#Pressure
			print(theData["frames"][0]["inputs"][0]["name"] + "(" + str(theData["frames"][0]["inputs"][0]["min"]) + " - " + str(theData["frames"][0]["inputs"][0]["max"]) + ")" + ": " + str(theData["frames"][0]["inputs"][0]["lines"][0]["data"][0]) + " " + theData["frames"][0]["inputs"][0]["units"])
		'''	
		if theData["id"] == 8219:
			#Parsing Variables
			BottomID = theData["id"]
			BottomMode = theData["name"]
			BottomTime = theData["timeStampStr"]
			BottomStatus = theData["frames"][1]["inputs"][0]["lines"][0]["data"][0]
			
			#Speed of Sound variables
			BottomSpeedOfSoundMin = theData["frames"][2]["inputs"][0]["min"]
			BottomSpeedOfSoundMax = theData["frames"][2]["inputs"][0]["max"]
			BottomSpeedOfSoundUnit = theData["frames"][2]["inputs"][0]["units"]
			BottomSpeedOfSoundData = theData["frames"][2]["inputs"][0]["lines"][0]["data"][0]
			
			#Temperature varliables
			BottomTempMin = theData["frames"][3]["inputs"][0]["min"]
			BottomTempMax = theData["frames"][3]["inputs"][0]["max"]
			BottomTempUnit = theData["frames"][3]["inputs"][0]["units"]
			BottomTempData = theData["frames"][3]["inputs"][0]["lines"][0]["data"][0]
			
			#Pressure variables
			BottomPressureName = theData["frames"][4]["inputs"][0]["name"]
			BottomPressureMin = theData["frames"][4]["inputs"][0]["min"]
			BottomPressureMax = theData["frames"][4]["inputs"][0]["max"]
			BottomPressureData = theData["frames"][4]["inputs"][0]["lines"][0]["data"][0]
			BottomPressureUnit = theData["frames"][4]["inputs"][0]["units"]
			
			#Print Data---------
			print("id: " + str(BottomID) + ". Mode: " + BottomMode + ". Status: " + BottomStatus + ". Time: " + BottomTime)
			
			#Speed of sound
			print("Speed of Sound(" + str(BottomSpeedOfSoundMin) + " - " + str(BottomSpeedOfSoundMax) + "): " + str(BottomSpeedOfSoundData) + " " + BottomSpeedOfSoundUnit)
			
			#Temperature
			print("Temperature(" + str(BottomTempMin) + " - " + str(BottomTempMax) + "): " + str(BottomTempData) + " " + BottomTempUnit)
			
			#Pressure
			print(BottomPressureName + "(" + str(BottomPressureMin) + " - " + str(BottomPressureMax) + ")" + ": " + str(BottomPressureData) + " " + BottomPressureUnit)

		
		time.sleep(0.005)
except KeyboardInterrupt:
    pass


ws.close()
