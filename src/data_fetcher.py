import requests 
import pandas as pd 
import streamlit as st 
import time 


BASE_URL ="https://api.coingecko.com/api/v3"

@st .cache_data (ttl =60 )
def get_top_coins (limit =10 ):
    url =f"{BASE_URL }/coins/markets"
    params ={
    "vs_currency":"usd",
    "order":"market_cap_desc",
    "per_page":limit ,
    "page":1 ,
    "sparkline":"false"
    }
    try :
        response =requests .get (url ,params =params )
        response .raise_for_status ()
        return pd .DataFrame (response .json ())
    except Exception as e :
        st .error (f"Error fetching data: {e }")
        return pd .DataFrame ()

@st .cache_data (ttl =300 )
def get_historical_data (coin_id ,days ='7'):
    url =f"{BASE_URL }/coins/{coin_id }/market_chart"
    params ={
    "vs_currency":"usd",
    "days":days 
    }
    try :
        response =requests .get (url ,params =params )
        response .raise_for_status ()
        data =response .json ()

        prices =data .get ('prices',[])
        df =pd .DataFrame (prices ,columns =['timestamp','price'])
        df ['timestamp']=pd .to_datetime (df ['timestamp'],unit ='ms')
        return df 
    except Exception as e :
        st .error (f"Error fetching historical data: {e }")
        return pd .DataFrame ()
