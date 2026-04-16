from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

def setup_game():
    session['answer'] = [random.randint(0, 9) for _ in range(5)]
    session['history'] = []
    session['tries'] = 6
    session['won'] = False
    session['current_row'] = 0
    session.modified = True

def get_feedback(user_input, answer):
    feedback = []
    for j in range(5):
        diff = abs(user_input[j] - answer[j])
        if diff == 0:
            feedback.append("green")
        elif diff <= 2:
            feedback.append("yellow")
        elif diff <= 4:
            feedback.append("orange")
        else:
            feedback.append("red")
    return feedback

def get_optimal_solution(answer):
    sim_start = [0]*5
    sim_end = [9]*5
    solution_path = []

    for _ in range(6):
        guess = [(sim_start[i] + sim_end[i]) // 2 for i in range(5)]
        solution_path.append(guess)

        if guess == answer:
            break

        for i in range(5):
            if guess[i] == answer[i]:
                sim_start[i] = guess[i]
                sim_end[i] = guess[i]
            elif abs(guess[i] - answer[i]) <= 2:
                if guess[i] < answer[i]:
                    sim_start[i] = guess[i]
                else:
                    sim_end[i] = guess[i]
            elif abs(guess[i] - answer[i]) <= 4:
                if guess[i] < answer[i]:
                    sim_start[i] = guess[i] + 2
                else:
                    sim_end[i] = guess[i] - 2
            else:
                if guess[i] < answer[i]:
                    sim_start[i] = guess[i] + 5
                else:
                    sim_end[i] = guess[i] - 5

    return solution_path

def calculate_skill(history, optimal, answer):
    skill_score = 100
    for i, (guess, fb) in enumerate(history):
        if i < len(optimal):
            user_error = sum(abs(guess[j] - answer[j]) for j in range(5))
            optimal_error = sum(abs(optimal[i][j] - answer[j]) for j in range(5))
            if user_error > optimal_error:
                skill_score -= 15
    return min(skill_score, 100)

def range_size(start, end):
    return sum(end[i] - start[i] for i in range(5))

def calculate_luck(history, answer):
    sim_start = [0]*5
    sim_end = [9]*5
    luck = 0

    for guess, fb in history:
        before = range_size(sim_start, sim_end)

        for i in range(5):
            if fb[i] == "green":
                sim_start[i] = guess[i]
                sim_end[i] = guess[i]
            elif fb[i] == "yellow":
                sim_start[i] = max(sim_start[i], guess[i] - 2)
                sim_end[i] = min(sim_end[i], guess[i] + 2)
            elif fb[i] == "orange":
                sim_start[i] = max(sim_start[i], guess[i] - 4)
                sim_end[i] = min(sim_end[i], guess[i] + 4)
            elif fb[i] == "red":
                low = guess[i] - 4
                high = guess[i] + 4
                if sim_start[i] >= low and sim_start[i] <= high:
                    sim_start[i] = high + 1
                if sim_end[i] >= low and sim_end[i] <= high:
                    sim_end[i] = low - 1

        after = range_size(sim_start, sim_end)
        reduction = before - after
        if reduction > 10:
            luck += reduction

    return min(int(luck), 100)

@app.route('/api/guess', methods=['POST'])
def api_guess():
    try:
        # Ensure game is initialized
        if 'answer' not in session:
            setup_game()
        
        if session['tries'] <= 0 or session['won']:
            return jsonify({'success': False, 'message': 'Game over'}), 400

        user_input_str = request.json.get('guess', '')
        
        if not user_input_str or len(user_input_str) != 5 or not user_input_str.isdigit():
            return jsonify({'success': False, 'message': 'Invalid input'}), 400

        user_input = [int(d) for d in user_input_str]
        feedback = get_feedback(user_input, session['answer'])
        session['history'].append((user_input, feedback))
        session['tries'] -= 1

        if user_input == session['answer']:
            session['won'] = True

        session.modified = True
        
        return jsonify({
            'success': True,
            'feedback': feedback,
            'remaining_tries': session['tries'],
            'won': session['won']
        })
    except Exception as e:
        print(f"ERROR in api_guess: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/')
def index():
    # Reset game if it's already over, or initialize if not started
    if 'answer' not in session or session.get('won') or session.get('tries', 6) <= 0:
        setup_game()
    
    session.modified = True
    answer_str = ''.join(map(str, session['answer']))
    return render_template('index.html', history=session['history'], tries=session['tries'], won=session['won'], answer_str=answer_str)

@app.route('/guess', methods=['POST'])
def guess():
    if session['tries'] <= 0 or session['won']:
        return redirect(url_for('index'))

    user_input_str = request.form.get('guess')
    if not user_input_str or len(user_input_str) != 5 or not user_input_str.isdigit():
        return redirect(url_for('index'))  # Invalid input, redirect back

    user_input = [int(d) for d in user_input_str]
    feedback = get_feedback(user_input, session['answer'])
    session['history'].append((user_input, feedback))
    session['tries'] -= 1

    if user_input == session['answer']:
        session['won'] = True

    session.modified = True
    return redirect(url_for('index'))

@app.route('/analyze')
def analyze():
    if not session.get('won') and session.get('tries', 0) > 0:
        return redirect(url_for('index'))  # Game not finished

    optimal = get_optimal_solution(session['answer'])
    skill = calculate_skill(session['history'], optimal, session['answer'])
    luck = calculate_luck(session['history'], session['answer'])
    answer_str = ''.join(map(str, session['answer']))

    # Calculate errors and feedback for each turn
    errors = []
    optimal_feedback = []
    for i in range(len(session['history'])):
        if i < len(optimal):
            user_error = sum(abs(session['history'][i][0][j] - session['answer'][j]) for j in range(5))
            optimal_error = sum(abs(optimal[i][j] - session['answer'][j]) for j in range(5))
            errors.append((user_error, optimal_error))
            optimal_feedback.append(get_feedback(optimal[i], session['answer']))
        else:
            errors.append(None)
            optimal_feedback.append(None)

    return render_template('analyze.html', history=session['history'], optimal=optimal, optimal_feedback=optimal_feedback, skill=skill, luck=luck, answer=session['answer'], answer_str=answer_str, errors=errors)

@app.route('/new_game')
def new_game():
    setup_game()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
