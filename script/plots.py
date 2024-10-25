import plotly.graph_objects as go


def plot_generator(
        df,
        parameter : str = None,
        title: str = None,
        colors: list = None,
        mode: str = 'lines',
        xlabel: str = None,
        ylabel: str = None,
        equipments_sn: list = [],
):
    
    fig = go.Figure()
    
    for n, equipment in enumerate(equipments_sn):

        fig = fig.add_trace(
            go.Scatter(
                x = df.index,
                y = df[f'{parameter}_{n+1}'], 
                name = equipment,
                mode = mode,
            )
        )
        if colors:
            color = colors[parameter.index(parameter)]
            fig.update_traces(marker=dict(color=color))
    
        if xlabel: fig.update_layout(xaxis_title = xlabel)
        if ylabel: fig.update_layout(yaxis_title = ylabel)
        if title: fig.update_layout(title=title)
    fig['data'][0]['showlegend']=True
    
    return fig


