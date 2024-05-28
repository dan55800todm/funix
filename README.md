![funixpnghigh](https://github.com/dan55800todm/funix/assets/168951635/186ce756-edd3-4182-bb75-4fe6d2d6c1cc)
# Funix

Funix is ​​a lightweight command line interface (CLI) emulator that emulates basic Windows and Linux commands. (but also includes its own) It includes a lot of useful commands and a very simple text-based web browser. It is written in Python using libraries such as: sys, os, subprocess, requests, HTMLParser, platform, ctypes.

## Features

- Execute common CLI commands like `cls`, `echo`, `pwd`, and more.
- Simple text-based web browser to fetch and display web pages.
- Platform-specific commands like `ipconfig` for Windows.
- Ping websites directly from the Funix CLI.
- And much more.

## Installation

You can clone the repository...

   ```sh
   git clone https://github.com/dan55800todm/funix.git
```
# After installation...
Launch Funix with this command:
   ```sh
python Funix.py
```
Once you launch Funix, you will see something similar to this:
```plaintext
Welcome to Funix <version>
>
```
From here, you can start typing commands. For example:
```plaintext
> date
Current date: 2024-05-25

> echo(hello, funix!)
hello, funix!

> ping(google.com)
Pinging google.com with 32 bytes of data:
Reply from 142.250.190.78: bytes=32 time=24ms TTL=54
```
# Available commands
- `about` - Display information about Funix.
- `exit` - Exit the Funix emulator.
- `cls` **or** `clear` - Clear the screen.
- `say(text)` **or** `echo(text)` - Print the specified text.
- `date` - Display the current date.
- `pwd` - Print the current working directory.
- `rem` - Displays the contents of the current folder in which you are working.
- `ipconfig` - Display network configuration (platform-specific).
- `ping(host)` - Ping the specified host.
- `hostname` - Display the system's hostname.
- `whoami` - Display the current user's username.
- `time` - Display the current time.
- `help` - Display a list of available commands.
- `browser` - Open the Funix text-based browser.
- `df` - Returns information about available space on disks/partitions.
- `uptime` - Displays the current system uptime, as well as system load information, including average load for the last 1, 5 and 15 minutes.
- `tasklist` - Lists running processes on the system along with their PIDs, names, and other process information.
- `kill(PID)` - Used to terminate a process based on its PID. It sends a termination signal to the process, allowing it to exit gracefully.
- `shutdown` - Shuts down the computer using Funix.
- `reboot` - Reboots the computer from Funix.
- `systeminfo` - Displays computer information
- `netstat` - Displays active connections
# Keyboard shortcuts
- `CTRL + C` - Terminates an operation early (for example: netstat)
# Funix Browser
This is an example of how the browser works:
```plaintext
> browser
Welcome to Funix Browser!
Enter URL (type 'exit' to quit browser): https://example.com (or any other domain)
==================================================
Example Domain
This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.
==================================================
```
# Latest version
At the moment the latest version of Funix is ​​1.4

# License
This project is licensed under the MIT License.
