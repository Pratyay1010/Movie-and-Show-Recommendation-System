import streamlit as st
import recommender
from poster_url import get_poster_url

movie_name = ""
movie_name = st.selectbox('Select a Show', recommender.show_df["title"])


columns1 = st.columns(5, gap='medium')
columns2 = st.columns(5, gap='medium')

columns = columns1 + columns2

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

