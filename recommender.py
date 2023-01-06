import pickle

show_df = pickle.load(open("DataFiles/shows_df.pkl", "rb"))
similarities = pickle.load(open("DataFiles/similarities.pkl", "rb"))


def recommend_show(title):
    index = show_df[show_df["title"] == title].index[0]

    recommendation_list = []
    for i in sorted(list(enumerate(similarities[index])), key=lambda x: x[1], reverse=True)[1:11]:
        recommendation_list.append(show_df.iloc[i[0]]["title"])

    return recommendation_list
