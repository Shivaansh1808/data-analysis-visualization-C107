import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("pixelmath.csv")
studentdf = df.loc[df["student_id"]== "TRL_zny"]

mean = studentdf.groupby("level")["attempt"].mean()
print(mean)

fig = go.Figure(go.Bar(x=mean,y=["level1", "level2", "level3", "level4"], orientation="h"))
fig.show()