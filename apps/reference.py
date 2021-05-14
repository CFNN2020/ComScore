import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from sqlalchemy import create_engine
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from app import app
import base64

work_engine = create_engine('postgresql://dmp_dashboard79oygu43bw:ss244isuiqbmk9os@db-data-analysis-do-user-3211830-0.b.db.ondigitalocean.com:25060/dmp_dashboard', pool_pre_ping=True)

context_taxonomy = pd.read_sql_query('select * from iab_content_taxonomy', con=work_engine)

index = context_taxonomy.set_index('unique_id')


fig = go.Figure(data=[go.Table(
    header = dict(values = list(context_taxonomy.columns), 
    fill_color ='paleturquoise',
    align = 'left'),
    cells =dict(values=[index.index, index.parent, index.name, index.tier_1, index.tier_2, index.tier_3, index.tier_4],
    align='left'))
])


layout = html.Div(children=[
    # All elements from the top of the page
        html.Div([
            html.H1(children='Comscore metric definitions and reference'),
            html.H2(children= 'Collection of all relevant comscore methodology, terms and thier definitions',
            style={'fontSize': 20, 'fontcolor' : 'blue'}),
            html.Br(),
            html.Br(),
            html.H2(children= 'Millions (MM)'),
            html.Div(children='''
                (MM) refers to millions. For example, when the Total Minutes (MM) metric reports “24”, that means that there were 24 million minutes spent on that entity in the given month.
            '''),
            html.Br(),
            html.Br(),
            html.H2(children='Total Views (MM)'),
            html.Div(children='''
                In Media Metrix Multi-Platform,

                Total Digital Population Total Views = Media Metrix Desktop page views + Video Metrix video views (Desktop) + Video Metrix video Views (Mobile) + Mobile Metrix page views (note this is from web browsing only).

                Desktop Total Views = Media Metrix Desktop page views + Video Metrix video views (Desktop) 

                Mobile Total Views = Video Metrix video Views (Mobile) + Mobile Metrix page views (note this is from web browsing only). 
            '''),
            html.Br(),
            html.Br(),
            html.H2(children='Total Unique Visitors (000)'),
            html.Div(children='''
                The estimated number of different individuals (in thousands) that visited any content of a website, a category, a channel, or an application during the selected reporting period.
            '''),
            html.Br(),
            html.Br(),
            html.H2(children='% Reach'),
            html.Div(children='''
                The percent of the total universe accounted for by the total site visitors. Reach percent can also be shown for target markets (cells) comprised of specific demographic groups.
            '''),
            html.Br(),
            html.Br(),
            html.H2(children='Composition Index UV'),
            html.Div(children='''
                Measures the extent to which visitors to a website, either in total or defined per a demographic category, are over or underrepresented compared to the corresponding percentage in the universe.
                In the example below, Males 18-49 are 47% more likely to visit [P] Reddit than the average internet site.
            '''),
            html.Br(),
            html.Br(),
            html.H2(children='Average Minutes per Visit'),
            html.Div(children='''
                The average number of minutes spent on the website during each visit. Please note that Mobile in MMX MP includes both app and browser consumption. The concept of a Visit does not exist for Mobile apps, so we only account for Mobile Browser visitations in calculating Avg. Minutes per Visit for MMX MP. 
            '''),
            html.Br(),
            html.Br(),
            html.H2(children='Average Minutes per Visitor'),
            html.Div(children='''
                The average number of minutes spent on the website during the month, per visitor. Average Minutes per Usage Day The average number of minutes spent on the website during a day, per visitor. 
            '''),
            html.Br(),
            html.Br(),
            html.H2(children='Advanced audience context'),
            html.Div(children='''
                Data is based on panellist visiting pages defined as Console Games as per the IAB Taxonomy V2. Our data shows they are users that have shown an interest in Console Games topic by visiting at least 5 pages categorized in the Console Games IAB category on a monthly basis, which will indicate they were at least exposed to - and possibly consumed - content related to this specific category. You can select additional measures in the reports such as Average Minutes per Visitor and Composition Index Minutes to better determine their content consumption of Games Console classified pages. A scrollable list of IAB content taxonomy categories can be found below
            '''),
            html.Br(),
            html.Br(),
            html.Div([
                html.Br(),
                html.H1(children='IAB Content Taxonomy'),
                dcc.Graph(id='iab_list', 
                figure=fig)
            ]),
        ]),
])
