import yt_dlp
import os
import re

print("\n [ -- YT TO M4A DOWNLOADER BY HITLER -- ]")

# THE PATH WHERE YOU WANT TO SAVE YOUR SHIT
# Example: C:\Users\Nignog\Downloads\python_niggies\soundtrip
save_path = r"#" # SET THIS SHIT UP NOW OR I'LL TOUCH YOU

ydl_opts = {
    'format': 'bestaudio[ext=m4a]/bestaudio/best',
    'outtmpl': f'{save_path}/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
        'preferredquality': '192',
    }],
}

def clean_url(link):

    # Cleanup link
    link = link.strip()

    # Add https:// if missing
    if not re.match(r'^https?://', link):
        link = 'https://' + link

    # Common YouTube shorteners
    if 'youtu.be' in link or 'youtube.com' in link:
        return link
    return None

def is_valid_url(link):
    # Check if looks like a valid YouTube URL
    pattern = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'
    return re.match(pattern, link)

# Magic happens here :D
while True:
    
    url = input("\n[!] GIMME THE YOUTUBE LINK: ").strip()
    url = clean_url(url)

    if not url or not is_valid_url(url):
        print("\n[!] INVALID YOUTUBE LINK YOU SPECKY LITTLE SHIT\n")
        continue

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get("title", "Unknown Title")
            print(f"\n[!] GRABBING: {title}\n")

            ydl.download([url])
            print(f"\n[!] SUCCESSFULLY DOWNLOADED THIS SHIT: {title}")
            print(f"\n[!] FILE SAVED AT: {save_path}\n")
            print("[!] DAVAIIIII RETARD, YOU'RE DONE. EXITING...\n")
            break  # ONLY BREAKS WHEN SUCCESSFUL DOWNLOAD OK?

    except Exception as e:
        print(f"\n[!] HOLY FUCKING SHIT, SOMETHING WENT WRONG:\n{e}\n")
        print("\n[!] TRY AGAIN RETARD\n")
