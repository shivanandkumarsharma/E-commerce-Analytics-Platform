from fastapi import APIRouter, HTTPException
from app.services.data_services import (
    load_data,
    load_to_db,
    get_data_from_db,
    revenue_by_city,
    top_products,
    get_data_by_city,
    get_revenue_dynamic,
    monthly_revenue,
    revenue_by_year,
    average_order_value,
    orders_by_city,
    daily_revenue
)
from app.logger import logger

router = APIRouter()


@router.get("/test")
def test_api():
    try:
        logger.info("Test API hit")
        return {
            "status": "success",
            "message": "API is working"
        }
    except Exception as e:
        logger.error(f"Error in /test: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/revenue-by-city")
def get_revenue(limit: int = 5):
    try:
        logger.info(f"Fetching revenue from CSV | limit={limit}")
        df = load_data()
        data = df.head(limit).to_dict(orient="records")

        return {
            "status": "success",
            "count": len(data),
            "data": data
        }
    except Exception as e:
        logger.error(f"Error in /revenue-by-city: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/load-data-to-db")
def load_data_to_db():
    try:
        logger.info("Loading data into PostgreSQL")
        result = load_to_db()

        return {
            "status": "success",
            "message": result
        }
    except Exception as e:
        logger.error(f"Error in /load-data-to-db: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get-data-from-db")
def fetch_data():
    try:
        logger.info("Fetching data from DB")
        df = get_data_from_db()
        data = df.to_dict(orient="records")

        return {
            "status": "success",
            "count": len(data),
            "data": data
        }
    except Exception as e:
        logger.error(f"Error in /get-data-from-db: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/revenue-by-city-db")
def get_revenue_city():
    try:
        logger.info("Fetching revenue by city from DB")
        df = revenue_by_city()
        data = df.to_dict(orient="records")

        return {
            "status": "success",
            "count": len(data),
            "data": data
        }
    except Exception as e:
        logger.error(f"Error in /revenue-by-city-db: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/top-products")
def get_top_products():
    try:
        logger.info("Fetching top products")
        df = top_products()
        data = df.to_dict(orient="records")

        return {
            "status": "success",
            "count": len(data),
            "data": data
        }
    except Exception as e:
        logger.error(f"Error in /top-products: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/city/{city_name}")
def get_city_data(city_name: str):
    try:
        logger.info(f"Fetching data for city: {city_name}")
        df = get_data_by_city(city_name)
        data = df.to_dict(orient="records")

        return {
            "status": "success",
            "count": len(data),
            "data": data
        }
    except Exception as e:
        logger.error(f"Error in /city/{city_name}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/revenue")
def revenue(city: str = None, limit: int = 10):
    try:
        logger.info(f"Dynamic revenue API | city={city}, limit={limit}")
        df = get_revenue_dynamic(city, limit)
        data = df.to_dict(orient="records")

        return {
            "status": "success",
            "count": len(data),
            "data": data
        }
    except Exception as e:
        logger.error(f"Error in /revenue: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/monthly-revenue")
def get_monthly_revenue():
    try:
        logger.info("Fetching monthly revenue trend")
        df = monthly_revenue()
        data = df.to_dict(orient="records")

        return {"status": "success", "count": len(data), "data": data}
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/revenue-by-year")
def get_revenue_year():
    try:
        logger.info("Fetching yearly revenue")
        df = revenue_by_year()
        data = df.to_dict(orient="records")

        return {"status": "success", "count": len(data), "data": data}
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/average-order-value")
def get_aov():
    try:
        logger.info("Fetching AOV")
        df = average_order_value()
        data = df.to_dict(orient="records")

        return {"status": "success", "data": data}
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/orders-by-city")
def get_orders_city():
    try:
        logger.info("Fetching order count by city")
        df = orders_by_city()
        data = df.to_dict(orient="records")

        return {"status": "success", "count": len(data), "data": data}
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/daily-revenue")
def get_daily_revenue(limit: int = 100):
    try:
        logger.info(f"Fetching daily revenue | limit={limit}")
        df = daily_revenue(limit)
        data = df.to_dict(orient="records")

        return {"status": "success", "count": len(data), "data": data}
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail=str(e))