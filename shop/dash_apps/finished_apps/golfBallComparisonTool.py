import pandas as pd
import numpy as np
import dash
from dash import dcc
from dash import html
from PIL import Image
import plotly.express as px
import skimage.io
import plotly.graph_objects as go
from dash.dependencies import Input, Output  
import dash_bootstrap_components as dbc
import datetime
import os
from django_plotly_dash import DjangoDash


#Initialize app and set meta data for screen responsiveness
app = DjangoDash('golfcomp', external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{'name': 'viewport', 'content': 'width-device-width, initial-scale-1.0'}])

#Import and clean data (importing csv into pandas from local machine for now)
#df = pd.read_csv('/Users/damonburrow/Desktop/Golf EQ Code/Flask App/golfBallVgolfBall2022.csv')

df = pd.read_csv('/home/raktim/Downloads/pyproject/Django-dash-plotly_3/Django-dash-plotly/home/dash_apps/finished_apps/golfBallVgolfBall2022.csv')
# print(df[:5])

# App page layouts
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Golf Ball v. Golf Ball', className='text-center mb-4'), width = {'size': 9, 'offset': 1})
    ]),

    dbc.Row([
        dbc.Col([dcc.Dropdown(id='golfBall1', multi=False, options=[
                        {"label": "Bridgestone Tour B RXS", "value": 'Bridgestone Tour B RXS'},
                        {"label": "Bridgestone Tour B X", "value": 'Bridgestone Tour B X'},
                        {"label": "Bridgestone Tour B XS", "value": 'Bridgestone Tour B XS'},
                        {"label": "Callaway Chrome Soft", "value": 'Callaway Chrome Soft'},
                        {"label": "Callaway Chrome Soft X", "value": 'Callaway Chrome Soft X'},
                        {"label": "Callaway Chrome Soft X LS", "value": 'Callaway Chrome Soft X LS'},
                        {"label": "OnCore ELIXR", "value": 'OnCore ELIXR'},
                        {"label": "OnCore VERO X1", "value": 'OnCore VERO X1'},
                        {"label": "Snell MTB Black", "value": 'Snell MTB Black'},
                        {"label": "Snell MTB X", "value": 'Snell MTB X'},
                        {"label": "Srixon Q-Star Tour", "value": 'Srixon Q-Star Tour'},
                        {"label": "Srixon Z-Star", "value": 'Srixon Z-Star'},
                        {"label": "Srixon Z-Star XV", "value": 'Srixon Z-Star XV'},
                        {"label": "TaylorMade TP5", "value": 'TaylorMade TP5'},
                        {"label": "TaylorMade TP5x", "value": 'TaylorMade TP5x'},
                        {"label": "Titleist AVX", "value": 'Titleist AVX'},
                        {"label": "Titleist ProV1", "value": 'Titleist ProV1'},
                        {"label": "Titleist ProV1x", "value": 'Titleist ProV1x'},
                        {"label": "Titleist ProV1x Left Dash", "value": 'Titleist ProV1x Left Dash'},
                        {"label": "Titleist Tour Speed", "value": 'Titleist Tour Speed'}
                     ], 
                     value='Titleist ProV1'
        )
        ], width = {'size': 5, 'offset': 0}),

        dbc.Col([dcc.Dropdown(id='golfBall2', multi=False, options=[
                        {"label": "Bridgestone Tour B RXS", "value": 'Bridgestone Tour B RXS'},
                        {"label": "Bridgestone Tour B X", "value": 'Bridgestone Tour B X'},
                        {"label": "Bridgestone Tour B XS", "value": 'Bridgestone Tour B XS'},
                        {"label": "Callaway Chrome Soft", "value": 'Callaway Chrome Soft'},
                        {"label": "Callaway Chrome Soft X", "value": 'Callaway Chrome Soft X'},
                        {"label": "Callaway Chrome Soft X LS", "value": 'Callaway Chrome Soft X LS'},
                        {"label": "OnCore ELIXR", "value": 'OnCore ELIXR'},
                        {"label": "OnCore VERO X1", "value": 'OnCore VERO X1'},
                        {"label": "Snell MTB Black", "value": 'Snell MTB Black'},
                        {"label": "Snell MTB X", "value": 'Snell MTB X'},
                        {"label": "Srixon Q-Star Tour", "value": 'Srixon Q-Star Tour'},
                        {"label": "Srixon Z-Star", "value": 'Srixon Z-Star'},
                        {"label": "Srixon Z-Star XV", "value": 'Srixon Z-Star XV'},
                        {"label": "TaylorMade TP5", "value": 'TaylorMade TP5'},
                        {"label": "TaylorMade TP5x", "value": 'TaylorMade TP5x'},
                        {"label": "Titleist AVX", "value": 'Titleist AVX'},
                        {"label": "Titleist ProV1", "value": 'Titleist ProV1'},
                        {"label": "Titleist ProV1x", "value": 'Titleist ProV1x'},
                        {"label": "Titleist ProV1x Left Dash", "value": 'Titleist ProV1x Left Dash'},
                        {"label": "Titleist Tour Speed", "value": 'Titleist Tour Speed'}
                    ],
                     value='TaylorMade TP5'
        )
        ], width = {'size': 5, 'offset': 2})
    ]),

    dbc.Row([
        dbc.Col(html.Img(id='golfBall1_img', width=250, height=250), width = {'size': 3, 'offset': 0},
            align="center"), 
        dbc.Col(dcc.Graph(id='golfBallVgolfBallRadarPlot', figure={}), width = {'size': 6, 'offset': 0}),
        dbc.Col(html.Img(id='golfBall2_img', width=250, height=250), width = {'size': 3, 'offset': 0},
        align="center")
    ]),


    dbc.Row([
        dbc.Col(dcc.Graph(id='golfBallVgolfBallBarPlot_compression', figure={}
        ), width = {'size': 5}),

        dbc.Col(dcc.Graph(id='golfBallVgolfBallBarPlot_distance', figure={}
        ), width = {'size': 5, 'offset': 2}),
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='golfBallVgolfBallBarPlot_launch', figure={}
        ), width = {'size': 4}),

        dbc.Col(dcc.Graph(id='golfBallVgolfBallBarPlot_peakHeight', figure={}
        ), width = {'size': 4}),

        dbc.Col(dcc.Graph(id='golfBallVgolfBallBarPlot_spin', figure={}
        ), width = {'size': 4}),
    ]),
])


# ------------------------------------------------------------------------------
#Connect the Plotly graphs with Dash Components

#Images for Drivers
@app.callback(
    Output(component_id='golfBall1_img', component_property='src'),
    Input(component_id='golfBall1', component_property='value')
)

def update_img1(golfBall1):
    df1 = df.copy()
    df1 = df1[df1["ball"] == golfBall1]
    golfBall1_image = df1["image"].values.tolist()
    golfBall1_image = golfBall1_image[0]
    return golfBall1_image


@app.callback(
    Output(component_id='golfBall2_img', component_property='src'),
    Input(component_id='golfBall2', component_property='value')
)

def update_img2(golfBall2):
    df2 = df.copy()
    df2 = df2[df2["ball"] == golfBall2]
    golfBall2_image = df2["image"].values.tolist()
    golfBall2_image = golfBall2_image[0]
    return golfBall2_image

#Radar Charts for Drivers
@app.callback(
    Output(component_id='golfBallVgolfBallRadarPlot', component_property='figure'),
    [Input(component_id='golfBall1', component_property='value'), 
    Input(component_id='golfBall2', component_property='value')]
)

def update_radar(golfBall1, golfBall2):
    # print(driver1)
    # print(driver2)

    df1 = df.copy()
    df1 = df1[df1["ball"] == golfBall1]
    ball_color1 = df1['color'].values.tolist()
    ball_color1 = ball_color1[0]
    ball_stats1 = df1[['compression', 'launch', 'spin', 'peakHeight', 'distance']].values.tolist()
    ball_stats1 = ball_stats1[0]

    df2 = df.copy()
    df2 = df2[df2["ball"] == golfBall2]
    ball_color2 = df2['color'].values.tolist()
    ball_color2 = ball_color2[0]
    ball_stats2 = df2[['compression', 'launch', 'spin', 'peakHeight', 'distance']].values.tolist()
    ball_stats2 = ball_stats2[0]
    
    categories = ['Compression', 'Launch', 'Spin', 'Peak Height', 'Distance']


    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        name = golfBall1,
        r=ball_stats1,
        theta=categories,
        line=dict(color=ball_color1), fill='toself', fillcolor=ball_color1, opacity=0.5
    ))
    fig.add_trace(go.Scatterpolar(
          name = golfBall2,
          r=ball_stats2,
          theta=categories,
          line=dict(color=ball_color2), fill='toself', fillcolor=ball_color2, opacity=0.5
    ))

    fig.update_layout(
        title=go.layout.Title(text="{} v. {}".format(golfBall1, golfBall2), x = 0.5),
        polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 12]
        )),
    showlegend=True
    )

    return fig


#Compression bar chart for golf balls
@app.callback(
    Output(component_id='golfBallVgolfBallBarPlot_compression', component_property='figure'),
    [Input(component_id='golfBall1', component_property='value'), 
    Input(component_id='golfBall2', component_property='value')]
)

def update_compression(golfBall1, golfBall2):

    df1 = df.copy()
    df1 = df1[df1["ball"] == golfBall1]
    ball_color1 = df1['color'].values.tolist()
    ball_color1 = ball_color1[0]
    ball_stats1 = df1[['compression', 'launch', 'spin', 'peakHeight', 'distance']].values.tolist()
    ball_stats1 = ball_stats1[0]
    
    df2 = df.copy()
    df2 = df2[df2["ball"] == golfBall2]
    ball_color2 = df2['color'].values.tolist()
    ball_color2 = ball_color2[0]
    ball_stats2 = df2[['compression', 'launch', 'spin', 'peakHeight', 'distance']].values.tolist()
    ball_stats2 = ball_stats2[0]
    
    categories = ['Compression', 'Launch', 'Spin', 'Peak Height', 'Distance']

    fig = go.Figure([
                go.Bar(
                    x = [golfBall1, golfBall2], 
                    y = [ball_stats1[0], ball_stats2[0]],
                    marker_color = [ball_color1, ball_color2]
                    )
                ]
            )

    fig.update_layout(
        title=go.layout.Title(text='Golf Ball Compressions', x = 0.5),
        yaxis_title="Relative Compression",
        showlegend=False
    )

    return fig


#Distance bar chart for golf balls
@app.callback(
    Output(component_id='golfBallVgolfBallBarPlot_distance', component_property='figure'),
    [Input(component_id='golfBall1', component_property='value'), 
    Input(component_id='golfBall2', component_property='value')]
)

def update_distance(golfBall1, golfBall2):

    df1 = df.copy()
    df1 = df1[df1["ball"] == golfBall1]
    ball_color1 = df1['color'].values.tolist()
    ball_color1 = ball_color1[0]
    ball_stats1 = df1[['compression', 'launch', 'spin', 'peakHeight', 'distance']].values.tolist()
    ball_stats1 = ball_stats1[0]
    
    df2 = df.copy()
    df2 = df2[df2["ball"] == golfBall2]
    ball_color2 = df2['color'].values.tolist()
    ball_color2 = ball_color2[0]
    ball_stats2 = df2[['compression', 'launch', 'spin', 'peakHeight', 'distance']].values.tolist()
    ball_stats2 = ball_stats2[0]
    
    categories = ['Compression', 'Launch', 'Spin', 'Peak Height', 'Distance']

    fig = go.Figure([
                go.Bar(
                    x = [golfBall1, golfBall2], 
                    y = [ball_stats1[4], ball_stats2[4]],
                    marker_color = [ball_color1, ball_color2]
                    )
                ]
            )

    fig.update_layout(
        title=go.layout.Title(text="Golf Ball Distances", x = 0.5),
        yaxis_title="Relative Distance",
        showlegend=False
    )

    return fig

#Launch bar chart for golf balls
@app.callback(
    Output(component_id='golfBallVgolfBallBarPlot_launch', component_property='figure'),
    [Input(component_id='golfBall1', component_property='value'), 
    Input(component_id='golfBall2', component_property='value')]
)

def update_launch(golfBall1, golfBall2):

    df1 = df.copy()
    df1 = df1[df1["ball"] == golfBall1]
    ball_color1 = df1['color'].values.tolist()
    ball_color1 = ball_color1[0]
    ball_stats1 = df1[['compression', 'launch', 'spin', 'peakHeight', 'distance']].values.tolist()
    ball_stats1 = ball_stats1[0]
    
    df2 = df.copy()
    df2 = df2[df2["ball"] == golfBall2]
    ball_color2 = df2['color'].values.tolist()
    ball_color2 = ball_color2[0]
    ball_stats2 = df2[['compression', 'launch', 'spin', 'peakHeight', 'distance']].values.tolist()
    ball_stats2 = ball_stats2[0]
    
    categories = ['Compression', 'Launch', 'Spin', 'Peak Height', 'Distance']

    fig = go.Figure([
                go.Bar(
                    x = [golfBall1, golfBall2], 
                    y = [ball_stats1[1], ball_stats2[1]],
                    marker_color = [ball_color1, ball_color2]
                    )
                ]
            )

    fig.update_layout(
        title=go.layout.Title(text="Golf Ball Launch Angles", x = 0.5),
        yaxis_title="Relative Launch Angle",
        showlegend=False
    )

    return fig

#Peak height bar chart for golf balls
@app.callback(
    Output(component_id='golfBallVgolfBallBarPlot_peakHeight', component_property='figure'),
    [Input(component_id='golfBall1', component_property='value'), 
    Input(component_id='golfBall2', component_property='value')]
)

def update_height(golfBall1, golfBall2):

    df1 = df.copy()
    df1 = df1[df1["ball"] == golfBall1]
    ball_color1 = df1['color'].values.tolist()
    ball_color1 = ball_color1[0]
    ball_stats1 = df1[['compression', 'launch', 'spin', 'peakHeight', 'distance']].values.tolist()
    ball_stats1 = ball_stats1[0]
    
    df2 = df.copy()
    df2 = df2[df2["ball"] == golfBall2]
    ball_color2 = df2['color'].values.tolist()
    ball_color2 = ball_color2[0]
    ball_stats2 = df2[['compression', 'launch', 'spin', 'peakHeight', 'distance']].values.tolist()
    ball_stats2 = ball_stats2[0]
    
    categories = ['Compression', 'Launch', 'Spin', 'Peak Height', 'Distance']

    fig = go.Figure([
                go.Bar(
                    x = [golfBall1, golfBall2], 
                    y = [ball_stats1[3], ball_stats2[3]],
                    marker_color = [ball_color1, ball_color2]
                    )
                ]
            )

    fig.update_layout(
        title=go.layout.Title(text="Golf Ball Peak Heights", x = 0.5),
        yaxis_title="Relative Peak Heights",
        showlegend=False
    )

    return fig

#Spin bar chart for golf balls
@app.callback(
    Output(component_id='golfBallVgolfBallBarPlot_spin', component_property='figure'),
    [Input(component_id='golfBall1', component_property='value'), 
    Input(component_id='golfBall2', component_property='value')]
)

def update_spin(golfBall1, golfBall2):

    df1 = df.copy()
    df1 = df1[df1["ball"] == golfBall1]
    ball_color1 = df1['color'].values.tolist()
    ball_color1 = ball_color1[0]
    ball_stats1 = df1[['compression', 'launch', 'spin', 'peakHeight', 'distance']].values.tolist()
    ball_stats1 = ball_stats1[0]
    
    df2 = df.copy()
    df2 = df2[df2["ball"] == golfBall2]
    ball_color2 = df2['color'].values.tolist()
    ball_color2 = ball_color2[0]
    ball_stats2 = df2[['compression', 'launch', 'spin', 'peakHeight', 'distance']].values.tolist()
    ball_stats2 = ball_stats2[0]
    
    categories = ['Compression', 'Launch', 'Spin', 'Peak Height', 'Distance']

    fig = go.Figure([
                go.Bar(
                    x = [golfBall1, golfBall2], 
                    y = [ball_stats1[2], ball_stats2[2]],
                    marker_color = [ball_color1, ball_color2]
                    )
                ]
            )

    fig.update_layout(
        title=go.layout.Title(text="Golf Ball Backspins", x = 0.5),
        yaxis_title="Relative Backspin",
        showlegend=False
    )

    return fig



