from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError, VideoUnavailable
import re, os

print("\n [ -- YT TO VIDEO DOWNLOADER BY HITLER -- ]")

# THE PATH WHERE YOU WANT TO SAVE YOUR SHIT
# Example: C:\Users\Nignog\Downloads\python_niggies\soundtrip
save_path = r"#"  # SET THIS SHIT UP NOW OR I'LL TOUCH YOU

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

# Magic happens here :DDDDDDD
while True:
    link = input("\n[!] GIMME THE YOUTUBE LINK: ").strip()
    url = clean_url(link)

    if not url or not is_valid_url(url):
        print("\n[!] INVALID YOUTUBE LINK YOU SPECKY LITTLE SHIT\n")
        continue

    clean_link = url.split("?")[0]

    try:
        yt = YouTube(clean_link)
        print(f"\n[!] DOWNLOADING... VIDEO TITLE: {yt.title}")

        safe_title = re.sub(r'[<>:"/\\|?*]', '', yt.title) + ".mp4"
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=save_path, filename=safe_title)

        print(f"\n[!] SUCCESS! SAVED AT: {os.path.join(save_path, safe_title)}\n")
        print("[!] DAVAIIIII RETARD, YOU'RE DONE. EXITING...\n")
        break  # ONLY BREAKS WHEN SUCCESSFUL DOWNLOAD.!111!1

    except RegexMatchError:
        print("\nHEY RETARD, INVALID LINK FORMAT! TRY AGAIN!\n")
    except VideoUnavailable:
        print("\nTHIS VIDEO IS UNAVAILABLE, PICK ANOTHER ONE.\n")
    except Exception as e:
        print(f"\nSOMETHING WENT HORRIBLY WRONG, LOLZ: {e}\n")
        print("TRY AGAIN, RETARD!\n")
