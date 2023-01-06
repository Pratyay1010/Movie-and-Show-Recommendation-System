import streamlit as st
import recommender
from poster_url import get_poster_url

movie_name = ""
movie_name = st.selectbox('Select a Show', recommender.show_df["title"])


col_shape = []
for i in range(10):
    col_shape.append(4)

columns = st.columns(col_shape, gap='medium')

if st.button('Recommend'):

    recommendation_list = recommender.recommend_show(movie_name)
    print(movie_name, ":", recommendation_list)

    for show, column in zip(recommendation_list, columns):

        movie_poster_url = get_poster_url(show)

        with column:
            if movie_poster_url == "not found":
                st.write(show)
            else:
                st.write(show)
                st.image(movie_poster_url)

