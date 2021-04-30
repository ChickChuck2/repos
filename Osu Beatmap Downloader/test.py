import requests
import random

Url = f"https://api.chimu.moe/v1/search"
r = requests.get(Url)

BeatmapJson = r.json()

for i in range(1):

    try:
        BeatmapData = BeatmapJson["data"]

        beaatsetsRandom = random.randint(0, 16)
        BeatmapSets = BeatmapData[beaatsetsRandom] #16

        beatmapSet = BeatmapSets["ChildrenBeatmaps"]
        
        randombeatss = random.randint(0,18)
        beatsss = beatmapSet[1] #18
        beatsetlen = len(beatsss)
    except:
        print("ohoho")

    print(beatsss)