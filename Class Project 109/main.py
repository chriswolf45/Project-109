import pandas as pd 
import plotly.figure_factory as ff
import csv
df = pd.read_csv("StudentsPerformance.csv")
fig = ff.create_distplot([df["math score"].tolist()],["math score"],show_hist = False)
fig.show()