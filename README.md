# Madlibs Generator

A fun web-based Madlibs generator built with Flask and Jinja2! This project lets users fill in story templates with their own words, creating hilarious and unique stories.

## Features

- Extracts placeholders from raw story files and stores them in a SQLite database.
- Fetches a random story template for each session.
- Lets users fill in their choices via a web form.
- Generates and displays the completed story using user input.

## Project Structure

```
madlibs generator/
├── app/
│   ├── app.py
│   ├── models.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── fill.html
│       └── result.html
├── Scripts/
│   ├── createDatabase.py
│   ├── extract_story_data.py
│   └── insert_data.py
├── stories/
│   └── story_*.txt
├── data/
│   └── madlibs.db
└── requirements.txt
```

## Getting Started

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Create the database:**
   ```
   python Scripts/createDatabase.py
   ```

3. **Insert stories into the database:**
   ```
   python Scripts/insert_data.py
   ```

4. **Run the web app:**
   ```
   python app/app.py
   ```

5. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

## How It Works

- Story templates are stored in the `stories/` folder with placeholders like `{noun}` or `{verb}`.
- Scripts extract placeholders and store story data in a SQLite database.
- The Flask app fetches a random story, displays a form for user input, and renders the completed story.

## Requirements

See `requirements.txt` for all dependencies.

