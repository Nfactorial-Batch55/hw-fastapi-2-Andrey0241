from fastapi import FastAPI, Response, HTTPException
from typing import Optional
from .cars import create_cars

cars = create_cars(100)  # Здесь хранятся список машин
app = FastAPI()

@app.get("/")
def index():
    return Response("<a href='/cars'>Cars</a>")

# Маршрут для получения списка машин с пагинацией
@app.get("/cars")
def get_cars(page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit
    paginated_cars = cars[start:end]
    if not paginated_cars:
        raise HTTPException(status_code=404, detail="Cars not found")
    return paginated_cars

# Маршрут для получения машины по ID
@app.get("/cars/{car_id}")
def get_car_by_id(car_id: int):
    car = next((car for car in cars if car["id"] == car_id), None)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car
