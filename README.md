---

# Flask + ReactJS Application

This README contains instructions on how to set up and run a Flask backend and ReactJS frontend locally.

## Prerequisites

Make sure you have the following installed:

- **Python 3.x** (for Flask)
- **Node.js** and **npm** (for ReactJS)

## Setup Instructions

### Backend (Flask)

1. **Clone the repository**

   Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create and activate a virtual environment**

   It’s recommended to use a virtual environment to avoid installing dependencies globally.

   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Python dependencies**

   Install the necessary Python packages from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server**

   Start the Flask backend:

   ```bash
   flask run
   ```

   The Flask application will run by default on [http://localhost:5000](http://localhost:5000).

---

### Frontend (ReactJS)

1. **Navigate to the React folder**

   Assuming your React app is located in a folder named `frontend`:

   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies**

   Install all necessary Node.js packages for the frontend:

   ```bash
   npm install
   ```

3. **Run the React development server**

   Start the React app:

   ```bash
   npm start
   ```

   The React app will run by default on [http://localhost:3000](http://localhost:3000).

---

### Connecting Flask and React

If your React app needs to communicate with the Flask backend (via API calls):

- Use `http://localhost:5000` as the base URL in your React app for API calls to the Flask backend.
- Ensure CORS is set up in Flask by adding the following to your Flask app:
  ```python
  from flask_cors import CORS
  CORS(app)
  ```

---

### Additional Notes

- **Environment Variables**: If your app requires specific environment variables, create a `.env` file in the root folder for Flask and add the variables.
  
  Example `.env` file:
  ```bash
  FLASK_APP=app.py
  FLASK_ENV=development
  ```

- **Building for Production**: To build the React frontend for production, run:
  ```bash
  npm run build
  ```
  Then, serve the static files using Flask or a production-ready web server like Nginx.

---

### Troubleshooting

- Ensure both servers are running correctly by checking `http://localhost:3000` (React) and `http://localhost:5000` (Flask).
- If you encounter CORS issues, ensure CORS is properly configured in your Flask app.

---

That's it! You should now have both your Flask backend and React frontend running locally.

