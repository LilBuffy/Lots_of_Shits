from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError, VideoUnavailable
import re, os

# this time in full hd video.

save_path = r"FUCKING PATH" # example: C:\Users\...\Downloads

link = input("\nENTER YOUTUBE VIDEO LINK: ").strip()
clean_link = link.split("?")[0]

try:
    yt = YouTube(clean_link)
    print("\nVIDEO TITLE:", yt.title)

    # anti stupidity
    safe_title = re.sub(r'[<>:"/\\|?*]', '', yt.title) + ".mp4"

    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=save_path, filename=safe_title)

    print("\nDONE BRO. SAVED AT:", os.path.join(save_path, safe_title), "\n")

except RegexMatchError:
    print("\nYOU ENTERED INVALID YOUTUBE LINK YOU ABSOLUTE RETARD.\n")
except VideoUnavailable:
    print("\nVIDEO IS UNAVAILABLE GO FCK YOURSELF.\n")
except Exception as e:
    print("\nSOMETHING WENT WRONG LMAO:", e, "\n")
