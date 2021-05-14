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

#sql engine

'''
html.H1(children='Network N gaming rankings'),
        html.H2(children='Network N gaming rankings vs top 50 listed properties. This sunburst shows the rankings for US and UK, broken down by total uv ranking, avg views per visitor ranking, avg views per visit ranking and avg mins per visit ranking', style={'fontSize': 14}),

        dcc.Graph(
            id='sunburst ranking',
            figure=fig1
        ),
    ]), 
'''

#drop totaL digital population row

work_engine = create_engine('postgresql://dmp_dashboard79oygu43bw:ss244isuiqbmk9os@db-data-analysis-do-user-3211830-0.b.db.ondigitalocean.com:25060/dmp_dashboard', pool_pre_ping=True)
df = pd.read_sql_query('select * from us_comscore_adv_audiences_gaming_index', con=work_engine)
df2 = pd.read_sql_query('select * from uk_comscore_adv_audiences_gaming_index', con=work_engine)


#rankings = {'country' : ['US', 'UK'], 'total_uv_rank' : [26,26], 'avg_views_per_visitor_rank' : [8,28], 'avg_views_per_visit_rank' : [14,9], 'avg_mins_per_visit_rank' : [27,18]}
#df = pd.DataFrame(data=rankings)
#fig1 = px.sunburst(df, path=['country', 'total_uv_rank', 'avg_views_per_visitor_rank', 'avg_views_per_visit_rank', 'avg_mins_per_visit_rank'], height=800, width=2000)
df.drop(axis=0, index=0, inplace=True)
df2.drop(axis=0, index=0, inplace=True)



layout = html.Div([

    html.Div([

        html.Br(),
        html.Div(id='output_data_2'),
        html.Br(),

        

        html.H1(children='US Gaming Index: percent reach'),
        html.H1(children='Percent reach by vertical and media property', style={'fontSize': 14}),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold'}),

        dcc.Dropdown(id='reach_dropdown',
            options=[
                     {'label': 'PC', 'value': 'pc_percent_reach'},
                     {'label': 'Console', 'value': 'console_percent_reach'},
                     {'label': 'Mobile', 'value': 'mobile_percent_reach'},
                     {'label': 'eSports', 'value': 'esports_percent_reach'},
            ],
            optionHeight=35,                  #height/space between dropdown options
            value='pc_percent_reach',                    #dropdown value selected automatically when page loads
            disabled=False,                     #disable dropdown value selection
            multi=False,                        #allow multiple dropdown values to be selected
            searchable=True,                    #allow user-searching of dropdown values
            search_value='',                    #remembers the value searched in dropdown
            placeholder='Please select...',     #gray, default text shown when no option is selected
            clearable=True,
            style={'width':"80%", 'align':"center"},                     #allow user to removes the selected value
                         #use dictionary to define CSS styles of your dropdown
            # className='select_box',           #activate separate CSS document in assets folder
            persistence=True,                 #remembers dropdown value. Used with persistence_type
            persistence_type='memory'         #remembers dropdown value selected until...
            ),                                  #'memory': browser tab is refreshed
                                                #'session': browser tab is closed
                                                #'local': browser cookies are deleted
    ],className='four columns'),

    html.Div([
        dcc.Graph(id='reach_graph',
        style={
            'margin-left':"auto",
            'margin-right':"auto"
        }),
    ],
    
    className='six columns'),

    html.Div([

        html.Br(),
        html.Div(id='output_data_3'),
        html.Br(),

        
        html.H1(children='US Gaming Index: average views per visit'),
        html.H1(children='Avgerage views per visit by vertical and media property', style={'fontSize': 14}),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold'}),

        dcc.Dropdown(id='avg_views_dropdown',
            options=[
                     {'label': 'PC', 'value': 'pc_avg_views_per_visit'},
                     {'label': 'Console', 'value': 'console_avg_views_per_visit'},
                     {'label': 'Mobile', 'value': 'mobile_avg_views_per_visit'},
                     {'label': 'eSports', 'value': 'esports_avg_views_per_visit'},
            ],
            optionHeight=35,                  
            value='pc_avg_views_per_visit',                    
            disabled=False,                     
            multi=False,                        
            searchable=True,                    
            search_value='',                    
            placeholder='Please select...',     
            clearable=True,
            style={'width':"80%", 'align':"center"},                    
                         
           
            persistence=True,                 
            persistence_type='memory'       
            ),                                  
                                              
    ],className='four columns'),

    html.Div([
        dcc.Graph(id='avg_views_graph',
        style={
            'margin-left':"auto",
            'margin-right':"auto"
        }),
    ],
    
    className='six columns'),  

    html.Div([

        html.Br(),
        html.Div(id='output_data_4'),
        html.Br(),


        html.H1(children='US Gaming Index: average minutes per visit'),
        html.H1(children='Average minutes per visit by vertical and media property', style={'fontSize': 14}),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold'}),

        dcc.Dropdown(id='avg_mins_dropdown',
            options=[
                     {'label': 'PC', 'value': 'pc_avg_mins_per_visit'},
                     {'label': 'Console', 'value': 'console_avg_mins_per_visit'},
                     {'label': 'Mobile', 'value': 'mobile_avg_mins_per_visit'},
                     {'label': 'eSports', 'value': 'esports_avg_mins_per_visit'},
            ],
            optionHeight=35,                 
            value='pc_avg_views_per_visit',                    
            disabled=False,                     
            multi=False,                        
            searchable=True,                    
            search_value='',                    
            placeholder='Please select...',     
            clearable=True,
            style={'width':"80%", 'align':"center"},                     
                         
           
            persistence=True,                 
            persistence_type='memory'         
            ),                                 
    ],className='four columns'),

    html.Div([
        dcc.Graph(id='avg_mins_graph',
        style={
            'margin-left':"auto",
            'margin-right':"auto"
        }),
    ],
    
    
    className='six columns'),  

    html.Div([
        html.Br(),
        html.Div(id='output_data_5'),
        html.Br(),


        html.H1(children='UK Gaming Index: total UV'),
        html.H1(children='Total UV by vertical and media property', style={'fontSize': 14}),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold'}),

        dcc.Dropdown(id='views_dropdown_2',
        options=[
                     {'label': 'PC', 'value': 'pc_total_views_per_million'},
                     {'label': 'Console', 'value': 'console_total_views_per_million'},
                     {'label': 'Mobile', 'value': 'mobile_total_views_per_million'},
                     {'label': 'eSports', 'value': 'esports_total_views_per_million'},
            ],
        optionHeight=35,                 
            value='pc_total_views_per_million',                    
            disabled=False,                     
            multi=False,                        
            searchable=True,                    
            search_value='',                    
            placeholder='Please select...',     
            clearable=True,
            style={'width':"80%", 'align':"center"},                     
                         
           
            persistence=True,                 
            persistence_type='memory'         
            ),                                 
    ],className='four columns'),

    html.Div([
        dcc.Graph(id='views_graph_2',
        style={
            'margin-left':"auto",
            'margin-right':"auto"
        }),
    ],
    className='six columns'),  
])

#---------------------------------------------------------------
# Connecting the Dropdown values to the graph
@app.callback(
    [Output(component_id='reach_graph', component_property='figure'),
    Output(component_id='avg_views_graph', component_property='figure'),
    Output(component_id='avg_mins_graph', component_property='figure'),
    Output(component_id='views_graph_2', component_property='figure')],
    [Input(component_id='reach_dropdown', component_property='value'),
    Input(component_id='avg_views_dropdown', component_property='value'),
    Input(component_id='avg_mins_dropdown', component_property='value'),
    Input(component_id='views_dropdown_2', component_property='value')]
)

def build_graph(column_chosen,column_chosen_2,column_chosen_3,column_chosen_4):
    dff=df
    dff2=df2
    fig2= px.bar(dff, x='media_property', y=column_chosen)
    fig2.update_yaxes(type="linear")
    fig2.update_layout(height=600, width=1750)
    fig2.update_traces(marker_color='green')
    fig3 = px.bar(dff, x='media_property', y=column_chosen_2)
    fig3.update_yaxes(type="linear")
    fig3.update_layout(height=600, width=1750)
    fig3.update_traces(marker_color='yellow')
    fig4 = px.bar(dff, x='media_property', y=column_chosen_3)
    fig4.update_yaxes(type="linear")
    fig4.update_layout(height=600, width=1750)
    fig5 = px.bar(dff2, x='media_property', y=column_chosen_4)
    fig5.update_yaxes(autorange=True, type="linear")
    fig5.update_layout(height=600, width=1750)
    fig5.update_traces(marker_color='red')
    return fig2,fig3,fig4,fig5

#---------------------------------------------------------------
# For tutorial purposes to show the user the search_value
