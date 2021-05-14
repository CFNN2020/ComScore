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

us = pd.read_sql_query("select * from combined_non_endemic_indexing where geo = 'US'", con=work_engine)

x = us['media_property']
#comp index
hh_income_1 = us['hh_income_<25k_comp_index_uv']
hh_income_2 = us['hh_income_25-39k_comp_index_uv']
hh_income_3 = us['hh_income_40-59k_comp_index_uv']
hh_income_4 = us['hh_income_>60k_comp_index_uv']
#percent reach
hh_income_1_reach = us['hh_income_<25k_percent_reach']
hh_income_2_reach = us['hh_income_25-39k_percent_reach']
hh_income_3_reach = us['hh_income_40-59k_percent_reach']
hh_income_4_reach = us['hh_income_>60k_percent_reach']

fig1 = go.Figure()

trace_1 = go.Bar(x=x, y=hh_income_1, name='comp index')
trace_2 = go.Bar(x=x, y=hh_income_2, name='comp index', visible=False)
trace_3 = go.Bar(x=x, y=hh_income_3, name='comp index', visible=False)
trace_4 = go.Bar(x=x, y=hh_income_4, name='comp index',  visible=False)
trace_5 = go.Bar(x=x, y=hh_income_1_reach, name='percent reach')
trace_6 = go.Bar(x=x, y=hh_income_2_reach, name='percent reach',  visible=False)
trace_7 = go.Bar(x=x, y=hh_income_3_reach, name='percent reach', visible=False)
trace_8 = go.Bar(x=x, y=hh_income_4_reach, name='percent reach', visible=False)


fig1.add_traces([trace_1,trace_2,trace_3,trace_4,trace_5,trace_6,trace_7,trace_8])

fig1.update_layout(barmode='group')
fig1.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    label = "Household Income <25k",
                    method = "update",
                    args = [{"visible": [True,False,False,False,True,False,False,False]}]
                ),
                dict(
                    label = "Household Income 25-39k",
                    method = "update",
                    args = [{"visible": [False,True,False,False,False,True,False,False]}]
                ),
                dict(
                    label = "Household Income 40-59k",
                    method = "update",
                    args = [{"visible": [False,False,True,False,False,False,True,False]}]
                ),
                dict(
                    label = "Household Income >60k",
                    method = "update",
                    args = [{"visible": [False,False,False,True,False,False,False,True]}]
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
                    label = "Household Income <25k",
                    method = "update",
                    args = [{"visible": [False,False,False,False,True,False,False,False]}]
                ),
                dict(
                    label = "Household Income 25-39k",
                    method = "update",
                    args = [{"visible": [False,False,False,False,False,True,False,False]}]
                ),
                dict(
                    label = "Household Income 40-59k",
                    method = "update",
                    args = [{"visible": [False,False,False,False,False,False,True,False]}]
                ),
                dict(
                    label = "Household Income >60k",
                    method = "update",
                    args = [{"visible": [False,False,False,False,False,False,False,True]}]
                ),
            ]),
            direction="down",
            showactive=True,
            pad={"r": -90, "t": -90},
            x=0.25,
            xanchor="left",
            yanchor="top"
        ),
    ]
)
x = us['media_property']
y = us['smartphones_comp_index_uv']
y1 = us['wearable_tech_comp_index_uv']

y3 = us['smartphones_percent_reach']
y4 = us['wearable_tech_percent_reach']

fig2 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig4 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])

fig2.add_trace(go.Pie(labels=x, values=y, pull=[0,0,0,0.4,0,0.4], name='comp_index'), row=1, col=1)
fig2.add_trace(go.Pie(labels=x, values=y3, pull=[0,0,0.4,0,0,0.4], name='percent_reach'), row=1, col=2)

fig4.add_trace(go.Pie(labels=x, values=y1, pull=[0,0,0,0,0,0.4,0,0], name='comp_index'), row=1, col=1)
fig4.add_trace(go.Pie(labels=x, values=y4, pull=[0,0,0,0,0,0,0,0.4], name='percent_reach'), row=1, col=2)

fig2.update_layout(title_text="Technology Indexing: smartphones composition index uv and percent reach", autosize=False, width=2190, height=800)

fig4.update_layout(title_text="Technology Indexing: wearable technology composition index uv and percent reach", autosize=False, width=2190, height=800)

y5 = us['credit_cards_comp_index_uv']
y6 = us['mortgages_comp_index_uv']
y7 = us['credit_cards_percent_reach']
y8 = us['mortgages_percent_reach']

y_credit = y5
y_mortgage = y6
y_credit_reach = y7
y_mortgage_reach = y8
x = x


# Creating two subplots
fig5 = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                    shared_yaxes=False, vertical_spacing=0.001)

fig5.append_trace(go.Bar(
    x=y_credit,
    y=x,
    marker=dict(
        color='rgba(50, 171, 96, 0.6)',
        line=dict(
            color='rgba(50, 171, 96, 1.0)',
            width=1),
    ),
    name='credit card comp index',
    orientation='h',
), 1, 1)

fig5.append_trace(go.Scatter(
    x=y_mortgage, y=x,
    mode='lines+markers',
    line_color='rgb(128, 0, 128)',
    name='mortgage comp index',
), 1, 2)

fig5.update_layout(
    title='Credit card & Mortgage composition index comparison',
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
        domain=[0, 0.85],
    ),
    yaxis2=dict(
        showgrid=False,
        showline=True,
        showticklabels=False,
        linecolor='rgba(102, 102, 102, 0.8)',
        linewidth=2,
        domain=[0, 0.85],
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0, 0.42],
    ),
    xaxis2=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0.47, 1],
        side='top',
        dtick=25000,
    ),
    legend=dict(x=0.029, y=1.038, font_size=10),
    margin=dict(l=100, r=20, t=70, b=70),
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
)

annotations = []

y_s = np.round(y_credit, decimals=2)
y_nw = np.rint(y_mortgage)

# Adding labels

for ydn, yd, xd in zip(y_nw, y_s, x):
    # labeling the scatter savings
    annotations.append(dict(xref='x2', yref='y2',
                            y=xd, x=ydn,
                            text='{:,}'.format(ydn) + '%',
                            font=dict(family='Arial', size=14,
                                      color='rgb(128, 0, 128)'),
                            showarrow=False))
    # labeling the bar net worth
    annotations.append(dict(xref='x1', yref='y1',
                            y=xd, x=yd,
                            text=str(yd) + '%',
                            font=dict(family='Arial', size=14,
                                      color='rgb(50, 171, 96)'),
                            showarrow=False))

# Source
annotations.append(dict(xref='paper', yref='paper',
                        x=0.2, y=-0.109,
                        text='Comscore "' +
                             '(2021), Credit card affinity (indicator), ' +
                             'Mortgage affinity (indicator).',
                        font=dict(family='Arial', size=10, color='rgb(150,150,150)'),
                        showarrow=False))

fig5.update_layout(annotations=annotations)



fig6 = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                    shared_yaxes=False, vertical_spacing=0.001)

fig6.append_trace(go.Bar(
    x=y_credit_reach,
    y=x,
    marker=dict(
        color='rgba(50, 171, 96, 0.6)',
        line=dict(
            color='rgba(50, 171, 96, 1.0)',
            width=1),
    ),
    name='Credit cards composition index uv',
    orientation='h',
), 1, 1)

fig6.append_trace(go.Scatter(
    x=y_mortgage_reach, y=x,
    mode='lines+markers',
    line_color='rgb(128, 0, 128)',
    name='Mortgage and house loan borrowing',
), 1, 2)

fig6.update_layout(
    title='Credit card & Mortgage percent reach comparison',
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
        domain=[0, 0.85],
    ),
    yaxis2=dict(
        showgrid=False,
        showline=True,
        showticklabels=False,
        linecolor='rgba(102, 102, 102, 0.8)',
        linewidth=2,
        domain=[0, 0.85],
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0, 0.42],
    ),
    xaxis2=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0.47, 1],
        side='top',
        dtick=25000,
    ),
    legend=dict(x=0.029, y=1.038, font_size=10),
    margin=dict(l=100, r=20, t=70, b=70),
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
)

annotations = []

y_s = np.round(y_credit_reach, decimals=2)
y_nw = np.rint(y_mortgage_reach)

# Adding labels

for ydn, yd, xd in zip(y_nw, y_s, x):
    # labeling the scatter savings
    annotations.append(dict(xref='x2', yref='y2',
                            y=xd, x=ydn,
                            text='{:,}'.format(ydn) + '%',
                            font=dict(family='Arial', size=14,
                                      color='rgb(128, 0, 128)'),
                            showarrow=False))
    # labeling the bar net worth
    annotations.append(dict(xref='x1', yref='y1',
                            y=xd, x=yd,
                            text=str(yd) + '%',
                            font=dict(family='Arial', size=14,
                                      color='rgb(50, 171, 96)'),
                            showarrow=False))

# Source
annotations.append(dict(xref='paper', yref='paper',
                        x=0.2, y=-0.109,
                        text='Comscore "' +
                             '(2021), Credit card affinity (indicator), ' +
                             'Mortgage affinity (indicator).',
                        font=dict(family='Arial', size=10, color='rgb(150,150,150)'),
                        showarrow=False))

fig6.update_layout(annotations=annotations)

y5 = us['car_culture_comp_index_uv']
y6 = us['car_culture_percent_reach']

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
                id='hh_income',
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
        dcc.Graph(id='tech_pie_2', 
        figure=fig5),
    ]),
    html.Br(),
    html.Br(),
    html.Div([
        html.Br(),
        html.H1(children=''),
        html.H2(children='',  style={'fontSize': 14}),
        dcc.Graph(id='tech_pie_2', 
        figure=fig6),
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
