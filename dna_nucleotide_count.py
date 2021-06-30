import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
import altair as alt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plot


#import image
image1 = Image.open("C:/data/dna3.jpg")
st.image(image1, use_column_width=True)


#page title
st.write("""  
    # DNA Nucleotide Count Web App

    This app counts the nucleotide composition of query DNA

*** """)

# input text box
st.header("Enter DNA Sequence")


# text-area
sequence_input = "DNA QUERY\nAGCTTTTCATTCTGACTGCAAC\nGGGCAATATGTCTCTGTGTGGATTAA\nAAAAAGAGTGTCTGATAGCAGC"
sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # DNA QUERY text is omitted from sequence
sequence = "".join(sequence)

st.write("""  *** """)

st.header("Input (DNA Query)")
st.write(sequence)

st.header("Output (DNA Nucleotide Count)")

#print dictionary
st.subheader("Print Dictionary")
def count_dna(seq):
    data = dict([
        ("A", seq.count("A")),
        ("T", seq.count("T")),
        ("C", seq.count("C")),
        ("G", seq.count("G")),
    ])
    return data

x= count_dna(sequence)
st.write(x)
st.write("\n")

#print text
st.subheader("Print Text")
st.write("\n")
st.write("there are " + str(x["A"]) + "adenine(A)")
st.write("there are " + str(x["T"]) + "thymine(T)")
st.write("there are " + str(x["C"]) + "cytosine(C)")
st.write("there are " + str(x["G"]) + "guanine(G)")
st.write("\n")
# print dataframe
st.subheader("Print Dataframe")

d = list(x. items())
an_array = np. array(d)
df = pd.DataFrame(an_array)

df.rename(columns = {0:'Nucleotide', 1: "Count"}, inplace = True)
df
st.write("\n")


#Creating bar chart using altair

st.header("Print Bar Chart - Altair")

df["Count"]=df["Count"].astype(float)

chart = alt.Chart(df).mark_bar().encode(
    alt.X("Nucleotide"),
    y='Count',
).interactive()
chart = chart.properties(width = alt.Step(80))
st.altair_chart(chart)
st.write("\n")


#Creating bar chart using matlpotlib


st.header("Print Bar Chart - Matplotlib")

ax = df.plot.bar(x='Nucleotide', y='Count', rot=0)
plot.savefig("C:/data/mygraph.png")
image2 = Image.open("C:/data/mygraph.png")
st.image(image2, use_column_width=True)





