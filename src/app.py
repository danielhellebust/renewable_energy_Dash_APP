import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px


# Read data
df = pd.read_csv('dataset/energy_dataset.csv')

sub_df = df[df['Entity'] == 'Chile']
fig = px.area(sub_df,x='Year', y=['Hydro (% equivalent primary energy)',
                                   'Wind (% equivalent primary energy)',
                                   'Solar (% equivalent primary energy)',
                                   'Other Renewables (% equivalent primary energy)'],
              color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_layout(
    title="Renewable Energy in Chile",
    xaxis_title="Year",
    yaxis_title="Renewable Energy (%)",
    legend_title="Energy Source",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    xaxis=dict(
        tickmode='array',
        tickvals=[1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020,2022],
        ticktext=['1965', '1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010', '2015', '2020','2022'],
        tickfont=dict(
            family='Courier New, monospace',
            size=18,
            color='#696969'
        )
    ),
    yaxis=dict(
        tickmode='array',
        tickvals=[0,10,20,30,40,50,60,70,80,90,100],
        ticktext=['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
        tickfont=dict(
            family='Courier New, monospace',
            size=18,
            color='#696969'
        ),

    ),
)
fig.update_yaxes(nticks=10)
fig.update_yaxes(autorange=False, range=[0, 40])
fig.update_xaxes(anchor="free", position=1)


sub_df_world = df[df['Entity'] == 'World']
fig2 = px.area(sub_df_world,x='Year', y=['Hydro (% equivalent primary energy)',
                                      'Wind (% equivalent primary energy)',
                                      'Solar (% equivalent primary energy)',
                                      'Other Renewables (% equivalent primary energy)'],
                  color_discrete_sequence=px.colors.qualitative.Pastel)
fig2.update_layout(
    title="Renewable Energy in the World",
    xaxis_title="Year",
    yaxis_title="Renewable Energy (%)",
    legend_title="Energy Source",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    xaxis=dict(
        tickmode='array',
        tickvals=[1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020,2022],
        ticktext=['1965', '1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010', '2015', '2020','2022'],
        tickfont=dict(
            family='Courier New, monospace',
            size=18,
            color='#696969'
        )
    ),
    yaxis=dict(
        tickmode='array',
        tickvals=[0,10,20,30,40,50,60,70,80,90,100],
        ticktext=['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
        tickfont=dict(
            family='Courier New, monospace',
            size=18,
            color='#696969'
        ),

    ),
)
fig2.update_yaxes(nticks=10)
fig2.update_yaxes(autorange=False, range=[0, 40])


df_energy_2021 = df[(df['Year'] == 2021)&(df['Entity'].isin(['World', 'Norway']))]
top10_df_energy_2021 = df_energy_2021.sort_values(by=['Renewables (% equivalent primary energy)'], ascending=False)[:15]
top10_df_energy_2021 = top10_df_energy_2021.sort_values(by=['Entity'], ascending=False)



fig3 = go.Figure(data=[
go.Bar(name='Hydro( % of Renewable)', x=top10_df_energy_2021['Hydro (% renewable)'], y=top10_df_energy_2021['Entity'], orientation='h', text=top10_df_energy_2021['Hydro (% renewable)'],
       textposition='inside',
        textfont=dict(
                family="Courier New, monospace",
                size=18,
                color="black"
            ),
       marker_color='rgb(102, 197, 204)'),
    go.Bar(name='Wind( % of Renewable)', x=top10_df_energy_2021['Wind (% renewable)'], y=top10_df_energy_2021['Entity'], orientation='h',text=top10_df_energy_2021['Wind (% renewable)'],
           textposition='inside',
           textfont=dict(
                family="Courier New, monospace",
                size=18,
                color="black"
            ),
           marker_color='rgb(246, 207, 113)'),
    go.Bar(name='Solar( % of Renewable)', x=top10_df_energy_2021['Solar (% renewable)'], y=top10_df_energy_2021['Entity'], orientation='h',text=top10_df_energy_2021['Solar (% renewable)'],
           textposition='inside',
            textfont=dict(
                family="Courier New, monospace",
                size=18,
                color="black"
            ),
           marker_color='rgb(248, 156, 116)'),
    go.Bar(name='Other renewable( % of Renewable)', x=top10_df_energy_2021['Others (% renewable)'], y=top10_df_energy_2021['Entity'], orientation='h',text=top10_df_energy_2021['Others (% renewable)'],
           textposition='inside',
            textfont=dict(
                family="Courier New, monospace",
                size=18,
                color="black"
            ),
           marker_color='rgb(220, 176, 242)'),
],)
# Change the bar mode
fig3.update_layout(barmode='stack',
                   title="Distribution of Renewable Energy in Chile VS the World",
                   xaxis_title="Percentage (%)",
                    yaxis_title="Country",
                     legend_title="Energy Source",
                     font=dict(
                          family="Courier New, monospace",
                          size=14,
                          color="#7f7f7f"
                        ),


)
fig3.update_yaxes(tickfont=dict(
            family='Courier New, monospace',
            size=18,
            color='#696969'
        )
)
fig3.update_xaxes(tickfont=dict(
            family='Courier New, monospace',
            size=18,
            color='#696969'
        )
)



# Create app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Create layout
app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Row(html.Div(html.H1('Renewable Energy',
                    style={'text-align': 'center', 'color': 'white', 'padding-top': '10px'}))),
            dbc.Row([
            dbc.Row(dcc.Loading(dcc.Graph(id='line_chart1', figure=fig))),
            dbc.Row(dcc.Loading(dcc.Graph(id='line_chart2', figure=fig2))),
            dbc.Row(
                dbc.Row(
                    dcc.Loading(dcc.Graph(id='bar_chart', figure=fig3), style={'width': '95%','height': '300px'})),
                style={'width': '100%','background-color': 'white'}),
            ],style={'width': '100%','background-color': 'white'}),

        ],md=10),
        dbc.Col([
            dbc.Row(html.Div(html.H1('Filter',
                    style={'text-align': 'center', 'color': 'white', 'padding-top': '10px'}))),
            dbc.Row([
                html.Div(html.H4('Select a country',
                    style={'text-align': 'left', 'color': 'white', 'padding-top': '10px'})),
                dcc.Dropdown(
                id='dropdown',
                style={'width': '100%', 'font-size': '20px', 'color': 'grey'},
                options=[{'label': i, 'value': i} for i in df['Entity'].unique()],
                placeholder="Select a country, default Norway",
                value=None,
                multi=False

            )]),
            dbc.Row([
                html.Div(html.H4('Select a comparison country',
                    style={'text-align': 'left', 'color': 'white', 'padding-top': '10px'})),
                dcc.Dropdown(
                id='dropdown2',
                style={'width': '100%', 'font-size': '20px', 'color': 'grey'},
                options=[{'label': i, 'value': i} for i in df['Entity'].unique()],
                placeholder="Select a country, default World",
                value=None,
                multi=False

            )]),
            dbc.Row([
                html.Div(html.H4('Select a year for Renewable Energy distribution',
                    style={'text-align': 'left', 'color': 'white', 'padding-top': '800px'})),
                dcc.Dropdown(
                id='dropdown3',
                style={'width': '100%', 'font-size': '20px', 'color': 'grey'},
                options=[{'label': i, 'value': i} for i in df['Year'].unique()],
                placeholder="Select a year, default 2021",
                value=None,
                multi=False

            )]),
        ],md=2),

], style={'width': '100%', 'height': '1400px' ,'background-color': 'black'})

])

# Create callback
@app.callback(
    [Output('line_chart1', 'figure'),
     Output('line_chart2', 'figure'),
     Output('bar_chart', 'figure')],
    [Input('dropdown', 'value'),
     Input('dropdown2', 'value'),
     Input('dropdown3', 'value')]
)

def update_graph(country1,country2,year):
    if country1 == None:
        country1 = 'Norway'
    if country2 == None:
        country2 = 'World'

    if year == None:
        year = 2021



    df_energy_1 = df[df['Entity'] == country1]
    df_energy_2 = df[df['Entity'] == country2]

    df_energy_year = df[(df['Year'] == year) & (df['Entity'].isin([country1, country2]))]
    top10_df_energy_2021 = df_energy_year.sort_values(by=['Renewables (% equivalent primary energy)'], ascending=False)[
                           :15]


    top10_df_energy_2021['sort'] = top10_df_energy_2021['Entity'].apply(lambda x: 1 if x == country1 else 0)
    top10_df_energy_2021 = top10_df_energy_2021.sort_values(by=['sort'], ascending=True)



    max_y_value_graph1_c1 = df_energy_1['Renewables (% equivalent primary energy)'].max()+5
    max_y_value_graph1_c2 = df_energy_2['Renewables (% equivalent primary energy)'].max() + 5
    max_y_value_graph1 = max(max_y_value_graph1_c1, max_y_value_graph1_c2)


    fig = px.area(df_energy_1, x='Year', y=['Hydro (% equivalent primary energy)',
                                 'Wind (% equivalent primary energy)',
                                 'Solar (% equivalent primary energy)',
                                 'Other Renewables (% equivalent primary energy)'],
            color_discrete_sequence=px.colors.qualitative.Pastel)

    fig.update_layout(
        title=f'Renewable Energy(% equivalent primary energy) in {country1}',
        xaxis_title="Year",
        yaxis_title="Percentage (%)",
        legend_title="Energy Source",
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="#7f7f7f"
        ),
        xaxis=dict(
            tickmode='array',
            tickvals=[1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2022],
            ticktext=['1965', '1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010', '2015', '2020',
                      '2022'],
            tickfont=dict(
                family='Courier New, monospace',
                size=18,
                color='#696969'
            )
        ),
        yaxis=dict(
            tickmode='array',
            tickvals=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
            ticktext=['0','5','10','15','20','25','30','35','40','45','50','55','60','65','70','75','80','85','90','95','100'],
            tickfont=dict(
                family='Courier New, monospace',
                size=18,
                color='#696969'
            ),

        ),
    )
    fig.update_yaxes(autorange=False, range=[0, max_y_value_graph1])
    fig.update_yaxes(nticks=5)


    fig2 = px.area(df_energy_2, x='Year', y=['Hydro (% equivalent primary energy)',
                                            'Wind (% equivalent primary energy)',
                                            'Solar (% equivalent primary energy)',
                                            'Other Renewables (% equivalent primary energy)'],
                  color_discrete_sequence=px.colors.qualitative.Pastel)

    fig2.update_layout(
        title=f'Renewable Energy(% equivalent primary energy) in {country2}',
        xaxis_title="Year",
        yaxis_title="Percentage (%)",
        legend_title="Energy Source",
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="#7f7f7f"
        ),
        xaxis=dict(
            tickmode='array',
            tickvals=[1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2022],
            ticktext=['1965', '1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010', '2015', '2020',
                      '2022'],
            tickfont=dict(
                family='Courier New, monospace',
                size=18,
                color='#696969'
            )
        ),
        yaxis=dict(
            tickmode='array',
            tickvals=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
            ticktext=['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75',
                      '80', '85', '90', '95', '100'],
            tickfont=dict(
                family='Courier New, monospace',
                size=18,
                color='#696969'
            ),

        ),
    )
    fig2.update_yaxes(autorange=False, range=[0, max_y_value_graph1])
    fig2.update_yaxes(nticks=5)

    fig3 = go.Figure(data=[
        go.Bar(name='Hydro( % of Renewable)', x=top10_df_energy_2021['Hydro (% renewable)'],
               y=top10_df_energy_2021['Entity'], orientation='h', text=top10_df_energy_2021['Hydro (% renewable)'],
               textposition='inside',
               textfont=dict(
                   family="Courier New, monospace",
                   size=18,
                   color="black"
               ),
               marker_color='rgb(102, 197, 204)'),
        go.Bar(name='Wind( % of Renewable)', x=top10_df_energy_2021['Wind (% renewable)'],
               y=top10_df_energy_2021['Entity'], orientation='h', text=top10_df_energy_2021['Wind (% renewable)'],
               textposition='inside',
               textfont=dict(
                   family="Courier New, monospace",
                   size=18,
                   color="black"
               ),
               marker_color='rgb(246, 207, 113)'),
        go.Bar(name='Solar( % of Renewable)', x=top10_df_energy_2021['Solar (% renewable)'],
               y=top10_df_energy_2021['Entity'], orientation='h', text=top10_df_energy_2021['Solar (% renewable)'],
               textposition='inside',
               textfont=dict(
                   family="Courier New, monospace",
                   size=18,
                   color="black"
               ),
               marker_color='rgb(248, 156, 116)'),
        go.Bar(name='Other renewable( % of Renewable)', x=top10_df_energy_2021['Others (% renewable)'],
               y=top10_df_energy_2021['Entity'], orientation='h', text=top10_df_energy_2021['Others (% renewable)'],
               textposition='inside',
               textfont=dict(
                   family="Courier New, monospace",
                   size=18,
                   color="black"
               ),
               marker_color='rgb(220, 176, 242)'),
    ], )
    # Change the bar mode
    fig3.update_layout(barmode='stack',
                       title=f'Distribution of Renewable Energy in {country1} VS {country2} in {year}',
                       xaxis_title="Percentage (%)",
                       yaxis_title="Country",
                       legend_title="Energy Source",
                       font=dict(
                           family="Courier New, monospace",
                           size=14,
                           color="#7f7f7f"
                       ),

                       )
    fig3.update_yaxes(tickfont=dict(
        family='Courier New, monospace',
        size=18,
        color='#696969'
    )
    )
    fig3.update_xaxes(tickfont=dict(
        family='Courier New, monospace',
        size=18,
        color='#696969'
    )
    )

    return fig,fig2,fig3


if __name__ == '__main__':
    app.run_server(debug=True)