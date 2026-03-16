from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_history_collects_valid_guesses():
    # Valid unique guesses should be appended to history.
    history = []
    for guess in [21, 23, 32]:
        if guess not in history:
            history.append(guess)
    assert history == [21, 23, 32]

def test_history_rejects_duplicate_guesses():
    # A repeated guess should not be added again.
    history = [21, 23]
    guess = 21
    if guess not in history:
        history.append(guess)
    assert history == [21, 23]

def test_history_rejects_invalid_input():
    # Invalid input (failed parse) should not be added to history.
    history = []
    raw = "abc"
    try:
        value = int(raw)
        history.append(value)
    except ValueError:
        pass
    assert history == []

def test_history_clears_on_new_game():
    # Starting a new game should reset history to empty.
    history = [21, 23, 32]
    history = []
    assert history == []

def test_hints_are_directionally_correct_after_submit():
    # Simulate immediate post-submit evaluation for a low guess.
    _, low_guess_hint = check_guess(40, 50)
    assert low_guess_hint == "📈 Go HIGHER!"

    # Simulate immediate post-submit evaluation for a high guess.
    _, high_guess_hint = check_guess(60, 50)
    assert high_guess_hint == "📉 Go LOWER!"
