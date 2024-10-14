import google.generativeai as genai  # pip install -q -U google-generativeai


API_KEY = 'YOUR-API-KEY'
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")