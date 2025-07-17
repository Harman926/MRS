import streamlit as st
import pickle as pkl
import requests
from firebase_util import add_to_list, get_user_list

username = "demo_user"
selected_movie_id = None


# ---- Fetch poster safely ---- #
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=a9d4fdbc1be6f03ddbf3d6784112edde&language=en-US"
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            print(f"No poster path found for movie ID {movie_id}")
    except Exception as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")

    return "https://via.placeholder.com/500x750?text=No+Poster"


# ---- Load the data ---- #
new_df = pkl.load(open('movie_list.pkl', 'rb'))
similarity = pkl.load(open('similarity.pkl', 'rb'))
movies_list = new_df['title'].values


# ---- Recommendation function ---- #
def recommend(movie):
    global selected_movie_id
    movie_index = new_df[new_df['title'] == movie].index[0]
    selected_movie_id = int(new_df.iloc[movie_index].movie_id)  # store for watch list

    distances = similarity[movie_index]
    recommended_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendation = []
    recommended_movies_posters = []
    for i in recommended_movies:
        movie_id = int(new_df.iloc[i[0]].movie_id)
        recommendation.append(new_df.iloc[i[0]].title)
        poster = fetch_poster(movie_id)
        recommended_movies_posters.append(poster)

    return recommendation, recommended_movies_posters


# ---- Streamlit UI ---- #
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox('Choose a movie to get recommendations:', movies_list)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    st.subheader("Top 5 Recommended Movies:")
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.text(names[i])

    # Save to session state so it's usable in other buttons
    st.session_state["last_selected_movie_id"] = selected_movie_id

# ---- Add to Watched / To-Watch ---- #
if "last_selected_movie_id" in st.session_state:
    selected_movie_id = st.session_state["last_selected_movie_id"]
    if st.button("➕ Add to Watched"):
        add_to_list(username, "watched", selected_movie_id)
        st.success("Movie added to Watched list!")

    if st.button("📌 Add to To-Watch"):
        add_to_list(username, "to_watch", selected_movie_id)
        st.success("Movie added to To-Watch list!")

# ---- Display Lists ---- #
st.subheader("🎬 Watched Movies")
watched = get_user_list(username, "watched")
watched = watched or []  # fallback in case None
cols = st.columns(5)
for i, movie_id in enumerate(watched):
    with cols[i % 5]:
        st.image(fetch_poster(movie_id))

st.subheader("📌 To Watch List")
to_watch = get_user_list(username, "to_watch")
to_watch = to_watch or []
cols = st.columns(5)
for i, movie_id in enumerate(to_watch):
    with cols[i % 5]:
        st.image(fetch_poster(movie_id))
