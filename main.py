import dash
import dash_core_components as dcc
import dash_html_components as html
from phrase_interface.main import Phrase
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table

app = dash.Dash(__name__)

phrase = Phrase()
phrase.read_model()
phrase.batch_normalise()
phrase.batch_cosine()

app.layout = html.Div(children=[
    html.H1(children='Phrase It', style={'textAlign': 'center'}),
    dbc.Row([
        dbc.Col(children=[
            html.H2(children='User phrase input'),
            dcc.Input(
                id="user_phrase",
                type='text',
                placeholder="Input phrase to match",
            ),
            dbc.Button("Match Phrase", id="button_phrase"),
            html.P(id="matched_phrase"),
            html.P(id="matched_cosine")
        ]),
        dbc.Col(children=[
            html.H2(children='Cosine Similarity Matrix'),
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in phrase.cosine_matrix.columns],
                data=phrase.cosine_matrix.to_dict('records'),
                style_table={
                        'overflowY': 'auto',
                        'overflowX': 'auto',
                        "height": 600, "width":1200
                    }
                ),
            ],style={"margin-top": "50px"}),
    ])
])


@app.callback(
    [Output(component_id='matched_phrase', component_property='children'),
     Output(component_id='matched_cosine', component_property='children')],
    Input(component_id='button_phrase', component_property='n_clicks'),
    State(component_id='user_phrase', component_property='value')
)
def update_output_div(click, input_value):
    try:
        matched_phrase, matched_cosine_value = phrase.similar_phrase(input_value)
    except:
        matched_phrase, matched_cosine_value = 'Not matched', 0
    return [f"Matched Phrase - {matched_phrase}"], [f"Cosine Value - {matched_cosine_value}"]


if __name__ == '__main__':
    print(phrase.similar_phrase('acquisitions in 2020'))
    app.run_server()
