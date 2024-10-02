import streamlit as st
import speech_recognition as sr
import requests
from transformers import pipeline

# Set up NLP model for command parsing (use a pre-trained model like BERT for complex parsing)
nlp_model = pipeline("zero-shot-classification")

# Open Library API URL
OPEN_LIBRARY_URL = "http://openlibrary.org/search.json"

# Streamlit Page Configuration
st.set_page_config(page_title="Voice-Based Book Search & Recommendation", layout='wide')
st.title("Voice-Based Book Search and Recommendation System")

# Create a Recognizer instance
recognizer = sr.Recognizer()

def fetch_books(query):
    """Fetch books from Open Library API based on query."""
    response = requests.get(OPEN_LIBRARY_URL, params={'q': query})
    if response.status_code == 200:
        return response.json()['docs'][:5]  # Return top 5 results for display
    else:
        return []

def voice_to_text():
    """Convert voice input to text using SpeechRecognition."""
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            st.warning("Sorry, I could not understand the audio.")
        except sr.RequestError:
            st.error("Could not request results from the speech recognition service.")
        return ""

# Sidebar Section for Voice Command
st.sidebar.header("Voice Command Input")
if st.sidebar.button("Start Listening"):
    user_command = voice_to_text()
    if user_command:
        st.sidebar.write(f"Command: {user_command}")

        # Parse Command with NLP Model (replace with custom intent parsing model if needed)
        candidate_labels = ["search by author", "search by genre", "find similar books", "get book details"]
        parsed_command = nlp_model(user_command, candidate_labels)

        # Determine the intent and act accordingly
        intent = parsed_command['labels'][0]
        st.sidebar.write(f"Identified Intent: {intent}")

        # Handle different intents
        if "search by author" in intent:
            author_name = user_command.replace("find books by", "").strip()
            books = fetch_books(f"author:{author_name}")
            st.write(f"Books by {author_name}:")
        elif "search by genre" in intent:
            genre = user_command.replace("show books in", "").strip()
            books = fetch_books(f"subject:{genre}")
            st.write(f"Books in {genre}:")
        else:
            st.write("Sorry, I couldn't identify the search criteria.")

        # Display books if any were found
        if books:
            for book in books:
                st.subheader(book.get('title', 'No Title'))
                st.write(f"Author: {book.get('author_name', ['Unknown'])[0]}")
                st.write(f"First Published: {book.get('first_publish_year', 'Unknown')}")
                st.write("---")
        else:
            st.write("No books found.")
