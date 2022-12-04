# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import all_infos


colors = {
  'background': '#222222',
  'text': '#fff'
}

external_css = [
    "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",
    "//fonts.googleapis.com/css?family=Roboto|Lato"
]

table_style = {
  "border": "1px solid",
  "padding": "5px"
}

app = Dash(__name__, external_stylesheets=external_css)
# get values statically
system_info = all_infos.system_info()
processes = all_infos.all_processes()
memorys = all_infos.memorys()
disks = all_infos.disk_info()

def list_of_processes(processes):
  list = []
  for process in processes:
    process_info = str([process.pid[0]]) + " " + process.name[0] + "   " + process.status
    list.append(html.Li(children=process_info))
  
  return list

def list_of_disks(disks):
  list = []

  for disk in disks:
    disk_info = disk.mountpoint[0] + " " + disk.fstype[0] + " " + disk.opts[0]
    print(disk_info)
    list.append(html.Tr(
      children=[(
        html.Td(children=disk_info, style=table_style)
      )]
    ))
  print(list)
  return list


# get values dynamically
@app.callback(Output('vmemory_used', 'children'), Input('interval-component', 'n_intervals'))
def get_dynamic_vmemory_used(n):
 return all_infos.memorys()[0].used[0]

@app.callback(Output('vmemory_available', 'children'), Input('interval-component', 'n_intervals'))
def get_dynamic_vmemory_available(n):
 return all_infos.memorys()[0].available[0]

@app.callback(Output('smemory_used', 'children'), Input('interval-component', 'n_intervals'))
def get_dynamic_smemory_used(n):
 return all_infos.memorys()[1].used[0]

@app.callback(Output('smemory_available', 'children'), Input('interval-component', 'n_intervals'))
def get_dynamic_smemory_available(n):
 return all_infos.memorys()[1].available[0]

@app.callback(Output('process-update', 'children'), Input('interval-process-component', 'n_intervals'))
def get_process_update(n):
  processes = all_infos.all_processes()
  return list_of_processes(processes)


app.layout = html.Div(
  style={
    'background-color': colors['background'],
    'background-size': '100%',
    'position': 'fixed',
    'display': 'flex',
    'width': '100%',
    'height': '100%',
    'justify-content': 'space-between',
    'color': colors['text'],
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
        dcc.Interval(
          id='interval-process-component',
          interval=1*3000, # in milliseconds
          n_intervals=0
        ),
        html.H3("Processes", 
        style={
          "margin": "15px"
        }),
        html.Ul(
          id="process-update",
          style={"list-style-type": "none"},
          children=list_of_processes(processes)
        )
      ]
    ),
    # Memory Information
    html.Div(
      style={
        "position": "relative",
        "top": 200,
        "margin-right": '0.5vw',
        "height": "20vh",
        "padding": "5px"
      },
      children=[
        dcc.Interval(
          id='interval-component',
          interval=1*1000, # in milliseconds
          n_intervals=0
        ),
        html.H3(style={"text-align": "center"}, children="Memory Information"),
        html.Table(
          children=[
            html.Tr(
              children=[
                html.Th(
                  style=table_style,
                ),
                html.Th(
                  style=table_style,
                  children="Used"
                ),
                html.Th(
                  style=table_style,
                  children="Available"
                ),
                html.Th(
                  style=table_style,
                  children="Total"
                )
              ]
            ),
            html.Tr(
              children=[
                html.Td(
                  style=table_style,
                  children="Virtual Memory:  "
                ),
                html.Td(
                  id="vmemory_used",
                  style=table_style,
                  children=memorys[0].used[0]
                ),
                html.Td(
                  id="vmemory_available",
                  style=table_style,
                  children=memorys[0].available[0]
                ),
                html.Td(
                  style=table_style,
                  children=memorys[0].total[0]
                ),
              ]
            ),
            html.Tr(
              children=[
                html.Td(
                  style=table_style,
                  children="Swap Memory: "
                ),
                html.Td(
                  id="smemory_used",
                  style=table_style,
                  children=memorys[1].used[0]
                ),
                html.Td(
                  id="smemory_available",
                  style=table_style,
                  children=memorys[1].available[0]
                ),
                html.Td(
                  style=table_style,
                  children=memorys[1].total[0]
                ),
              ]
            )
          ]
        )
      ]
    ),
    # Cpu Information
    html.Div(),
    # File System Information
    html.Div(
      style={
        "position": "relative",
        "top": 200,
        "margin-right": '0.5vw',
        "height": "20vh",
        "padding": "5px"
      },
      children=[
        html.H3("Disks", 
          style={
            "margin": "15px"
          },
        ),
        html.Ul(
          children=[
            html.Tr(
              children=[
                html.Th(
                  style=table_style,
                ),
                html.Th(
                  style=table_style,
                  children="mountpoint"
                ),
                html.Th(
                  style=table_style,
                  children="fstype"
                ),
                html.Th(
                  style=table_style,
                  children="opts"
                )
              ]
            ),
            list_of_disks(disks)[0]
          ],
          style={"list-style-type": "none"}
        )
      ]
    )
  ]
)


if __name__ == '__main__':
  app.run_server(debug=True)