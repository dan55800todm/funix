import sys
import os
import ctypes
import requests
from datetime import datetime
from html.parser import HTMLParser
import platform
import subprocess
import signal

os.system("chcp 65001 > nul")

class Funix:
    def __init__(self):
        self.commands = {
            "about": self.about,
            "exit": self.exit,
            "cls": self.clear_screen,
            "clear": self.clear_screen,
            "say": self.say,
            "date": self.show_date,
            "rem": self.rem,
            "echo": self.echo,
            "pwd": self.print_working_directory,
            "ipconfig": self.show_ip_config,
            "ping": self.ping,
            "browser": self.open_browser,
            "hostname": self.show_hostname,
            "whoami": self.show_username,
            "time": self.show_time,
            "help": self.show_help,
            "df": self.show_disk_usage,
            "uptime": self.show_uptime,
            "tasklist": self.list_tasks,
            "kill": self.kill_task,
            "shutdown": self.shutdown,
            "reboot": self.reboot,
            "systeminfo": self.show_system_info,
            "netstat": self.show_netstat,
        }
        self.parser = HTMLTextParser()
        self.operation_in_progress = False
        self.signal_handler = SignalHandler(self.operation_in_progress)

    def about(self, _):
        print("Funix 1.4 a simple command-line interface emulator.")
        print("Developed to provide basic CLI functionalities in a simulated environment.")
        print("Features include:")
        print("- Navigation and file operations (e.g., pwd, rem, etc.)")
        print("- Network tools (e.g., ping, ipconfig, etc.)")
        print("- System information (e.g., date, time, hostname, etc.)")
        print("- Basic text-based web browser")
        print("- More commands and features to explore!")
        print("\nDeveloped by: dan55800todm")
        print("Version: 1.4")
        print("GitHub: https://github.com/dan55800todm/funix")
        print("For more information, use the 'help' command.")

    def exit(self, _):
        print("Exiting the application...")
        self.signal_handler.restore_original_sigint_handler()
        sys.exit()

    def clear_screen(self, _):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def say(self, text):
        print(text)

    def show_date(self, _):
        current_time = datetime.now()
        print("Current date:", current_time.strftime("%Y-%m-%d"))

    def rem(self, argument):
        files = os.listdir(argument if argument else '.')
        print("Directory contents:")
        for file in files:
            print(file)

    def echo(self, text):
        print(text)

    def print_working_directory(self, _):
        print("Current working directory:", os.getcwd())

    def show_ip_config(self, _):
        if os.name == 'nt':
            os.system('ipconfig')
        else:
            os.system('ifconfig')

    def ping(self, host):
        self.operation_in_progress = True
        if host:
            response = os.system(f"ping {host}")
            if response == 0:
                print(f"{host} is reachable")
            else:
                print(f"{host} is not reachable")
        else:
            print("Please specify a host to ping")
        self.operation_in_progress = False

    def open_browser(self, _):
        self.operation_in_progress = True
        print("Welcome to Funix Browser!")
        while True:
            url = input("Enter URL (type 'exit' to quit browser): ")
            if url.lower() == 'exit':
                break
            else:
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    content = response.text
                    print("=" * 50)
                    self.parser.feed(content)
                    print("=" * 50)
                except requests.RequestException as e:
                    print("Error:", e)
        self.operation_in_progress = False

    def show_hostname(self, _):
        print("Hostname:", platform.node())

    def show_username(self, _):
        if os.name == 'nt':
            print("Username:", os.getenv('USERNAME'))
        else:
            print("Username:", os.getenv('USER'))

    def show_time(self, _):
        print("Current time:", datetime.now().strftime("%H:%M:%S"))

    def show_help(self, _):
        print("Available commands:")
        for command in self.commands:
            print(command)

    def show_disk_usage(self, _):
        if os.name == 'nt':
            os.system('wmic logicaldisk get size,freespace,caption')
        else:
            os.system('df -h')

    def show_uptime(self, _):
        if os.name == 'nt':
            os.system('net stats workstation')
        else:
            os.system('uptime')

    def list_tasks(self, _):
        if os.name == 'nt':
            os.system('tasklist')
        else:
            os.system('ps -aux')

    def kill_task(self, pid):
        if pid:
            if os.name == 'nt':
                os.system(f'taskkill /PID {pid} /F')
            else:
                os.system(f'kill {pid}')
        else:
            print("Please specify a PID to kill")

    def shutdown(self, _):
        if os.name == 'nt':
            os.system('shutdown /s /t 1')
        else:
            os.system('sudo shutdown -h now')

    def reboot(self, _):
        if os.name == 'nt':
            os.system('shutdown /r /t 1')
        else:
            os.system('sudo reboot')

    def show_system_info(self, _):
        if os.name == 'nt':
            os.system('systeminfo')
        else:
            print("systeminfo command is only available on Windows")

    def show_netstat(self, _):
        if os.name == 'nt':
            os.system('netstat')
        else:
            print("netstat command is only available on Windows")

class HTMLTextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ignore_tags = {"script", "style"}
        self.in_ignore_tag = False
        self.text_lines = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() in self.ignore_tags:
            self.in_ignore_tag = True

    def handle_endtag(self, tag):
        if tag.lower() in self.ignore_tags:
            self.in_ignore_tag = False

    def handle_data(self, data):
        if not self.in_ignore_tag:
            self.text_lines.append(data.strip())

    def feed(self, data):
        super().feed(data)
        self.print_pretty_text()

    def print_pretty_text(self):
        terminal_width = os.get_terminal_size().columns
        for line in self.text_lines:
            if line:
                print(line.center(terminal_width))

class SignalHandler:
    def __init__(self, operation_in_progress):
        self.operation_in_progress = operation_in_progress
        signal.signal(signal.SIGINT, self.sigint_handler)

    def sigint_handler(self, signum, frame):
        if not self.operation_in_progress:
            print("\nOperation interrupted. Type 'exit' to quit Funix or enter another command.")

    def restore_original_sigint_handler(self):
        signal.signal(signal.SIGINT, signal.default_int_handler)

def set_console_title(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        sys.stdout.write(f"\x1b]2;{title}\x07")

def set_console_icon(icon_path):
    if os.name == 'nt':
        icon_handle = ctypes.windll.user32.LoadImageW(None, icon_path, 1, 0, 0, 0x00000010)
        if icon_handle == 0:
            raise Exception("Failed to load icon")

        console_handle = ctypes.windll.kernel32.GetConsoleWindow()
        if console_handle == 0:
            raise Exception("Failed to get console window")

        ctypes.windll.user32.SendMessageW(console_handle, 0x0080, 0, icon_handle)
        ctypes.windll.user32.SendMessageW(console_handle, 0x0080, 1, icon_handle)

if __name__ == "__main__":
    set_console_title("Funix")

    icon_path = "assets/funixico.ico"
    if os.path.exists(icon_path):
        set_console_icon(icon_path)
    else:
        print("File not found. Please specify the correct path to the icon file.")

    emulator = Funix()
    print("Welcome to Funix 1.4")
    while True:
        try:
            command_input = input("> ").strip().lower()
            command_parts = command_input.split("(")
            command_name = command_parts[0]

            if command_name in emulator.commands:
                if len(command_parts) > 1:
                    command_argument = command_parts[1][:-1]
                else:
                    command_argument = ""

                emulator.commands[command_name](command_argument)
            else:
                print(f"Unknown command: {command_input}")
        except KeyboardInterrupt:
            print("\nOperation interrupted. Type 'exit' to quit Funix or enter another command.")
