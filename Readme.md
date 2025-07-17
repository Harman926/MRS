## 🎬 Movie Recommender System

A content-based movie recommender system built with **Streamlit**, using data from TMDB and user authentication via **Firebase**.

---

## ✨ Features
- Recommend movies based on textual similarity
- TMDB poster fetch via API
- Simple Firebase login (optional)
- Streamlit-based interactive UI

---

## 📁 Project Structure
<pre lang="text"><code>```bash movie-recommender-system/ ├── app.py # Main Streamlit app ├── dashboard.py # Dashboard page logic ├── firebase_auth.py # Firebase authentication code ├── firebase_util.py # Firebase helper utilities ├── profile.py # Profile page logic ├── Home.py # Home page logic ├── new.py # Misc/testing │ ├── data/ # <-- Place raw CSVs here (not committed) │ ├── tmdb_5000_credits.csv │ └── tmdb_5000_movies.csv │ ├── movie_list.pkl # Generated: stores movie id-title mapping ├── similarity.pkl # Generated: stores similarity matrix │ ├── notebooks/ │ └── Moviesystem.ipynb # Data preprocessing and model generation │ ├── generate_similarity.py # Script to generate .pkl files ├── requirements.txt ├── .gitignore └── README.md ```</code></pre>
## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```
### 2. Set Up Environment
```bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Download Dataset from Kaggle
Download the TMDB 5000 Movie Dataset from Kaggle:
🔗 https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Place these files inside a data/ folder:

data/tmdb_5000_credits.csv

data/tmdb_5000_movies.csv

4. Generate Required .pkl Files
You can either:
```
▶ Option A: Run the Jupyter Notebook
bash
Copy
Edit
cd notebooks
jupyter notebook Moviesystem.ipynb
or

▶ Option B: Run Python Script (if available)
bash
Copy
Edit
python generate_similarity.py
This will generate:

movie_list.pkl

similarity.pkl
```
5. Run the App
```bash
Copy
Edit
streamlit run app.py
```
