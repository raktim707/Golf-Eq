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
app = DjangoDash('drivercomp', external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{'name': 'viewport', 'content': 'width-device-width, initial-scale-1.0'}])

#Import and clean data (importing csv into pandas from local machine for now)
#df = pd.read_csv('/Users/damonburrow/Desktop/Golf EQ Code/Flask App/drivervdriver.csv')

df = pd.read_csv('/home/raktim/PycharmProjects/Ecom/myshop/shop/dash_apps/finished_apps/drivervdriver.csv')
# print(df[:5])

# App page layouts
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Driver v. Driver', className='text-center mb-4'), width = {'size': 9, 'offset': 1})
    ]),

    dbc.Row([
        dbc.Col([dcc.Dropdown(id='driver1', multi=False, options=[
                        {"label": "Callaway Rogue ST Max", "value": 'Callaway Rogue ST Max'},
                        {"label": "Callaway Rogue ST Max D", "value": 'Callaway Rogue ST Max D'},
                        {"label": "Callaway Rogue ST Max LS", "value": 'Callaway Rogue ST Max LS'},
                        {"label": "Callaway Rouge ST Triple Diamond LS", "value": 'Callaway Rouge ST Triple Diamond LS'},
                        {"label": "Cobra LTDx", "value": 'Cobra LTDx'},
                        {"label": "Cobra LTDx LS", "value": 'Cobra LTDx LS'},
                        {"label": "Cobra LTDx Max", "value": 'Cobra LTDx Max'},
                        {"label": "Mizuno ST-G 220", "value": 'Mizuno ST-G 220'},
                        {"label": "Ping G425 LST", "value": 'Ping G425 LST'},
                        {"label": "Ping G425 Max", "value": 'Ping G425 Max'},
                        {"label": "Ping G425 SFT", "value": 'Ping G425 SFT'},
                        {"label": "TaylorMade Stealth", "value": 'TaylorMade Stealth'},
                        {"label": "TaylorMade Stealth HD", "value": 'TaylorMade Stealth HD'},
                        {"label": "TaylorMade Stealth Plus", "value": 'TaylorMade Stealth Plus'},
                        {"label": "Titleist TSi1", "value": 'Titleist TSi1'},
                        {"label": "Titleist TSi2", "value": 'Titleist TSi2'},
                        {"label": "Titleist TSi3", "value": 'Titleist TSi3'},
                        {"label": "Titleist TSi4", "value": 'Titleist TSi4'}
                     ], 
                     value='Callaway Rogue ST Max'
        )
        ], width = {'size': 5, 'offset': 0}),

        dbc.Col([dcc.Dropdown(id='driver2', multi=False, options=[
                        {"label": "Callaway Rogue ST Max", "value": 'Callaway Rogue ST Max'},
                        {"label": "Callaway Rogue ST Max D", "value": 'Callaway Rogue ST Max D'},
                        {"label": "Callaway Rogue ST Max LS", "value": 'Callaway Rogue ST Max LS'},
                        {"label": "Callaway Rouge ST Triple Diamond LS", "value": 'Callaway Rouge ST Triple Diamond LS'},
                        {"label": "Cobra LTDx", "value": 'Cobra LTDx'},
                        {"label": "Cobra LTDx LS", "value": 'Cobra LTDx LS'},
                        {"label": "Cobra LTDx Max", "value": 'Cobra LTDx Max'},
                        {"label": "Mizuno ST-G 220", "value": 'Mizuno ST-G 220'},
                        {"label": "Ping G425 LST", "value": 'Ping G425 LST'},
                        {"label": "Ping G425 Max", "value": 'Ping G425 Max'},
                        {"label": "Ping G425 SFT", "value": 'Ping G425 SFT'},
                        {"label": "TaylorMade Stealth", "value": 'TaylorMade Stealth'},
                        {"label": "TaylorMade Stealth HD", "value": 'TaylorMade Stealth HD'},
                        {"label": "TaylorMade Stealth Plus", "value": 'TaylorMade Stealth Plus'},
                        {"label": "Titleist TSi1", "value": 'Titleist TSi1'},
                        {"label": "Titleist TSi2", "value": 'Titleist TSi2'},
                        {"label": "Titleist TSi3", "value": 'Titleist TSi3'},
                        {"label": "Titleist TSi4", "value": 'Titleist TSi4'}
                    ],
                     value='TaylorMade Stealth'
        )
        ], width = {'size': 5, 'offset': 2})
    ]),

    dbc.Row([
        dbc.Col(html.Img(id='driver1_img', width=250, height=250), width = {'size': 3, 'offset': 0},
            align="center"), 
        dbc.Col(dcc.Graph(id='drivervdriverRadarPlot', figure={}), width = {'size': 6, 'offset': 0}),
        dbc.Col(html.Img(id='driver2_img', width=250, height=250), width = {'size': 3, 'offset': 0},
        align="center")
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='driver1_HorizontalBarPlot_direction', figure={}
        ), width = {'size': 5}),
        dbc.Col(dcc.Graph(id='driver2_HorizontalBarPlot_direction', figure={}
        ),  width = {'size': 5, 'offset': 2})
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='drivervdriverBarPlot_distance', figure={}
        ), width = {'size': 5}),

        dbc.Col(dcc.Graph(id='drivervdriverBarPlot_accuracy', figure={}
        ), width = {'size': 5, 'offset': 2}),
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='drivervdriverBarPlot_ball_speed', figure={}
        ), width = {'size': 4}),

        dbc.Col(dcc.Graph(id='drivervdriverBarPlot_launch', figure={}
        ), width = {'size': 4}),

        dbc.Col(dcc.Graph(id='drivervdriverBarPlot_spin', figure={}
        ), width = {'size': 4}),
    ]),
])


# ------------------------------------------------------------------------------
#Connect the Plotly graphs with Dash Components

#Images for Drivers
@app.callback(
    Output(component_id='driver1_img', component_property='src'),
    Input(component_id='driver1', component_property='value')
)

def update_img1(driver1):
    df1 = df.copy()
    df1 = df1[df1["club"] == driver1]
    driver1_image = df1["image"].values.tolist()
    driver1_image = driver1_image[0]
    return driver1_image


@app.callback(
    Output(component_id='driver2_img', component_property='src'),
    Input(component_id='driver2', component_property='value')
)

def update_img2(driver2):
    df2 = df.copy()
    df2 = df2[df2["club"] == driver2]
    driver2_image = df2["image"].values.tolist()
    driver2_image = driver2_image[0]
    return driver2_image

#Radar Charts for Drivers
@app.callback(
    Output(component_id='drivervdriverRadarPlot', component_property='figure'),
    [Input(component_id='driver1', component_property='value'), 
    Input(component_id='driver2', component_property='value')]
)

def update_radar(driver1, driver2):
    # print(driver1)
    # print(driver2)

    df1 = df.copy()
    df1 = df1[df1["club"] == driver1]
    club_color1 = df1['color'].values.tolist()
    club_color1 = club_color1[0]
    club_stats1 = df1[['distance', 'accuracy', 'ball_speed', 'launch', 'spin', 'dispersion']].values.tolist()
    club_stats1 = club_stats1[0]

    df2 = df.copy()
    df2 = df2[df2["club"] == driver2]
    club_color2 = df2['color'].values.tolist()
    club_color2 = club_color2[0]
    club_stats2 = df2[['distance', 'accuracy', 'ball_speed', 'launch', 'spin', 'dispersion']].values.tolist()
    club_stats2 = club_stats2[0]
    
    categories = ['Distance', 'Accuracy', 'Ball Speed', 'Launch', 'Spin', 'Forgiveness']


    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        name = driver1,
        r=club_stats1,
        theta=categories,
        line=dict(color=club_color1), fill='toself', fillcolor=club_color1, opacity=0.5
    ))
    fig.add_trace(go.Scatterpolar(
          name = driver2,
          r=club_stats2,
          theta=categories,
          line=dict(color=club_color2), fill='toself', fillcolor=club_color2, opacity=0.5
    ))

    fig.update_layout(
        title=go.layout.Title(text="{} v. {}".format(driver1, driver2), x = 0.5),
        polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 12]
        )),
    showlegend=True
    )

    return fig

#Direction Horizontal bar chart for Driver 1
@app.callback(
    Output(component_id='driver1_HorizontalBarPlot_direction', component_property='figure'),
    Input(component_id='driver1', component_property='value')
)

def update_distance(driver1):

    df1 = df.copy()
    df1 = df1[df1["club"] == driver1]
    club_color1 = df1['color'].values.tolist()
    club_color1 = club_color1[0]
    club_stats1 = df1['direction'].values.tolist()
    club_stats1 = club_stats1[0]

    fig = go.Figure([
                go.Bar(
                    x = [club_stats1], 
                    y = [driver1],
                    marker_color = [club_color1],
                    orientation = 'h'
                    )
                ]
            )

    fig.update_layout(
        title=go.layout.Title(text="{} <br> Directional Bias".format(driver1), x = 0.5),
        showlegend=False,
        yaxis={'visible': False},
        xaxis={'range': [-5, 5], 'tickvals' : [-5, -3, 0, 3, 5], 'ticktext' : ['Max Draw', 'Draw', 'Neutral', 'Fade', 'Max Fade'], 'tickangle': 45},
        height = 200
    )

    return fig

#Direction Horizontal bar chart for Driver 2
@app.callback(
    Output(component_id='driver2_HorizontalBarPlot_direction', component_property='figure'),
    Input(component_id='driver2', component_property='value')
)

def update_distance(driver2):

    df2 = df.copy()
    df2 = df2[df2["club"] == driver2]
    club_color2 = df2['color'].values.tolist()
    club_color2 = club_color2[0]
    club_stats2 = df2['direction'].values.tolist()
    club_stats2 = club_stats2[0]

    fig = go.Figure([
                go.Bar(
                    x = [club_stats2], 
                    y = [driver2],
                    marker_color = [club_color2],
                    orientation = 'h'
                    )
                ]
            )

    fig.update_layout(
        title=go.layout.Title(text="{} <br> Directional Bias".format(driver2), x = 0.5,),
        showlegend=False,
        yaxis={'visible': False},
        xaxis={'range': [-5, 5], 'tickvals' : [-5, -3, 0, 3, 5], 'ticktext' : ['Max Draw', 'Draw', 'Neutral', 'Fade', 'Max Fade'], 'tickangle': 45},
        height = 200
    )

    return fig

#Distance bar chart for Drivers
@app.callback(
    Output(component_id='drivervdriverBarPlot_distance', component_property='figure'),
    [Input(component_id='driver1', component_property='value'), 
    Input(component_id='driver2', component_property='value')]
)

def update_distance(driver1, driver2):

    df1 = df.copy()
    df1 = df1[df1["club"] == driver1]
    club_color1 = df1['color'].values.tolist()
    club_color1 = club_color1[0]
    club_stats1 = df1[['distance', 'accuracy', 'ball_speed', 'launch', 'spin']].values.tolist()
    club_stats1 = club_stats1[0]
    
    df2 = df.copy()
    df2 = df2[df2["club"] == driver2]
    club_color2 = df2['color'].values.tolist()
    club_color2 = club_color2[0]
    club_stats2 = df2[['distance', 'accuracy', 'ball_speed', 'launch', 'spin']].values.tolist()
    club_stats2 = club_stats2[0]
    
    categories = ['Distance', 'Accuracy', 'Ball Speed', 'Launch', 'Spin']

    fig = go.Figure([
                go.Bar(
                    x = [driver1, driver2], 
                    y = [club_stats1[0], club_stats2[0]],
                    marker_color = [club_color1, club_color2]
                    )
                ]
            )

    fig.update_layout(
        title=go.layout.Title(text='Driver Distances', x = 0.5),
        yaxis_title="Relative Distance Percentile",
        showlegend=False
    )

    return fig


#Accuracy bar chart for Drivers
@app.callback(
    Output(component_id='drivervdriverBarPlot_accuracy', component_property='figure'),
    [Input(component_id='driver1', component_property='value'), 
    Input(component_id='driver2', component_property='value')]
)

def update_accuracy(driver1, driver2):

    df1 = df.copy()
    df1 = df1[df1["club"] == driver1]
    club_color1 = df1['color'].values.tolist()
    club_color1 = club_color1[0]
    club_stats1 = df1[['distance', 'accuracy', 'ball_speed', 'launch', 'spin']].values.tolist()
    club_stats1 = club_stats1[0]
    
    df2 = df.copy()
    df2 = df2[df2["club"] == driver2]
    club_color2 = df2['color'].values.tolist()
    club_color2 = club_color2[0]
    club_stats2 = df2[['distance', 'accuracy', 'ball_speed', 'launch', 'spin']].values.tolist()
    club_stats2 = club_stats2[0]
    
    categories = ['Distance', 'Accuracy', 'Ball Speed', 'Launch', 'Spin']

    fig = go.Figure([
                go.Bar(
                    x = [driver1, driver2], 
                    y = [club_stats1[1], club_stats2[1]],
                    marker_color = [club_color1, club_color2]
                    )
                ]
            )

    fig.update_layout(
        title=go.layout.Title(text="Driver Accuracies", x = 0.5),
        yaxis_title="Relative Accuracy Percentile",
        showlegend=False
    )

    return fig

#Ball Speed bar chart for Drivers
@app.callback(
    Output(component_id='drivervdriverBarPlot_ball_speed', component_property='figure'),
    [Input(component_id='driver1', component_property='value'), 
    Input(component_id='driver2', component_property='value')]
)

def update_ball_speed(driver1, driver2):

    df1 = df.copy()
    df1 = df1[df1["club"] == driver1]
    club_color1 = df1['color'].values.tolist()
    club_color1 = club_color1[0]
    club_stats1 = df1[['distance', 'accuracy', 'ball_speed', 'launch', 'spin']].values.tolist()
    club_stats1 = club_stats1[0]
    
    df2 = df.copy()
    df2 = df2[df2["club"] == driver2]
    club_color2 = df2['color'].values.tolist()
    club_color2 = club_color2[0]
    club_stats2 = df2[['distance', 'accuracy', 'ball_speed', 'launch', 'spin']].values.tolist()
    club_stats2 = club_stats2[0]
    
    categories = ['Distance', 'Accuracy', 'Ball Speed', 'Launch', 'Spin']

    fig = go.Figure([
                go.Bar(
                    x = [driver1, driver2], 
                    y = [club_stats1[2], club_stats2[2]],
                    marker_color = [club_color1, club_color2]
                    )
                ]
            )

    fig.update_layout(
        title=go.layout.Title(text="Driver Ball Speeds", x = 0.5),
        yaxis_title="Relative Ball Speed Percentile",
        showlegend=False
    )

    return fig

#Launch bar chart for Drivers
@app.callback(
    Output(component_id='drivervdriverBarPlot_launch', component_property='figure'),
    [Input(component_id='driver1', component_property='value'), 
    Input(component_id='driver2', component_property='value')]
)

def update_launch(driver1, driver2):

    df1 = df.copy()
    df1 = df1[df1["club"] == driver1]
    club_color1 = df1['color'].values.tolist()
    club_color1 = club_color1[0]
    club_stats1 = df1[['distance', 'accuracy', 'ball_speed', 'launch', 'spin']].values.tolist()
    club_stats1 = club_stats1[0]
    
    df2 = df.copy()
    df2 = df2[df2["club"] == driver2]
    club_color2 = df2['color'].values.tolist()
    club_color2 = club_color2[0]
    club_stats2 = df2[['distance', 'accuracy', 'ball_speed', 'launch', 'spin']].values.tolist()
    club_stats2 = club_stats2[0]
    
    categories = ['Distance', 'Accuracy', 'Ball Speed', 'Launch', 'Spin']

    fig = go.Figure([
                go.Bar(
                    x = [driver1, driver2], 
                    y = [club_stats1[3], club_stats2[3]],
                    marker_color = [club_color1, club_color2]
                    )
                ]
            )

    fig.update_layout(
        title=go.layout.Title(text="Driver Launch Angles", x = 0.5),
        yaxis_title="Relative Launch Percentile",
        showlegend=False
    )

    return fig

#Spin bar chart for Drivers
@app.callback(
    Output(component_id='drivervdriverBarPlot_spin', component_property='figure'),
    [Input(component_id='driver1', component_property='value'), 
    Input(component_id='driver2', component_property='value')]
)

def update_spin(driver1, driver2):

    df1 = df.copy()
    df1 = df1[df1["club"] == driver1]
    club_color1 = df1['color'].values.tolist()
    club_color1 = club_color1[0]
    club_stats1 = df1[['distance', 'accuracy', 'ball_speed', 'launch', 'spin']].values.tolist()
    club_stats1 = club_stats1[0]
    
    df2 = df.copy()
    df2 = df2[df2["club"] == driver2]
    club_color2 = df2['color'].values.tolist()
    club_color2 = club_color2[0]
    club_stats2 = df2[['distance', 'accuracy', 'ball_speed', 'launch', 'spin']].values.tolist()
    club_stats2 = club_stats2[0]
    
    categories = ['Distance', 'Accuracy', 'Ball Speed', 'Launch', 'Spin']

    fig = go.Figure([
                go.Bar(
                    x = [driver1, driver2], 
                    y = [club_stats1[4], club_stats2[4]],
                    marker_color = [club_color1, club_color2]
                    )
                ]
            )

    fig.update_layout(
        title=go.layout.Title(text="Driver Backspin", x = 0.5),
        yaxis_title="Relative Spin Percentile",
        showlegend=False
    )

    return fig




