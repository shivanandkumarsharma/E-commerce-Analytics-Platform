
import os
import pandas as pd
from sqlalchemy import create_engine

def load_data():
    file_path = os.path.join("app", "data", "cleaned_data.csv")
    df = pd.read_csv(file_path)
    return df

def load_to_db():
    file_path = os.path.join("app", "data", "cleaned_data.csv")
    df = pd.read_csv(file_path)

    engine = create_engine("postgresql://postgres:Shiva%40123@localhost:5432/ecommerce_db")
    df.to_sql("orders_data", engine, if_exists='replace', index=False)

    return "Data loaded to DB"

def get_data_from_db():
    engine = create_engine("postgresql://postgres:Shiva%40123@localhost:5432/ecommerce_db")
    
    query = "SELECT * FROM orders_data LIMIT 10"
    df = pd.read_sql(query, engine)
    
    return df

def revenue_by_city():
    engine = create_engine("postgresql://postgres:Shiva%40123@localhost:5432/ecommerce_db")
    
    query = """
    SELECT customer_city, SUM(revenue) AS total_revenue
    FROM orders_data
    GROUP BY customer_city
    ORDER BY total_revenue DESC
    """
    
    df = pd.read_sql(query, engine)
    return df

def top_products():
    engine = create_engine("postgresql://postgres:Shiva%40123@localhost:5432/ecommerce_db")
    
    query = """
    SELECT product_category_name, SUM(revenue) AS total_revenue
    FROM orders_data
    GROUP BY product_category_name
    ORDER BY total_revenue DESC
    LIMIT 5
    """
    
    df = pd.read_sql(query, engine)
    return df

def get_data_by_city(city: str):
    engine = create_engine("postgresql://postgres:Shiva%40123@localhost:5432/ecommerce_db")
    
    query = """
    SELECT *
    FROM orders_data
    WHERE customer_city = %(city)s
    LIMIT 10
    """
    
    df = pd.read_sql(query, engine, params={"city": city})
    return df

def get_revenue_dynamic(city: str = None, limit: int = 10):
    engine = create_engine("postgresql://postgres:Shiva%40123@localhost:5432/ecommerce_db")
    
    base_query = """
    SELECT customer_city, SUM(revenue) AS total_revenue
    FROM orders_data
    """
    
    params = {}

    if city:
        base_query += " WHERE LOWER(customer_city) = LOWER(%(city)s)"
        params["city"] = city

    base_query += " GROUP BY customer_city ORDER BY total_revenue DESC"
    base_query += " LIMIT %(limit)s"
    params["limit"] = limit

    df = pd.read_sql(base_query, engine, params=params)
    return df

def monthly_revenue():
    engine = create_engine("postgresql://postgres:Shiva%40123@localhost:5432/ecommerce_db")

    query = """
    SELECT year, month, SUM(revenue) AS total_revenue
    FROM orders_data
    GROUP BY year, month
    ORDER BY year, month
    """

    df = pd.read_sql(query, engine)
    return df

def revenue_by_year():
    engine = create_engine("postgresql://postgres:Shiva%40123@localhost:5432/ecommerce_db")

    query = """
    SELECT year, SUM(revenue) AS total_revenue
    FROM orders_data
    GROUP BY year
    ORDER BY year
    """

    df = pd.read_sql(query, engine)
    return df

def average_order_value():
    engine = create_engine("postgresql://postgres:Shiva%40123@localhost:5432/ecommerce_db")

    query = """
    SELECT AVG(revenue) AS avg_order_value
    FROM orders_data
    """

    df = pd.read_sql(query, engine)
    return df

def orders_by_city():
    engine = create_engine("postgresql://postgres:Shiva%40123@localhost:5432/ecommerce_db")

    query = """
    SELECT customer_city, COUNT(order_id) AS total_orders
    FROM orders_data
    GROUP BY customer_city
    ORDER BY total_orders DESC
    """

    df = pd.read_sql(query, engine)
    return df

def daily_revenue(limit: int = 100):
    engine = create_engine("postgresql://postgres:Shiva%40123@localhost:5432/ecommerce_db")

    query = """
    SELECT order_date, SUM(revenue) AS total_revenue
    FROM orders_data
    GROUP BY order_date
    ORDER BY order_date
    LIMIT %(limit)s
    """

    df = pd.read_sql(query, engine, params={"limit": limit})
    return df