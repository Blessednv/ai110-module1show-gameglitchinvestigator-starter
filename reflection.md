# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.


## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, it looked functional on the surface, but interacting with it quickly revealed major logic and state management issues. Here are the concrete bugs I noticed:
1. Reversed & Unbounded Hint Logic: The game told me to go "lower" when I guessed 1 (and even 0), and told me to go "higher" when I guessed above 100.
2. Scrambled Difficulty Settings: The ranges and attempt limits were mapped incorrectly. "Hard" mode used a 1-20 range (which is easier than Normal's 1-100 range), and attempt limits were mismatched across all levels.
3. Broken Game Reset (State Issue): After winning, the game prompted me to "Start a new game to play again," but no functionality existed to actually reset the board.
4. Debug State Initialization: The "Developer Debug Info" displayed 0 attempts allowed instead of the correct limits (5, 6, or 8).
5. App Freezing: The Streamlit app would completely freeze and become unresponsive during certain interactions.

Original quick notes while working on the app:

  1. I started guess gamae with 1 and it told me that hint was to go lower, but the range is from 1 to 100, I tried 0 and it told me go even lower.
  2.  Settings Difficulty Levels:
   easy range 1 to 20, but hard level 1 to 20 and normal 1 to 100, it not right. Attempts allowed are not right, for hard one 5 attemos, but for eassy ones 6 attemps, for rnormal 8.
  3. After guessign correct numbret it says" You already won. Start a new game to play again." But I couldnt, it does not go to a new game. 
  4. "In Developer Debug Info" shows wrong number of atttemos, can be zero when it should be 5,6 or 8 depending on difficulty levels. 
  5. the app is frozeen
  6. When I guess number larger thne 100 it tell me to go higher
  7. 


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
1. | 0 | too low | go lower | 20  |
2. | 1000| too high | go higher | 85 |
3. |on hard level - I submit 5 | go higher/go lower | after first attemp Game over. Start a new game to try again. | |
4. Attempts allowed are not right, for hard one 5 
attemos, but for easy ones 6 attemps, for rnormal 8.
5. | 99800| too high | go higher | 42|
5. Game completely frozen only after 1 game. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude AI directly within VS Code as my primary coding assistant to diagnose logic errors and attempt code refactoring. I also used Gemini, as my CLaude AI already used 88 percent with 9 days remaining until the quota resets 
I am not sure how it happened, I thought we should have more then enough to be able to complete our assignemnts. However, this experience highlighted the importance of being tool-agnostic and managing my "AI budget" effectively when working on complex, multi-step assignments.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

**Correct Suggestion:** I asked Claude to explain the underlying logic causing my 'reversed hint' glitch. It correctly identified that the string messages were swapped in the `check_guess` function's `if/else` block, and it even proactively found a secondary, hidden `TypeError` string-casting bug. I verified this by manually reviewing lines 35-46 in `app.py` and confirming the inequalities were indeed backward

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

**Incorrect/Misleading Suggestion:** 
1. I gave Claude a prompt to fix the hint bugs *and* move the `check_guess` function into `logic_utils.py`. Claude took a shortcut; it applied the fixes directly in `app.py` but completely ignored my instruction to refactor the code. I verified this by checking the file diffs and seeing that `logic_utils.py` was untouched and still contained `NotImplementedError` stubs.

2. The AI demonstrated a tendency to prioritize speed over structural integrity. When asked to refactor the game code into logic_utils.py, it repeatedly took shortcuts, such as leaving NotImplementedError stubs or failing to remove redundant try/except type-casting blocks. It treated the task as "code fixing" rather than "architectural refactoring."
How I verified/corrected this: I verified these shortcomings by reviewing the file diffs after each suggestion. I had to assume the role of a Senior Developer, providing iterative, corrective feedback to the AI. I used targeted prompts to enforce clean code principles—specifically demanding the removal of technical debt (the try/except blocks) and ensuring all logic was fully migrated. This taught me that AI assistants require rigorous oversight and explicit instructions to maintain architectural standards.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

A bug was not considered fixed until I could verify it in two ways: first by manually playing the game and seeing the correct behavior, and second by running `pytest` and confirming all tests passed. If either check failed, I kept iterating. I specifically retested edge cases — like guessing 1 on Easy or guessing above the range — because those were the inputs that originally exposed the bugs.

- Describe at least one test you ran (manual or using pytest)  

**Tests Ran:**

1. **Manual test:** I ran `python -m streamlit run app.py` and deliberately guessed `1` as my first guess. Before the fix, the game incorrectly said "Go LOWER." After the fix, it correctly returned "Too Low, Go HIGHER!" I also tested the New Game button — after winning, clicking it cleared the board and started a fresh round without freezing, confirming the `st.rerun()` fix worked.

2. **Automated pytest:** I ran `pytest tests/test_game_logic.py` from the terminal. All 14 tests passed. The most important test was `test_check_guess_rejects_string_secret`, which proved that the old hidden string-casting try/except bug and its workaround were both fully removed — the function now raises a `TypeError` on a string input instead of silently mis-comparing. This gave me confidence that the refactor into `logic_utils.py` was clean, not just cosmetically moved.

- Did AI help you design or understand any tests? How?

AI was highly effective at helping me understand the mathematical flaws in the original buggy code — it explained exactly which inequalities were swapped in `check_guess` and why that caused the reversed hints. However, I had to manually enforce the architectural rules: the AI kept fixing bugs directly in `app.py` instead of moving the logic to `logic_utils.py` as instructed. By keeping functions isolated in `logic_utils.py`, I was able to import and test them independently with `pytest`, without needing to mock Streamlit.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time you click a button in Streamlit, the entire Python script reruns from the top — like refreshing the page. Without st.session_state, any variable you defined (like the secret number or attempt count) gets reset to its starting value on every click, which is exactly why guesses felt random and the game kept "forgetting" what happened. st.session_state is like a small locker that survives each rerun — you put values in it once and they stick between clicks. The st.rerun() call is how you manually trigger that refresh after a state change, like resetting the game, or a "rerun" is simply the mechanism that forces the app to cycle back to the top of the script so it can display the updated data held in that memory bucket.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? (  - This could be a testing habit, a prompting strategy, or a way you used Git.)

One habit I want to reuse is isolating core logic into separate functions before testing. In this project, keeping functions like check_guess, parse_guess, and get_range_for_difficulty in logic_utils.py allowed me to test them with pytest without needing to run or interact with the Streamlit interface. This saved time and made debugging much easier.
I also want to make test-driven verification a default habit. Before this project, I thought of tests as something to write after the code was finished. Now I see tests as a tool for checking the logic while the project is still being built. By refactoring the logic into logic_utils.py and writing pytest cases right away, I caught bugs I might have missed otherwise. This strategy of separating logic from the UI is something I will definitely apply to future AI engineering projects.


- What is one thing you would do differently next time you work with AI on a coding task?

Next time, I would give the AI one task at a time. I learned that asking Claude to “fix the bug and refactor the code into logic_utils.py” in a single prompt caused it to focus on one part of the request while silently skipping the refactor. Smaller, more focused prompts produced more reliable results.
This taught me that AI works best when the instructions are specific, limited, and easy to verify. In future projects, I would break larger requests into smaller steps, check each result carefully, and only move on after confirming that the previous step was completed correctly.


- In one or two sentences, describe how this project changed the way you think about AI generated code.

 This project taught me that AI is an excellent "coder" but a poor "architect." It changed the way I think about AI-generated code because I learned that code can run without crashing and still be logically wrong. I now see AI as a fast first-draft coding assistant, not a finished solution; it still needs a developer to provide constraints, review the logic, test the behavior, and make sure the codebase is maintainable, modular, and verifiable. AI is a fast first draft, not a finished product.