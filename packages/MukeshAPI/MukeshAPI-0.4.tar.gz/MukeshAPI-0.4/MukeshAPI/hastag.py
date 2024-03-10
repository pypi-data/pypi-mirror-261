from base64 import b64decode as m, b64encode as n
from bs4 import BeautifulSoup as BSP
import requests
def hastag(arg:str):
    """
    Purpose: arg
    """
    ux = m("aHR0cHM6Ly9hbGwtaGFzaHRhZy5jb20vbGlicmFyeS9jb250ZW50cy9hamF4X2dlbmVyYXRvci5waHA=")
    ux_decoded = ux.decode("utf-8")
    data = dict(keyword=args, filter="top")
    res = requests.post(ux_decoded, data).text
    content = BSP(res, "html.parser").find("div", {"class": "copy-hashtags"}).string
    return content