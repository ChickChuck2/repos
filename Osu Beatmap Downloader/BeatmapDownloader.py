import requests
import ChimuInfoBeatmap
from ChimuInfoBeatmap import Beatmaps
from ChimuInfoBeatmap import BeatmapName
import os
import json

if (os.path.isfile("Config.json") == False):
    print("Criado arquivo de configuração")

    data = {}

    with open("Config.json", "w") as outfile:
        json.dump(data, outfile)
    
    loop = True

    while loop == True:
        directory = input("coloque seu Osu/Songs Directory \n >>")
        Direc = os.path.isdir(directory)

        if Direc == False:
            print("Não é um directorio correto")
        if Direc == True:
            data["Directory"] = []
            data["Directory"].append(
                f"{directory}")
        
        with open("Config.json", "w") as outfile:
            json.dump(data, outfile, indent=4)
        loop = False
    

def Downloader():
    quantidadeDown = int(input("quantidade: "))
    ChimuInfoBeatmap.BeatmapInfo(quantidade= quantidadeDown)

    print("Beatmaps: ",len(Beatmaps))
    print(Beatmaps)

    for i in range(len(Beatmaps)):
        Url = f"https://api.chimu.moe/v1/download/{Beatmaps[i]}?n=1"
        request = requests.get(Url, allow_redirects=True)

        fname = f"{BeatmapName[i]}"

        BPname = (f"{fname}").replace("']", "")

        try:
            with open("Config.json") as json_file:
                data = json.load(json_file)
                for p in data["Directory"]:

                    print(f"baixando {BPname}")

                    open(f"{p}\{BPname}.osz", "wb").write(request.content)

        except:
            print("Erro na salvação do beatmap")

Downloader()