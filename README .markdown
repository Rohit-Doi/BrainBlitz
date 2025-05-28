# BrainBlitz Quiz Game

## Overview
BrainBlitz is an interactive quiz game built with Flask, designed to challenge users with questions across multiple categories: Science, History, and Pop Culture. Users can log in, select avatars (with a Brain Coins cost), take quizzes, and track their scores. The game features adaptive difficulty, voice-enabled questions, and a 3D background for an engaging experience.

## Tech Stack
- **Backend:** Flask (Python)
- **Database:** SQLite (via Flask-SQLAlchemy)
- **Frontend:** HTML, CSS, JavaScript (with Jinja2 templating)
- **Authentication:** Werkzeug for password hashing
- **Voice Feature:** Browser SpeechSynthesis API

## Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/brainblitz.git
   cd brainblitz
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` file includes:
   ```
   flask==2.0.1
   flask-sqlalchemy==2.5.1
   werkzeug==2.0.1
   ```

4. **Add Avatar Images:**
   The app expects three avatar images in `static/images/`:
   - `avatar1.png`
   - `avatar2.png`
   - `avatar3.png`

   Download or create these images and place them in `static/images/`. You can find free avatars on sites like Flaticon or Unsplash.

5. **Set Up the Database:**
   The app uses SQLite, so no external database setup is required. Run the application to automatically create the database (`brainblitz.db`):
   ```bash
   python app.py
   ```

6. **Run the Application:**
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://127.0.0.1:5000`.