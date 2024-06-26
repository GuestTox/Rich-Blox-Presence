import psutil, time, re, requests, pystray, webbrowser, threading
from PIL import Image
from pypresence import Presence

Client_ID = "1071175301402480722"
DiscordRPC = Presence(Client_ID)
DiscordRPC.connect()

cmdline = ""

icon = Image.open("icon.png")

def after_click(icon, query):
    global running
    if str(query) == "GuestTox's Website":
        webbrowser.open("https://guesttox.github.io")
    elif str(query) == "Exit":
        icon.stop()

icon = pystray.Icon("Roblox RPC", icon, "Roblox RPC", menu=pystray.Menu(
    pystray.MenuItem("GuestTox's Website", after_click),
    pystray.MenuItem("Exit", after_click)))

def run_icon():
    icon.run()

thread = threading.Thread(target=run_icon)
thread.start()

while True:
        if not thread.is_alive(): break
        for process in psutil.process_iter():
            if process.name() == "RobloxPlayerBeta.exe":
                print("working")
                try:
                    if cmdline != process.cmdline()[1]:
                        cmdline = process.cmdline()[1]

                        r = re.search(r'placeId%3D\d+', cmdline)
                        placeID = r.group(0)[10:]

                        r = requests.get(f"https://www.roblox.com/games/{placeID}/better-discovery")
                        placeName = str(re.search(r'<h1 class="game-name" title=".+">', r.text).group(0)[11:]).split('"')[2]

                        launctime = re.search(r'launchtime:\d+', cmdline)
                        launchtime = int(int(launctime.group(0)[11:]) / 1000)
                        DiscordRPC.update(
                            details="Playing Roblox",
                            state=f"Currently in {placeName}",
                            start=launchtime,
                            large_image="icon.png",
                            large_text="Roblox SDK by GuestTox",
                        )
                        
                        break
                except Exception as e:
                    if e is psutil.NoSuchProcess: pass
                    else: raise e
                break
        else:
            DiscordRPC.clear()