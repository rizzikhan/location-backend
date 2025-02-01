from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

# ✅ Fix CORS
origins = ["https://location-frontend-ashy.vercel.app", "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Database Connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://neondb_owner:npg_1JGo0DBRbcyq@ep-still-butterfly-a8tudp7p-pooler.eastus2.azure.neon.tech/neondb?sslmode=require")

def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        return conn
    except Exception as e:
        print("🚨 Database Connection Error:", str(e))  
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

# ✅ Data Model
class LocationData(BaseModel):
    latitude: float
    longitude: float

# ✅ Store Location (POST Request)
@app.post("/location")
async def receive_location(data: LocationData):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Log incoming data for debugging
        print(f"📍 Inserting: Latitude={data.latitude}, Longitude={data.longitude}")

        cursor.execute("INSERT INTO locations (latitude, longitude) VALUES (%s, %s)", 
                       (data.latitude, data.longitude))
        conn.commit()
        cursor.close()
        conn.close()
        return {"status": "success", "message": "Location saved successfully"}
    except Exception as e:
        print("🚨 Error inserting data into database:", str(e))
        raise HTTPException(status_code=500, detail=f"Error saving location data: {str(e)}")

# ✅ View Stored Locations
@app.get("/admin", response_class=HTMLResponse)
async def admin_page():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, latitude, longitude FROM locations")
        locations = cursor.fetchall()
        cursor.close()
        conn.close()

        table = "<h2>Collected Locations</h2><table border='1'><tr><th>ID</th><th>Latitude</th><th>Longitude</th></tr>"
        for loc in locations:
            table += f"<tr><td>{loc[0]}</td><td>{loc[1]}</td><td>{loc[2]}</td></tr>"
        table += "</table>"

        return table
    except Exception as e:
        print("🚨 Error fetching data:", str(e))
        raise HTTPException(status_code=500, detail="Error retrieving location data")

# ✅ Root Endpoint (Fix "Not Found" on base URL)
@app.get("/")
def home():
    return {"message": "FastAPI Backend is running!"}
