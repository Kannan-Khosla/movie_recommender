import streamlit as st
import altair as alt
import pickle
import pandas as pd

# Sample list of movie names (you should replace this with actual movie data)
movie_names = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_names)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommendations(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    Recommended_Movies = []
    for i in movies_list:
        Recommended_Movies.append(movies.iloc[i[0]].title)
    return Recommended_Movies   

st.title("Movie Recommender System")

option = st.selectbox(
    "Select a Movie",
    movies['title'].values)  # Provide the list of movie names as options

# Display the selected movie name
st.write("You selected:", option)

if st.button("Recommend"):
    # Get recommendations for the selected movie
    recommended = recommendations(option)

    # Display the recommendations
    st.write("Recommended Movies:")
    for i in recommended:
        st.write(i)







# # TypeError: 'builtin_function_or_method' object is not iterable
# # Traceback:
# # File "/Users/kannankhosla/opt/anaconda3/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 556, in _run_script
# #     exec(code, module.__dict__)
# # File "/Users/kannankhosla/Desktop/movie_recommenderpy/movie.py", line 70, in <module>
# #     selected_movie = st.selectbox(
# # File "/Users/kannankhosla/opt/anaconda3/lib/python3.9/site-packages/streamlit/elements/selectbox.py", line 99, in selectbox
# #     return self._selectbox(
# # File "/Users/kannankhosla/opt/anaconda3/lib/python3.9/site-packages/streamlit/elements/selectbox.py", line 132, in _selectbox
# #     opt = ensure_indexable(options)
# # File "/Users/kannankhosla/opt/anaconda3/lib/python3.9/site-packages/streamlit/type_util.py", line 471, in ensure_indexable
# #     it = ensure_iterable(obj)
# # File "/Users/kannankhosla/opt/anaconda3/lib/python3.9/site-packages/streamlit/type_util.py", line 451, in ensure_iterable
# #     iter(obj)





