# Number Wordle Web App

A web-based Number Wordle game inspired by Wordle, where players guess a 5-digit number with color-coded feedback on each digit's accuracy. Features an interactive Wordle-style tile interface, on-screen keyboard, and detailed game analysis.

## Features

- **Wordle-Style Interface**: 
  - 6×5 grid of interactive tiles showing your guesses
  - Real-time tile coloring with animation
  - Responsive design for desktop and mobile
  
- **Input Methods**:
  - Virtual on-screen keyboard (digits 0-9)
  - Physical keyboard support (0-9, Enter to submit, Backspace to delete)
  - Backspace button for easy correction
  - Submit button to finalize each guess

- **Color-Coded Feedback**:
  - 🟢 **Green**: Correct digit in the correct position
  - 🟡 **Yellow**: Correct digit but too high/low (within ±2)
  - 🟠 **Orange**: Digit is close (within ±4)
  - 🔴 **Red**: Digit is far (difference > 4)

- **Game Analysis**: After winning, analyze your performance with:
  - Skill score (0-100): Based on how close your guesses were to optimal
  - Luck score (0-100): Based on how much each guess reduced the solution space
  - Side-by-side comparison of your guesses vs optimal guesses
  - Visual tile feedback for optimal path
  - Performance badges (Good move vs Suboptimal)

- **Session-Based**: Each user session maintains its own game state
- **Dark Mode**: Toggle between light and dark themes (persisted in browser)
- **Auto-Reset**: Game automatically resets when loading after completion

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or Download the Project**:
   - Ensure all files are in the same directory:
     ```
     /your-project-directory/
     ├── app.py
     ├── number_wordle_ai.py
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
   - The game will start automatically with a fresh 5-digit number.

3. **Play the Game**:
   - Click numbers on the on-screen keyboard or use your physical keyboard (0-9)
   - Each digit you enter will appear in the current row
   - Use Backspace button or physical Backspace key to delete the last digit
   - Click Submit button or press Enter to submit your guess
   - Tiles will turn green, yellow, orange, or red based on feedback
   - Continue until you win or eliminate all 6 attempts
   - After each turn, the attempts counter updates

4. **Analyze Your Game**:
   - After winning, click "Analyze Game" to see detailed performance analysis
   - View your guesses vs optimal guesses side-by-side with feedback colors
   - Check your Skill and Luck scores
   - See the final answer in green
   - Use "New Game" to play again or go back "Home"

5. **Start a New Game**:
   - Click "New Game" link at any time to reset and start over

## How to Play

- The computer generates a random 5-digit number (each digit is 0-9)
- You have 6 attempts to guess it
- Use the on-screen keyboard or your physical keyboard to enter digits
- After each guess, the tiles show color feedback:
  - **Green**: Perfect match in that position
  - **Yellow**: Right digit but too close/far (within 2)
  - **Orange**: Close digit (within 4)
  - **Red**: Very far digit (more than 4 away)
- Use the feedback colors to strategize your next guess
- Win by guessing the exact number within 6 attempts

## Technical Details

- **Backend**: Flask (Python web framework) with JSON API
- **Frontend**: HTML5, CSS3 with Jinja2 templating, vanilla JavaScript
- **Session Management**: Flask server-side sessions for game state persistence
- **API Endpoint**: `/api/guess` (POST) for real-time guess submission and feedback
- **Animation**: CSS transitions for tile color changes
- **Algorithm**: 
  - Feedback based on absolute difference between guessed and correct digits
  - Optimal solution uses binary search-like approach on each digit position
  - Skill score penalizes suboptimal/risky moves
  - Luck score rewards guesses that maximize information gain

## File Structure

- `app.py`: Main Flask application with game logic and routes
- `number_wordle_ai.py`: Optional AI analysis module (used by backend)
- `templates/index.html`: Main game interface with tile grid and keyboard
- `templates/analyze.html`: Post-game analysis page with performance metrics
- `static/style.css`: Styling for both pages (light and dark modes)
- `requirements.txt`: Python dependencies

## Troubleshooting

- **Port Already in Use**: If you see an error about port 5000 being in use:
  ```
  python app.py
  ```
  Then modify the `app.run()` line in `app.py` to use a different port:
  ```python
  app.run(debug=True, port=5001)
  ```

- **Import Errors**: Ensure Flask is installed correctly:
  ```
  pip uninstall flask
  pip install flask
  ```

- **Tiles Not Showing Colors**: Clear your browser cache (Ctrl+Shift+Delete) and refresh
- **Session Issues**: Clear browser cookies for localhost if game state seems inconsistent
- **Keyboard Not Working**: Ensure the game window is focused (click inside the game area)
- **Dark Mode Not Persisting**: Check browser localStorage is enabled

## Keyboard Shortcuts

- **0-9**: Enter digits
- **Enter**: Submit guess
- **Backspace**: Delete last digit
- **Theme Toggle**: Click button in header to switch dark/light mode

## Development

To modify the application:

- Edit `app.py` for backend game logic, routing, or API changes
- Modify `templates/index.html` for main game interface
- Modify `templates/analyze.html` for post-game analysis page
- Update `static/style.css` for styling (includes responsive design)
- Both light and dark mode variables defined in CSS custom properties

## Browser Compatibility

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

This project is open-source. Feel free to modify and distribute.
