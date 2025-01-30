---

# URL Shortener  

## Tech Stack  
- Python (Flask) for the backend  
- React with Vite for the frontend  
- PostgreSQL for data storage  
- Prisma ORM for database management  
- Tailwind CSS for styling  
- Flask-CORS for handling cross-origin requests  
- Render for deployment  

## Features  
- Generate short URLs from long links  
- Customize shortened URLs  
- Track and manage shortened URLs  
- Scalable and consistently available deployment  

## Setup  
1. Clone the repository:  
   ```sh
   git clone https://github.com/CalebAkomaye/url-shortener.git
   cd url-shortener
   ```  
2. Set up the backend:  
   ```
   cd backend
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```  
3. Configure environment variables:  
   - Create a `.env` file in the backend directory with:  
     ```
     DATABASE_URL=your_awesome_connection_string
     SECRET_KEY=your_secret_key
     ```  
4. Run the backend:  
   ```sh
   flask run
   ```  
5. Set up the frontend:  
   ```sh
   cd ../frontend
   npm install
   ```  
6. Configure environment variables:  
   - Create a `.env` file in the frontend directory with:  
     ```
     VITE_API_URL=http://localhost:5000
     ```  
7. Run the frontend:  
   ```
   npm run dev
   ```  

## Deployment  
- The backend is deployed on Render for scalability.  
- The frontend can be deployed on platforms like Vercel or Netlify.  

---
