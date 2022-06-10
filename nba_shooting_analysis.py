#import matplotlib.pyplot as plt
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px



def displayData():
    df = pd.read_csv("nba_shooting_6+.csv")
    df['3FG Freq_6+'] = df['3FG Freq_6+'].str.rstrip('%').astype('float')

    #long_df = px.data.medals_long()
    fig = make_subplots(rows=1, cols=2, row_heights=[0.2, 0.8])
    f = fig.add_trace(
        go.Scatter(x=df['3FG Freq_6+'], y=df['3P%_6+'], mode= 'markers'),
        row = 1, col = 1
    )
    f['layout']['yaxis']['title'] = '3P% 6+ Feet Separation'
    f['layout']['xaxis']['title'] = '3P Frequency 6+ Feet Separation'
    #f['layout']['height']=700
    f1 = fig.add_trace(
        go.Bar(y= df['Team'], x=df['3FG Freq_6+'], showlegend= False, orientation='h'),
        row=2, col=1
    )
    f1['layout']['xaxis']['title'] = '3P Frequency 6+ Feet Separation'
    #f1['layout']['height']=1500
    fig.show()


if __name__ == '__main__':
   displayData()