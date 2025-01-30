# Audio-to-Text API

## Tech Stack

- Node.js with Express for the backend
- PostgreSQL for data storage
- Prisma ORM for database management
- Speech synthesis engine for text-to-speech conversion
- Flask-CORS for handling cross-origin requests
- Render for deployment

## Features

- Convert text input into high-quality speech output
- Support for multiple languages and voice options
- RESTful API endpoints for easy integration
- Scalable and consistently available deployment

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/audio-to-text-api.git
   cd audio-to-text-api
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Configure environment variables:
   - Create a `.env` file in the root directory with:
     ```
     DATABASE_URL=your_postgresql_connection_string
     SECRET_KEY=your_secret_key
     ```
4. Run the application:
   ```sh
   npm start
   ```

## Deployment

- The API is deployed on Render for scalability and reliable hosting.
- Can be integrated with other applications via RESTful endpoints.

---
