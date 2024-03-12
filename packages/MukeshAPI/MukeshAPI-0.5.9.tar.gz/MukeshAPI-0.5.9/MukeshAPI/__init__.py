import random
import requests
import string,re
import base64,json
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import urllib
__version__ = "0.5.9"




MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}

# __all__ = ["hastag_gen","bhagwatgita","chatbot","pass_gen","imdb"]
__all__ = ["api"]

class MukeshAPI:
    """Api for various purpose
    support group : https://t.me/the_support_chat
    owner : @mr_sukkun
    """
    def __init__(self)->None:
        """
        Purpose: value
        """
        
    

    def password(self, num: int = 12)-> str:
        """
        This function generates a random password by combining uppercase letters, lowercase letters, punctuation marks, and digits.

        Parameters:
        - num (int): The length of the generated password. Default is 12 if not specified.

        Returns:
        - str: A randomly generated password consisting of characters from string.ascii_letters, string.punctuation, and string.digits.

        Example usage:
        >>> api = API()
        >>> api.password()
        'r$6Ag~P{32F+'
        >>> api.password(10)
        'ZnK"9|?v3a'
        """
        characters = string.ascii_letters + string.punctuation + string.digits
        password = "".join(random.sample(characters, num))
        return password

    def hashtag(self, arg: str)-> list:
        """
        Generate hashtags based on the given keyword using a specific website.
        
        Args:
        arg (str): The keyword for which hashtags need to be generated.
        
        Returns:
        str: A string of hashtags related to the given keyword.
        
        Example usage:
        >>> api = API()
        >>> keyword = "python"
        >>> hashtags = api.hashtag(keyword)
        >>> print(hashtags)
        """
        url = base64.b64decode("aHR0cHM6Ly9hbGwtaGFzaHRhZy5jb20vbGlicmFyeS9jb250ZW50cy9hamF4X2dlbmVyYXRvci5waHA=").decode("utf-8")
        data = {"keyword": arg, "filter": "top"}
        response = requests.post(url, data=data).text
        content = BeautifulSoup(response, "html.parser").find("div", {"class": "copy-hashtags"}).string
        output=content.split()
        return output
    def chatbot(self,args:str)->str:
        """
        Interact with a chatbot to get a response based on the provided input text.

        Args:
        args (str): The text input to the chatbot for generating a response.

        Returns:
        str: The response from the chatbot based on the input text.

        Example usage:
        >>> api = API()
        >>> user_input = "Hello, how are you?"
        >>> response = api.chatbot(user_input)
        >>> print(response)
        """
        x = base64.b64decode("aHR0cHM6Ly9mYWxsZW54Ym90LnZlcmNlbC5hcHAvYXBpL2FwaWtleT01OTM1NjA4Mjk3LWZhbGxlbi11c2JrMzNrYnN1L2dyb3VwLWNvbnRyb2xsZXIvbXVrZXNoL21lc3NhZ2U9").decode("utf-8")
        full_url = f"{x}{args}"
        response = requests.get(full_url).json()["reply"]
        return response

    def bhagwatgita(self,chapter: int, shalok: int = 1) -> requests.Response:
        """
        Retrieve a verse from the Bhagavad Gita based on the provided chapter and shalok number.

        Args:
        chapter (int): The chapter number from which the verse will be retrieved.
        shalok (int, optional): The shalok number within the chapter. Default is 1.

        Returns:
        dict: A dictionary containing the chapter number, verse text, chapter introduction, and the specified shalok text.

        Example usage:
        >>> api = API()
        >>> verse_data = api.get_gita_verse(1, 5)
        >>> print(verse_data)
        """
        xc=base64.b64decode("aHR0cHM6Ly93d3cuaG9seS1iaGFnYXZhZC1naXRhLm9yZy9jaGFwdGVyLw==").decode(encoding="utf-8")
        url = f"{xc}{chapter}/hi"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraph = soup.find("p")
        chapter_intro = soup.find("div", class_="chapterIntro")
        co = soup.find_all("section", class_="listItem")
        output = [i.text.strip().replace("View commentary »", "").replace("Bhagavad Gita ", "").strip()  for i in co]
        data = {
            "chapter_number": chapter,
            "verse": paragraph.text,
            "chapter_intro": chapter_intro.text,
            "shalok": output[shalok],
        }

        return data


    def imdb(self,args: str) -> dict:
        """
        Retrieve information about a movie or TV show from IMDb based on the search query.

        Args:
        args (str): The movie or TV show to search for on IMDb.

        Returns:
        dict: A dictionary containing details about the movie or TV show, such as name, description, genre,
            actors, trailer link, and more.

        Example usage:
        >>> api = API()
        >>> movie_data = api.imdb("The Godfather")
        >>> print(movie_data)
        """

        session = HTMLSession()

        url = f"https://www.imdb.com/find?q={args}"
        response = session.get(url)
        results = response.html.xpath("//section[@data-testid='find-results-section-title']/div/ul/li")
        urls = [result.find("a")[0].attrs["href"] for result in results][0]

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(f"https://www.imdb.com/{urls}", headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        movie_name = soup.title.text.strip()

        meta_tags = soup.find_all("meta")
        description = ""
        keywords = ""

        for tag in meta_tags:
            if tag.get("name", "") == "description":
                description = tag.get("content", "")
            elif tag.get("name", "") == "keywords":
                keywords = tag.get("content", "")

        json_data = soup.find("script", type="application/ld+json").string
        parsed_json = json.loads(json_data)

        movie_url = parsed_json["url"]
        movie_image = parsed_json["image"]
        movie_description = parsed_json["description"]
        movie_review_body = parsed_json["review"]["reviewBody"]
        movie_review_rating = parsed_json["review"]["reviewRating"]["ratingValue"]
        movie_genre = parsed_json["genre"]
        movie_actors = [actor["name"] for actor in parsed_json["actor"]]
        movie_trailer = parsed_json["trailer"]
        
        output = []
        for result in results:
            name = result.text.replace("\n", " ")
            url = result.find("a")[0].attrs["href"]
            if ("Podcast" not in name) and ("Music Video" not in name):
                try:
                    image = result.xpath("//img")[0].attrs["src"]
                    file_id = url.split("/")[2]
                    output.append({
                        "movie_name": movie_name,
                        "id": file_id,
                        "poster": image,
                        "description": description,
                        "keywords": keywords,
                        "movie_url": movie_url,
                        "movie_image": movie_image,
                        "movie_description": movie_description,
                        "movie_review_body": movie_review_body,
                        "movie_review_rating": movie_review_rating,
                        "movie_genre": movie_genre,
                        "movie_actors": movie_actors,
                        "movie_trailer": movie_trailer,
                        "join": "@Mr_Sukkun",
                        "success": True,
                    })
                    return {"results": output}
                except:
                    return {"Success": False}
    def morse_encode(self,args:str)->str:
        """
    Encode the input string into Morse code.

    Args:
        args (str): The input string to be encoded into Morse code. ✨

    Returns:
        str: The Morse code representation of the input string along with additional information. 🔠

    Example usage:
    >>> api = API()
    >>> encoded_result = api.morse_encode("Hello World")
    >>> print(encoded_result)
    """

        cipher = ""
        for letter in args.upper():
            if letter != " ":
                cipher += MORSE_CODE_DICT[letter] + " "
            else:
                cipher += " "
        output = {
            "input": args,
            "results": cipher,
            "join": "@Mr_Sukkun",
            "sucess": True
        }
        return (output)
    
    def morse_decode(self,args: str) -> str:
        """
    Decode the Morse code back into the original text. 🔄

    Args:
        args (str): The Morse code to be decoded back into text.

    Returns:
        str: The decoded text from the Morse code.

    Example usage:
    >>> api = API()
    >>> decoded_result =api.morse_decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
    >>> print(decoded_result)
    """

        args += " "
        decipher = ""
        citext = ""
        for letter in args:
            if letter != " ":
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2:
                    decipher += " "
                else:
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                    citext = ""
        output = {
            "input": args,
            "results": decipher,
            "join": "@Mr_Sukkun",
            "success": True
        }
        return output
    def gemini(self, args: str) -> dict:
        """
    Generate content using the Gemini API. ✨

    Args:
        args (str): The input text to generate content.

    Returns:
        dict: A dictionary containing the generated content with metadata.

    Example usage:
    >>> api = API()
    >>> generated_content = api.gemini("Hello, how are you?")
    >>> print(generated_content)
    {
        "results": "Generated content text",
        "join": "@Mr_Sukkun",
        "success": True
    }
    """
        url = base64.b64decode('aHR0cHM6Ly9nZW5lcmF0aXZlbGFuZ3VhZ2UuZ29vZ2xlYXBpcy5jb20vdjFiZXRhL21vZGVscy9nZW1pbmktcHJvOmdlbmVyYXRlQ29udGVudD9rZXk9QUl6YVN5QlFhb1VGLUtXalBWXzRBQnRTTjBEUTBSUGtOZUNoNHRN').decode("utf-8")
        headers = {'Content-Type': 'application/json'}
        payload = {
            'contents': [
                {'parts': [{'text': args}]}
            ]
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            if response.status_code == 200:
                generated_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
                return generated_text
        except Exception as e:
            return e
    
    def blackbox(self,args: str) -> requests.Response:
        """
        Interact with the Blackbox AI API for generating content. 🧠

        Args:
            args (str): The input text to interact with the Blackbox AI chat API.

        Returns:
            requests.Response: The response object from the API request.

        Example usage:
        >>> api = API()
        >>> response = api.blackbox("Hello, how are you?")
        >>> print(response.text)
        {
            "response": "Generated content response",
            "status": 200
        }
        """

        url = bas64.b64decode('aHR0cHM6Ly93d3cuYmxhY2tib3guYWkvYXBpL2NoYXQ=').decode("utf-8")
        
        payload = {
            "agentMode": {},
            "codeModelMode": True,
            "id": "XM7KpOE",
            "isMicMode": False,
            "maxTokens": None,
            "messages": [
                {
                    "id": "XM7KpOE",
                    "content": urllib.parse.unquote(args),
                    "role": "user"
                }
            ],
            "previewToken": None,
            "trendingAgentMode": {},
            "userId": "87cdaa48-cdad-4dda-bef5-6087d6fc72f6",
            "userSystemPrompt": None
        }

        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'sessionId=f77a91e1-cbe1-47d0-b138-c2e23eeb5dcf; intercom-id-jlmqxicb=4cf07dd8-742e-4e3f-81de-38669816d300; intercom-device-id-jlmqxicb=1eafaacb-f18d-402a-8255-b763cf390df6; intercom-session-jlmqxicb=',
            'Origin': 'https://www.blackbox.ai',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return {"results": response.text, "join": "@Mr_Sukkun", "success": True}
        else:
            return {f"status code: {response.status_code}"}
       
    
    def unsplash(self,args)->requests.Response:
        """
    Get image URLs related to the query using the iStockphoto API.

    Args:
        args (str): The search query for images.

    Returns:
        list: List of image URLs related to the query.
        
    Example usage:
    >>> api = API()
    >>> response = api.unsplash("boy image")
    >>> print(response)
    

    """
        url = f'https://www.istockphoto.com/search/2/image?alloweduse=availableforalluses&phrase={args}&sort=best'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://unsplash.com/'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            
        
            soup = BeautifulSoup(response.content, 'html.parser')
            image_tags = soup.find_all('img')
            image_urls = [img['src'] for img in image_tags if img['src'].startswith('https://media.istockphoto.com')]
            
            return {"results": image_urls, "join": "@Mr_Sukkun", "success": True}
        else:
            return {f"status code: {response.status_code}"}
        
    def leetcode(self,username):
        """
    Retrieve user data including activity streak, profile information, and contest badges from LeetCode using GraphQL API.

    Args:
        username (str): The username of the LeetCode user.

    Returns:
        dict: A dictionary containing user data such as streak, total active days, badges, user profile information, and social media URLs.

    Example usage:
    >>> api = API()
    >>> user_data = api.leetcode("noob-mukesh")
    >>> print(user_data)"""
        url = base64.b64decode('aHR0cHM6Ly9sZWV0Y29kZS5jb20vZ3JhcGhxbC8=').decode("utf-8")

        payload = {
        'operationName': 'userProfileCalendar',
        'query': '''
        query userProfileCalendar($username: String!, $year: Int) {
        matchedUser(username: $username) {
            userCalendar(year: $year) {
            activeYears
            streak
            totalActiveDays
            dccBadges {
                timestamp
                badge {
                name
                icon
                }
            }
            submissionCalendar
            }
        }
        }
        ''',
        'variables': {'username': username, 'year': 2024}
    }

        payload_2 = {
        'operationName': 'userPublicProfile',
        'query': '''
        query userPublicProfile($username: String!) {
        matchedUser(username: $username) {
            contestBadge {
            name
            expired
            hoverText
            icon
            }
            username
            githubUrl
            twitterUrl
            linkedinUrl
            profile {
            ranking
            userAvatar
            realName
            aboutMe
            school
            websites
            countryName
            company
            jobTitle
            skillTags
            postViewCount
            postViewCountDiff
            reputation
            reputationDiff
            solutionCount
            solutionCountDiff
            categoryDiscussCount
            categoryDiscussCountDiff
            }
        }
        }
        ''',
        'variables': {'username': username}
    }

        try:
            response = requests.post(url, json=payload)
            data_1 = response.json()['data']['matchedUser']

            response = requests.post(url, json=payload_2)
            data_2 = response.json()['data']['matchedUser']

            output_dict2 = {} 
            output_dict2.update(data_1)
            output_dict2.update(data_2)
            output_dict = {}

            for key, value in output_dict2.items():
                if isinstance(value, dict):
                    output_dict[key] = {}
                    for k, v in value.items():
                        output_dict[key][k] = v
                else:
                    output_dict[key] = value
            return output_dict
        except Exception as e:
            return e
        
    def datagpt(self,args):
        """
        Sends a query to a specified datagpt API endpoint to retrieve a response based on the provided question.

        Args:
            args (str): The question or input for the datagpt.

        Returns:
            str: The response text from the datagpt API.

        Example usage:
        >>> api = API()
        >>> response = api.datagpt("What are the latest trends in AI?")
        >>> print(response)
        """
        url = base64.b64decode("aHR0cHM6Ly9hcHAuY3JlYXRvci5pby9hcGkvY2hhdA==").decode("utf-8")
        payload = {
            "question": args,
            "chatbotId": "712544d1-0c95-459e-ba22-45bae8905bed",
            "session_id": "8a790e7f-ec7a-4834-be4a-40a78dfb525f",
            "site": "datacareerjumpstart.mykajabi.com"
        }

        response = requests.post(url, json=payload)

        extracted_text = re.findall(r"\{(.*?)\}", response.text, re.DOTALL)
        extracted_json = "{" + extracted_text[0] + "}]}"
        json_text = extracted_json.replace('\n', ' ')

        data = json.loads(json_text)
        return data["text"]
    def pypi(self,args):
        """
    Retrieve package information from the Python Package Index (PyPI) by providing the package name.

    Args:
        args (str): The name of the package to search for on PyPI.

    Returns:
        dict: A dictionary containing information about the specified package, such as name, version, description, author, license, and more.

    Example usage:
    >>> api = API()
    >>> package_info = api.pypi("requests")
    >>> print(package_info)
    """
   
        n = base64.b64decode("aHR0cHM6Ly9weXBpLm9yZy9weXBpLw==").decode("utf-8")
        result = requests.get(f"{n}{args}/json").json()["info"]
        return result
    
    def chatgpt(self,args):
        """
        Sends a query to a specified chatgpt API endpoint to retrieve a response based on the provided question.

        Args:
            args (str): The question or input for the chatgpt.

        Returns:
            str: The response text from the chatgpt API.

        Example usage:
        >>> api = API()
        >>> response = api.chatgpt("What are the latest trends in AI?")
        >>> print(response)
        """
        url = base64.b64decode("aHR0cHM6Ly9jaGF0Z3B0ZnJlZS5haS93cC1hZG1pbi9hZG1pbi1hamF4LnBocA==").decode("utf-8")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 import requests'
        }
        payload = {
            '_wpnonce': '6ec8dd3b74',
            'url': base64.b64decode('aHR0cHM6Ly9jaGF0Z3B0ZnJlZS5haQ==').decode("utf-8"),
            'action': 'wpaicg_chat_shortcode_message',
            'message': args }
        try:
            response = requests.post(url, headers=headers, data=payload)
            response_text = response.text
            return json.loads(response_text)["data"]
        except Exception as e:
            return e

        
            


        

api=MukeshAPI()
print(api.chatgpt("what is ai"))