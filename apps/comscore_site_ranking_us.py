import pandas as pd
from sqlalchemy import create_engine
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
from plotly.subplots import make_subplots
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import numpy as np
from app import app

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

   
work_engine = create_engine('postgresql://doadmin:d86f7w5kk4lei9pd@db-data-analysis-do-user-3211830-0.b.db.ondigitalocean.com:25060/dmp_dashboard', pool_pre_ping=True)
df_sites = pd.read_sql_query('select * from comscore_site_rankings', con=work_engine)
us_feb = pd.read_sql_query('select * from us_site_rankings_feb', con=work_engine)
joined_engagement = pd.read_sql_query('select * from us_joined_site_rankings', con=work_engine)

fig1 = go.Figure()

x = df_sites['media_property']
x2 = us_feb['media_property']
y = df_sites['total_uv_in_thousands']
y2 = us_feb['total_uv_in_thousands']


trace_1 = go.Bar(x=x, y=y, name='feb_data')
trace_2 = go.Bar(x=x2, y=y2, name='nov_data', visible=False)

fig1.add_traces([trace_1, trace_2])

fig1.update_layout(
    updatemenus = list([
        dict(active=0,
            showactive = True,
            buttons=list([   
                dict(label = "Feb 2021",
                    method = "update",
                    args = [{"visible": [True, False]}]), # hide trace2
                dict(label = "Nov 2020",
                    method = "update",
                    args = [{"visible": [False, True]}]) # hide trace1
                ]))
            ]),
),
fig1.update_layout(paper_bgcolor="#acc4cc", margin=dict(t=0, b=0, l=0, r=0))
fig1.update_yaxes(type='linear')
fig1.update_yaxes(tickformat=",f")
fig1.update_traces(marker_color='green')

nov = joined_engagement['nov_avg_mins_per_visit']
feb = joined_engagement['feb_avg_mins_per_visit']
x = joined_engagement['media_property']

fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=feb,
    y=x,
    marker=dict(color="crimson", size=12),
    mode="markers",
    name="Nov 2020"
))

fig2.add_trace(go.Scatter(
    x=nov,
    y=x,
    marker=dict(color="gold", size=12),
    mode="markers",
    name="Feb 2021"
))

fig2.update_layout(title="Site engagement, quarter by quarter",
                    xaxis_title="avg_mins_per_visit",
                    yaxis_title='site')
fig2.update_layout(autosize=True, paper_bgcolor="#acc4cc")


fig3 = px.scatter(df_sites, y='avg_mins_per_visit', x='avg_mins_per_visitor', color='media_property')
fig3.update_layout(paper_bgcolor="#acc4cc")
fig4 = px.scatter(df_sites, y='avg_views_per_visit', x='avg_mins_per_visit', color='media_property')
fig4.update_layout(paper_bgcolor="#acc4cc")

layout = html.Div(children=[
    html.Div([
        html.H1(children='PCGamesN and competitor sites by UV'), 
        html.H2(children='US site visitors and views include key competitor sites and PCGN', style={'fontSize':14}),
        dcc.Graph(
            id='site_bar',
            figure=fig1
        ),
        html.Div(html.P(html.Br())),
        html.Div(html.P(html.Br())),
        html.Div(html.P(html.Br())),
        html.Div(html.P(html.Br())),
        
    ]),
   html.Div([
        html.H1(children='Dot plot of sites, by avg mins per visit, quarter by quarter comparison'),
        html.H2(children='The below split is show by site and avg minutes per visit', style={'fontSize':14}),
        html.Div(html.P(html.Br())),
        html.Div(html.P(html.Br())),
        html.Div(html.P(html.Br())),
        html.Div(html.P(html.Br())),
        dcc.Graph(
            id='sunburst',
            figure=fig2
        ),
        html.Div(html.P(html.Br())),
        html.Div(html.P(html.Br())),
    ]), 
    html.Div([
        html.H1(children='Scatter graph comparing avg minutes spent per visit and visitor'),
        html.H2(children='The below scatter examines the relationship between mins per visit and visitor from each site', style={'fontSize':14}),
        html.Div(html.P(html.Br())),
        html.Div(html.P(html.Br())),
        dcc.Graph(
            id='scatter',
            figure=fig3
        ),
    ]),
    html.Div([
        html.H1(children='Scatter graph comparing avg views per visit and mins per visit'),
        html.H2(children='The below scatter examines the relationship between views per visit and visitor from each site', style={'fontSize':14}),
        html.Div(html.P(html.Br())),
        html.Div(html.P(html.Br())),
        dcc.Graph(
            id='scatter2',
            figure=fig4
        ),
    ])
])
