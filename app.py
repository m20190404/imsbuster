

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

#old
# dfcritic = pd.read_csv(data_path + 'Critic_File_v2.csv', sep=';')
#end old

# data_path = 'C:/Users/pb937wu/NOVAIMS/Data Visualization - General/Project Development/'
data_path= 'https://raw.githubusercontent.com/m20190404/imsbuster/master/data/'
dfmaster = pd.read_excel(data_path + 'filmsDataset.xlsx', sheet_name='master')
dfevo = pd.read_excel(data_path + 'filmsDataset.xlsx', sheet_name='evo')

# options definition
genre_options = [dict(label=genre, value=genre) for genre in dfmaster['Genre'].unique()]
moviename_options = [dict(label=moviename, value=moviename) for moviename in dfmaster['Name'].unique()]

# auxiliary variables

scatterweek = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

#------------------------------------------#
#
# THE APP
#
#------------------------------------------#

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

server = app.server

app.layout = html.Div([

    #first vertical section (LOGO)
    html.Div([
        html.Img(
            src=app.get_asset_url("Logo v2.png"),
            id="logo",
            width='auto',
            height='120px',
        )
    ], style={'margin-left': '50px'}),

    # second vertical section
    html.Div([

        #left section
        html.Div([
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
                    value='Jurassic World',
                    style={'font-family': 'Impact, Charcoal, sans-serif'}
                ),
            ], className='box_type1'),
            # movie image
            html.Div([
                html.Div([
                    html.Img(
                        src='https://m.media-amazon.com/images/M/MV5BNWEyNTE0YTEtY2FkMi00MmY3LTg4MWMtODdjYjRkNGM4ZTZhXkEyXkFqcGdeQXVyMzI0NDc4ODY@._V1_SX300.jpg',
                        id="cover",
                    )
                ], style={'margin-left': '80px', 'margin-top': '50px'}),
            ], style={'margin-left': 'auto'}),
        ], style={'margin': '5px'}, className='box'),

        # right section
        html.Div([
            # right section upper
            html.Div([
                # right section upper left (movie data)
                html.Div([
                    # box inside
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
                        ], style={'display': 'grid', 'grid-template-columns': '22% 78%'}),
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
                        ], style={'display': 'grid', 'grid-template-columns': '22% 78%', 'marginTop': 14}),
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
                        ], style={'display': 'grid', 'grid-template-columns': '22% 78%', 'marginTop': 14}),
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
                        ], style={'display': 'grid', 'grid-template-columns': '22% 78%', 'marginTop': 14}),
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
                        ], style={'display': 'grid', 'grid-template-columns': '22% 78%', 'marginTop': 14}),
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
                        ], style={'display': 'grid', 'grid-template-columns': '22% 78%', 'marginTop': 14}),
                        # Language
                        html.Div([
                            html.Div([
                                html.Label(children='Language:',
                                           className='box_type3'),
                            ]),
                            dcc.Loading(
                                html.Label(children='-',
                                           className='box_type2',
                                           id='language_label'),
                            )
                        ], style={'display': 'grid', 'grid-template-columns': '22% 78%', 'marginTop': 14}),
                        # Plot
                        html.Div([
                            html.Div([
                                html.Label(children='Plot:',
                                           className='box_type3'),
                            ]),
                            dcc.Loading(
                                html.Label(children='-',
                                           className='box_type2',
                                           id='plot_label'),
                            )
                        ], style={'display': 'grid', 'grid-template-columns': '22% 78%', 'marginTop': 12}),
                    ], className='box_type1'),
                ]),
                # right section upper right (revenue dynamic)
                html.Div([
                    html.Div([
                        html.Label(children='Box Office Evolution',
                                   style={'font-family': 'Impact, Charcoal, sans-serif', 'color': '#ffab03'}),
                    ], className='box_type4'),
                    html.Div([
                        dcc.Loading(dcc.Graph(id='scatter_fig')),
                    ]),
                ], style={'border': '2px solid', 'border-color': '#E5E5E5', 'border-radius': 5, 'margin': 5}),
            ], style={'display': 'grid', 'grid-template-columns': '55% 45%'}),

            # right section bottom
            html.Div([
                html.Div([
                    html.Div([
                        html.Label(children='Critic',
                                   style={'font-family': 'Impact, Charcoal, sans-serif', 'color': '#ffab03'}),
                    ], className='box_type4'),
                    html.Div([
                        dcc.Loading(dcc.Graph(id='radar_fig')),
                    ])
                ], style={'border':'2px solid', 'border-color': '#E5E5E5', 'border-radius': 5, 'margin': 5}),
                html.Div([
                    html.Div([
                        html.Label(children='Awards',
                                   style={'font-family': 'Impact, Charcoal, sans-serif', 'color': '#ffab03'}),
                    ], className='box_type4'),
                    html.Div([
                        dcc.Loading(dcc.Graph(id='bar_fig')),
                    ]),
                ], style={'border': '2px solid', 'border-color': '#E5E5E5', 'border-radius': 5, 'margin': 5}),
            ], style={'display': 'grid', 'grid-template-columns': '55% 45%'}, className='box'),
        ])

    ], style={'display': 'grid', 'grid-template-columns': '30% 70%'}, className='box'),

    # bottom section (signature)
#    html.Div([
#        html.Label(children='Created by: Bruno Medley (M20190404), Júlio Félix (M20190228), João Palma (20190347)',
#                   style={'font-family': 'Impact, Charcoal, sans-serif', 'color': '#ffab03'}),
#    ], style={'margin': 8}),
])


    #------------------------------------------#
    #
    # CALLBACKS
    #
    #------------------------------------------#

@app.callback(
    [
        Output("cover", "src"),
        Output("movie_drop", "options"),
        Output("movie_name_label", "children"),
        Output("release_year_label", "children"),
        Output("director_label", "children"),
        Output("main_actors_label", "children"),
        Output("production_studio_label", "children"),
        Output("box_office_revenue_label", "children"),
        Output("language_label", "children"),
        Output("plot_label", "children")
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

        # Language
    dflanguage = dfmoviefilter['Language'].values[0]

        # Plot
    dfplot = dfmoviefilter['Plot'].values[0]


    return url_poster, filtered_movie_options, moviename, dfreleaseyear, dfdirector, dfactors, dfproductionstudio, dfboxofficerevenue, dflanguage, dfplot

@app.callback(
     [
         Output(component_id='radar_fig', component_property='figure'),
         Output(component_id='bar_fig', component_property='figure'),
         Output(component_id='scatter_fig', component_property='figure'),
         # Output(component_id='updatemenu-item-text user-select-none', component_property='figure')
     ],
    [Input(component_id="movie_drop", component_property='value')]
)
def update_output_div2(moviename_cb2):

    #------------------------------------------#
    # RADAR GRAPH
    #------------------------------------------#

    dfmasterfilter = dfmaster[dfmaster['Name'] == moviename_cb2]  # dynamic variable here
    radarvalues = dfmasterfilter[['Rotten Tomatoes Bin', 'Metascore Bin', 'imdbVotes Bin']]
    radarvalues = radarvalues.values.tolist()[0]
    radarvalues.append(radarvalues[0])
    radarlabels = ['Rotten Tomatoes', 'MetaScore', 'IMDB', 'Rotten Tomatoes']

    radarfig = go.Figure(data=go.Scatterpolar(
        r=radarvalues,
        theta=radarlabels,
        fill='toself',
        connectgaps=True,
        marker=dict(size=8,
                    ),
        line=dict(color='#0e3fa9')
    ))

    radarfig.update_layout(
        paper_bgcolor='#353535',
        margin=dict(
            l=50,
            r=50,
            t=15,
            b=15,
        ),
        polar=dict(
            bgcolor='#969696',
            radialaxis=dict(
                visible=True,
                ticktext=[0, 1, 2, 3, 4, 5],
                tickvals=[0, 1, 2, 3, 4, 5],
                tickmode='array',
                range=[0, 5],
            ),
        ),
        font=dict(
            color='#ffab03',
        ),
        showlegend=False
    )

    #------------------------------------------#
    # BAR GRAPH
    #------------------------------------------#

    colors = ['#ffab03', 'lightslategray']
    barlabels = ['Oscars', 'Nominations']
    barvalues = dfmasterfilter[['Oscar', 'Nominations']]
    barvalues = barvalues.values.tolist()[0]

    barfig = go.Figure(data=[go.Bar(
        x=barlabels,
        y=barvalues,
        text=barvalues,
        textfont=dict(
            color='white'
        ),
        textposition='auto',
        # opacity=0.50,
        marker=dict(
            color='rgba(255,171,3,0.45)',
            line=dict(
                color='#FFAB03',
                width=3,
            )
        )

       # marker_color=colors,
    )])

    barfig.update_layout(
        yaxis=dict(
            ticktext=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            tickvals=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            tickmode='array',
        ),
        plot_bgcolor='#353535',
        paper_bgcolor='#353535',
        margin=dict(
            l=50,
            r=50,
            t=15,
            b=15,
        ),
        font=dict(
            family='Impact, Charcoal, sans - serif',
            size=12,
            color='#ffab03',
        )
    ),

    #------------------------------------------#
    # SCATTER ANIMATED GRAPH
    #------------------------------------------#

    dfevofilter = dfevo[dfevo['Name'] == moviename_cb2]  # dynamic variable here
    dfevofilter = dfevofilter.drop(columns=['id', 'Name'])
    dfevofilter = dfevofilter.values.tolist()[0]
    dfevofilter = [0]+dfevofilter

    scatterfig = go.Figure(
        data=[go.Scatter(
            x=[0],
            y=[0],
            marker_color='#ffab03',
        )],
        layout=go.Layout(
            xaxis_title="Weeks",
            yaxis_title="Revenue",
            font=dict(
                family='Impact, Charcoal, sans - serif',
                size=12,
                color='#ffab03',
            ),
            margin=dict(
                l=50,
                r=50,
                t=15,
                b=15,
            ),
            plot_bgcolor='#353535',
            paper_bgcolor='#353535',
            xaxis=dict(range=[0, 23], autorange=False),
            yaxis=dict(range=[0, 950000000], autorange=False),
            updatemenus=[dict(
                type="buttons",
                y=-0,
                buttons=[dict(label="Play",
                              method="animate",
                              args=[None])])],
        ),
        frames=[go.Frame(data=[go.Scatter(x=scatterweek[0:1], y=dfevofilter[0:1])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:2], y=dfevofilter[0:2])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:3], y=dfevofilter[0:3])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:4], y=dfevofilter[0:4])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:5], y=dfevofilter[0:5])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:6], y=dfevofilter[0:6])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:7], y=dfevofilter[0:7])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:8], y=dfevofilter[0:8])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:9], y=dfevofilter[0:9])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:10], y=dfevofilter[0:10])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:11], y=dfevofilter[0:11])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:12], y=dfevofilter[0:12])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:13], y=dfevofilter[0:13])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:14], y=dfevofilter[0:14])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:15], y=dfevofilter[0:15])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:16], y=dfevofilter[0:16])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:17], y=dfevofilter[0:17])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:18], y=dfevofilter[0:18])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:19], y=dfevofilter[0:19])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:20], y=dfevofilter[0:20])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:21], y=dfevofilter[0:21])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:22], y=dfevofilter[0:22])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:23], y=dfevofilter[0:23])]),
                go.Frame(data=[go.Scatter(x=scatterweek[0:24], y=dfevofilter[0:24])]),
                ],
    )

    return radarfig, barfig, scatterfig

if __name__ == '__main__':
    app.run_server(debug=True)

#------------------------------------------#
