import plotly .graph_objects as go 
import plotly .express as px 

def plot_price_history (df ,coin_name ):
    if df .empty :
        return go .Figure ()

    fig =px .line (df ,x ='timestamp',y ='price',
    title =f'{coin_name } Price Trend',
    labels ={'price':'Price (USD)','timestamp':'Time'})

    fig .update_layout (
    template ='plotly_dark',
    xaxis_title =None ,
    yaxis_title =None ,
    margin =dict (l =0 ,r =0 ,t =30 ,b =0 )
    )
    return fig 

def plot_candlestick (df ,coin_name ):






    pass 

def plot_market_overview (df ):
    if df .empty :
        return go .Figure ()

    fig =px .treemap (df ,path =['Name'],values ='Market Cap',
    color ='Price Change Percentage 24H',
    color_continuous_scale ='RdYlGn',
    color_continuous_midpoint =0 ,
    title ='Crypto Market Cap Heatmap (24h Change)')
    fig .update_layout (template ='plotly_dark')
    return fig 
