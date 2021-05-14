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


work_engine = create_engine('postgresql://doadmin:d86f7w5kk4lei9pd@db-data-analysis-do-user-3211830-0.b.db.ondigitalocean.com:25060/dmp_dashboard', pool_pre_ping=True)

uk = pd.read_sql_query("select * from combined_non_endemic_indexing where geo = 'UK'", con=work_engine)




#xaxis
x = uk['media_property']
#comp index
social_grade_a = uk['social_grade_a_comp_index_uv']
social_grade_b = uk['social_grade_b_comp_index_uv']
social_grade_c = uk['social_grade_c_comp_index_uv']
#percent reach
social_grade_a_reach = uk['social_grade_a_percent_reach']
social_grade_b_reach = uk['social_grade_b_percent_reach']
social_grade_c_reach = uk['social_grade_c_percent_reach']

fig1 = go.Figure()

trace_1 = go.Bar(x=x, y=social_grade_a, name='comp_index')
trace_2 = go.Bar(x=x, y=social_grade_b, name='comp_index',  visible=False)
trace_3 = go.Bar(x=x, y=social_grade_c, name='comp_index',  visible=False)
trace_4 = go.Bar(x=x, y=social_grade_a_reach, name='percent reach')
trace_5 = go.Bar(x=x, y=social_grade_b_reach, name='percent reach', visible=False)
trace_6 = go.Bar(x=x, y=social_grade_c_reach, name='percent reach', visible=False)

fig1.add_traces([trace_1,trace_2,trace_3,trace_4, trace_5, trace_6])

fig1.update_layout(barmode='group')
fig1.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    label = "Social grade a",
                    method = "update",
                    args = [{"visible": [True, False, False, True, False, False]}]
                ),
                dict(
                    label = "Social grade b",
                    method = "update",
                    args = [{"visible": [False, True, False, False, True, False]}]
                ),
                dict(
                    label = "Social grade c",
                    method = "update",
                    args = [{"visible": [False, False, True, False, False, True]}]
                ),
            ]),
            direction="down",
            showactive=True,
            pad={"r": -90, "t": -90},
            x=0.1,
            xanchor="left",
            yanchor="top"
        ),
        dict(
            buttons=list([
                dict(
                    label = "Social grade a",
                    method = "update",
                    args = [{"visible": [False, False, False, True, False, False]}]
                ),
                dict(
                    label = "Social grade b",
                    method = "update",
                    args = [{"visible": [False, False, False, False, True, False]}]
                ),
                 dict(
                    label = "Social grade c",
                    method = "update",
                    args = [{"visible": [False, False, False, False, False, True]}]
                ),
            ]),
            direction="down",
            showactive=True,
            pad={"r": -90, "t": -90},
            x=0.17,
            xanchor="left",
            yanchor="top"
        ),
    ]
)

x = uk['media_property']
y = uk['smartphones_comp_index_uv']
y1 = uk['wearable_tech_comp_index_uv']

y3 = uk['smartphones_percent_reach']
y4 = uk['wearable_tech_percent_reach']

fig2 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig4 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])

fig2.add_trace(go.Pie(labels=x, values=y, pull=[0,0,0,0.4,0,0.4], name='comp_index'), row=1, col=1)
fig2.add_trace(go.Pie(labels=x, values=y3, pull=[0,0,0.4,0,0,0.4], name='percent_reach'), row=1, col=2)

fig4.add_trace(go.Pie(labels=x, values=y1, pull=[0,0,0,0,0,0.4,0,0], name='comp_index'), row=1, col=1)
fig4.add_trace(go.Pie(labels=x, values=y4, pull=[0,0,0,0,0,0,0,0.4], name='percent_reach'), row=1, col=2)

fig2.update_layout(title_text="Technology Indexing: smartphones composition index uv and percent reach", width=2190, height=800)

fig4.update_layout(title_text="Technology Indexing: wearable technology composition index uv and percent reach", width=2190, height=800)

y5 = uk['car_culture_comp_index_uv']
y6 = uk['car_culture_percent_reach']

fig3 = go.Figure(data=[
    go.Bar(name='car culture index', x=x, y=y5),
    go.Bar(name='car culture reach', x=x, y=y6)
])
fig3.update_layout(barmode='group')
fig3.update_yaxes(type='linear')

layout = html.Div(children=[
    # All elements from the top of the page
        html.Div([
            html.H1(children=''),
            html.H2(children='', style={'fontSize': 14}),

            html.Div(children='''
                
            '''),
            dcc.Graph(
                id='social_grade',
                figure=fig1
            ), 
    ]),
    html.Br(),
    html.Br(),
    html.Div([
        html.Br(),
        html.H1(children=''),
        html.H2(children='',  style={'fontSize': 14}),
        dcc.Graph(id='tech_pie', 
        figure=fig2),
    ]),
    html.Br(),
    html.Br(),
    html.Div([
        html.Br(),
        html.H1(children=''),
        html.H2(children='',  style={'fontSize': 14}),
        dcc.Graph(id='tech_pie_2', 
        figure=fig4),
    ]),
    html.Br(),
    html.Br(),
    html.Div([
        html.Br(),
        html.H1(children=''),
        html.H2(children='',  style={'fontSize': 14}),
        dcc.Graph(id='hh_graph', 
        figure=fig3)
    ]),
])

#---------------------------------------------------------------
# Connecting the Dropdown values to the graph
'''
@app.callback(
    Output(component_id='combo_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value'), 
    Input(component_id='my_dropdown_2', component_property='value')]
)

def build_graph(column_chosen, column_chosen_2):
    dff = df_all
    fig = px.bar(dff, x='media_property', y=column_chosen_2, color=column_chosen)
    fig.update_yaxes(type='linear')
    fig.update_layout(height=500, width=2500)
   
    return fig

@app.callback(
    Output(component_id='demo_graph', component_property='figure'),
    [Input(component_id='my_dropdown_3', component_property='value')]
)

def update_demo(demo_chosen):
    dfd = df_demo_index
    fig1 = px.pie(dfd, names='metrics', values=demo_chosen)

    return fig1
'''

    