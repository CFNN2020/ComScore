import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash
import base64
# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import reference, comscore_quarterly_US, comscore_site_ranking_us, comscore_site_rankings_uk, comscore_quarterly_UK, comscore_custom_entity_debug, comscore_index_comparisons, comscore_index_comparisons_uk, non_endemic_us, non_endemic_uk

image_filename = r"C:\Users\chris\Pictures\Picture1.png" # replace with your own image
nn_logo = base64.b64encode(open(image_filename, 'rb').read())

 
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#cfd9e4",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#acc4cc",    
}

logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=nn_logo, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Logo", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://plot.ly",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-5",
)

sidebar = html.Div(
    [
        html.H2("Network N Comscore Application", className="display-4"),
        html.Hr(),
        html.P(

        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
        html.P(
            "Key measures and rankings", className="lead"
        ),
         dbc.Nav(
            [
                dbc.NavLink("United States", href="/apps/comscore_quarterly_US", active="exact"),
                html.Br(),
                dbc.NavLink("US Sites", href="/apps/comscore_site_ranking_us", active="exact"),
                html.Br(),
                dbc.NavLink("United Kingdom", href="/apps/comscore_quarterly_UK", active="exact"),
                html.Br(),
                dbc.NavLink("UK sites", href="/apps/comscore_site_rankings_uk", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
        html.P(
            "Indexing", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("US index", href="/apps/comscore_index_comparison", active="exact"),
                html.Br(),
                dbc.NavLink("UK index", href="/apps/comscore_index_comparison_uk", active="exact"),
                html.Br(),
                dbc.NavLink("US non_endemic index", href="/apps/non_endemic_us", active="exact"),
                html.Br(),
                dbc.NavLink("UK non_endemic index", href="/apps/non_endemic_uk", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
        html.P(
            "Custom entities", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Custom entity list", href="/apps/comscore_custom_entity_debug", active="exact"),
                html.Br(),
            ],
            vertical=True,
            pills=True,
        ),
        html.P(
            "Reference and definitions", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Reference", href="/apps/reference", active="exact"),
                html.Br(),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
'''
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('ComScore Key Measures US', href='/apps/comscore_quarterly_US'),
        html.Br(),
        dcc.Link('ComScore Competitor List - Key sites only - US', href='/apps/comscore_site_ranking_us'),
        html.Br(),
        dcc.Link('Comscore Key Measures UK', href='/apps/comscore_quarterly_UK'),
        html.Br(),
        dcc.Link('Comscore Competitor List - Key sites only - UK', href='/apps/comscore_site_rankings_uk'),
        html.Br(),
        dcc.Link('US Network N indexing vs index composition', href='/apps/comscore_index_comparison'),
        html.Br(),
        dcc.Link('UK Network N indexing vs index composition', href='/apps/comscore_index_comparison_uk'),
        html.Br(),
        dcc.Link('TEST', href='/apps/non_endemic_us'),
        html.Br(),
        dcc.Link('ComScore Custom Entity debugging', href='/apps/comscore_custom_entity_debug'),
        html.Br(),
        dcc.Link('Comscore reference and dictionary', href='/apps/reference'),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
        html.Br()
    ], className="col"),
    html.Div(id='page-content', children=[])
])
'''

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/comscore_quarterly_US':
        return comscore_quarterly_US.layout
    if pathname == '/apps/comscore_site_ranking_us':
        return comscore_site_ranking_us.layout
    if pathname == '/apps/comscore_quarterly_UK': 
        return comscore_quarterly_UK.layout
    if pathname == '/apps/comscore_site_rankings_uk':
        return comscore_site_rankings_uk.layout
    if pathname == '/apps/comscore_index_comparison':
        return comscore_index_comparisons.layout
    if pathname == '/apps/comscore_index_comparison_uk':
        return comscore_index_comparisons_uk.layout
    if pathname == '/apps/non_endemic_us':
        return non_endemic_us.layout
    if pathname == '/apps/comscore_custom_entity_debug':
        return comscore_custom_entity_debug.layout
    if pathname == '/apps/non_endemic_uk':
        return non_endemic_uk.layout
    if pathname == '/apps/reference':
        return reference.layout
    else:
        return "\n Welcome to Network N's Comscore Analysis Application. Please select a page to start"

if __name__ == '__main__':
    app.run_server(debug=False)