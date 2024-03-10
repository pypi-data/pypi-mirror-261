import base64
from bs4 import BeautifulSoup
import requests

def hastag_gen(arg: str):
    """
    Generate hashtags based on the given keyword using a specific website.
    
    Args:
    arg (str): The keyword for which hashtags need to be generated.
    
    Returns:
    str: A string of hashtags related to the given keyword.
    
    Example usage:
    >>> keyword = "python"
    >>> hashtags = hastag_gen(keyword)
    >>> print(hashtags)
    """
    m = base64.b64decode
    ux = m("aHR0cHM6Ly9hbGwtaGFzaHRhZy5jb20vbGlicmFyeS9jb250ZW50cy9hamF4X2dlbmVyYXRvci5waHA=").decode("utf-8")
    data = {"keyword": arg, "filter": "top"}
    res = requests.post(ux, data=data).text
    content = BeautifulSoup(res, "html.parser").find("div", {"class": "copy-hashtags"}).string
    return content


