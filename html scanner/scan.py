import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Define the URL of the website to be translated
url = "https://example.com"

# Retrieve the HTML content of the website
response = requests.get(url)
html_content = response.text

# Parse the HTML content to extract the text and headers that need to be translated
soup = BeautifulSoup(html_content, "html.parser")
text_to_translate = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"])
original_text = [text.get_text() for text in text_to_translate]

# Use the Google Translate API to translate the text to Hindi
translator = Translator()
translated_text = [translator.translate(text, dest='hi').text for text in original_text]

# Replace the original text with the translated text in the HTML code
for i, text in enumerate(text_to_translate):
    text.string.replace_with(translated_text[i])

# Write the updated HTML code to a new file
with open("translated.html", "w", encoding="utf-8") as file:
    file.write(str(soup))
