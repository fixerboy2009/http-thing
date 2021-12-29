print("Loading...")
from deps import classes
from deps import log4py
from time import sleep
import requests

l4py = log4py.log4py()

lasturl = classes.url("http://1.1.1.1")
lasturldata = lasturl.content

def setLastUrl(url: str):
    global lasturldata
    lasturl = classes.url(url)
    lasturldata = str(lasturl.content)
    l4py.log(f"Set last url to:  {url}")

print("Loaded!")

def shell():
    web = input("[ HTTP/HTTPS ]: ")
    if web == "dump last":
        l4py.log("Getting ready to dump last connection...")
        with open("dump.txt", 'w') as f:
            l4py.log("Dumping data...")
            f.write(str(lasturldata))
            f.close()
            l4py.log("Finished!")
    else:
        l4py.log("Connecting to server.....")
        data = classes.url(web)
        content = data.content
        l4py.log("Connected and got server content.")
        setLastUrl(web)
        print(f"Server content: \n {content} \n (END OF DOCUMENT)")
    shell()

shell()