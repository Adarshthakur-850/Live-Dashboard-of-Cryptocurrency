import streamlit as st 
import pandas as pd 
from src .data_fetcher import get_top_coins ,get_historical_data 
from src .processing import process_market_data ,format_currency ,format_percentage 
from src .visualization import plot_price_history ,plot_market_overview 
from streamlit_autorefresh import st_autorefresh 


st .set_page_config (page_title ="Crypto Live Dashboard",layout ="wide",page_icon ="🪙")


count =st_autorefresh (interval =60000 ,limit =100 ,key ="fizzbuzz")

def main ():
    st .title ("🪙 Live Cryptocurrency Trends Dashboard")
    st .markdown ("Real-time market data fetched from CoinGecko.")


    st .sidebar .header ("Settings")
    num_coins =st .sidebar .slider ("Number of Coins",5 ,50 ,10 )
    days_history =st .sidebar .selectbox ("History Duration",["1","7","30","90","365"],index =1 )


    raw_df =get_top_coins (limit =num_coins )

    if raw_df .empty :
        st .warning ("Unable to fetch data. Check API connection.")
        return 


    top_coin =raw_df .iloc [0 ]
    col1 ,col2 ,col3 ,col4 =st .columns (4 )
    with col1 :
        st .metric (label =f"{top_coin ['name']} Price",
        value =format_currency (top_coin ['current_price']),
        delta =format_percentage (top_coin ['price_change_percentage_24h']))
    with col2 :
         st .metric (label ="Global Market Cap",value ="Unknown")


    col_table ,col_chart =st .columns ([1 ,2 ])

    processed_df =process_market_data (raw_df )

    with col_table :
        st .subheader ("Top Cryptocurrencies")
        st .dataframe (processed_df [['Name','Symbol','Current Price','Price Change Percentage 24H']],
        use_container_width =True )

    with col_chart :
        st .subheader ("Market Heatmap")
        fig_map =plot_market_overview (processed_df )
        st .plotly_chart (fig_map ,use_container_width =True )


    st .divider ()
    st .subheader ("Detailed Analysis")

    selected_coin_name =st .selectbox ("Select Coin for Detail View",raw_df ['name'].values )
    selected_coin_data =raw_df [raw_df ['name']==selected_coin_name ].iloc [0 ]
    coin_id =selected_coin_data ['id']


    hist_df =get_historical_data (coin_id ,days =days_history )


    fig_line =plot_price_history (hist_df ,selected_coin_name )
    st .plotly_chart (fig_line ,use_container_width =True )


    c1 ,c2 ,c3 =st .columns (3 )
    c1 .info (f"Market Cap: {format_currency (selected_coin_data ['market_cap'])}")
    c2 .info (f"Volume (24h): {format_currency (selected_coin_data ['total_volume'])}")
    c3 .info (f"24h Low/High: N/A")

if __name__ =="__main__":
    main ()
