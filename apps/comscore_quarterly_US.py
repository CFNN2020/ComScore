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

#Establish database connection with postgres

work_engine = create_engine('postgresql://doadmin:d86f7w5kk4lei9pd@db-data-analysis-do-user-3211830-0.b.db.ondigitalocean.com:25060/dmp_dashboard', pool_pre_ping=True)
df = pd.read_sql_query('select * from comscore_competitor_key_measures_nov_2020', con=work_engine)
df_mean_age = pd.read_sql_query('select media_property, mean_adult_age from comscore_competitor_key_measures_nov_2020', con=work_engine)
df_gaming_index = pd.read_sql_query('select * from comscore_gaming_index', con=work_engine)
df_gaming_index_ranked = pd.read_sql_query('select media_property, "total_unique_visitors_/_views_per_million[pop=213m]",rank () over ( order by "total_unique_visitors_/_views_per_million[pop=213m]" desc) media_rank from comscore_gaming_index', con=work_engine)
df_core_demo = pd.read_sql_query('select * from males_18_34_US', con=work_engine)
us_nov_demographic = pd.read_sql_query('select * from comscore_core_demographic', con=work_engine)
us_feb_demographic = pd.read_sql_query('select * from males_18_34_US', con=work_engine)
us_feb_demographic.drop(axis=1, columns=['geo.1', 'geo.1.1', 'geo.1.1.1', 'composition_index_uv'], inplace=True)
us_feb_demographic.rename(columns={'Composition Index UV' : 'composition_index_uv'}, inplace=True)
us_feb_key_measures = pd.read_sql_query('select * from key_measures_us_feb', con=work_engine)
feb_uv = pd.read_sql_query('select media_property, total_uv_in_thousands from key_measures_us_feb order by total_uv_in_thousands desc', con=work_engine)
nov_uv = pd.read_sql_query('select media_property, total_uv_in_thousands from comscore_competitor_key_measures_nov_2020', con=work_engine)
us = pd.read_sql_query("select * from combined_media_trend where geo = 'US'", con=work_engine)

#Create visualisations

labels = df['media_property']
values = df['percent_reach']


feb_key = us_feb_key_measures
nov_key = df

fig1 = go.Figure()

x = feb_key['media_property']
x2 = nov_key['media_property']
y = feb_key['percent_reach']
y2 = nov_key['percent_reach']

trace_1 = go.Pie(labels=x, values=y, pull=[0,0,0,0,0,0,0.4])
trace_2 = go.Pie(labels=x2, values=y2, pull=[0,0,0,0,0,0.4], visible=False)

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

#fig1 = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0,0,0,0,0,0.4])])
fig1.update_layout(margin=dict(t=0, b=0, l=0, r=0),paper_bgcolor="#acc4cc")


x = feb_uv['media_property'] 
y = feb_uv['total_uv_in_thousands']
x2 = nov_uv['media_property']
y2 = nov_uv['total_uv_in_thousands']

fig2 = go.Figure(data=[
    go.Bar(name='Feb 2021', x=x, y=y),
    go.Bar(name='Nov 2020', x=x2, y=y2)
])
fig2.update_layout(barmode='group',paper_bgcolor="#acc4cc")




labels_2 = df_core_demo['media_property']
values_2 = df_core_demo['total_uv_in_thousands']
fig3 = go.Figure(data=[go.Pie(labels=labels_2, values=values_2, pull=[0,0,0,0,0,0,0.4])])
fig3.update_layout(margin=dict(t=0, b=0, l=0, r=0),paper_bgcolor="#acc4cc")


#define figure factory variables

x = df_core_demo['media_property']
y1 = df_core_demo['percent_reach']
y2 = df_core_demo['Composition Index UV']

fig8 = go.Figure()
fig8.add_trace(go.Bar(
    y= x,
    x= y1,
    name='percent_reach',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))
fig8.add_trace(go.Bar(
    y=x,
    x=y2,
    name='comp_index_uv',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 0.6)', width=3)
    )
))
fig8.update_layout(barmode='stack',paper_bgcolor="#acc4cc")
fig9 = px.bar(df_gaming_index_ranked, x='media_property', y='total_unique_visitors_/_views_per_million[pop=213m]', text='media_rank', height=1500, width=2100,log_y=True)
fig9.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',paper_bgcolor="#acc4cc")
fig9.update_yaxes(tickformat=",f")
fig9.update_traces(marker_color='green')

x = us['date']
nn = us['network_n']
fd = us['fandom_games']
fg = us['future_games']
eg = us['enthusiast_gaming']
gn = us['gamer_network']
ign = us['ign_entertainment']
pw = us['playwire_media']

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=x, y=nn,
                    mode='lines+markers',
                    name='network_n'))
fig4.add_trace(go.Scatter(x=x, y=fg,
                    mode='lines+markers',
                    name='future_games'))
fig4.add_trace(go.Scatter(x=x, y=fd,
                    mode='lines+markers',
                     name='fandom_gamess'))
fig4.add_trace(go.Scatter(x=x, y=eg,
                    mode='lines+markers',
                    name='enthusiast_gaming'))
fig4.add_trace(go.Scatter(x=x, y=gn,
                    mode='lines+markers',
                    name='gamer_network'))
fig4.add_trace(go.Scatter(x=x, y=ign,
                    mode='lines+markers',
                     name='ign_entertainment'))
fig4.add_trace(go.Scatter(x=x, y=pw,
                    mode='lines+markers',
                    name='playwire_media'))

fig5 = px.scatter(df, x='avg_views_per_visit', y='avg_mins_per_visit', size='percent_reach', color='media_property', hover_name='media_property', log_x=True, size_max=60)

merged_frame = [us_feb_demographic, us_nov_demographic]
result = pd.concat(merged_frame)

df = result
feb = df.iloc[[0,1,2,3,4,5,6,7]]
nov = df.iloc[[8,9,10,11,12,13,14,15]]

fig10 = go.Figure()

x = feb['media_property']
x2 = nov['media_property']
y = feb['percent_reach']
y2 = nov['percent_reach']

trace_1 = go.Bar(x=x, y=y, name='feb_data')
trace_2 = go.Bar(x=x2, y=y2, name='nov_data', visible=False)

fig10.add_traces([trace_1, trace_2])

fig10.update_layout(
    updatemenus = list([
        dict(active=0,
            showactive = True,
            buttons=list([   
                dict(label = "Feb 2021",
                    method = "update",
                    args = [{"visible": [True, False]}]),
                     # hide trace2
                dict(label = "Nov 2020",
                    method = "update",
                    args = [{"visible": [False, True]}]
                    ) # hide trace1
                ]))
            ]),
),
fig10.update_layout(margin=dict(t=0, b=0, l=0, r=0))
#instigate layout

layout = html.Div(children=[
    # All elements from the top of the page
        html.Div([
            html.H1(children='Media by percent_reach'),
            html.H2(children='US media by % vs the total digital population[default of 100%]. The below chart highlights the potential reach and share of voice of Network N vs its key competitors in the context of the total digital population (as defined by Comscore)', style={'fontSize': 14} ),

            html.Div(children='''
                Please select a report period below
            '''),
            dcc.Graph(
                id='media_pie',
                figure=fig1
            ),
             html.Div(children='''
                Network N and key competitors UV, quarter by quarter comparison
            '''),
            dcc.Graph(
                id='table1',
                figure=fig2
        ),  
    ]),
    html.Div(html.P(html.Br())),
    html.Div(html.P(html.Br())),
    html.Div(html.P(html.Br())),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Media by UV [core_demographic]'),
        html.H2(children='US Media by Unique Views/Visitors segmented by Network Ns core demographic[male, age 18-34]. This chart shows only this demographic split and the resulting rankings vs key competitors', style={'fontSize': 14} ),

        html.Div(children='''
            Core demographics only[18-34, Males] - total core demo population == 38,000
        '''),

        dcc.Graph(
            id='bar2',
            figure=fig3
        ),  
    ]),
    html.Div(html.P(html.Br())),
    html.Div(html.P(html.Br())),
    html.Div([
        html.H1(children='Media by percent reach [core_demographic]'),
        html.H2(children='UK Media by percent reach segmented by Network Ns core demographic[male, age 18-34]. This chart shows only this demographic split and the resulting rankings vs key competitors', style={'fontSize': 14}),
        
        html.Div(
            children='''
            Core demographics only[18-34, Males] - quarter by quarter comparison
        '''
        ),
        
        dcc.Graph(
            id='bar2',
            figure=fig10
        ),
        html.Div(html.P(html.Br())),
        html.Div(html.P(html.Br())),
    ]),
    html.Div(html.P(html.Br())),
    html.Div(html.P(html.Br())),
    html.Div([
        html.H1(children='Core demographic comparison by percent reach'),
        html.H2(children='US media by % vs the total digital population[default of 100%]. The below chart highlights this split only with Network Ns core demographic[male, age 18-34] and visually includes the total population of 100% to better highlight the equity each media property holds', style={'fontSize': 14} ),

        html.Div(children='''
            Network N [competitors, total pop = composition index % - 100]
        '''),

        dcc.Graph(
            id='bar_demo',
            figure=fig8
        ),
    ]),
    html.Div(html.P(html.Br())),
    html.Div(html.P(html.Br())),
    html.Div([
        html.H1(children='Media trend - aug 18/20'),
        html.H2(children='US media trend, 2018 vs 2020. The graph belows shows the increase or decrease in media rankings from 2018 to 2020 per key competitor', style={'fontSize': 14} ),

        html.Div(children='''
            Network N and key competitors
        '''),

        dcc.Graph(
            id='line',
            figure=fig4
        ),
    ]),
    html.Div(html.P(html.Br())),
    html.Div(html.P(html.Br())),
     html.Div([
        html.H1(children='Engagement deepdive'),
        html.H2(children='US media engagement examining avg views per visit, avg mins per vist per media property. Mainly for internal use', style={'fontSize': 14} ),

        html.Div(children='''
            Network N and competitors
        '''),

        dcc.Graph(
            id='scatter',
            figure=fig5
        ),
    ])
])

    

