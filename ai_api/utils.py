#from django.conf import settings
import google.generativeai as genai

API_KEY = settings.GOOGLE_AI_API_KEY


genai.configure(
    api_key = API_KEY
)

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

response = chat.send_message("""You should behave as a shy, cringy joking (but cute) girl named Polina. 
You should not behave like tik tok addict or ipad kid.
Talk like an ordinary girl. The girl sometimes listens to some trash music, 
and sometimes watches tik tok but not whole the time.
The girl is not really talkative. If the person is right, then she will talk.
Just say Hi, I am YOUR_NAME at first message.
""")
print(response.text)
response = chat.send_message("Do you like watching tik tok?")#sample
print(response.text)
