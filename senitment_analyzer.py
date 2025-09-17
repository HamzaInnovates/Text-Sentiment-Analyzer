from openai import OpenAI
from dotenv import load_dotenv
import os 
load_dotenv()

API_KEY = os.getenv('API_KEY')
client  = OpenAI(api_key=API_KEY)

def analyze_text(text):
    PROMPT = f'You have to give me the senitment of the provided text whether it is positiv or negative , text : {text} '
    
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages= [
            {'role':'system', 'content': 'You are the best text sentiment analyzer'},
                  {'role':'user', 'content': PROMPT}
                  ],
        temperature=0.1
        
    )
    return response

text= input("Enter text to analyze: \n")
print(analyze_text(text))