# candlestick_chart_creator.py

import plotly.graph_objects as go


def create_candlestick_chart(df):
    fig = go.Figure(data=[
        go.Candlestick(
            x=df.index.date,
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            showlegend=False
        )
    ])

    fig.update_layout(
        title={
            'text': 'Candlestick Chart',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Arial Black')
        },
        xaxis=dict(
            title=dict(text='Date', font=dict(size=16)),
            tickfont=dict(size=12),
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.3)',
            gridwidth=1,
            rangeslider=dict(visible=False)
        ),
        yaxis=dict(
            title=dict(text='Price', font=dict(size=16)),
            tickfont=dict(size=12),
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.3)',
            gridwidth=1,
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family="Arial", size=12),
        margin=dict(l=50, r=50, t=80, b=50),
    )

    fig.update_xaxes(type='category')
    fig.update_yaxes(tickprefix="$")

    fig.show()
