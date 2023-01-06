import streamlit as st
from st_clickable_images import clickable_images
import base64

images = []
for file in ["Assets/Netflix.png", "Assets/Amazon_Prime.png", "Assets/Hulu.png", "Assets/Hotstar.webp"]:
    with open(file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        images.append(f"data:image/jpeg;base64,{encoded}")

clicked = clickable_images(
    images,
    titles=[f"Image #{str(i)}" for i in range(4)],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)

txt = ""
if clicked == 0:
    txt = "Netflix"
elif clicked == 1:
    txt = "Prime Video"
elif clicked == 2:
    txt = "Hulu"
elif clicked == 3:
    txt = "Hotstar"

if clicked > -1:
    st.write(txt, "is selected")
else:
    st.write("")