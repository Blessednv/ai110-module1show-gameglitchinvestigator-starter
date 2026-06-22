# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`
3. Run automated tests: `python -m pytest tests/test_game_logic.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game purpose:** A number guessing game built with Streamlit where the player tries to guess a secret number within a limited number of attempts. The difficulty setting controls the range (Easy: 1–20, Normal: 1–100, Hard: 1–50) and attempt limit (Easy: 6, Normal: 8, Hard: 5). A score is tracked based on how quickly the player guesses correctly.
- [x] **Bugs found:** (1) Reversed hint messages — "Go HIGHER" showed when guess was too high, "Go LOWER" when too low. (2) Scrambled difficulty ranges — Hard used 1–20, which was easier than Normal's 1–100. (3) Broken New Game button — clicking it did nothing after a win or loss. (4) Hidden TypeError — secret number was sometimes cast to a string on even attempts, causing silent comparison failures.
- [x] **Fixes applied:** Swapped the hint messages in `check_guess`; corrected difficulty ranges in `get_range_for_difficulty`; added `st.rerun()` and proper state reset to the New Game button; removed the string-casting try/except block from `parse_guess`. All core logic was refactored into `logic_utils.py` so it can be tested independently with `pytest`.

## 📸 Demo Walkthrough

General:
1. **Launch:** Start the game and select "Normal" difficulty.
2. **Guessing:** User enters a guess of `40`.
3. **Feedback:** Game returns "Too Low, 📈 Go HIGHER!"
4. **Range Logic:** User guesses `80`. Game returns "Too High, 📉 Go LOWER!"
5. **Winning:** User guesses the correct secret. Game triggers a win condition, updates the score, and displays final stats.
6. **New Game:** User clicks "New Game." The state resets, attempts clear, and a new secret is generated without page refresh.

Step by step:
1. Player opens the app and selects **Normal** difficulty (range 1–100, 8 attempts).
2. Player guesses **40** → game returns "📈 Go HIGHER!" and decrements the attempt counter.
3. Player guesses **70** → game returns "📉 Go LOWER!" confirming the hints are now correct.
4. Player guesses **55** → game returns "📈 Go HIGHER!" — score updates after each guess.
5. Player guesses **62** → game returns "🎉 Correct!" — balloons appear, final score is displayed.
6. Player clicks **New Game** → board resets immediately, a fresh secret number is generated, and the game is ready to play again without freezing.

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================


My Output:
(.venv) blessednatalia@MacBookPro ai110-module1show-gameglitchinvestigator-starter % python -m pytest tests/test_game_logic.py
=================================================== test session starts ====================================================
platform darwin -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/blessednatalia/Documents/A+CodePathAI/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 13 items                                                                              
tests/test_game_logic.py .............                                                                               [100%]

==================================================== 13 passed in 0.06s ====================================================
(.venv) blessednatalia@MacBookPro ai110-module1show-gameglitchinvestigator-starter % 

```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
