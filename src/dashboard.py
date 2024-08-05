from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# Load cleaned data
data_path = '/Users/vaibhavmonpara/Documents/GitHub/ecsa-project/data/visualization/'
eda_data = pd.read_csv(f'{data_path}eda_results.csv')
predictive_data = pd.read_csv(f'{data_path}predictive_results.csv')
sustainability_data = pd.read_csv(f'{data_path}sustainability_results.csv')

# Create visualizations
eda_fig = px.histogram(eda_data, x='Total Renewable Energy', title='EDA Results: Feature Distribution')
predictive_fig = px.line(predictive_data, x='Date', y='Prediction', title='Predictive Analysis: Forecasted Values')
sustainability_fig = px.bar(sustainability_data, x='Sector', y='Energy_Usage', title='Sustainability Analysis: Energy Usage by Sector')

# Create the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Energy Consumption and Sustainability Dashboard'),

    html.Div(children=[
        html.H2(children='Exploratory Data Analysis'),
        dcc.Graph(id='eda-graph', figure=eda_fig),
    ]),
    
    html.Div(children=[
        html.H2(children='Predictive Analysis'),
        dcc.Graph(id='predictive-graph', figure=predictive_fig),
    ]),

    html.Div(children=[
        html.H2(children='Sustainability Analysis'),
        dcc.Graph(id='sustainability-graph', figure=sustainability_fig),
    ]),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)