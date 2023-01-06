import requests


def get_poster_url(movie_name):
    name = ""
    for i in movie_name:
        if i == " ":
            name += "%20"
        else:
            name += i

    url = "https://api.themoviedb.org/3/search/multi?api_key=e766eeeab9ba01bc2aa7867eeefecbd9&query={}&page=1&include_adult=true".format(
        name)

    website_url = "https://image.tmdb.org/t/p/w500"

    image_url = ''

    response = requests.get(url)
    print("nulltype:", response.json()['results'])

    if not response.json()['results']:
        return "not found"
    else:
        try:
            image_url = response.json()['results'][0]['poster_path']
            if image_url is None:
                return "not found"
        except:
            print("not")
        return website_url + image_url
