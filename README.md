# Rich Blox Presence 🎮

A lightweight Python script that detects when you are playing Roblox and displays your current game, server details, and a direct link to the game page on your Discord Rich Presence (RPC).

---

## Features

* **Real-Time Detection:** Automatically detects when `RobloxPlayerBeta.exe` starts up and fetches the game you are playing.
* **Rich Presence Details:** Displays the game's title, elapsed play time, and a clickable button to open the Roblox game page directly from Discord.
* **System Tray Integration:** Runs quietly in your system tray with a custom icon, featuring quick links and an easy exit option.

---

## Prerequisites & Dependencies

Make sure you have Python installed along with the required libraries. You can install them using `pip`:

```bash
pip install psutil requests pystray pillow pypresence
