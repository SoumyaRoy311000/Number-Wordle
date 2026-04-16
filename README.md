# Number Wordle Web App

A web-based version of the Number Wordle game, where players guess a 5-digit number with color-coded feedback on each digit's accuracy.

## Features

- **Interactive Gameplay**: Guess a 5-digit number with 6 attempts.
- **Color-Coded Feedback**:
  - 🟢 **Green**: Correct digit in the correct position
  - 🟡 **Yellow**: Correct digit but in the wrong position (difference ≤ 2)
  - 🟠 **Orange**: Digit is close (difference ≤ 4)
  - 🔴 **Red**: Digit is far (difference > 4)
- **Game Analysis**: After completing the game, analyze your performance with:
  - Optimal solution path
  - Move-by-move comparison with optimal guesses
  - Skill score (based on how close your guesses were to optimal)
  - Luck score (based on how much information each guess provided)
- **Session-Based**: Each user session maintains its own game state.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or Download the Project**:
   - Ensure all files are in the same directory:
     ```
     /your-project-directory/
     ├── app.py
     ├── requirements.txt
     ├── templates/
     │   ├── index.html
     │   └── analyze.html
     └── static/
         └── style.css
     ```

2. **Install Dependencies**:
   - Open a terminal in the project directory.
   - Run the following command to install Flask:
     ```
     pip install -r requirements.txt
     ```

## Running the Application

1. **Start the Flask Server**:
   - In the terminal, navigate to the project directory.
   - Run the application:
     ```
     python app.py
     ```
   - You should see output like:
     ```
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     ```

2. **Access the Web App**:
   - Open a web browser.
   - Go to `http://127.0.0.1:5000/` (or the URL shown in the terminal).
   - The game will start automatically.

3. **Play the Game**:
   - Enter a 5-digit number in the input field (e.g., `12345`).
   - Click "Guess" to submit.
   - View the color-coded feedback for each digit.
   - Continue guessing until you win or run out of attempts.

4. **Analyze Your Game**:
   - After winning or losing, click "Analyze Game" to see detailed analysis.
   - Review the optimal solution, compare your moves, and check your skill/luck scores.

5. **Start a New Game**:
   - Click "New Game" at any time to reset and start over.

## How to Play

- The computer generates a random 5-digit number (digits 0-9).
- You have 6 attempts to guess it.
- After each guess, each digit gets colored feedback based on how close it is to the correct digit in that position.
- Use the feedback to refine your next guess.
- Win by guessing the exact number within 6 attempts.

## Technical Details

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS (with Jinja2 templating)
- **Session Management**: Flask sessions for game state
- **Algorithm**: 
  - Feedback based on absolute difference between guessed and correct digits
  - Optimal solution uses binary search-like approach on each digit
  - Skill score penalizes suboptimal moves
  - Luck score rewards guesses that significantly reduce the search space

## Troubleshooting

- **Port Already in Use**: If you see an error about port 5000 being in use, you can specify a different port:
  ```
  python app.py
  ```
  Then modify the `app.run()` line in `app.py` to use a different port, e.g., `app.run(debug=True, port=5001)`

- **Import Errors**: Ensure Flask is installed correctly. Try reinstalling:
  ```
  pip uninstall flask
  pip install flask
  ```

- **Browser Issues**: Clear your browser cache if styles don't load properly.

- **Session Issues**: If the game state seems inconsistent, try clearing your browser cookies for localhost.

## Development

To modify the application:

- Edit `app.py` for backend logic.
- Modify templates in `templates/` for frontend changes.
- Update `static/style.css` for styling.

## License

This project is open-source. Feel free to modify and distribute.
