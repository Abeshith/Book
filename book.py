import streamlit as st
import requests
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Recommending System" ,page_icon= "🌠")

# Open Library API base URL
BASE_URL = "https://openlibrary.org"

# OMDb API base URL and key
OMDB_API_URL = "http://www.omdbapi.com/"
OMDB_API_KEY = "a696991"  # Updated OMDb API key

# Function to fetch book details using the Open Library API
def get_book_details(book_title):
    search_url = f"{BASE_URL}/search.json"
    params = {'title': book_title}
    response = requests.get(search_url, params=params)
    
    if response.status_code == 200:
        results = response.json().get('docs', [])
        if results:
            book_key = results[0].get('key')
            return {
                'title': results[0].get('title'),
                'author_name': results[0].get('author_name', ['Unknown'])[0],
                'key': book_key
            }
    return None

# Function to get books by the same author
def get_books_by_author(author_name):
    search_url = f"{BASE_URL}/search.json"
    params = {'author': author_name}
    response = requests.get(search_url, params=params)
    
    if response.status_code == 200:
        results = response.json().get('docs', [])
        books = [{'title': book.get('title'), 'cover_id': book.get('cover_i')} for book in results if 'title' in book]
        return books
    return []

# Function to get the book cover image URL
def get_cover_image_url(cover_id, size='M'):
    if cover_id:
        return f"https://covers.openlibrary.org/b/id/{cover_id}-{size}.jpg"
    return None

# Function to fetch movie recommendations using the OMDb API
def get_movie_recommendations(movie_title):
    params = {
        's': movie_title,
        'apikey': OMDB_API_KEY
    }
    
    response = requests.get(OMDB_API_URL, params=params)
    if response.status_code == 200:
        results = response.json().get('Search', [])
        movies = [{'Title': movie['Title'], 'Year': movie['Year'], 'Type': movie['Type'], 'Poster': movie['Poster']} for movie in results if 'Poster' in movie]
        return movies
    return []

# Streamlit UI with option menu
selected = option_menu("Main Menu", ["Book Recommendations", "Movie Recommendations"],
                       icons=['book', 'film'], menu_icon="cast", default_index=0)

if selected == "Book Recommendations":
    st.title("Book Recommendation System")
    st.write("Enter a book title to get recommendations for books by the same author:")

    # Input for book title
    book_title = st.text_input("Book Title")

    # Fetch and display books by the same author if a book title is provided
    if book_title:
        book_details = get_book_details(book_title)
        
        if book_details:
            st.subheader(f"Books by **{book_details['author_name']}**")
            
            # Search by author and display results
            same_author_books = get_books_by_author(book_details['author_name'])
            if same_author_books:
                # Display books in a grid format (4 per row)
                cols = st.columns(4)  # Create 4 columns for a grid layout
                for idx, book in enumerate(same_author_books):
                    cover_image_url = get_cover_image_url(book['cover_id'])
                    with cols[idx % 4]:
                        if cover_image_url:
                            st.image(cover_image_url, width=150)
                        st.write(f"**{book['title']}**")
            else:
                st.write(f"No books found by {book_details['author_name']}.")
        else:
            st.write("Book not found. Please try a different title.")

elif selected == "Movie Recommendations":
    st.title("Movie Recommendation System")
    st.write("Enter a movie title to get recommendations:")

    # Input for movie title
    movie_title = st.text_input("Movie Title")

    # Fetch and display movie recommendations if a movie title is provided
    if movie_title:
        recommended_movies = get_movie_recommendations(movie_title)
        
        if recommended_movies:
            st.subheader(f"Related Movies for **{movie_title}**")
            
            # Display movies in a grid format (4 per row)
            cols = st.columns(4)  # Create 4 columns for a grid layout
            for idx, movie in enumerate(recommended_movies):
                similar_movie_poster = movie['Poster']
                with cols[idx % 4]:
                    if similar_movie_poster and similar_movie_poster != "N/A":
                        st.image(similar_movie_poster, width=150)
                    else:
                        st.image("https://via.placeholder.com/150?text=No+Image", width=150)  # Placeholder for missing images
                    st.write(f"**{movie['Title']}**")
                    st.write(f"**Year:** {movie['Year']}")
                    st.write(f"**Type:** {movie['Type']}")
        else:
            st.write(f"No recommendations found for '{movie_title}'.")
