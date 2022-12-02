# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import all_infos

app = Dash(__name__)

colors = {
  'background': '#111111',
  'text': '#7FDBFF'
}

# fig3 = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
#                  cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
#                 ])

system_info = all_infos.system_info().node


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
  html.H1(
    children='Dashboard',
    style={
      'textAlign': 'center',
      'color': colors['text']
    }
  ),
  html.Div(children=system_info, style={
    'textAlign': 'center',
    'color': colors['text']
  }),
  html.Ul(
    html.Li(
      
    )
  )

])

if __name__ == '__main__':
  app.run_server(debug=True)