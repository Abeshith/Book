# Book and Movie Recommendation System

This Streamlit application provides recommendations for books by the same author and movies based on a user-input movie title. The app uses the Open Library API for book details and the OMDb API for movie recommendations.

**Click here for the app:** [Recommendation App](https://recommendationsystems-abe.streamlit.app/)

## Features
1. **Book Recommendations**:
   - Search for a book by title and find other books by the same author.
   - Displays book covers and titles using the Open Library API.
2. **Movie Recommendations**:
   - Search for a movie by title and get similar movies based on the input title.
   - Displays movie posters, titles, year, and type using the OMDb API.

## Code Explanation

### 1. Import Necessary Libraries
The following libraries are used:
- **Streamlit (`st`)**: For creating the interactive web application.
- **Requests (`requests`)**: For making HTTP requests to the Open Library and OMDb APIs.
- **Streamlit Option Menu (`option_menu`)**: To create a sidebar option menu for navigation between "Book Recommendations" and "Movie Recommendations".

### 2. Page Configuration
The `st.set_page_config` function sets the page title to "Recommending System" and adds a star emoji (`🌠`) as the icon.

### 3. Define API Endpoints
- **Open Library API**: Used to fetch book details and cover images.
- **OMDb API**: Used for fetching movie recommendations. The `OMDB_API_KEY`  (replace with your own key if needed).

### 4. Helper Functions
#### `get_book_details(book_title)`
- **Description**: Fetches book details (title, author, and unique key) using the Open Library API.
- **Input**: `book_title` (string) - The title of the book to search for.
- **Output**: Returns a dictionary with `title`, `author_name`, and `key` if found, else returns `None`.

#### `get_books_by_author(author_name)`
- **Description**: Retrieves a list of books by the same author using the Open Library API.
- **Input**: `author_name` (string) - The name of the author.
- **Output**: Returns a list of dictionaries containing `title` and `cover_id` for each book.

#### `get_cover_image_url(cover_id, size='M')`
- **Description**: Constructs a URL to display the cover image using the `cover_id`.
- **Input**: `cover_id` (integer) - The ID of the book cover.
- **Output**: Returns a URL string to display the cover image.

#### `get_movie_recommendations(movie_title)`
- **Description**: Fetches movie recommendations using the OMDb API.
- **Input**: `movie_title` (string) - The title of the movie to search for.
- **Output**: Returns a list of dictionaries containing `Title`, `Year`, `Type`, and `Poster` for each recommended movie.

### 5. Streamlit Option Menu
The `option_menu` function is used to create a sidebar with two options:
1. **"Book Recommendations"**
2. **"Movie Recommendations"**

### 6. Book Recommendation System
If the user selects **"Book Recommendations"**:
1. **Title and Instructions**: The app title is set to "Book Recommendation System", and a brief instruction is displayed.
2. **Input Field**: Users can enter a book title in the text input box (`st.text_input`).
3. **Fetch Book Details**:
   - If a book title is provided, `get_book_details` is called to fetch the book's details.
   - If the book is found, the app fetches other books by the same author using `get_books_by_author`.
4. **Display Books by Author**:
   - The books are displayed in a 4-column grid format using `st.columns(4)`.
   - If a book cover is available, it is displayed with the book title. If not, a placeholder image is used.

### 7. Movie Recommendation System
If the user selects **"Movie Recommendations"**:
1. **Title and Instructions**: The app title is set to "Movie Recommendation System", and a brief instruction is displayed.
2. **Input Field**: Users can enter a movie title in the text input box (`st.text_input`).
3. **Fetch Movie Recommendations**:
   - If a movie title is provided, `get_movie_recommendations` is called to fetch related movies.
   - Each recommended movie is displayed in a 4-column grid format.
4. **Display Movie Details**:
   - If a movie poster is available, it is displayed with the movie title, year, and type.
   - If a movie poster is not available, a placeholder image is shown.

## Requirements
The following libraries are needed to run the app:
- **Streamlit**: `pip install streamlit`
- **Requests**: `pip install requests`
- **Streamlit Option Menu**: `pip install streamlit-option-menu`

## How to Run the Application Locally
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/book-movie-recommendation-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd book-movie-recommendation-system
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Streamlit application:
    ```bash
    streamlit run recommending_system.py
    ```

## Example Usage
1. **Book Recommendations**:
   - Enter a book title (e.g., "Pride and Prejudice") to get recommendations for other books by the same author.
2. **Movie Recommendations**:
   - Enter a movie title (e.g., "The Matrix") to get related movies.

