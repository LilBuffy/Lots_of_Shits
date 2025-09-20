import yt_dlp # very important.

# this shit grabs a youTube link, then rips the audio straight into an .m4a file.

save_path = r"FUCKING PATH"  # example: C:\Users\...\Downloads

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{save_path}/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
        'preferredquality': '192',
    }],
}

url = "https://youtu.be/U06jlgpMtQs?si=ej_2yacEZBDY9jvt" # or url = input("gimme ur link")

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # extract fucking infos without downloading first
        info = ydl.extract_info(url, download=False)
        title = info.get("title", "Unknown Title")
        print(f"\nGrabbing: {title}\n")

        # now download
        ydl.download([url])
        print(f"\nDONE YOU SPECKY LITTLE SHIT. FILE SAVED AT: {save_path}\n")

except Exception as e:
    print(f"\nHOLY FUCK SOMETHING WENT WRONG: {e}\n")
