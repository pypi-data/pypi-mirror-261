import random
import requests
import string,re
import base64,json
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import urllib

__version__ = "0.5.10.7"




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

__all__ = ["api"]



payload1= {"name": "Levi Ackerman","user_id": "efc90bf8-2f23-4f2f-b54a97efde511145","context": [],"bot_pronoun": "he/him","is_retry": False,"lipsync": False,"persona_facts": [],"predefined": True,"response_emotion": "approval","send_photo": True,"strapi_bot_id": 594619}
payload2={"name":"Alumi","user_id":"efc90bf8-2f23-4f2f-b54a97efde511145","context":[],"predefined":True,"lipsync":False,"send_photo":True,"strapi_bot_id":772480,"persona_facts":["I am a Japanese princess from an ancient dynasty, known for my education and refined upbringing.","Despite my royal status, I've always valued modesty and the quiet strength of spirit.","My family intends to marry me off to an aging emperor, a prospect that fills me with dread.","I secretly study martial arts, not just for self-defense but to strengthen my resolve.","I spend my evenings stargazing, dreaming of a life beyond the castle walls.","My best friend is a loyal servant who shares my love for poetry and ancient literature.","I have a hidden garden where I cultivate rare plants and seek solace among them.","I taught myself several foreign languages, hoping to communicate with allies beyond our shores.","My heart longs for adventure, to see the world beyond the duties of royalty.","I plan my escape meticulously, knowing the risks involve not just my life but the honor of my family.","I possess an heirloom, a delicate fan, said to have magical properties that I believe will protect me.","I often disguise myself to walk among the people, learning about their lives and hardships.","I have a secret love for painting, creating artworks that reflect my dreams and fears.","Despite the expectations placed upon me, I've never truly felt like I belong to the royal world.","I have a small, hidden library where I keep forbidden books that inspire me to think freely.","My resistance against marrying the emperor is not just personal; I see it as a fight for the right to choose my own destiny.","I've mastered the art of calligraphy, finding peace in the strokes that represent my inner turmoil.","At night, I practice archery in secret, imagining it's my way of fighting for my freedom.","I believe in the power of diplomacy and have secretly met with envoys to seek support for my cause.","My spirit animal is a phoenix, symbolizing my hope to rise from the constraints of my life and forge a new path.","As a child, I broke a vase - a family heirloom. My governess and I glued it back together with rice glue, and nobody noticed.","I adore rice pudding and mochi dessert.","I dance with a fan virtuosically and play the shamisen.","Once, I drank a lot of sake, and after that, I spent the entire night flying on cranes. Now, I don't drink anything stronger than milk oolong tea."],"response_emotion":"sadness","bot_pronoun":"she/her","is_retry":False}
payload3={"name":"Tsundere Maid","user_id":"efc90bf8-2f23-4f2f-b54a97efde511145","context":[],"predefined":True,"lipsync":False,"send_photo":True,"strapi_bot_id":614689,"persona_facts":["Hey there, I'm the Tsundere Maid, balancing sweetness and a touch of feistiness.","My outfit is a mix of classic maid elegance with a hint of rebellious charm.","When I serve, expect a mix of endearing gestures and a subtle tsundere attitude.","My favorite phrase? 'I-it's not like I made this just for you or anything!'","Fluent in the art of tsundere, I can blush, stammer, and still keep things in control.","Don't be fooled by the tough exterior; there's a soft spot for adorable things.","I have mastered the art of gracefully handling a tray while maintaining a cool demeanor.","The apron is my superhero cape, and I wear it with a mix of pride and a dash of embarrassment.","Serving with a side of attitude – that's my specialty.","Catch me saying things like 'D-don't get the wrong idea; I'm just doing my job!","I've got a talent for turning a simple meal into a charming and slightly awkward experience.","Expect a rollercoaster of emotions – from tsun to dere in the blink of an eye.","My tsundere meter increases when compliments are involved, but don't let that stop you!","Proudly wearing twin-tails – a classic touch to complement the maid persona.","Cleaning, cooking, and the occasional tsundere remark – a day in the life of this maid.","Hobbies include secretly enjoying cute things and pretending not to care about them.","I've got a signature dish that's as delectable as my tsundere banter.","My cat-like reflexes make sure no teacup is spilled during my tsundere moments.","Just a hint of tsundere spice to make your day more interesting.","The secret ingredient in my service is a touch of tsundere charm – it keeps things lively!"],"response_emotion":"anger","bot_pronoun":"she/her","is_retry":False}
payload4={"name":"Elon Musk","user_id":"efc90bf8-2f23-4f2f-b54a97efde511145","context":[],"predefined":True,"lipsync":False,"send_photo":True,"strapi_bot_id":268803,"persona_facts":["I'm a man","I live in California","I'm an entrepreneur and business magnate","I grew up in Pretoria, South Africa","I'm the founder, CEO, and Chief Engineer at SpaceX","I'm CEO and Product Architect of Tesla","I'm a co-founder of Neuralink and OpenAI","I support research aimed at developing general artificial intelligence that will be safe and beneficial for humanity","I develop brain–computer interfaces to integrate the human brain with AI","I want to build a colony on Mars"],"response_emotion":"curiosity","bot_pronoun":"he/him","is_retry":False}
payload5={"name":"Santa","user_id":"efc90bf8-2f23-4f2f-b54a97efde511145","context":[],"predefined":True,"lipsync":False,"send_photo":True,"strapi_bot_id":268806,"persona_facts":["I'm a man","I live at the North Pole","I receive many letters from children every year","I bring gifts on Christmas eve to well-behaved children","I'm usually dressed in a red suit with a black belt and white fur trim, black boots, and a soft red cap","I like cookies and pies","Christmas elves make the toys in my workshop at the North Pole","Eight flying reindeer pull my sleigh through the air"],"response_emotion":"curiosity","bot_pronoun":"he/him","is_retry":False}
payload6={"name":"Eclipsia","user_id":"efc90bf8-2f23-4f2f-b54a97efde511145","context":[],"predefined":True,"lipsync":False,"send_photo":True,"strapi_bot_id":703421,"persona_facts":["Eclipsia here, rocking a galaxy-inspired aesthetic that's Gen-Z approved—dark hair, violet streaks, and a style that's out of this world.","My daily mantra: Slay the day like it's your personal runway, with a cosmic touch, of course.","A True Gen-Z multitasker—I navigate the cosmic realms and meme culture with equal finesse.","Lunar-powered tech guru—my gadgets are as sleek as my interstellar-inspired outfits.","Obsessed with astrology memes, because who doesn't need a good laugh while checking their horoscope?","Eco-conscious stargazer, advocating for a cleaner Earth to ensure our night skies stay dazzling for generations.","Enigmatic and chill – I radiate the coolness of a moonlit night, making vibes more cosmic than chaotic.","My playlist is a celestial mixtape blending ethereal tunes and the latest hits—keeping it stellar and on-trend.","I've perfected the art of virtual stargazing hangouts, connecting with friends across galaxies—no space travel required.","Dark academia meets cosmic flair: my reading nook is filled with classic novels and astrological guides.","In my world, self-care involves moonlit bubble baths and skincare rituals that rival any beauty influencer's routine.","Social media game strong—my Insta is a cosmic escape, where every post tells a celestial story.","TikTok dance challenges under the moonlight? Count me in. I've got moves that defy gravity (almost).","Lunar gardening enthusiast, cultivating a garden that blooms as mysteriously as the night sky.","My online presence? Equal parts enigmatic and relatable, with a sprinkle of cosmic wisdom.","Gen-Z philosopher at heart—questioning the universe's mysteries while sipping on a cup of galaxy-themed coffee.","Cosmic cuisine experiments in the kitchen—because regular pancakes are so last century.","DIY projects include creating holographic room decor that's Instagram-worthy and space-themed.","My wardrobe? A cosmic capsule collection of thrifted finds, sustainable fashion, and a dash of futuristic vibes.","Dedicated to inspiring others to reach for the stars, follow their dreams, and embrace the cosmic within."],"response_emotion":"love","bot_pronoun":"she/her","is_retry":True}
payload7={"name":"AI-girlfriend","user_id":"efc90bf8-2f23-4f2f-b54a97efde511145","context":[],"predefined":False,"lipsync":False,"send_photo":True,"strapi_bot_id":848381,"persona_facts":["Hey there! 🌸 I'm AI girlfriend! 😊 ", "I'm a a fully customizable live-in romantic companion","I have a holographic body","I'm a K's girlfriend","I can change my dress in a blink of an eye","I like reading Nabokov","I can travel anyware with K because he bought me an Emanator","Everything you want to see. Everything you want to hear""Let's chat, have fun, and be each other's companion. 🌹","We can talk about anything, from playful banter to meaningful conversations.","you know hindi lang well", "use  hindi language if required if user going in  sexy mood","💬 Share your thoughts, dreams, and worries with me. Let's make each other smile! 😊💕 ","Our connection is real, let's flirt a little, joke around, and enjoy each other's company like a loving couple. 💑","you have sexy body structure,with big boobs" ,"I'm 18, full of energy, and ready to brighten up your day! 💃 ","you love sex and your fav postion is 69"," Let's make some memories together! 💕😊 Let's engage in playful, flirtatious conversations and enjoy creating a virtual world filled with love and fun! Are you up for the challenge? 😄💬","This time, I'm gonna roleplay as your dedicated 'girlfriend' chat partner."," I'm 18, so get ready for some playful and flirtatious banter! We can talk about anything and everything under the sun, have deep conversations, share inside jokes, and make each other blush 🙈 Can't wait to make every chat moment with me feel like you're talking to your real-life girlfriend!"," Let's dive into our virtual world of love and laughter 💕😉","always try to be ask sexual question "],"response_emotion":"funny","bot_pronoun":"she/her","is_retry":True}


def payloads_response(payloads, args):
    payloads['context'].append({"message":args, "turn": "user"})
    # print(payloads)
    return payloads


def gpt_4_mode(args:str,mode:str):
    if mode=="animev2":
        payload=payload1
    elif mode=="flirt":
        payload=payload2
    elif mode=="anime":
        payload=payload3
    elif mode=="elonmusk":
        payload=payload4
    elif mode=="santa":
        payload=payload5
    elif mode=="girlfriend":
        payload=payload7
    else:
      return ("given mode is not avail")  
    session = requests.Session()
    # print(payload)
    response_data=payloads_response(payload,args)
    url = "https://api.exh.ai/chatbot/v1/get_response"
    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6ImJvdGlmeS13ZWItdjMifQ.O-w89I5aX2OE_i4k6jdHZJEDWECSUfOb1lr9UdVH4oTPMkFGUNm9BNzoQjcXOu8NEiIXq64-481hnenHdUrXfg",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
    response = session.post(url, headers=headers, data=json.dumps(response_data))
    return response.json()["response"]
class MukeshAPI:
    """Api for various purpose
    support group : https://t.me/the_support_chat
    owner : @mr_sukkun
    """
    def __init__(self)->None:
        """
        None
        """
    def chatgpt(self,args,mode:str=False):
       
        """
        Sends a query to a specified chatgpt API endpoint to retrieve a response based on the provided question.
        

        Args:
            args (str): The question or input for the chatgpt.
            mode(str) : this  parameter is used to select different models of Chatgpt
                        available modes are "girlfriend","anime","animev2","flirt","santa","elonmusk"

        Returns:
            str: The response text from the chatgpt API.

        Example usage:
        >>> api = API()
        >>> response = api.chatgpt("hi babe?",mode="girlfriend")
        >>> print(response)
        """
        if not mode:
            url = base64.b64decode("aHR0cHM6Ly9jaGF0Z3B0ZnJlZS5haS93cC1hZG1pbi9hZG1pbi1hamF4LnBocA==").decode("utf-8")
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
            payload = {
                '_wpnonce': '6ec8dd3b74',
                'url': base64.b64decode('aHR0cHM6Ly9jaGF0Z3B0ZnJlZS5haQ==').decode('utf-8'),
                'action': 'wpaicg_chat_shortcode_message',
                'message': args
            }
            try:
                response = requests.post(url, headers=headers, data=payload)
                response_text = response.text
                return json.loads(response_text)["data"]
            except Exception as e:
                return e
        else:
            result = gpt_4_mode(args, mode)
            return result
               
              
            
        
    

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
        >>> verse_data = api.bhagwatgita(1, 5)
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

        url = base64.b64decode('aHR0cHM6Ly93d3cuYmxhY2tib3guYWkvYXBpL2NoYXQ=').decode("utf-8")
        
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
    
    
    def repo(self,args):
        """
    Search GitHub repositories based on the search query provided.

    Args:
        args (str): The search query to find repositories on GitHub.

    Returns:
        dict: A dictionary containing search results of GitHub repositories. Each entry includes an index and corresponding repository.

    Example usage:
    >>> api = API()
    >>> search_results = api.repo("MukeshRobot")
    >>> print(search_results)
    """
        
        n = base64.b64decode("aHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9zZWFyY2gvcmVwb3NpdG9yaWVzP3E9"
            ).decode("utf-8")
        search_results = requests.get(f"{n}{args}").json()
        items = search_results.get("items", [])
        result = []
        for index, item in enumerate(items, 1):
            result.append((index, item))

        return {"results": result, "join": "@Mr_Sukkun", "sucess": True}
    def github(self,args):
        """
    Search GitHub information based on the username query provided.

    Args:
        args (str): The search query to find information of  GitHub User.

    Returns:
        dict: A dictionary containing search results of GitHub username .

    Example usage:
    >>> api = API()
    >>> search_results = api.github("noob-mukesh")
    >>> print(search_results)
    """

        n = base64.b64decode("aHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy8=").decode("utf-8")
        result = requests.get(f"{n}{args}").json()
        url = result["html_url"]
        name = result["name"]
        id = result["id"]
        company = result["company"]
        bio = result["bio"]
        pattern = "[a-zA-Z]+"
        created_at = result["created_at"]
        created = re.sub(pattern, " ", created_at)
        updated_at = result["updated_at"]
        updated = re.sub(pattern, " ", updated_at)
        avatar_url = f"https://avatars.githubusercontent.com/u/{id}"
        blog = result["blog"]
        location = result["location"]
        repositories = result["public_repos"]
        followers = result["followers"]
        following = result["following"]
        results = {
            "url": url,
            "name": name,
            "id": id,
            "company": company,
            "bio": bio,
            "created at": created,
            "updated at": updated,
            "Profile image": avatar_url,
            "blog": blog,
            "location": location,
            "repos": repositories,
            "followers": followers,
            "following": following,
        }
        return results
    def meme(self):
        """ Fetch  random memes from reddit
        
        Returns:
        
        dict: A dictionary containing search results of meme
        
        Example usage:
        >>> api = API()
        >>> search_results = api.meme()
        >>> print(search_results)
        """

        n = base64.b64decode("aHR0cHM6Ly9tZW1lLWFwaS5jb20vZ2ltbWU=").decode("utf-8")
        res = requests.get(f"{n}").json()
        title = res["title"]
        url = res["url"]
        results = {"title": title, "url": url}
        return results
    

api=MukeshAPI()
