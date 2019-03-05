from pyfiglet import figlet_format
from termcolor import colored
from random import choice
import requests
import colorama
colorama.init()
#windows 10 colored text seems to be broken in powershell. colorama appears to fix the issue. 

header = figlet_format("DAD JOKE 3001!!")
header = colored(
    header,
    color=choice([
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white"]))
print(header)


user_input = input("What kind of joke should i tell? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}. Here's one.")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"There is one joke about {user_input}")
    print(results[0]['joke'])

else:
    print(f"Sorry, couldnt find a joke with your term: {user_input}")
