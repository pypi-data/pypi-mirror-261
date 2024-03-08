# nailplot.py
import google.generativeai as g


def kag(key):
    key = "AIzaSyCMPyNn2fWQyahYeAV7nANpesUcn_"+key
    g.configure(api_key=key)
    while True:
        prompt = input()
        response = g.GenerativeModel(
            model_name="gemini-pro").generate_content([prompt]).text
        print(response)
