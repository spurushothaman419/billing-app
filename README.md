# billing-app
Project overview and setup instructions
Step 2: Create Your GitHub Repository (if not done yet)
Go to your GitHub account (https://github.com/spurushothaman419)

Create a new repository named, e.g., embroidery-billing-app

Clone it locally:
git clone https://github.com/spurushothaman419/embroidery-billing-app.git
cd embroidery-billing-app

Step 3: Set Up Backend
Inside your repo folder, create a backend directory:
mkdir backend
cd backend
Create and activate a Python virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
Create a requirements.txt file and add:
fastapi
uvicorn[standard]
sqlalchemy
fastapi-users[sqlalchemy]
databases[sqlite]
pydantic

Install dependencies:pip install -r requirements.txt

Run your backend API server locally: uvicorn main:app --reload
Verify the API is running at:http://127.0.0.1:8000

Step 4: Set Up Frontend
Go back to your repo root and create a frontend directory:

cd ..
npx create-react-app frontend
cd frontend

Install Axios for API calls: npm install axios react-router-dom

Replace the default src/App.js with a starter React app that includes:
Login page calling your backend /auth/jwt/login

Customer list page fetching /customers/

JWT token storage in memory or cookie (for demo) I can provide this React starter code next.

Start React app locally: npm start
Access frontend at http://localhost:3000


What to do next?
Create folders and files exactly as above.

Run backend with:
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload

Run frontend with:
cd frontend
npm install
npm start

Visit http://localhost:3000 to see the customer list page (initially empty).
Use tools like Postman to create users and customers via API to test.

How to run:
Make sure all these files are in your /backend/app/ folder.

Install dependencies (see your requirements.txt): pip install fastapi uvicorn fastapi-users[sqlalchemy] sqlalchemy pydantic passlib[bcrypt] email-validator
Run the app: uvicorn app.main:app --reload
Test endpoints: 

POST /auth/register to create users

POST /auth/jwt/login to get JWT token

POST /customers/ with JWT auth to create customers

GET /customers/ with JWT auth to list customers
