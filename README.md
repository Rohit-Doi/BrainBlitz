<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BrainBlitz README</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
        h1, h2, h3 { color: #333; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 5px; }
        code { font-family: monospace; }
    </style>
</head>
<body>
    <h1>BrainBlitz Quiz Game</h1>

    <h2>Overview</h2>
    <p>BrainBlitz is an interactive quiz game built with Flask, designed to challenge users with questions across multiple categories: Science, History, and Pop Culture. Users can log in, select avatars (with a Brain Coins cost), take quizzes, and track their scores. The game features adaptive difficulty, voice-enabled questions, and a 3D background for an engaging experience.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>User Authentication:</strong> Sign up and log in to access the quiz.</li>
        <li><strong>Multiple Categories:</strong> Choose from Science, History, or Pop Culture quizzes.</li>
        <li><strong>Customizable Quiz Length:</strong> Select 5 to 10 questions per quiz.</li>
        <li><strong>Adaptive Difficulty:</strong> Question difficulty increases with a streak of correct answers.</li>
        <li><strong>Voice-Enabled Questions:</strong> Toggle voice narration for questions using browser speech synthesis.</li>
        <li><strong>Avatar Selection:</strong> Choose from three avatars, with a 50 Brain Coins cost to change.</li>
        <li><strong>Brain Coins System:</strong> Earn coins by completing quizzes (10 coins per correct answer, 5 bonus coins per streak).</li>
        <li><strong>Score Tracking:</strong> View your scores and insights after each quiz.</li>
        <li><strong>Responsive Design:</strong> Styled with CSS and a 3D background for visual appeal.</li>
    </ul>

    <h2>Tech Stack</h2>
    <ul>
        <li><strong>Backend:</strong> Flask (Python)</li>
        <li><strong>Database:</strong> SQLite (via Flask-SQLAlchemy)</li>
        <li><strong>Frontend:</strong> HTML, CSS, JavaScript (with Jinja2 templating)</li>
        <li><strong>Authentication:</strong> Werkzeug for password hashing</li>
        <li><strong>Voice Feature:</strong> Browser SpeechSynthesis API</li>
    </ul>

    <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.8 or higher</li>
        <li>Git (for cloning the repository)</li>
        <li>A virtual environment tool (e.g., <code>venv</code>)</li>
    </ul>

    <h2>Setup Instructions</h2>
    <ol>
        <li><strong>Clone the Repository:</strong>
            <pre><code>git clone https://github.com/yourusername/brainblitz.git
cd brainblitz</code></pre>
        </li>
        <li><strong>Create and Activate a Virtual Environment:</strong>
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate</code></pre>
        </li>
        <li><strong>Install Dependencies:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
            <p>The <code>requirements.txt</code> file includes:</p>
            <pre><code>flask==2.0.1
flask-sqlalchemy==2.5.1
werkzeug==2.0.1</code></pre>
        </li>
        <li><strong>Add Avatar Images:</strong>
            <p>The app expects three avatar images in <code>static/images/</code>:</p>
            <ul>
                <li><code>avatar1.png</code></li>
                <li><code>avatar2.png</code></li>
                <li><code>avatar3.png</code></li>
            </ul>
            <p>Download or create these images and place them in <code>static/images/</code>. You can find free avatars on sites like Flaticon or Unsplash.</p>
        </li>
        <li><strong>Set Up the Database:</strong>
            <p>The app uses SQLite, so no external database setup is required. Run the application to automatically create the database (<code>brainblitz.db</code>):</p>
            <pre><code>python app.py</code></pre>
        </li>
        <li><strong>Run the Application:</strong>
            <pre><code>python app.py</code></pre>
            <p>Open your browser and navigate to <code>http://127.0.0.1:5000</code>.</p>
        </li>
    </ol>

    <h2>Project Structure</h2>
    <pre><code>brainblitz/
├── app.py                # Main Flask application
├── models.py             # Database models (User, Question, UserScore)
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── quiz.html
│   ├── results.html
│   ├── avatars.html
│   ├── login.html
│   ├── signup.html
├── static/               # Static files (CSS, JS, images)
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── scripts.js
│   ├── images/
│   │   ├── avatar1.png
│   │   ├── avatar2.png
│   │   ├── avatar3.png
├── requirements.txt      # Python dependencies
└── brainblitz.db         # SQLite database (created on first run)
</code></pre>

    <h2>Usage</h2>
    <ol>
        <li><strong>Sign Up and Log In:</strong>
            <p>Navigate to <code>/signup</code> to create an account. Log in at <code>/login</code> with your credentials.</p>
        </li>
        <li><strong>Select a Quiz:</strong>
            <p>On the homepage, choose a category (Science, History, Pop Culture) and the number of questions (5-10). Click "Start Quiz" to begin.</p>
        </li>
        <li><strong>Answer Questions:</strong>
            <p>Select an answer for each question and submit. Use the "Toggle Voice" button to hear questions read aloud.</p>
        </li>
        <li><strong>Change Avatar:</strong>
            <p>Click "Change Avatar" on the homepage. Select a new avatar (costs 50 Brain Coins).</p>
        </li>
        <li><strong>View Results:</strong>
            <p>After completing a quiz, view your score, earned Brain Coins, and performance insights.</p>
        </li>
    </ol>

    <h2>Contributing</h2>
    <p>Contributions are welcome! To contribute:</p>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch (<code>git checkout -b feature/your-feature</code>).</li>
        <li>Make your changes and commit (<code>git commit -m "Add your feature"</code>).</li>
        <li>Push to your branch (<code>git push origin feature/your-feature</code>).</li>
        <li>Open a Pull Request.</li>
    </ol>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Contact</h2>
    <p>For any questions or issues, please open an issue on GitHub or contact [your email].</p>
</body>
</html>
