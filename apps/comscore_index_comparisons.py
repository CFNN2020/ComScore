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


work_engine = create_engine('postgresql://dmp_dashboard79oygu43bw:ss244isuiqbmk9os@db-data-analysis-do-user-3211830-0.b.db.ondigitalocean.com:25060/dmp_dashboard', pool_pre_ping=True)
df_us = pd.read_sql_query(
    'select * from us_comscore_adv_audiences_gaming_index', 
    con=work_engine)

#rankings = {'country' : ['US', 'UK'], 'total_uv_rank' : [26,26], 'avg_views_per_visitor_rank' : [8,28], 'avg_views_per_visit_rank' : [14,9], 'avg_mins_per_visit_rank' : [27,18]}
#df = pd.DataFrame(data=rankings)
#fig1 = px.sunburst(df, path=['country', 'total_uv_rank', 'avg_views_per_visitor_rank', 'avg_views_per_visit_rank', 'avg_mins_per_visit_rank'], height=800, width=2000)

x = df_us['media_property']
y1 = df_us['pc_percent_reach']
y1_1 = df_us['console_percent_reach']
y1_2 = df_us['mobile_percent_reach']
y1_3 = df_us['esports_percent_reach']
y2 = df_us['pc_composition_index_uv']
y2_1 = df_us['console_composition_index_uv']
y2_2 = df_us['mobile_composition_index_uv']
y2_3 = df_us['esports_composition_index_uv']
table_data = df_us[['media_property', 'pc_percent_reach','pc_composition_index_uv']]
table_data2 = df_us[['media_property', 'console_percent_reach','console_composition_index_uv']]
table_data3 = df_us[['media_property', 'mobile_percent_reach','mobile_composition_index_uv']]
table_data4 = df_us[['media_property', 'esports_percent_reach','esports_composition_index_uv']]

fig1 = ff.create_table(table_data, height_constant=60)

trace1 = go.Bar(x=x, y=y1, name='A',marker_color='green', xaxis='x2', yaxis='y2')

trace2 = go.Scatter(x=x, y=y2, line=dict(color='red'), name='B', xaxis='x2', yaxis='y2')

fig1.add_traces([trace1,trace2])

fig1['layout']['xaxis2'] = {}
fig1['layout']['yaxis2'] = {}

# Edit layout for subplots
fig1.layout.xaxis.update({'domain': [0, .5]})
fig1.layout.xaxis2.update({'domain': [0.6, 1.]})

# The graph's yaxis MUST BE anchored to the graph's xaxis
fig1.layout.yaxis2.update({'anchor': 'x2'})


# Update the margins to add a title and see graph x-labels.
fig1.layout.margin.update({'t':50, 'b':100})

#####
fig2 = ff.create_table(table_data2, height_constant=60)

trace1_1 = go.Bar(x=x, y=y1_1, name='A',marker_color='green', xaxis='x2', yaxis='y2')

trace2_1 = go.Scatter(x=x, y=y2_1, line=dict(color='red'), name='B', xaxis='x2', yaxis='y2')

fig2.add_traces([trace1_1,trace2_1])

fig2['layout']['xaxis2'] = {}
fig2['layout']['yaxis2'] = {}

fig2.layout.xaxis.update({'domain': [0, .5]})
fig2.layout.xaxis2.update({'domain': [0.6, 1.]})


fig2.layout.yaxis2.update({'anchor': 'x2'})
fig2.layout.yaxis2.update({'title': 'test'})

fig2.layout.margin.update({'t':50, 'b':100})

#####
fig3 = ff.create_table(table_data3, height_constant=60)

trace1_2 = go.Bar(x=x, y=y1_2, name='A',marker_color='green', xaxis='x2', yaxis='y2')

trace2_2 = go.Scatter(x=x, y=y2_2, line=dict(color='red'), name='B', xaxis='x2', yaxis='y2')

fig3.add_traces([trace1_2,trace2_2])

fig3['layout']['xaxis2'] = {}
fig3['layout']['yaxis2'] = {}

fig3.layout.xaxis.update({'domain': [0, .5]})
fig3.layout.xaxis2.update({'domain': [0.6, 1.]})


fig3.layout.yaxis2.update({'anchor': 'x2'})


fig3.layout.margin.update({'t':50, 'b':100})

#####
fig4 = ff.create_table(table_data4, height_constant=60)

trace1_3 = go.Bar(x=x, y=y1_3, name='A',marker_color='green', xaxis='x2', yaxis='y2')

trace2_3 = go.Scatter(x=x, y=y2_3, line=dict(color='red'), name='B', xaxis='x2', yaxis='y2')

fig4.add_traces([trace1_3,trace2_3])
 
fig4['layout']['xaxis2'] = {}
fig4['layout']['yaxis2'] = {}

fig4.layout.xaxis.update({'domain': [0, .5]})
fig4.layout.xaxis2.update({'domain': [0.6, 1.]})


fig4.layout.yaxis2.update({'anchor': 'x2'})


fig4.layout.margin.update({'t':50, 'b':100})


layout = html.Div([

    html.Div([
        html.Br(),
        html.Div(id='output_data_1'),
        html.Br(),

        html.H1(children='US Gaming Index: composition index UV'),
        html.H1(children='Total UV', style={'fontSize': 14}),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold'}),

        dcc.Dropdown(id='us_views_dropdown',
            options=[
                    {'label': 'PC', 'value': 'pc_composition_index_uv'},
                    {'label': 'Console', 'value': 'console_composition_index_uv'},
                    {'label': 'Mobile', 'value': 'mobile_composition_index_uv'},
                    {'label': 'eSports', 'value': 'esports_composition_index_uv'},

        ],
            optionHeight=35,                    
            value='pc_composition_index_uv',                   
            disabled=False,                     
            multi=False,                        
            searchable=True,                    
            search_value='',                    
            placeholder='Please select...',     
            clearable=True,#
            style={'width':"80%", 'marigin':"auto"},                                             
            persistence=True,                 
            persistence_type='memory'         
            ),  
    ],className='three columns'),
    html.Br(),
    html.Br(),

    html.Div([
        dcc.Graph(id='us_comp_graph', 
        style={
            'align':"left"
        }),
    ]),
    html.Div(children=[
        html.Div([
            html.H1(children='PC category percent reach with pc category composition index UV'),
            html.H1(children='The following subplots outline media property percent reach (defining the media properties percentage of 100% within the given category) compared to the specfic category compostion index. < 100 == under_index, > 100 == over_index', style={'fontSize': 14}),
            html.H3(children='The below compares media property reach within the PC gaming category, indexed against the PC gaming category composition index. Any figure over 100 composition index is an over-indexing of category affinity.', style={'fontSize': 12}),
            dcc.Graph(
                id='graph_1',
                figure=fig1
            )
        ])
    ]),
    html.Div(children=[
        html.Div([
            html.H1(children='Console category percent reach with pc category composition index UV'),
            html.H2(children='The below compares media property reach within the Console gaming category, indexed against the Console gaming category composition index. Any figure over 100 composition index is an over-indexing of category affinity.',  style={'fontSize': 12}),
            dcc.Graph(
                id='graph_2',
                figure=fig2
            )
        ])
    ]),
    html.Div(children=[
        html.Div([
            html.H1(children='Mobile category percent reach with pc category composition index UV'),
            html.H2(children='The below compares media property reach within the Mobile gaming category, indexed against the Mobile gaming category composition index. Any figure over 100 composition index is an over-indexing of category affinity.', style={'fontSize': 12}),
            dcc.Graph(
                id='graph_3',
                figure=fig3
            )
        ])
    ]),
    html.Div(children=[
        html.Div([
            html.H1(children='eSports category percent reach with pc category composition index UV'),
            html.H2(children='The below compares media property reach within the eSports gaming category, indexed against the eSports gaming category composition index. Any figure over 100 composition index is an over-indexing of category affinity.', style={'fontSize': 12}),
            dcc.Graph(
                id='graph_4',
                figure=fig4
            )
        ])
    ]),
])

@app.callback(
    Output(component_id='us_comp_graph', component_property='figure'),
    Input(component_id='us_views_dropdown', component_property='value'),
)

def build_graph(column_chosen):
    fig = px.pie(df_us, values=column_chosen, names='media_property', hole=(0.4))
    return fig

'''
html.Div(children=[
    html.Div([
        html.H1(children='US and UK comparison: Gaming index PC by percent reach'),
        dcc.Graph(
            id='',
            figure=fig1
        ),
    ]),

   html.Div([
        html.H1(children='US and UK comparison: Gaming index Console by percent reach'),
        dcc.Graph(
            id='',
            figure=fig2
        ),
    ]),

    html.Div([
        html.H1(children='US and UK comparison: Gaming index Mobile by percent reach'),
        dcc.Graph(
            id='',
            figure=fig3
        ),
    ]),
    html.Div([
        html.H1(children='US and UK comparison: Gaming index eSports by percent reach'),
        dcc.Graph(
            id='',
            figure=fig4
        ),
    ]),
])
'''