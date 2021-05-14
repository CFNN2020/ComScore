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

   
work_engine = create_engine('postgresql://dmp_dashboard79oygu43bw:ss244isuiqbmk9os@db-data-analysis-do-user-3211830-0.b.db.ondigitalocean.com:25060/dmp_dashboard', pool_pre_ping=True)
df_entities = pd.read_sql_query('select * from comscore_entity_status', con=work_engine)
updated_list = pd.read_sql_query('select * from comscore_updated_list', con=work_engine)

table_data = [['status', 'count'],['Eligible', 34],['Get Tag', 31], ['Private', 2], ['Public', 31], ['Tagged', 1]]
fig1 = ff.create_table(table_data, height_constant=30)
status = ['Eligible', 'Get Tag', 'Private', 'Public', 'Tagged']
count = [34, 31, 2, 31, 1]
trace1 = go.Bar(x=status, y=count, xaxis='x2', yaxis='y2', name='Network N entity status')
fig1.add_traces(trace1)
fig1['layout']['xaxis2'] = {}
fig1['layout']['yaxis2'] = {}

# Edit layout for subplots
fig1.layout.yaxis.update({'domain': [0, .45]})
fig1.layout.yaxis2.update({'domain': [.6, 1]})

# The graph's yaxis2 MUST BE anchored to the graph's xaxis2 and vice versa
fig1.layout.yaxis2.update({'anchor': 'x2'})
fig1.layout.xaxis2.update({'anchor': 'y2'})
fig1.layout.yaxis2.update({'title': 'Goals'})

# Update the margins to add a title and see graph x-labels.
fig1.layout.margin.update({'t':75, 'l':50})
fig1.layout.update({'title': 'Network N entities'})

# Update the height because adding a graph vertically will interact with
# the plot height calculated for the table

fig1.layout.update({'height':800})

fig2 = go.Figure(data=[go.Table(
    header = dict(values = list(df_entities.columns), 
    fill_color ='paleturquoise',
    align = 'left'),
    cells =dict(values=[df_entities.index, df_entities.status, df_entities.entity_name, df_entities.eligibility, df_entities.data_last_received],
    align='left'))
])

fig3 = go.Figure(data=[go.Table(
    header = dict(values = list(updated_list.columns), 
    fill_color ='paleturquoise',
    align = 'left'),
    cells =dict(values=[updated_list.index, updated_list.Site, updated_list.Domain, updated_list.Status],
    align='left'))
])


layout = html.Div(children=[
    html.Div([
        html.H1(children='Network deployment status, custom entity list, data ingestion volumes and tag deployment'),
        html.Div(children=''' 
            Internal use only[auditing]
            '''),
    ]),
    html.Div(html.P(html.Br())),
    html.Div(html.P(html.Br())),
    html.Div([
        html.H1(children='Network N entity status'),

        html.Div(children='''
            Network N only [current entity volumes and deployment]
        '''),

        dcc.Graph(
            id='figuref',
            figure=fig1
        ),
    ]),
    html.Div(html.P(html.Br())),
    html.Div(html.P(html.Br())),
    html.Div([
        html.H1(children='Network N entity list'),

        html.Div(children=''' 
            Network N only [current entity and domain status]
        '''),

        dcc.Graph(
            id='table_e',
            figure=fig2
        ),
    ]),
    html.Div(html.P(html.Br())),
    html.Div(html.P(html.Br())),
    html.Div([
        html.H1(children='Network N added domain list'),

        html.Div(children=''' 
            Network N only [current entity and domain list]
        '''),

        dcc.Graph(
            id='table_2',
            figure=fig3
        ),
    ])
])