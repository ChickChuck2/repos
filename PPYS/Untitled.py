import requests
import random
import re
import json
import os

class Program():
    def Directory():

        if (os.path.isfile("Config.json") == False):
            data = {}

            with open("Config.json", "w") as outfile:
                json.dump(data, outfile)

            loop = True

            while loop == True:
                directory = input("Directory Osu Songs \n =>> ")
                Direc = os.path.isdir(directory)

                if Direc == False:
                    print("Este não é o directorio correto")
                    
                if Direc == True:
                    data["Directory"] = []
                    data["Directory"].append(
                        f"{directory}",)
                    
                    with open("Config.json", "w") as outfile:
                        json.dump(data, outfile, indent=4)
                    loop = False

        print("downloader")

        quantidade = int(input("Quantidade \n =>> "))

        for i in range(quantidade):
            set_id = random.randint(1, 9000)
            url = f"https://api.chimu.moe/v1/download/{set_id}?n=4"
            request = requests.get(url, allow_redirects=True)
            
            print (request.headers.get('content-type'))

            if(request.headers.get('content-type') == "application/json"):
                print("No beatmap")

            if (request.headers.get('content-type') == "application/zip"):

                d = request.headers['content-disposition'].replace(";", "\n").replace('"', '')
                fname = re.findall("filename=(.+)", d.replace("%20", " ") )[0]

                print(fname)
                with open ("Config.json") as json_file:

                    data = json.load(json_file)
                    for p in data["Directory"]:
                        open(f"{p}\{fname}", "wb").write(request.content)

    Directory()

