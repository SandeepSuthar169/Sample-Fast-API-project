## Sample FastAPI Project

A simple FastAPI application demonstrating basic API endpoints, data loading from a JSON file, and sorting functionality.

- Data Loading: Reads data from a JSON file (data.json).
- API Endpoints:
    - Root endpoint returning a greeting message.
    - View all data entries.
    - Sort data based on specified fields and order.



###  Project Structure
```bash
├── __pycache__
├── .gitignore          # Ignore .venv file 
├── data.json           # JSON file containing sample data
├── main.py             # Main application file with API endpoints
├── requirements.txt    # Python dependencies


```

###  Technologies Used
- Programming Language:`Python`
- Data Version Control: `DVC`
- Workflow Automation: `GitHub Actions`
- Machine Learning Libraries: `scikit-learn, pandas, NumPy`
- Visualization: `Matplotlib, Seaborn`
- Notebook Environment: `Jupyter Notebook`### Installation
1. Clone the Repository:
```
git clone https://github.com/SandeepSuthar169/Sample-Fast-API-project.git
cd Sample-Fast-API-project
```
2.  Create a Virtual Environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies:

```
pip install -r requirements.txt
```
4. Run the Application:
```
uvicorn main:app --reload
```
- The application will be accessible at http://127.0.0.1:8000.
### View Data
- URL: /view
- Method: GET
- Description: Retrieves all data entries from data.json.
```
[
  {
    "fixed_acidity": 9.3,
    "residual_sugar": 6.4,
    "alcohol": 13.6,
    "density": 1.0005,
    "quality_label": "high"
  },
  {
    "fixed_acidity": 11.2,
    "residual_sugar": 2.0,
    "alcohol": 14.0,
    "density": 0.9912,
    "quality_label": "medium"
  },
  {
    "fixed_acidity": 11.6,
    "residual_sugar": 0.9,
    "alcohol": 8.2,
    "density": 0.9935,
    "quality_label": "low"
  }
]
```

### Sort Data
- URL: `/sort`
- Method : `GET`
- `Description` : Sorts data based on specified field and order.

### Query Parameters:

- `sort_by` (string, required): Field to sort by. Valid options: `density`, `residual_sugar`.
- `order` (string, optional): Sort order. Valid options: `asc (default)`, `desc`.


Example:
`GET /sort?sort_by=density&order=asc`

```
[
  {
    "fixed_acidity": 11.2,
    "residual_sugar": 2.0,
    "alcohol": 14.0,
    "density": 0.9912,
    "quality_label": "medium"
  },
  {
    "fixed_acidity": 11.6,
    "residual_sugar": 0.9,
    "alcohol": 8.2,
    "density": 0.9935,
    "quality_label": "low"
  },
  {
    "fixed_acidity": 9.3,
    "residual_sugar": 6.4,
    "alcohol": 13.6,
    "density": 1.0005,
    "quality_label": "high"
  }
]
```

### Testing the API
Once the application is running, you can test the endpoints using:

- Swagger UI: Navigate to http://127.0.0.1:8000/docs for interactive API documentation.
- ReDoc: Navigate to http://127.0.0.1:8000/redoc for alternative API documentation.