# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import all_infos

app = Dash(__name__)

colors = {
  'background': '#222222',
  'text': '#fff'
}

# fig3 = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
#                  cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
#                 ])

system_info = all_infos.system_info()
processes = all_infos.all_processes()
memorys = all_infos.memorys()

def format_memory():
  vmemory = memorys[0].used[0] + "" + memorys[0].available[0] + "" + memorys[0].total[0] + "" + memorys[0].percent[0]
  smemory = memorys[1].used[0] + "" + memorys[1].available[0] + "" + memorys[1].total[0] + "" + memorys[1].percent[0]

  print(vmemory)
  print(smemory)

format_memory()
def list_of_processes():
  list = []
  for process in processes:
    process_info = str([process.pid[0]]) + " " + process.name[0] + "   " + process.status
    list.append(html.Li(children=process_info))
  
  return list

app.layout = html.Div(
  style={
    'background-color': colors['background'],
    'background-size': '100%',
    'position': 'fixed',
    'display': 'flex',
    'width': '100%',
    'height': '100%',
    'justify-content': 'space-between',
    'color': colors['text']
  }, 
  children=[
    # Machine and User Information
    html.Div(
      style={
        'position': 'relative',
        'width': '150px',
        'height': '350px',
        'margin-left': '45%'
      },
      children=[
        html.H1(
          children='Dashboard',
          style={
            'textAlign': 'center',
          }
        ),
        html.P(
          children=system_info.node,
          style={
            'textAlign': 'center'
          }
        ),
        html.P(
          children=system_info.machine[0] + " " + system_info.version[0] + " " +system_info.system[0],
          style={
            'textAlign': 'center'
          }
        ),
      ]
    ),
    # Processes Information
    html.Div(
      style={
        "border": "solid",
        "position": "fixed",
        "width": "350px",
        "overflow": "scroll",
        "top": 200,
        "left": 0,
        "bottom": 0,
      },
      children=[
        html.H3("Processes", 
        style={
          "margin": "15px"
        }),
        html.Ul(
          list_of_processes()
        )
      ]
    ),
    # Memory Information
    html.Div(
      style={
        "border": "solid",
        "position": "relative",
        "top": 200,
        "margin-right": '0.5vw',
        "height": "20vh"
      },
      children=[
        html.H3(style={"text-align": "center"}, children="Memory Information"),
        html.Table(
          children=[
            html.Tr(
              children=[
                html.Th(
                ),
                html.Th(
                  "Used"
                ),
                html.Th(
                  "Available"
                ),
                html.Th(
                  "Total"
                )
              ]
            ),
            html.Tr(
              children=[
                html.Td(
                  "Virtual Memory:  "
                ),
                html.Td(
                  memorys[0].used[0]
                ),
                html.Td(
                  memorys[0].available[0]
                ),
                html.Td(
                  memorys[0].total[0]
                ),
              ]
            ),
             html.Tr(
              children=[
                html.Td(
                  "Swap Memory: "
                ),
                html.Td(
                  memorys[1].used[0]
                ),
                html.Td(
                  memorys[1].available[0]
                ),
                html.Td(
                  memorys[1].total[0]
                ),
              ]
            )
          ]
        )
      ]
    ),
    # Cpu Information
    html.Div()
    # File System Information
  ]
)

if __name__ == '__main__':
  app.run_server(debug=True)