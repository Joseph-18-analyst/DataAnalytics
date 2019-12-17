from google.cloud import bigquery
from google.oauth2 import service_account
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
# from queries import data1, data2, data3, data4, count, x_pos, language
import flask

credentials = service_account.Credentials.from_service_account_file(
    'iconic-computer-256417-4f325a5a4405.json')
project_id = 'iconic-computer-256417'
client = bigquery.Client(credentials=credentials, project=project_id)

query_job = client.query("""
                  SELECT *
                  FROM dataset_id_assignment2.table_assignment2
                  LIMIT 30109""")
results = query_job.result()  # Waits for job to complete.
py_result = results.to_dataframe()
col_age = py_result['age']
col_avg_glucose = py_result['avg_glucose_level']
bmi = py_result['bmi']
hypertension = py_result['hypertension']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#server = flask.Flask(__name__)
#server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server)

app.layout = html.Div(children=[
    html.H1(children='HealthCare_Statistics Age vs Avg_Glucose_Level', style={'text-align': 'center'}),
    html.Div(
        dcc.Graph(
            id='Health_statistics',
            figure={
                'data': [go.Scatter(x=col_age,
                                    y=col_avg_glucose, name='Age_Glucose',
                                    mode='markers'),
                         #             orientation = 'h',
                         # marker = {'color': [0, 1], 'colorscale': 'RdBu'})
                         # go.Scatter(x=list(col_age),
                         # y=list(bmi), name='Age_Bmi'),
                         ],

                'layout': go.Layout(
                    title='health stats', titlefont=dict(size=80, color='#177a21'),
                    # yaxis_zeroline=False, xaxis_zeroline=False,
                    xaxis={'title': 'Age1'},
                    # yaxis = {'title': 'glucose'},
                    # margin = go.Margin( l = 250 )
                )
            },
            # style={'width': '2800'}
        ),  # style={'width': '2800'},
    ),
    html.H1(children='HealthCare_Statistics -Age versus BMI ', style={'text-align': 'center'}),
    html.Div(
        dcc.Graph(
            id='Health_statistics_bmi',
            figure={
                'data': [
                    go.Scatter(x=col_age,
                               y=bmi, name='bmi_name',
                               mode='markers',
                               orientation='h',
                               marker={'color': [0, 5], 'colorscale': 'RdBu'}
                               ),

                    # go.Scatter(x=list(col_age),
                    # y=list(bmi), name='Age_Bmi'),
                ],

                'layout': go.Layout(
                    title='AGE_BMI', titlefont=dict(size=30, color='#177a21'),
                    xaxis={'title': 'Age-title'},
                    yaxis={'title': 'BMI_title'},
                    margin=go.Margin(l=250),
                )
            },
            # style={'width': '1200'}
        ),  # style={'width': '800'},
    ),

]
)

if __name__ == '__main__':
    app.run_server(debug=True)
