from logic_utils import check_guess, parse_guess, get_range_for_difficulty

# --- Bug 1: Swapped hint messages in check_guess ---

def test_guess_too_high():
    # Guess 60, secret 50 — guess is above the secret
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_high_message():
    # When guess is too high, player must go LOWER (was incorrectly "Go HIGHER!")
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_guess_too_low():
    # Guess 40, secret 50 — guess is below the secret
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_too_low_message():
    # When guess is too low, player must go HIGHER (was incorrectly "Go LOWER!")
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

# --- Bug 2: String-casting glitch removed — check_guess only accepts ints ---

def test_check_guess_rejects_string_secret():
    # Before the fix, app.py cast secret to str on even attempts.
    # The old code silently handled int-vs-str with a try/except.
    # Now check_guess is pure — passing a string secret raises TypeError,
    # proving the type-coercion glitch and its workaround are both gone.
    import pytest
    with pytest.raises(TypeError):
        check_guess(50, "50")

# --- parse_guess: clean int parsing ---

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_non_number():
    ok, value, err = parse_guess("banana")
    assert ok is False
    assert value is None

def test_parse_guess_decimal_truncates():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7

# --- get_range_for_difficulty ---

def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100

def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 50




# --- Challenge 1: Advanced Edge-Case Testing ---

# Edge Case 1: Negative numbers
# Negative values like "-5" are valid ints, so parse_guess accepts them even though
# the game range starts at 1. Tests confirm the parser doesn't crash and check_guess
# still produces a defined outcome (Too Low) instead of blowing up.
def test_parse_guess_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert err is None

def test_check_guess_negative_guess_is_too_low():
    outcome, message = check_guess(-5, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

# Edge Case 2: Extremely large numbers
# A number like 9999999 is far outside any difficulty range (max is 100),
# but Python ints don't overflow. Tests confirm neither parse_guess nor check_guess
# crashes and that the hint is still correct.
def test_parse_guess_extremely_large_number():
    ok, value, err = parse_guess("9999999")
    assert ok is True
    assert value == 9999999
    assert err is None

def test_check_guess_extremely_large_is_too_high():
    outcome, message = check_guess(9999999, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

# Edge Case 3: Decimal with no leading digit (".5")
# ".5" contains "." so parse_guess takes the float path: int(float(".5")) == 0.
# Zero is outside the game range (starts at 1), but the parser currently accepts it
# as a valid guess. Test documents this boundary behaviour.
def test_parse_guess_dot_only_decimal():
    ok, value, err = parse_guess(".5")
    assert ok is True
    assert value == 0

def test_check_guess_zero_is_too_low():
    outcome, _ = check_guess(0, 50)
    assert outcome == "Too Low"


'''
#  3 Starter tests

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
    
    '''