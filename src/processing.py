import pandas as pd 

def process_market_data (df ):
    if df .empty :
        return df 


    cols =['id','symbol','name','current_price','market_cap',
    'total_volume','price_change_percentage_24h','image']


    cols =[c for c in cols if c in df .columns ]
    df =df [cols ]


    df .columns =[c .replace ('_',' ').title ()for c in df .columns ]

    return df 

def format_currency (value ):
    return f"${value :,.2f}"

def format_percentage (value ):
    return f"{value :.2f}%"
