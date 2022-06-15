import pandas as pd
from flask import Flask
import dash
from dash import html, dcc
import plotly.express as px




# load data
df =  pd.read_excel(r'C:\Users\gsarti\OneDrive - Deloitte (O365D)\Desktop\stockdata2.xlsx')


app_stock = dash.Dash(__name__)

# Define the app
app_stock.layout = html.Div()


app_stock.layout = html.Div(children=[
                      html.Div(className='row',  # Define the row element
                               children=[
					 # Define the left elements
                                  html.Div(className='four columns div-user-controls',
				  children=[
					html.H2('Dash - STOCK-PRICES'),
					html.P('''Visualising time series with Ploty - Dash'''),
					html.P('''Pick one or more stocks from the dropdown below''')
					]), 
					# Define the right element
                                  html.Div(className='eight columns div-for-charts bg-grey',
				  children=[
					dcc.Graph(id="timeseries",
						 config={'displayModeBar': False},
          					animate=True,
          					figure=px.line(df,
                         				x='Date',
                         				y='value',
                         				color='stock',
                         				template='plotly_dark').update_layout(
                                   			{'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    			'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                    )])  
                                  ])
                                ])


# Run the app
if __name__== '__main__':
	app_stock.run_server(debug=True)
