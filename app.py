from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Question, UserScore
import os
import random
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///brainblitz.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Sample data population
def populate_sample_data():
    if Question.query.count() > 0:
        return

    questions = [
        # Science (15 questions)
        {"text": "What is the chemical symbol for Gold?", "options": "Au,Ag,Fe,Cu", "correct_answer": "Au", "category": "Science", "difficulty": 1},
        {"text": "Which planet is known as the Red Planet?", "options": "Jupiter,Mars,Venus,Saturn", "correct_answer": "Mars", "category": "Science", "difficulty": 1},
        {"text": "What is the boiling point of water in Celsius?", "options": "0,50,100,150", "correct_answer": "100", "category": "Science", "difficulty": 1},
        {"text": "What gas do plants absorb during photosynthesis?", "options": "Oxygen,Carbon Dioxide,Nitrogen,Hydrogen", "correct_answer": "Carbon Dioxide", "category": "Science", "difficulty": 2},
        {"text": "What is the powerhouse of the cell?", "options": "Nucleus,Mitochondrion,Ribosome,Endoplasmic Reticulum", "correct_answer": "Mitochondrion", "category": "Science", "difficulty": 2},
        {"text": "What element is the most abundant in Earth's atmosphere?", "options": "Oxygen,Nitrogen,Carbon Dioxide,Argon", "correct_answer": "Nitrogen", "category": "Science", "difficulty": 2},
        {"text": "What is the primary source of energy for Earth's climate system?", "options": "Moon,Sun,Volcanoes,Oceans", "correct_answer": "Sun", "category": "Science", "difficulty": 3},
        {"text": "What is the speed of light in a vacuum (km/s)?", "options": "300,000,150,000,500,000,1,000,000", "correct_answer": "300,000", "category": "Science", "difficulty": 3},
        {"text": "Which scientist proposed the theory of relativity?", "options": "Isaac Newton,Albert Einstein,Niels Bohr,Galileo Galilei", "correct_answer": "Albert Einstein", "category": "Science", "difficulty": 3},
        {"text": "What gas, discovered on the sun before Earth, is the second most abundant element in the universe?", "options": "Hydrogen,Helium,Oxygen,Carbon", "correct_answer": "Helium", "category": "Science", "difficulty": 3},
        {"text": "Which planet is closest to the Sun?", "options": "Venus,Earth,Mercury,Mars", "correct_answer": "Mercury", "category": "Science", "difficulty": 1},
        {"text": "What is the hardest natural substance known?", "options": "Gold,Iron,Diamond,Quartz", "correct_answer": "Diamond", "category": "Science", "difficulty": 2},
        {"text": "What is the chemical symbol for water?", "options": "H2O,CO2,O2,N2", "correct_answer": "H2O", "category": "Science", "difficulty": 1},
        {"text": "What is the unit of electrical resistance?", "options": "Volt,Ampere,Ohm,Watt", "correct_answer": "Ohm", "category": "Science", "difficulty": 2},
        {"text": "What is the freezing point of water in Celsius?", "options": "0,32,100,-10", "correct_answer": "0", "category": "Science", "difficulty": 1},
        # History (15 questions)
        {"text": "Who was the first President of the United States?", "options": "Thomas Jefferson,George Washington,Abraham Lincoln,John Adams", "correct_answer": "George Washington", "category": "History", "difficulty": 1},
        {"text": "In which year did World War II end?", "options": "1943,1945,1947,1939", "correct_answer": "1945", "category": "History", "difficulty": 1},
        {"text": "What year did the Titanic sink?", "options": "1905,1912,1920,1930", "correct_answer": "1912", "category": "History", "difficulty": 1},
        {"text": "Who built the Taj Mahal?", "options": "Akbar,Shah Jahan,Jahangir,Aurangzeb", "correct_answer": "Shah Jahan", "category": "History", "difficulty": 2},
        {"text": "What ancient wonder was located in Alexandria?", "options": "Hanging Gardens,Great Pyramid,Lighthouse,Colossus", "correct_answer": "Lighthouse", "category": "History", "difficulty": 2},
        {"text": "In which year did the French Revolution begin?", "options": "1776,1789,1804,1815", "correct_answer": "1789", "category": "History", "difficulty": 2},
        {"text": "Who was the first woman to win a Nobel Prize?", "options": "Marie Curie,Jane Addams,Mother Teresa,Gertrude B. Elion", "correct_answer": "Marie Curie", "category": "History", "difficulty": 3},
        {"text": "What was the name of the ship that carried the Pilgrims to America in 1620?", "options": "Santa Maria,Mayflower,Nina,Pinta", "correct_answer": "Mayflower", "category": "History", "difficulty": 3},
        {"text": "Who was the leader of the Soviet Union during World War II?", "options": "Vladimir Lenin,Joseph Stalin,Leon Trotsky,Nikita Khrushchev", "correct_answer": "Joseph Stalin", "category": "History", "difficulty": 3},
        {"text": "Which ancient civilization built the Machu Picchu?", "options": "Maya,Aztec,Inca,Egyptian", "correct_answer": "Inca", "category": "History", "difficulty": 3},
        {"text": "In which year did India gain independence?", "options": "1945,1947,1950,1960", "correct_answer": "1947", "category": "History", "difficulty": 1},
        {"text": "Who was the first female Prime Minister of the UK?", "options": "Margaret Thatcher,Theresa May,Indira Gandhi,Golda Meir", "correct_answer": "Margaret Thatcher", "category": "History", "difficulty": 2},
        {"text": "What was the name of the first manned mission to land on the moon?", "options": "Apollo 11,Apollo 13,Gemini 4,Vostok 1", "correct_answer": "Apollo 11", "category": "History", "difficulty": 1},
        {"text": "Which empire was ruled by Julius Caesar?", "options": "Greek,Ottoman,Roman,Byzantine", "correct_answer": "Roman", "category": "History", "difficulty": 1},
        {"text": "What event marked the beginning of World War I?", "options": "Invasion of Poland,Assassination of Archduke Franz Ferdinand,Battle of Waterloo,Treaty of Versailles", "correct_answer": "Assassination of Archduke Franz Ferdinand", "category": "History", "difficulty": 2},
        # Pop Culture (15 questions)
        {"text": "Who played Jack Sparrow in Pirates of the Caribbean?", "options": "Brad Pitt,Johnny Depp,Leonardo DiCaprio,Tom Hanks", "correct_answer": "Johnny Depp", "category": "Pop Culture", "difficulty": 1},
        {"text": "What is the name of Harry Potter's owl?", "options": "Hedwig,Crookshanks,Scabbers,Fawkes", "correct_answer": "Hedwig", "category": "Pop Culture", "difficulty": 1},
        {"text": "Which band performed 'Bohemian Rhapsody'?", "options": "The Beatles,Queen,The Rolling Stones,ABBA", "correct_answer": "Queen", "category": "Pop Culture", "difficulty": 2},
        {"text": "Who directed the movie 'Inception'?", "options": "Steven Spielberg,Christopher Nolan,James Cameron,Quentin Tarantino", "correct_answer": "Christopher Nolan", "category": "Pop Culture", "difficulty": 2},
        {"text": "What is the name of the fictional city in Batman?", "options": "Metropolis,Gotham City,Star City,Central City", "correct_answer": "Gotham City", "category": "Pop Culture", "difficulty": 3},
        {"text": "Who is the creator of the Marvel Universe?", "options": "Stan Lee,Jack Kirby,Steve Ditko,All of the above", "correct_answer": "Stan Lee", "category": "Pop Culture", "difficulty": 1},
        {"text": "What TV show features the characters Ross, Rachel, and Monica?", "options": "The Office,Friends,How I Met Your Mother,Seinfeld", "correct_answer": "Friends", "category": "Pop Culture", "difficulty": 1},
        {"text": "Who won the Oscar for Best Actor in 2020?", "options": "Brad Pitt,Joaquin Phoenix,Leonardo DiCaprio,Adam Driver", "correct_answer": "Joaquin Phoenix", "category": "Pop Culture", "difficulty": 2},
        {"text": "What is the name of the dragon in 'The Hobbit'?", "options": "Drogon,Smaug,Toothless,Vermithrax", "correct_answer": "Smaug", "category": "Pop Culture", "difficulty": 3},
        {"text": "Which artist is known for the song 'Shape of You'?", "options": "Ed Sheeran,Justin Bieber,Drake,Shawn Mendes", "correct_answer": "Ed Sheeran", "category": "Pop Culture", "difficulty": 1},
        {"text": "What movie features a character named Simba?", "options": "The Jungle Book,The Lion King,Aladdin,Tarzan", "correct_answer": "The Lion King", "category": "Pop Culture", "difficulty": 1},
        {"text": "Who played the role of Tony Stark in the Marvel Cinematic Universe?", "options": "Chris Evans,Robert Downey Jr.,Chris Hemsworth,Mark Ruffalo", "correct_answer": "Robert Downey Jr.", "category": "Pop Culture", "difficulty": 1},
        {"text": "What is the name of the fictional school in Harry Potter?", "options": "Hogwarts,Durmstrang,Beauxbatons,Ilvermorny", "correct_answer": "Hogwarts", "category": "Pop Culture", "difficulty": 1},
        {"text": "Which 90s band is known for 'Smells Like Teen Spirit'?", "options": "Nirvana,Pearl Jam,Red Hot Chili Peppers,Green Day", "correct_answer": "Nirvana", "category": "Pop Culture", "difficulty": 2},
        {"text": "Who directed 'The Dark Knight' trilogy?", "options": "Zack Snyder,Christopher Nolan,Tim Burton,David Fincher", "correct_answer": "Christopher Nolan", "category": "Pop Culture", "difficulty": 2},
    ]

    for q in questions:
        new_question = Question(
            text=q["text"],
            options=q["options"],
            correct_answer=q["correct_answer"],
            category=q["category"],
            difficulty=q["difficulty"]
        )
        db.session.add(new_question)
    db.session.commit()

# Create database tables and populate sample data
with app.app_context():
    db.create_all()
    populate_sample_data()

# Helper function to fetch questions for a category and difficulty
def fetch_questions(category, difficulty, total_questions, exclude_ids=None):
    if exclude_ids is None:
        exclude_ids = []
    questions = Question.query.filter(
        Question.category == category,
        Question.difficulty == difficulty,
        ~Question.id.in_(exclude_ids)
    ).all()
    if not questions:  # If no questions at this difficulty, try a lower one
        for d in range(difficulty - 1, 0, -1):
            questions = Question.query.filter(
                Question.category == category,
                Question.difficulty == d,
                ~Question.id.in_(exclude_ids)
            ).all()
            if questions:
                break
    if not questions:  # If still no questions, get any questions from the category
        questions = Question.query.filter(
            Question.category == category,
            ~Question.id.in_(exclude_ids)
        ).all()
    if not questions:  # If no questions at all, return empty list
        return []
    question_ids = [q.id for q in questions]
    return random.sample(question_ids, min(len(question_ids), total_questions)) if question_ids else []

@app.route('/')
def index():
    categories = ["Science", "History", "Pop Culture"]
    user = None
    if 'user_id' in session:
        user = db.session.get(User, session['user_id'])
    return render_template('index.html', categories=categories, user=user)

@app.route('/avatars')
def avatars():
    if 'user_id' not in session:
        flash('Please log in to select an avatar.', 'error')
        return redirect(url_for('login'))

    avatars = [
        "static/images/avatar1.png",
        "static/images/avatar2.png",
        "static/images/avatar3.png",
    ]
    user = db.session.get(User, session['user_id'])
    return render_template('avatars.html', avatars=avatars, user=user)

@app.route('/quiz/<category>', methods=['GET', 'POST'])
def quiz(category):
    if 'user_id' not in session:
        flash('Please log in to start the quiz.', 'error')
        return redirect(url_for('login'))

    user = db.session.get(User, session['user_id'])
    
    # Always initialize a new quiz state to avoid category conflicts
    total_questions = int(request.args.get('num_questions', 5))
    if total_questions < 5 or total_questions > 10:
        total_questions = 5

    if 'used_questions' not in session:
        session['used_questions'] = {cat: [] for cat in ["Science", "History", "Pop Culture"]}

    session['used_questions'][category] = []

    all_questions = Question.query.filter_by(category=category).all()
    if not all_questions:
        flash(f'No questions available for {category}. Please choose another category.', 'error')
        return redirect(url_for('index'))
    
    total_questions = min(len(all_questions), total_questions)
    session['quiz_state'] = {
        'category': category,
        'questions': [],
        'current_question': 0,
        'score': 0,
        'streak': 0,
        'difficulty': 1,
        'total_questions': total_questions,
        'questions_fetched': 0
    }

    quiz_state = session['quiz_state']

    # Populate questions if the list is empty
    while len(quiz_state['questions']) < quiz_state['total_questions']:
        remaining = quiz_state['total_questions'] - len(quiz_state['questions'])
        new_questions = fetch_questions(
            category,
            quiz_state['difficulty'],
            remaining,
            exclude_ids=session['used_questions'][category]
        )
        if not new_questions:
            quiz_state['total_questions'] = len(quiz_state['questions'])
            break
        quiz_state['questions'].extend(new_questions)
        session['used_questions'][category].extend(new_questions)
        session['used_questions'][category] = session['used_questions'][category][-30:]
        session['quiz_state'] = quiz_state
        session.modified = True

    if not quiz_state['questions']:
        flash(f'No new questions available for {category}. Please choose another category or reset your progress.', 'error')
        return redirect(url_for('index'))

    # Check if quiz is complete
    if quiz_state['current_question'] >= quiz_state['total_questions']:
        score = quiz_state['score']
        total = quiz_state['total_questions']
        user.brain_coins += score * 10 + quiz_state['streak'] * 5
        user_score = UserScore(user_id=user.id, category=category, score=score, total_questions=total)
        db.session.add(user_score)
        db.session.commit()
        results = {
            'score': score,
            'total': total,
            'category': category,
            'brain_coins_earned': score * 10 + quiz_state['streak'] * 5
        }
        session.pop('quiz_state', None)
        return redirect(url_for('results', results=json.dumps(results)))

    # Fetch the current question
    question = db.session.get(Question, quiz_state['questions'][quiz_state['current_question']])
    options = question.options.split(',')
    return render_template('quiz.html', question=question, options=options, quiz_state=quiz_state, user=user)

@app.route('/answer', methods=['POST'])
def answer():
    if 'quiz_state' not in session:
        return redirect(url_for('index'))

    quiz_state = session['quiz_state']
    question = db.session.get(Question, quiz_state['questions'][quiz_state['current_question']])
    user_answer = request.form['answer']

    if user_answer == question.correct_answer:
        quiz_state['score'] += 1
        quiz_state['streak'] += 1
        if quiz_state['streak'] >= 3 and quiz_state['difficulty'] < 3:
            quiz_state['difficulty'] += 1
    else:
        quiz_state['streak'] = 0
        if quiz_state['difficulty'] > 1:
            quiz_state['difficulty'] -= 1

    quiz_state['current_question'] += 1
    session['quiz_state'] = quiz_state
    return redirect(url_for('quiz', category=quiz_state['category']))

@app.route('/results/<results>')
def results(results):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    results = json.loads(results)
    user = db.session.get(User, session['user_id'])
    category_scores = UserScore.query.filter_by(user_id=user.id, category=results['category']).all()
    avg_score = sum(s.score for s in category_scores) / sum(s.total_questions for s in category_scores) if category_scores else 0
    insights = f"Your average score in {results['category']} is {(avg_score * 100):.1f}%. "
    if avg_score < 0.5:
        insights += "Consider reviewing basic concepts in this category to improve your performance."
    elif avg_score < 0.8:
        insights += "Good job! Try tackling more challenging questions to boost your score further."
    else:
        insights += "Excellent performance! You're a master in this category."

    return render_template('results.html', results=results, insights=insights, user=user)

@app.route('/update-avatar', methods=['POST'])
def update_avatar():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = db.session.get(User, session['user_id'])
    avatar = request.form['avatar']
    cost = 50  # Cost to change avatar
    if user.brain_coins >= cost:
        user.brain_coins -= cost
        user.avatar = avatar
        db.session.commit()
        flash('Avatar updated successfully!', 'success')
    else:
        flash('Not enough Brain Coins to change avatar. You need 50 coins.', 'error')
    return redirect(url_for('avatars'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials.', 'error')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'error')
        elif User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('quiz_state', None)
    session.pop('used_questions', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)