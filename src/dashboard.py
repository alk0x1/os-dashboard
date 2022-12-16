# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import all_infos


colors = {
  'background': '#131516',
  'text': '#fff'
}

external_css = [
    "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",
    "//fonts.googleapis.com/css?family=Roboto|Lato"
]

table_style = {
  "border": "1px solid",
  "padding": "5px",
  "text-align": "center"
}

table_div_style = {
  "position": "relative",
  "margin-right": '0.5vw',
  "padding": "5px"
}

app = Dash(__name__, external_stylesheets=external_css)
server = app.server
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
  table = html.Table(
    style={"list-style-type": "none"},
    children=[
      html.Tr(
        children=[
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
    ]
  )

  for disk in disks:
    table.children.append(html.Tr(
      children=[
        html.Td(children=disk.mountpoint[0], style=table_style),
        html.Td(children=disk.fstype[0], style=table_style),
        html.Td(children=disk.opts[0], style=table_style)
      ]
    )
  )

  return table


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
    'backgroundColor': colors['background'],
    'backgroundSize': '100%',
    'position': 'fixed',
    'display': 'flex',
    'width': '100%',
    'height': '100%',
    'justifyContent': 'space-between',
    'color': colors['text'],
  }, 
  children=[
    html.Div(
      style={
        'width': '100%',
      },
      children=[
        # Machine and User Information
        html.Div(
          style={
            'position': 'relative',
            'width': '100%',
            'height': '150px',
            'text-align': 'center'
          },
          children=[
            html.H1(
              children='Dashboard',
              style={
                'textAlign': 'center',
                'margin-top': '2vh'
              }
            ),
            html.P(
              children=system_info.node,
              style={
                'textAlign': 'center'
              }
            ),
            html.P(
              children=system_info.system[0] + " " + system_info.machine[0] + " " + system_info.version[0],
              style={
                'textAlign': 'center'
              }
            ),
          ]
        ),
        # Hardware and processes Information
        html.Div(
          style={
            'display': 'flex',
            'justifyContent': 'center',
            'marginTop': 100,
          },
          children=[
            # Processes Information
            html.Div(
              style={
                "width": "350px",
                "left": 0,
                "bottom": 0,
                "position": "relative",
                "marginRight": '0.6vw',
              },
              children=[
                dcc.Interval(
                  id='interval-process-component',
                  interval=1* 3000, # in milliseconds
                  n_intervals=0
                ),
                html.H3("Processes", 
                style={
                  "margin": "0px",
                  "padding-bottom": "10px"
                }),
                html.Div(
                  style={
                    "border": "1px solid",
                    "overflow": "scroll",
                    "paddingTop": "5px",
                    "height": "200px",
                    "overflow-x": "hidden"
                  },
                  children=html.Ul(
                    id="process-update",
                    style={"list-style-type": "none"},
                    children=list_of_processes(processes)
                  )
                )
              ]
            ),
            # Memory Information
            html.Div(
              style=table_div_style,
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
            # File System Information
            html.Div(
              style=table_div_style,
              children=[
                dcc.Interval(
                  id='get-all-disks',
                  interval=1*1000, # in milliseconds
                  n_intervals=0
                ),
                html.H3("Disks", 
                  style={
                    'text-align': 'center'
                  },
                ),
                list_of_disks(disks)
              ]
            ),
            html.Div(
              children=all_infos.get_top_command()
            )
          ]
        ),
      ]
    ),
  ]
)


if __name__ == '__main__':
  app.run_server(debug=True)
