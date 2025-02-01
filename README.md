# 🗄️ Backend - Location Tracker

## 🚀 Project Overview

This is the backend for the Location Tracker application. It handles API requests from the frontend, stores user geolocation data in a PostgreSQL database, and provides an admin interface to view collected data.

## 🛠️ Technologies Used

- **FastAPI (Python)**: For building the REST API.
- **PostgreSQL (NeonDB)**: For storing geolocation data.
- **Vercel**: For deploying the backend as serverless functions.

---

## 📂 Folder Structure

```
location-backend/
├── index.py              # FastAPI application
├── requirements.txt     # Python dependencies
└── vercel.json          # Vercel deployment configuration
```

---

## ⚙️ Installation and Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/location-backend.git
   cd location-backend
   ```

2. **Set Up Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database Connection:**

   - Add your PostgreSQL database URL inside `main.py`:
     ```python
     DATABASE_URL = "postgresql://username:password@hostname:port/dbname"
     ```

5. **Run the API Locally:**

   ```bash
   uvicorn main:app --reload
   ```

6. **Deploy on Vercel:**
   ```bash
   vercel --prod
   ```

---

## 🚀 API Endpoints

### 1. **POST `/location`**

- **Description:** Stores geolocation data.
- **Request Body:**
  ```json
  {
    "latitude": 37.7749,
    "longitude": -122.4194
  }
  ```
- **Response:**
  ```json
  { "status": "success", "message": "Location saved successfully" }
  ```

### 2. **GET `/admin`**

- **Description:** Displays collected geolocation data in a table format.

---

## 📊 Database Schema

```sql
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL
);
```

---

## 🤝 Contribution

Feel free to fork the repo, make changes, and submit pull requests.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
