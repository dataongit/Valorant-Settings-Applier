import requests
import os
import json
import base64
import warnings
warnings.filterwarnings(action='ignore')








def saveSettingslocal():
    lockfile_path = os.path.join(
        os.getenv('LOCALAPPDATA'), R'Riot Games\Riot Client\Config\lockfile')
    lockfile = open(lockfile_path)
    data = lockfile.read().split(':')
    headers = {
        "Authorization": "Basic " + base64.b64encode(('riot:' + data[3]).encode()).decode()
    }
    request = requests.get(
        "https://127.0.0.1:"+data[2]+"/player-preferences/v1/data-json/Ares.PlayerSettings", verify=False, headers=headers).json()
    data = request["data"]
    file = open("settings.json", "w")
    json.dump(data, file)
    file.close()
    lockfile.close()


def applySettings():
    settings_data = open("settings.json", "r")
    lockfile_path = os.path.join(
        os.getenv('LOCALAPPDATA'), R'Riot Games\Riot Client\Config\lockfile')
    lockfile = open(lockfile_path)
    data = lockfile.read().split(':')
    headers = {
        "Authorization": "Basic " + base64.b64encode(('riot:' + data[3]).encode()).decode()
    }
    request = requests.put("https://127.0.0.1:"+data[2]+"/player-preferences/v1/data-json/Ares.PlayerSettings",
                           verify=False, headers=headers, data=settings_data).json()
    
    lockfile.close()
    settings_data.close()


print('''
 ___       _    _    _        __ _            ___  _ __  _ __  _  _           
/ __| ___ | |_ | |_ (_) _ _  / _` | ___      /   \| '_ \| '_ \| |(_) ___  _ _ 
\__ \/ -_)|  _||  _|| || ' \ \__. |(_-/      | - || .__/| .__/| || |/ -_)| '_|
|___/\___| \__| \__||_||_||_||___/ /__/      |_|_||_|   |_|   |_||_|\___||_|  

''')

print("Your Valorant Settings got reset? Don't worry, this mini-app reapplies them and saves your current config if you decide to.")
print("Mode 1. Save your current settings")
print("Mode 2. Apply settings")
userinput = int(input("Please enter the mode number: "))

while 1 == 1:
    if userinput == 1:
         saveSettingslocal()
         print("Settings successfully saved!")
         quit()
    elif userinput == 2:
       applySettings()
       print("Settings successfully applied!")
       quit()
    else:
        print("Open VALORANT or enter the right number!")
        quit()
       



