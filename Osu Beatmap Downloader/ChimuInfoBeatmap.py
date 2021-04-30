import requests

Beatmaps = []
BeatmapName = []

Url = f"https://api.chimu.moe/v1/search"
r = requests.get(Url, allow_redirects=True)

def BeatmapInfo(quantidade):

    BeatMapJson = r.json()

    BeatmapData = BeatMapJson["data"]
    for i in range(quantidade):
        try:
            BeatmapSets = BeatmapData[i]
            beatmapSet = BeatmapSets["ChildrenBeatmaps"]
            beatmaps = beatmapSet[1]

            BeatmapId = beatmaps["BeatmapId"]
            BeatmapDiff = beatmaps["DiffName"]
            BeatmapMode = beatmaps["Mode"]
            BeatmapBPM = beatmaps["BPM"]
            BeatmapOD = beatmaps["OD"]
            BeatmapCS = beatmaps["CS"]
            BeatmapHP = beatmaps["HP"]
            BeatmapTotalLength = beatmaps["TotalLength"]
            BeatmapHitLength = beatmaps["HitLength"]
            BeatmapPlaycount = beatmaps["Playcount"]
            BeatmapMaxCombo = beatmaps["MaxCombo"]
            BeatmapDifficultyRating = beatmaps["DifficultyRating"]
            BeatmapOsuFile = beatmaps["OsuFile"]
            BeatmapDownloadPath = beatmaps["DownloadPath"]

            DownloadPath = f"{BeatmapDownloadPath}".replace("/d/", "")
            FileName = f"{BeatmapOsuFile}".replace(".osu", "")

            print("")
            print(f"[BeatmapInfo]: {BeatmapId} {BeatmapOsuFile}")

            Beatmaps.append(DownloadPath)
            BeatmapName.append(FileName)
        except:
            print("Algo erradowwifk")