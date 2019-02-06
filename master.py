import json
import time
from websocket import create_connection

#Websocket connection stuff. Make sure the websocket-client python library is installed.
ws = create_connection("ws://10.42.0.96:10100", subprotocols=["data-transfer-nortek"])
print("Connecting to DVL1000 via websocket...")
result = ws.recv()
print("Status: '%s'" % result)

try:
	while True:
		result = ws.recv()

		#Get JSON Data
		theData = json.loads(result)
		
		#Alternating data each time data is recieved. Each with unique ID(4123 and 8219) and dataset. Using IF to sort this out
		#8219 seem to have additional information like Status, Speed of Sound, Temperature
		#More data if more modes of tracking is turned on. IDs 4125 and 8221 belongs to Water Tracking mode.
		#IDs 4123 and 8219 belongs to Bottom Track mode.
		
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
			
			#Beam Velocity Variables
			BottomBeamVelMin = theData["frames"][5]["inputs"][0]["min"]
			BottomBeamVelMax = theData["frames"][5]["inputs"][0]["max"]
			BottomBeamVelUnit = theData["frames"][5]["inputs"][0]["units"]
			BottomBeamVel1Data = theData["frames"][5]["inputs"][0]["lines"][0]["data"][0]
			BottomBeamVel2Data = theData["frames"][5]["inputs"][0]["lines"][1]["data"][0]
			BottomBeamVel3Data = theData["frames"][5]["inputs"][0]["lines"][2]["data"][0]
			BottomBeamVel4Data = theData["frames"][5]["inputs"][0]["lines"][3]["data"][0]
			BottomBeamVel1Valid = theData["frames"][5]["inputs"][0]["lines"][0]["valid"]
			BottomBeamVel2Valid = theData["frames"][5]["inputs"][0]["lines"][1]["valid"]
			BottomBeamVel3Valid = theData["frames"][5]["inputs"][0]["lines"][2]["valid"]
			BottomBeamVel4Valid = theData["frames"][5]["inputs"][0]["lines"][3]["valid"]
			
			#Beam FOM Variables
			BottomBeamFomMin = theData["frames"][5]["inputs"][1]["min"]
			BottomBeamFomMax = theData["frames"][5]["inputs"][1]["max"]
			BottomBeamFomUnit = theData["frames"][5]["inputs"][1]["units"]
			BottomBeamFom1Data = theData["frames"][5]["inputs"][1]["lines"][0]["data"][0]
			BottomBeamFom2Data = theData["frames"][5]["inputs"][1]["lines"][1]["data"][0]
			BottomBeamFom3Data = theData["frames"][5]["inputs"][1]["lines"][2]["data"][0]
			BottomBeamFom4Data = theData["frames"][5]["inputs"][1]["lines"][3]["data"][0]
			BottomBeamFom1Valid = theData["frames"][5]["inputs"][1]["lines"][0]["valid"]
			BottomBeamFom2Valid = theData["frames"][5]["inputs"][1]["lines"][1]["valid"]
			BottomBeamFom3Valid = theData["frames"][5]["inputs"][1]["lines"][2]["valid"]
			BottomBeamFom4Valid = theData["frames"][5]["inputs"][1]["lines"][3]["valid"]
			
			#Beam Dist Variables
			BottomBeamDistMin = theData["frames"][5]["inputs"][2]["min"]
			BottomBeamDistMax = theData["frames"][5]["inputs"][2]["max"]
			BottomBeamDistUnit = theData["frames"][5]["inputs"][2]["units"]
			BottomBeamDist1Data = theData["frames"][5]["inputs"][2]["lines"][0]["data"][0]
			BottomBeamDist2Data = theData["frames"][5]["inputs"][2]["lines"][1]["data"][0]
			BottomBeamDist3Data = theData["frames"][5]["inputs"][2]["lines"][2]["data"][0]
			BottomBeamDist4Data = theData["frames"][5]["inputs"][2]["lines"][3]["data"][0]
			BottomBeamDist1Valid = theData["frames"][5]["inputs"][2]["lines"][0]["valid"]
			BottomBeamDist2Valid = theData["frames"][5]["inputs"][2]["lines"][1]["valid"]
			BottomBeamDist3Valid = theData["frames"][5]["inputs"][2]["lines"][2]["valid"]
			BottomBeamDist4Valid = theData["frames"][5]["inputs"][2]["lines"][3]["valid"]
			
			#XYZ Velocity Variables
			BottomXyzVelMin = theData["frames"][6]["inputs"][0]["min"]
			BottomXyzVelMax = theData["frames"][6]["inputs"][0]["max"]
			BottomXyzVelUnit = theData["frames"][6]["inputs"][0]["units"]
			BottomXyzVel1Data = theData["frames"][6]["inputs"][0]["lines"][0]["data"][0]
			BottomXyzVel2Data = theData["frames"][6]["inputs"][0]["lines"][1]["data"][0]
			BottomXyzVel3Data = theData["frames"][6]["inputs"][0]["lines"][2]["data"][0]
			BottomXyzVel4Data = theData["frames"][6]["inputs"][0]["lines"][3]["data"][0]
			BottomXyzVel1Valid = theData["frames"][6]["inputs"][0]["lines"][0]["valid"]
			BottomXyzVel2Valid = theData["frames"][6]["inputs"][0]["lines"][1]["valid"]
			BottomXyzVel3Valid = theData["frames"][6]["inputs"][0]["lines"][2]["valid"]
			BottomXyzVel4Valid = theData["frames"][6]["inputs"][0]["lines"][3]["valid"]
			
			#XYZ FOM Variables
			BottomXyzFomMin = theData["frames"][6]["inputs"][1]["min"]
			BottomXyzFomMax = theData["frames"][6]["inputs"][1]["max"]
			BottomXyzFomUnit = theData["frames"][6]["inputs"][1]["units"]
			BottomXyzFom1Data = theData["frames"][6]["inputs"][1]["lines"][0]["data"][0]
			BottomXyzFom2Data = theData["frames"][6]["inputs"][1]["lines"][1]["data"][0]
			BottomXyzFom3Data = theData["frames"][6]["inputs"][1]["lines"][2]["data"][0]
			BottomXyzFom4Data = theData["frames"][6]["inputs"][1]["lines"][3]["data"][0]
			BottomXyzFom1Valid = theData["frames"][6]["inputs"][1]["lines"][0]["valid"]
			BottomXyzFom2Valid = theData["frames"][6]["inputs"][1]["lines"][1]["valid"]
			BottomXyzFom3Valid = theData["frames"][6]["inputs"][1]["lines"][2]["valid"]
			BottomXyzFom4Valid = theData["frames"][6]["inputs"][1]["lines"][3]["valid"]
			
			
			#----------Print Data---------
			print("id: " + str(BottomID) + ". Mode: " + BottomMode + ". Status: " + BottomStatus + ". Time: " + BottomTime)
			
			#Speed of sound
			print("Speed of Sound(" + str(BottomSpeedOfSoundMin) + " - " + str(BottomSpeedOfSoundMax) + "): " + str(BottomSpeedOfSoundData) + " " + BottomSpeedOfSoundUnit)
			
			#Temperature
			print("Temperature(" + str(BottomTempMin) + " - " + str(BottomTempMax) + "): " + str(BottomTempData) + " " + BottomTempUnit)
			
			#Pressure
			print(BottomPressureName + "(" + str(BottomPressureMin) + " - " + str(BottomPressureMax) + ")" + ": " + str(BottomPressureData) + " " + BottomPressureUnit)
			
			#Beam Velocity
			print("Beam Velocity(" + str(BottomBeamVelMin) + " - " + str(BottomBeamVelMax) + "): " + "1[" + str(BottomBeamVel1Valid) + "]:" + str(BottomBeamVel1Data) + " 2[" + str(BottomBeamVel2Valid) + "]:" + str(BottomBeamVel2Data) + " 3[" + str(BottomBeamVel3Valid) + "]:" + str(BottomBeamVel3Data) + " 4[" + str(BottomBeamVel4Valid) + "]:" + str(BottomBeamVel4Data) + " Unit: " + BottomBeamVelUnit)
			
			#Beam FOM
			print("Beam FOM(" + str(BottomBeamFomMin) + " - " + str(BottomBeamFomMax) + "): " + "1[" + str(BottomBeamFom1Valid) + "]:" + str(BottomBeamFom1Data) + " 2[" + str(BottomBeamFom2Valid) + "]:" + str(BottomBeamFom2Data) + " 3[" + str(BottomBeamFom3Valid) + "]:" + str(BottomBeamFom3Data) + " 4[" + str(BottomBeamFom4Valid) + "]:" + str(BottomBeamFom4Data))
			
			#Beam Dist
			print("Beam Dist(" + str(BottomBeamDistMin) + " - " + str(BottomBeamDistMax) + "): " + "1[" + str(BottomBeamDist1Valid) + "]:" + str(BottomBeamDist1Data) + " 2[" + str(BottomBeamDist2Valid) + "]:" + str(BottomBeamDist2Data) + " 3[" + str(BottomBeamDist3Valid) + "]:" + str(BottomBeamDist3Data) + " 4[" + str(BottomBeamDist4Valid) + "]:" + str(BottomBeamDist4Data) + " Unit: " + BottomBeamDistUnit)
			
			#XYZ Velocity
			print("XYZ Velocity(" + str(BottomXyzVelMin) + " - " + str(BottomXyzVelMax) + "): " + "1[" + str(BottomXyzVel1Valid) + "]:" + str(BottomXyzVel1Data) + " 2[" + str(BottomXyzVel2Valid) + "]:" + str(BottomXyzVel2Data) + " 3[" + str(BottomXyzVel3Valid) + "]:" + str(BottomXyzVel3Data) + " 4[" + str(BottomXyzVel4Valid) + "]:" + str(BottomXyzVel4Data) + " Unit: " + BottomXyzVelUnit)
			
			#XYZ FOM
			print("XYZ FOM(" + str(BottomXyzFomMin) + " - " + str(BottomXyzFomMax) + "): " + "1[" + str(BottomXyzFom1Valid) + "]:" + str(BottomXyzFom1Data) + " 2[" + str(BottomXyzFom2Valid) + "]:" + str(BottomXyzFom2Data) + " 3[" + str(BottomXyzFom3Valid) + "]:" + str(BottomXyzFom3Data) + " 4[" + str(BottomXyzFom4Valid) + "]:" + str(BottomXyzFom4Data) + " Unit: " + BottomXyzFomUnit)
			
			print(" ")
		
		time.sleep(0.005)
except KeyboardInterrupt:
    pass


ws.close()
