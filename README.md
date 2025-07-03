## 🌍 PlaceAPI - Django REST API for Location Hierarchy

A Simple nested API built with Django REST Framework to manage hierarchical Bangladeshi location data: Country → District → Subdistrict → Union → Semi-Metro areas.

---

### 🚀 Features

- 🔐 JWT Authentication
- 👤 User Registration
- 📍 Nested Place API:
  - District → Subdistrict → Union → SemiMetro
- 🧰 Full CRUD for all models
- 🗄️ PostgreSQL database support
- 🔐 `.env`-based environment configuration

---

### ⚙️ Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL
- JWT Authentication (`djangorestframework-simplejwt`)
- `python-decouple` for `.env`

---

### 📦 Installation

1. Clone the repo
```bash
git clone https://github.com/tushar-3549/PlacesAPI-Django
cd PlacesAPI-Django
```
2. Create virtual environment

```
python -m venv venv
source venv/bin/activate
```
3. Install requirements

`pip install -r requirements.txt`

4. Setup .env

Create a .env file in your project root:
```
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=placeapi_db
DB_USER=placeapi_user
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
```

5. Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
6. Create superuser
```
python manage.py createsuperuser
```
7. Run the server
```
python manage.py runserver
```

### 🔐 Auth Endpoints

| Action        | Endpoint                      |
| ------------- | ----------------------------- |
| Register      | `POST /api/v1/register_user/` |
| Login (JWT)   | `POST /token/`                |
| Refresh Token | `POST /token_refresh/`        |

### 🌍 Place API Endpoints

| Model           | CRUD Endpoint Prefix    |
| --------------- | ----------------------- |
| District        | `/api/v1/districts/`    |
| Subdistrict     | `/api/v1/subdistricts/` |
| Union           | `/api/v1/unions/`       |
| SemiMetroArea   | `/api/v1/semimetros/`   |
| Nested ReadOnly | `/api/v1/places/`       |

## API Structure

```
{
  "District Name": {
    "District_regex": "",
    "Sub_District": {
      "SubDistrict Name": {
        "Subdistrict_regex": "",
        "Union": {
          "Union Name": {
            "Union_regex": "",
            "thana_no": 1,
            "LatLong": [lat, long],
            "_isSuggested": true,
            "postcode": "9300",
            "Semi_Metro": {
              "Area Name": {
                "Area_regex": "",
                "LatLong": [lat, long]
              }
            }
          }
        },
        "LatLong": [lat, long]
      }
    }
  }
}
```
