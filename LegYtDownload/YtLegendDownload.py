from youtube_transcript_api import YouTubeTranscriptApi

videoID = "6bnaBnd4kyU"

dd = YouTubeTranscriptApi.get_transcript(videoID, languages=["en"])

print(dd)