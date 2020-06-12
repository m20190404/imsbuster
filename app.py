
#------------------------------------------#
#
# IMPORT REQUIRED PACKAGES
#
#------------------------------------------#


import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

#------------------------------------------#
#
# THE DATA
#
# here we import, handle and transform it
# so that we can then use it in the
# visualization required
#------------------------------------------#





data_path = 'C:/Users/pb937wu/NOVAIMS/Data Visualization - General/Project Development/'

dfcritic = pd.read_csv(data_path + 'Critic_File_v2.csv', sep=';')

dfmaster = pd.read_excel(data_path + 'filmsDataset.xlsx', sheet_name='Master_projeto')


#path para o grafico de mapa

path_dataset = 'https://raw.githubusercontent.com/jmmpalma/DV_Project_eatinghabbits/master/filmsDatasetvPM.xlsx'

df_filmsPerStudio = pd.read_excel(path_dataset, sheet_name='FilmsPerYearPerStudio2') #Variável com os filmes realizados por cada  studio

# definições iniciais para o gráfico do mapa

home_year = 2017

df_filmsPerStudio_filtered = df_filmsPerStudio[df_filmsPerStudio[home_year] != 0]


logo_img = data_path + 'Logo v1.png'

genre_options = [dict(label=genre, value=genre) for genre in dfmaster['Genre'].unique()]
moviename_options = [dict(label=moviename, value=moviename) for moviename in dfmaster['Name'].unique()]



# the logo code



box02_moviedrop = \
html.Label('Movie Name'),
dcc.Dropdown(
    id='movie_drop',
    options=moviename_options,
    multi=False
),


# The App itself

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

server = app.server

app.layout = html.Div([

    #upper section
    html.Div([
        #left upper section
        html.Div([
            #logo
            html.Div([
                html.Img(
                    src=app.get_asset_url("Logo v2.png"),
                    id="logo",
                    width='auto',
                    height='120px',
                )
            ], style={'margin-left': '50px'}),
            #dropdown genre
            html.Div([
                html.Label(children='Genre',
                           style={'font-family': 'Impact, Charcoal, sans-serif', 'color': '#ffab03'}),
                dcc.Dropdown(
                    id='genre_drop',
                    options=genre_options,
                    multi=False,
                    value='Action',
                    style={'font-family': 'Impact, Charcoal, sans-serif'}
                ),
            ], className='box_type1'),
            # dropdown movie
            html.Div([
                html.Label(children='Movie Name',
                           style={'font-family': 'Impact, Charcoal, sans-serif', 'color': '#ffab03'}),
                dcc.Dropdown(
                    id='movie_drop',
                    options=moviename_options,
                    multi=False,
                    style={'font-family': 'Impact, Charcoal, sans-serif'}
                ),
            ], className='box_type1'),
        ], style={'margin': '10px'}, className='box'),
        #right upper section
        html.Div([
            #map
            html.Div([
                dcc.Loading(dcc.Graph(id='example-graph')),
            ], style={'margin': '10px'}),
            # slider
            html.Div([
                dcc.Slider(
                    id='year_slider',
                    min=2010,
                    max=2017,
                    marks={str(i): '{}'.format(str(i)) for i in [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]},
                    value=home_year,
                    step=1,
                    included=False
                ),
            ]),
        ], style={'margin': '10px'}, className='box'),
    ], style={'display': 'grid', 'grid-template-columns': '30% 70%'}, className='box'),
    # bottom section
    html.Div([
        # bottom left (movie image)
        html.Div([
            html.Img(
                src='https://m.media-amazon.com/images/M/MV5BNWEyNTE0YTEtY2FkMi00MmY3LTg4MWMtODdjYjRkNGM4ZTZhXkEyXkFqcGdeQXVyMzI0NDc4ODY@._V1_SX300.jpg',
                id="cover",
            )
        ], style={'margin-left': 'auto', 'margin-right': 'auto', 'border': '5px solid', 'border-color': '#ffab03'}),
        # bottom right
        html.Div([
            # bottom right upper
            html.Div([
                # movie data
                html.Div([
                    # movie name
                    html.Div([
                        html.Div([
                            html.Label(children='Movie Name:',
                                       className='box_type3'),
                        ]),
                            dcc.Loading(
                            html.Label(children='-',
                                       className='box_type2',
                                       id='movie_name_label'),
                            )
                    ], style={'display': 'grid', 'grid-template-columns': '28% 72%'}),
                    # release year
                    html.Div([
                        html.Div([
                            html.Label(children='Release Year:',
                                       className='box_type3'),
                        ]),
                            dcc.Loading(
                            html.Label(children='-',
                                       className='box_type2',
                                       id='release_year_label'),
                            )
                    ], style={'display': 'grid', 'grid-template-columns': '28% 72%'}),
                    # director
                    html.Div([
                        html.Div([
                            html.Label(children='Director:',
                                       className='box_type3'),
                        ]),
                            dcc.Loading(
                            html.Label(children='-',
                                       className='box_type2',
                                       id='director_label'),
                            )
                    ], style={'display': 'grid', 'grid-template-columns': '28% 72%'}),
                    # Main Actors
                    html.Div([
                        html.Div([
                            html.Label(children='Main Actors:',
                                       className='box_type3'),
                        ]),
                        dcc.Loading(
                            html.Label(children='-',
                                       className='box_type2',
                                       id='main_actors_label'),
                        )
                    ], style={'display': 'grid', 'grid-template-columns': '28% 72%'}),
                    # Studio
                    html.Div([
                        html.Div([
                            html.Label(children='Production Studio:',
                                       className='box_type3'),
                        ]),
                        dcc.Loading(
                            html.Label(children='-',
                                       className='box_type2',
                                       id='production_studio_label'),
                        )
                    ], style={'display': 'grid', 'grid-template-columns': '28% 72%'}),
                    # Revenue
                    html.Div([
                        html.Div([
                            html.Label(children='Box Office Revenue:',
                                       className='box_type3'),
                        ]),
                        dcc.Loading(
                            html.Label(children='-',
                                       className='box_type2',
                                       id='box_office_revenue_label'),
                        )
                    ], style={'display': 'grid', 'grid-template-columns': '28% 72%'}),
                ], className='box_type1'),
                # awards graph
                html.Div([
                    dcc.Markdown('test graph')
                ], style={'background-color': '#FFDD9F'}, className='box'),
            ], style={'display': 'grid', 'grid-template-columns': '60% 37.5%', 'grid-column-gap': '2.5%'}, className='box'),
            # bottom right bottom (radar)
            html.Div([
                dcc.Loading(dcc.Graph(id='radar_fig')),
            ], style={'background-color': '#FFDD9F'}, className='box'),
        ], style={'margin': '10px'}, className='box'),
    ], style={'display': 'grid', 'grid-template-columns': '30% 70%'}, className='box'),
])





# Callbacks

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    [Input(component_id="year_slider", component_property='value')]
)

def plots(year_slider):

    df_filmsPerStudio_filtered = df_filmsPerStudio[df_filmsPerStudio[year_slider] != 0]

    scattermap = px.scatter_geo(df_filmsPerStudio_filtered,
                                lat="lat",
                                lon="lon",
                                color="ProductionStudio",  # which column to use to set the color of markers
                                hover_name="ProductionStudio",  # column added to hover information
                                size=year_slider,
                                size_max=25,# size of markers
                                projection="natural earth")

    return scattermap

@app.callback(
    [
        Output("cover", "src"),
        Output("movie_drop", "options"),
        Output("movie_name_label", "children"),
        Output("release_year_label", "children"),
        Output("director_label", "children"),
        Output("main_actors_label", "children"),
        Output("production_studio_label", "children"),
        Output("box_office_revenue_label", "children")
    ],
    [
        Input("movie_drop", "value"),
        Input("genre_drop", "value")
    ]
)
def update_output_div(moviename, genre):

    # changing list of movies according to genre

    dfgenrefilter1 = dfmaster[dfmaster['Genre'] == genre]
    filtered_movie_options = [dict(label=moviename, value=moviename) for moviename in dfgenrefilter1['Name'].unique()]

    # changing the cover image
    dfmoviefilter = dfmaster[dfmaster['Name'] == moviename]
    url_poster = dfmoviefilter['Poster'].values[0]

    # changing movie data

        # year
    dfreleaseyear = dfmoviefilter['Year_x'].values[0]

        # Director
    dfdirector = dfmoviefilter['Director'].values[0]

        # Actors
    dfactors = dfmoviefilter['Actors'].values[0]

        # Production Studio
    dfproductionstudio = dfmoviefilter['Production'].values[0]

        # Box Office Revenue
    dfboxofficerevenue = dfmoviefilter['Total Gross'].values[0]
    dfboxofficerevenue = '$ {:0,.0f}'.format(dfboxofficerevenue).replace(',', '.')


    return url_poster, filtered_movie_options, moviename, dfreleaseyear, dfdirector, dfactors, dfproductionstudio, dfboxofficerevenue


if __name__ == '__main__':
    app.run_server(debug=True)

# ---------------------------------------
