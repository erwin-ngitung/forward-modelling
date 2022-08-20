import streamlit as st
from PIL import Image
from tools import table_html
from tools import processing_data
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

# Title
st.markdown("<h1 style=\"text-align:center;\">Forward Gravity Modelling</h1>", unsafe_allow_html=True)
st.markdown("<svg width=\"705\" height=\"5\"><line x1=\"0\" y1=\"2.5\" x2=\"705\" y2=\"2.5\" stroke=\"black\" "
            "stroke-width=\"4\" fill=\"black\" /></svg>", unsafe_allow_html=True)

# Your Biography - Sidebar
link = r"images/Erwin Fernanda.jpg"
img = Image.open(link)
# st.sidebar.image(img, width=100)

st.sidebar.markdown("<h1 style=\"text-align:center;\">My Biography</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style=\"text-align:center;\">Erwin Fernanda</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p style=\"text-align:center;\">Mathematics Researcher | Data Science Enthusiast | Machine "
                    "Learning Engineer</p>", unsafe_allow_html=True)

data = {"Contact": ["088296455284"],
        "Email": ["fernandaerwin277@gmail.com"],
        "LinkedIn": ["www.linkedin.com/in/erwin-fernanda/"],
        "GitHub": ["github.com/erwinfernanda"]}

st.sidebar.markdown("<h2 style=\"text-align:center;\">About Me</h2>", unsafe_allow_html=True)
st.sidebar.markdown(table_html.create_table_rotate(data), unsafe_allow_html=True)

# Introduction
st.header("Introduction")
st.markdown("Based on paper Gravity and Density Relationship (Forward Modelling) "
            "[Mohammed El-Tokhey, et al, $2015$, International Journal of Scientific & Engineering Research, "
            "Volume $6$, Issue $1$, January-$2015$ ISSN $2229−5518$] terrain gravitation $g$ at a point $𝑃$ that "
            "generated by three dimensional at depth $z$, distance of mass point with anomaly $r$,"
            " and contrast of density with surroundings is $p$ mathematically can formulated as follows:")
st.latex("g_z = \\int_{}^{P} G \\cdot \\triangle p \\cdot \\frac{z}{r^3} dv")
st.markdown("<svg width=\"700\" height=\"5\"><line x1=\"0\" y1=\"2.5\" x2=\"700\" y2=\"2.5\" stroke=\"black\" "
            "stroke-width=\"4\" fill=\"black\" /></svg>", unsafe_allow_html=True)

# Basic Theory
st.header("Basic Theory")

model_anomaly = st.selectbox("Choose your model anomaly:", ["The Sphere",
                                                            "The Horizontal Cylinder",
                                                            "The Dipping Thin Sheet with Finite Length",
                                                            "The Semi-Infinite Horizontal Sheet"])

if model_anomaly == "The Sphere":
    st.markdown("The attraction at any external point of a homogeneous solid sphere to the attraction of a point mass "
                "located at it's center and can be computed from simple form:")
    st.latex("g_z (mgal) = \\frac{G \\cdot \\triangle p \\cdot V \\cdot z}{(x^{2} + z^{2})^{\\frac{3}{2}}}")
    st.markdown("Keterangan:")
    st.latex("\\begin{align*}"
             "g_z &= \\text{is the vertical component of attraction force.} \\\\"
             "G &= \\text{is universal gravity constant ($6.67 \\times 10^{-11}$ m$^{3}$ Kg$^{-1}$ s$^{-2}$).} \\\\"
             "\\triangle p (kg/m^{3}) &= \\text{is density contrast of the sphere.} \\\\"
             "V (m^{3}) &= \\text{is the volume of the sphere.} \\\\"
             "z (m) &= \\text{is the depth of the center of sphere.} \\\\"
             "x (m) &= \\text{is the location of calculation point.}"
             "\\end{align*}")

elif model_anomaly == "The Horizontal Cylinder":
    st.markdown("The attraction at any external point of a homogeneous solid horizontal cylinder to the attraction of "
                "a point mass located at it's center and can be computed from simple form:")
    st.latex("g_z (mgal) = \\frac{2 \\cdot G \\cdot \\pi \\cdot a^{2} \\cdot z \\cdot \\triangle p}{(x^{2} + z^{2})}")
    st.markdown("Keterangan:")
    st.latex("\\begin{align*}"
             "g_z &= \\text{is the vertical component of attraction force.} \\\\"
             "G &= \\text{is universal gravity constant ($6.67 \\times 10^{-11}$ m$^{3}$ Kg$^{-1}$ s$^{-2}$).} \\\\"
             "\\triangle p (kg/m^{3}) &= \\text{is density contrast of the sphere.} \\\\"
             "a (m) &= \\text{is the radius of cylinder.} \\\\"
             "z (m) &= \\text{is the depth of the center of sphere.} \\\\"
             "x (m) &= \\text{is the location of calculation point.}"
             "\\end{align*}")

elif model_anomaly == "The Dipping Thin Sheet with Finite Length":
    st.markdown("The vertical gravitational attraction of dipping thin sheet with an inclination $(\\alpha)$ equal "
                "($90^{o}$ dipping angle) with horizontal plan and has finite length $(l)$ and thickness $(T)$ can be"
                "computed from the following form:")
    st.latex("g_z (mgal) = \\frac{2 \\cdot G \\cdot \\triangle p \\cdot T}{\sin \\alpha \\cdot ln \\left ( \\frac{r_2}"
             "{r_1} \\right ) - \\left ( \\theta_{1} + \\theta_{2} \\right ) \\cdot \\alpha}")
    st.markdown("Keterangan:")
    st.latex("\\begin{align*}"
             "g_z &= \\text{is the vertical component of attraction force.} \\\\"
             "G &= \\text{is universal gravity constant ($6.67 \\times 10^{-11}$ m$^{3}$ Kg$^{-1}$ s$^{-2}$).} \\\\"
             "\\triangle p (kg/m^{3}) &= \\text{is density contrast of the sphere.} \\\\"
             "T (m) &= \\text{is the thickness.} \\\\"
             "a (^{o}) &= \\text{is the anomaly angle.} \\\\"
             "r_1 (m) &= \\sqrt{x^2 + h^2} \\\\"
             "r_2 (m) &= \\sqrt{(x + l \\cdot \\cos \\alpha)^2 + (h + l \\cdot \\sin \\alpha)^2}"
             "\\end{align*}")

elif model_anomaly == "The Semi-Infinite Horizontal Sheet":
    st.markdown("If the horizontal sheet sheet has infinity in one direction, the vertical gravity attraction $g$,"
                "will be as follows:")
    st.latex(
        "g_z (mgal) = \\frac{2 \\cdot G \\cdot \\triangle p \\cdot T}{\\frac{\\pi}{2} - \\tan^{-1} (\\frac{x}{z})}")
    st.markdown("Keterangan:")
    st.latex("\\begin{align*}"
             "g_z &= \\text{is the vertical component of attraction force.} \\\\"
             "G &= \\text{is universal gravity constant ($6.67 \\times 10^{-11}$ m$^{3}$ Kg$^{-1}$ s$^{-2}$).} \\\\"
             "\\triangle p (kg/m^{3}) &= \\text{is density contrast of the sphere.} \\\\"
             "T (m) &= \\text{is the thickness.} \\\\"
             "z (m) &= \\text{is the depth of the center of thin sheet.} \\\\"
             "x (m) &= \\text{is the location of calculation point.}"
             "\\end{align*}")

else:
    st.markdown("Please write with correct your model anomaly!")

st.markdown("<svg width=\"700\" height=\"5\"><line x1=\"0\" y1=\"2.5\" x2=\"700\" y2=\"2.5\" stroke=\"black\" "
            "stroke-width=\"4\" fill=\"black\" /></svg>", unsafe_allow_html=True)

# Forward Modelling
st.header("Forward Modelling")
st.subheader("Parameter Data")

col1, col2 = st.columns(2)

if model_anomaly == "The Sphere":
    with col1:
        xo = st.number_input("Input start position (x-axis) you want: (m)")
        delta_x = st.number_input("Input spacing position (x-axis) model you want: (m)")
        do = st.number_input("Input center position (x-axis) anomaly you want: (m)")

    with col2:
        xt = st.number_input("Input end position (x-axis) model you want: (m)")
        r = st.number_input("Input radius anomaly you want: (m)")
        zo = st.number_input("Input depth anomaly you want: (m)")

    p = st.number_input("Input density anomaly you want: (kg/m^3)")

    data_input = [model_anomaly, p, r, do, zo, xo, xt, delta_x]
    data_column = {"Position (x-axis)": 0,
                   "Gravity Calculated (10e-9 m/s^2)": 0,
                   "Density (kg/m^3)": p,
                   "Radius (m)": r,
                   "Start Position Anomaly (m)": do,
                   "Depth Anomaly (m)": zo}

elif model_anomaly == "The Horizontal Cylinder":
    with col1:
        xo = st.number_input("Input start position (x-axis) you want: (m)")
        delta_x = st.number_input("Input spacing position (x-axis) model you want: (m)")
        do = st.number_input("Input center position (x-axis) anomaly you want: (m)")

    with col2:
        xt = st.number_input("Input end position (x-axis) model you want: (m)")
        r = st.number_input("Input radius anomaly you want: (m)")
        zo = st.number_input("Input depth anomaly you want: (m)")

    p = st.number_input("Input density anomaly you want: (kg/m^3)")

    data_input = [model_anomaly, p, r, do, zo, xo, xt, delta_x]
    data_column = {"Position (x-axis)": 0,
                   "Gravity Calculated (10e-9 m/s^2)": 0,
                   "Density (kg/m^3)": p,
                   "Radius (m)": r,
                   "Start Position Anomaly (m)": do,
                   "Depth Anomaly (m)": zo}

elif model_anomaly == "The Dipping Thin Sheet with Finite Length":
    with col1:
        xo = st.number_input("Input start position (x-axis) you want: (m)")
        delta_x = st.number_input("Input spacing position (x-axis) model you want: (m)")
        do = st.number_input("Input start position (x-axis) anomaly you want: (m)")
        t = st.number_input("Input thickness anomaly you want: (m)")

    with col2:
        xt = st.number_input("Input end position (x-axis) model you want: (m)")
        a = st.number_input("Input angle anomaly you want: (m)")
        zo = st.number_input("Input depth anomaly you want: (m)")
        l = st.number_input("Input length anomaly you want: (m)")

    p = st.number_input("Input density anomaly you want: (kg/m^3)")

    data_input = [model_anomaly, p, t, l, do, zo, xo, xt, delta_x, a]
    data_column = {"Position (x-axis)": 0,
                   "Gravity Calculated (10e-9 m/s^2)": 0,
                   "Density (kg/m^3)": p,
                   "Thickness (m)": t,
                   "Length (m)": l,
                   "Start Position Anomaly (m)": do,
                   "Depth Anomaly (m)": zo,
                   "Angle (degree)": a}

elif model_anomaly == "The Semi-Infinite Horizontal Sheet":
    with col1:
        xo = st.number_input("Input start position (x-axis) you want: (m)")
        delta_x = st.number_input("Input spacing position (x-axis) model you want: (m)")
        do = st.number_input("Input start position (x-axis) anomaly you want: (m)")
        t = st.number_input("Input thickness anomaly you want: (m)")

    with col2:
        xt = st.number_input("Input end position (x-axis) model you want: (m)")
        p = st.number_input("Input density anomaly you want: (kg/m^3)")
        zo = st.number_input("Input depth anomaly you want: (m)")
        l = st.number_input("Input length anomaly you want: (m)")

    data_input = [model_anomaly, p, t, l, do, zo, xo, xt, delta_x]
    data_column = {"Position (x-axis)": 0,
                   "Gravity Calculated (10e-9 m/s^2)": 0,
                   "Density (kg/m^3)": p,
                   "Thickness (m)": t,
                   "Length (m)": l,
                   "Start Position Anomaly (m)": do,
                   "Depth Anomaly (m)": zo}

else:
    st.markdown("Please write with correct your model anomaly!")

st.subheader("Visualization Data")

data_cal = processing_data.gravity_calculated(data_input)
data_columns = tuple(data_column.keys())
dataset = np.eye(len(data_cal[0]), len(data_columns))

for i in range(len(data_columns)):
    for j in range(len(data_cal[0])):
        if i == 0:
            dataset[j][i] = data_cal[i][j]
        elif i == 1:
            dataset[j][i] = data_cal[i][j] * 1e10
        else:
            dataset[j][i] = data_column[data_columns[i]]

dataset = pd.DataFrame(dataset, columns=data_column)
st.write(dataset)


def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


csv = convert_df(dataset)

st.download_button(
     label="Download data as CSV File",
     data=csv,
     file_name='Forward Modelling Data.csv',
     mime='text/csv',
 )

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))
ax[0].plot(data_cal[0], data_cal[1])
ax[0].grid()
ax[0].set_title("Plot Graph Gravity Acceleration")
ax[0].set_ylim(min(data_cal[1]) - 0.1 * min(data_cal[1]), max(data_cal[1]) + 0.1 * max(data_cal[1]))
ax[0].set_xlabel("Spacing position $(m)$")
ax[0].set_ylabel("Gravity acceleration $\\left ( \\frac{m}{s^2} \\right )$")

ax[1].set_xlim(xo, xt + delta_x, delta_x)
ax[1].set_ylim(0, 2 * zo, 50)
ax[1].grid()
ax[1].invert_yaxis()
ax[0].set_title("Plot Graph Visualization Anomaly Body")
ax[1].set_xlabel("Spacing Line $(m)$")
ax[1].set_ylabel("Depth $(m)$")

if model_anomaly == "The Sphere":
    circle = plt.Circle((do, zo), r, fill=True)
    ax[1].add_artist(circle)

elif model_anomaly == "The Horizontal Cylinder":
    circle = plt.Circle((do, zo), r, fill=True)
    ax[1].add_artist(circle)

elif model_anomaly == "The Dipping Thin Sheet with Finite Length":
    rect = mpatches.Rectangle((do - 0.5 * l, zo - 0.5 * t), l, t,
                              fill=True,
                              color="blue",
                              linewidth=2,
                              angle=a)
    ax[1].add_patch(rect)


elif model_anomaly == "The Semi-Infinite Horizontal Sheet":
    rect = mpatches.Rectangle((do - 0.5 * l, zo - 0.5 * t), l, t,
                              fill=True,
                              color="blue",
                              linewidth=2,
                              angle=0)
    ax[1].add_patch(rect)

st.pyplot(fig)

img = plt.savefig("Forward Modelling Image.png")

with open("Forward Modelling Image.png", "rb") as file:
    btn = st.download_button(
        label="Download image",
        data=file,
        file_name="Forward Modelling Image.png",
        mime="image/png")
