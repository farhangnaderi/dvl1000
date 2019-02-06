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
			print("ID: " + str(BottomID) + ". Mode: " + BottomMode + ". Status: " + BottomStatus + ". Time: " + BottomTime)
			
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
			
		if theData["id"] == 8221:
			#Parsing Variables
			WaterID = theData["id"]
			WaterMode = theData["name"]
			WaterTime = theData["timeStampStr"]
			WaterStatus = theData["frames"][1]["inputs"][0]["lines"][0]["data"][0]
			
			#Speed of Sound variables
			WaterSpeedOfSoundMin = theData["frames"][2]["inputs"][0]["min"]
			WaterSpeedOfSoundMax = theData["frames"][2]["inputs"][0]["max"]
			WaterSpeedOfSoundUnit = theData["frames"][2]["inputs"][0]["units"]
			WaterSpeedOfSoundData = theData["frames"][2]["inputs"][0]["lines"][0]["data"][0]
			
			#Temperature varliables
			WaterTempMin = theData["frames"][3]["inputs"][0]["min"]
			WaterTempMax = theData["frames"][3]["inputs"][0]["max"]
			WaterTempUnit = theData["frames"][3]["inputs"][0]["units"]
			WaterTempData = theData["frames"][3]["inputs"][0]["lines"][0]["data"][0]
			
			#Pressure variables
			WaterPressureName = theData["frames"][4]["inputs"][0]["name"]
			WaterPressureMin = theData["frames"][4]["inputs"][0]["min"]
			WaterPressureMax = theData["frames"][4]["inputs"][0]["max"]
			WaterPressureData = theData["frames"][4]["inputs"][0]["lines"][0]["data"][0]
			WaterPressureUnit = theData["frames"][4]["inputs"][0]["units"]
			
			#Beam Velocity Variables
			WaterBeamVelMin = theData["frames"][5]["inputs"][0]["min"]
			WaterBeamVelMax = theData["frames"][5]["inputs"][0]["max"]
			WaterBeamVelUnit = theData["frames"][5]["inputs"][0]["units"]
			WaterBeamVel1Data = theData["frames"][5]["inputs"][0]["lines"][0]["data"][0]
			WaterBeamVel2Data = theData["frames"][5]["inputs"][0]["lines"][1]["data"][0]
			WaterBeamVel3Data = theData["frames"][5]["inputs"][0]["lines"][2]["data"][0]
			WaterBeamVel4Data = theData["frames"][5]["inputs"][0]["lines"][3]["data"][0]
			WaterBeamVel1Valid = theData["frames"][5]["inputs"][0]["lines"][0]["valid"]
			WaterBeamVel2Valid = theData["frames"][5]["inputs"][0]["lines"][1]["valid"]
			WaterBeamVel3Valid = theData["frames"][5]["inputs"][0]["lines"][2]["valid"]
			WaterBeamVel4Valid = theData["frames"][5]["inputs"][0]["lines"][3]["valid"]
			
			#Beam FOM Variables
			WaterBeamFomMin = theData["frames"][5]["inputs"][1]["min"]
			WaterBeamFomMax = theData["frames"][5]["inputs"][1]["max"]
			WaterBeamFomUnit = theData["frames"][5]["inputs"][1]["units"]
			WaterBeamFom1Data = theData["frames"][5]["inputs"][1]["lines"][0]["data"][0]
			WaterBeamFom2Data = theData["frames"][5]["inputs"][1]["lines"][1]["data"][0]
			WaterBeamFom3Data = theData["frames"][5]["inputs"][1]["lines"][2]["data"][0]
			WaterBeamFom4Data = theData["frames"][5]["inputs"][1]["lines"][3]["data"][0]
			WaterBeamFom1Valid = theData["frames"][5]["inputs"][1]["lines"][0]["valid"]
			WaterBeamFom2Valid = theData["frames"][5]["inputs"][1]["lines"][1]["valid"]
			WaterBeamFom3Valid = theData["frames"][5]["inputs"][1]["lines"][2]["valid"]
			WaterBeamFom4Valid = theData["frames"][5]["inputs"][1]["lines"][3]["valid"]
			
			#Beam Dist Variables
			WaterBeamDistMin = theData["frames"][5]["inputs"][2]["min"]
			WaterBeamDistMax = theData["frames"][5]["inputs"][2]["max"]
			WaterBeamDistUnit = theData["frames"][5]["inputs"][2]["units"]
			WaterBeamDist1Data = theData["frames"][5]["inputs"][2]["lines"][0]["data"][0]
			WaterBeamDist2Data = theData["frames"][5]["inputs"][2]["lines"][1]["data"][0]
			WaterBeamDist3Data = theData["frames"][5]["inputs"][2]["lines"][2]["data"][0]
			WaterBeamDist4Data = theData["frames"][5]["inputs"][2]["lines"][3]["data"][0]
			WaterBeamDist1Valid = theData["frames"][5]["inputs"][2]["lines"][0]["valid"]
			WaterBeamDist2Valid = theData["frames"][5]["inputs"][2]["lines"][1]["valid"]
			WaterBeamDist3Valid = theData["frames"][5]["inputs"][2]["lines"][2]["valid"]
			WaterBeamDist4Valid = theData["frames"][5]["inputs"][2]["lines"][3]["valid"]
			
			#XYZ Velocity Variables
			WaterXyzVelMin = theData["frames"][6]["inputs"][0]["min"]
			WaterXyzVelMax = theData["frames"][6]["inputs"][0]["max"]
			WaterXyzVelUnit = theData["frames"][6]["inputs"][0]["units"]
			WaterXyzVel1Data = theData["frames"][6]["inputs"][0]["lines"][0]["data"][0]
			WaterXyzVel2Data = theData["frames"][6]["inputs"][0]["lines"][1]["data"][0]
			WaterXyzVel3Data = theData["frames"][6]["inputs"][0]["lines"][2]["data"][0]
			WaterXyzVel4Data = theData["frames"][6]["inputs"][0]["lines"][3]["data"][0]
			WaterXyzVel1Valid = theData["frames"][6]["inputs"][0]["lines"][0]["valid"]
			WaterXyzVel2Valid = theData["frames"][6]["inputs"][0]["lines"][1]["valid"]
			WaterXyzVel3Valid = theData["frames"][6]["inputs"][0]["lines"][2]["valid"]
			WaterXyzVel4Valid = theData["frames"][6]["inputs"][0]["lines"][3]["valid"]
			
			#XYZ FOM Variables
			WaterXyzFomMin = theData["frames"][6]["inputs"][1]["min"]
			WaterXyzFomMax = theData["frames"][6]["inputs"][1]["max"]
			WaterXyzFomUnit = theData["frames"][6]["inputs"][1]["units"]
			WaterXyzFom1Data = theData["frames"][6]["inputs"][1]["lines"][0]["data"][0]
			WaterXyzFom2Data = theData["frames"][6]["inputs"][1]["lines"][1]["data"][0]
			WaterXyzFom3Data = theData["frames"][6]["inputs"][1]["lines"][2]["data"][0]
			WaterXyzFom4Data = theData["frames"][6]["inputs"][1]["lines"][3]["data"][0]
			WaterXyzFom1Valid = theData["frames"][6]["inputs"][1]["lines"][0]["valid"]
			WaterXyzFom2Valid = theData["frames"][6]["inputs"][1]["lines"][1]["valid"]
			WaterXyzFom3Valid = theData["frames"][6]["inputs"][1]["lines"][2]["valid"]
			WaterXyzFom4Valid = theData["frames"][6]["inputs"][1]["lines"][3]["valid"]
			
			
			#----------Print Data---------
			print("ID: " + str(WaterID) + ". Mode: " + WaterMode + ". Status: " + WaterStatus + ". Time: " + WaterTime)
			
			#Speed of sound
			print("Speed of Sound(" + str(WaterSpeedOfSoundMin) + " - " + str(WaterSpeedOfSoundMax) + "): " + str(WaterSpeedOfSoundData) + " " + WaterSpeedOfSoundUnit)
			
			#Temperature
			print("Temperature(" + str(WaterTempMin) + " - " + str(WaterTempMax) + "): " + str(WaterTempData) + " " + WaterTempUnit)
			
			#Pressure
			print(WaterPressureName + "(" + str(WaterPressureMin) + " - " + str(WaterPressureMax) + ")" + ": " + str(WaterPressureData) + " " + WaterPressureUnit)
			
			#Beam Velocity
			print("Beam Velocity(" + str(WaterBeamVelMin) + " - " + str(WaterBeamVelMax) + "): " + "1[" + str(WaterBeamVel1Valid) + "]:" + str(WaterBeamVel1Data) + " 2[" + str(WaterBeamVel2Valid) + "]:" + str(WaterBeamVel2Data) + " 3[" + str(WaterBeamVel3Valid) + "]:" + str(WaterBeamVel3Data) + " 4[" + str(WaterBeamVel4Valid) + "]:" + str(WaterBeamVel4Data) + " Unit: " + WaterBeamVelUnit)
			
			#Beam FOM
			print("Beam FOM(" + str(WaterBeamFomMin) + " - " + str(WaterBeamFomMax) + "): " + "1[" + str(WaterBeamFom1Valid) + "]:" + str(WaterBeamFom1Data) + " 2[" + str(WaterBeamFom2Valid) + "]:" + str(WaterBeamFom2Data) + " 3[" + str(WaterBeamFom3Valid) + "]:" + str(WaterBeamFom3Data) + " 4[" + str(WaterBeamFom4Valid) + "]:" + str(WaterBeamFom4Data))
			
			#Beam Dist
			print("Beam Dist(" + str(WaterBeamDistMin) + " - " + str(WaterBeamDistMax) + "): " + "1[" + str(WaterBeamDist1Valid) + "]:" + str(WaterBeamDist1Data) + " 2[" + str(WaterBeamDist2Valid) + "]:" + str(WaterBeamDist2Data) + " 3[" + str(WaterBeamDist3Valid) + "]:" + str(WaterBeamDist3Data) + " 4[" + str(WaterBeamDist4Valid) + "]:" + str(WaterBeamDist4Data) + " Unit: " + WaterBeamDistUnit)
			
			#XYZ Velocity
			print("XYZ Velocity(" + str(WaterXyzVelMin) + " - " + str(WaterXyzVelMax) + "): " + "1[" + str(WaterXyzVel1Valid) + "]:" + str(WaterXyzVel1Data) + " 2[" + str(WaterXyzVel2Valid) + "]:" + str(WaterXyzVel2Data) + " 3[" + str(WaterXyzVel3Valid) + "]:" + str(WaterXyzVel3Data) + " 4[" + str(WaterXyzVel4Valid) + "]:" + str(WaterXyzVel4Data) + " Unit: " + WaterXyzVelUnit)
			
			#XYZ FOM
			print("XYZ FOM(" + str(WaterXyzFomMin) + " - " + str(WaterXyzFomMax) + "): " + "1[" + str(WaterXyzFom1Valid) + "]:" + str(WaterXyzFom1Data) + " 2[" + str(WaterXyzFom2Valid) + "]:" + str(WaterXyzFom2Data) + " 3[" + str(WaterXyzFom3Valid) + "]:" + str(WaterXyzFom3Data) + " 4[" + str(WaterXyzFom4Valid) + "]:" + str(WaterXyzFom4Data) + " Unit: " + WaterXyzFomUnit)
			
			print("------")
			print(" ")
			
		
		time.sleep(0.005)
except KeyboardInterrupt:
    pass


ws.close()
