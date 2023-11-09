# Custom paths

import sys
from paths import main_path
sys.path.append(main_path)

from src.evaluateAll import evaluateAll
import pandas as pd
import streamlit as st
from PIL import Image

@st.cache_data
def main():
    # Array for storing the results of each image
    centering = []  # Format -> [orientation, centering, brightness, focus]
    lightning = []
    orientation = []
    focus = []

    try:
        fileIndex = [1, 2, 4, 8, 9, 11, 12, 14, 18, 19, 20,
                     21, 22, 24, 26, 27, 28, 29, 32, 36, "REF_23"]

        # Evaluation section
        for index in fileIndex:
            file = f"{index}.PNG"
            results = evaluateAll(file)

            # Append elements to results
            centering.append(results[0])
            lightning.append(results[1])
            orientation.append(results[2])
            focus.append(results[3])

        df = pd.DataFrame(
            {'Image_Index': fileIndex, 'Centering': centering, "Lightning": lightning, "Orientation": orientation,
             "Sharpness": focus})
        return df

    except Exception as ex:
        print(ex)


def unique_img(img):
    result = evaluateAll(f"{img}.PNG")

    colors = []
    for i in result:
        if i == True:
            colors.append("green")
        else:
            colors.append("red")


    with col1:
        st.markdown(f""":{colors[0]}[Centering : Image must have maximum offset of +- 10 px]""")
        st.markdown(f""":{colors[1]}[Lightning : Image light must range between 170 and 230 mean range color]""")
        st.markdown(f""":{colors[2]}[Orientation : Image must be Oriented correctly]""")
        st.markdown(f""":{colors[3]}[Sharpness : Image must be above MTF50 reference range]""")

    col3.metric(label="Centering : ", value=result[0])
    col4.metric(label="Lightning : ", value=result[1], delta="")
    col5.metric(label="Orientation : ", value=result[2], delta="")
    col6.metric(label="Sharpness : ", value=result[3], delta="")

    with col2:
        image = Image.open(f'../data/{img}.PNG')
        st.image(image, caption=f'Image {img}')


# Streamlit Code

st.title("Bosch Hackathon - ADAS Camera Image Quality Evaluation")

st.write("This App evaluates the Centering, Lightning, Orientation and Sharpness of ISO 12233 images")

col1, col2 = st.columns([0.5, 0.5])
col3, col4, col5, col6, col7 = st.columns([0.15, 0.15, 0.15, 0.15, 0.4])

with col1:
    options = st.selectbox("Select an Option", ["Calculate Quality of all Images", "Select an Specific Image"])

    if options == "Select an Specific Image":
        img_n = st.select_slider(
            'Select an Image of the Index',
            options=[1, 2, 4, 8, 9, 11, 12, 14, 18, 19, 20,
                     21, 22, 24, 26, 27, 28, 29, 32, 36, "REF_23"])

        unique_img(img_n)

with col2:
    if options == "Calculate Quality of all Images":
        st.dataframe(main())
