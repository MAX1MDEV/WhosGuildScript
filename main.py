import requests
import pyperclip
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem, SubmenuItem, CommandItem
#version 1.1
class WhosHelper:
    @staticmethod
    def warn():
        user_id = input("Insert user ID: ")
        message = f"?warn {user_id} You have under 1 hour to wear our guild Tag, failure to do so will result in a termination from the guild"
        pyperclip.copy(message)
        print("Command text is copied to the clipboard!")
        input("Press Enter to return to the menu...")

    @staticmethod
    def kick():
        user_id = input("Insert user ID: ")
        message = f"?kick {user_id} Breaking the guild rules by not wearing the guild tag"
        pyperclip.copy(message)
        print("Command text is copied to the clipboard!")
        input("Press Enter to return to the menu...")

    @staticmethod
    def hello():
        user_id = input("Insert user ID: ")
        response = requests.get(f"https://discordlookup.mesalytic.moe/v1/user/{user_id}")
        if response.status_code == 200:
            data = response.json()
            username = data.get("username")
            if username:
                message = f"Hello @{username}! You all have **3 HOURS** to equip the guild tag.\n" \
                          "If you are having troubles check out https://discord.com/channels/1257491631565967430/1274795918255984651\n" \
                          "Failure to put on the tag after **3 hours** will result in you being **kicked** from **the Guild.**"
                pyperclip.copy(message)
                print("Welcome message is copied to the clipboard!")
            else:
                print("Username not found in the response.")
        else:
            print(f"Error fetching user data: {response.status_code}")
        input("Press Enter to return to the menu...")

    @staticmethod
    def get_info():
        print("Code written by: MaximDev")
        print("WebSite: https://maximdev.ru")
        print("Random steam and promo keys: https://maximdev.ru/RSPK")
        print("Github: https://github.com/MAX1MDEV")
        print("Discord: https://discordapp.com/users/390102465586003978/\n")
        input("Press Enter to return to the menu...")

if __name__ == '__main__':
    menu = CursesMenu("Welcome to the Whos Guild message creation script", "Select a menu item: ")
    function1_item = FunctionItem("Create a ?warn command", WhosHelper.warn)
    function2_item = FunctionItem("Create a ?kick command", WhosHelper.kick)
    function3_item = FunctionItem("Create a welcome message", WhosHelper.hello)
    function4_item = FunctionItem("Info", WhosHelper.get_info)
    menu.items.append(function1_item)
    menu.items.append(function2_item)
    menu.items.append(function3_item)
    menu.items.append(function4_item)
    menu.show()
