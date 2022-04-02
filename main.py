import os
import json
import base64
import pathlib
import warnings
import requests

warnings.filterwarnings(action='ignore')


def saveSettingslocal():
    lockfile_path = pathlib.Path(os.getenv('LOCALAPPDATA')) / r'Riot Games\Riot Client\Config\lockfile'
    if not lockfile_path.is_file():
        raise RuntimeError('Lockfile not found')

    with open(lockfile_path, 'r') as lockfile:
        data = lockfile.read().split(':')
        headers = {
            "Authorization": "Basic " + base64.b64encode(('riot:' + data[3]).encode()).decode()
        }
        request = requests.get(
            "https://127.0.0.1:" + data[2] + "/player-preferences/v1/data-json/Ares.PlayerSettings", verify=False,
            headers=headers).json()
        data = request["data"]

        with open("settings.json", "w") as file:
            json.dump(data, file)


def applySettings():
    lockfile_path = pathlib.Path(os.getenv('LOCALAPPDATA')) / r'Riot Games\Riot Client\Config\lockfile'
    if not lockfile_path.is_file():
        raise RuntimeError('Lockfile not found')

    with open("settings.json", "r") as settings_data, open(lockfile_path, "r") as lockfile:
        data = lockfile.read().split(':')
        headers = {
            "Authorization": "Basic " + base64.b64encode(('riot:' + data[3]).encode()).decode()
        }
        requests.put("https://127.0.0.1:" + data[2] + "/player-preferences/v1/data-json/Ares.PlayerSettings",
                     verify=False, headers=headers, data=settings_data).json()


print(r'''
 ___       _    _    _        __ _            ___  _ __  _ __  _  _           
/ __| ___ | |_ | |_ (_) _ _  / _` | ___      /   \| '_ \| '_ \| |(_) ___  _ _ 
\__ \/ -_)|  _||  _|| || ' \ \__. |(_-/      | - || .__/| .__/| || |/ -_)| '_|
|___/\___| \__| \__||_||_||_||___/ /__/      |_|_||_|   |_|   |_||_|\___||_|  

''')

print(
    "Your Valorant Settings got reset? Don't worry, this mini-app reapplies them and saves your current config if you decide to.")
print("Mode 1. Save your current settings")
print("Mode 2. Apply settings")
userinput = int(input("Please enter the mode number: "))

while True:
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
