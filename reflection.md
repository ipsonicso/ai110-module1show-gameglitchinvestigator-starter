# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- Q: What did the game look like the first time you ran it?
- Q: List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

### **Expected behavior**. When first using the program, I expected it should:
  - Let the user guess a number
  - respond after user enters their answer
  - tell the user to go UP if they gues too LOW
  - tell the user to go DOWN if they gues too HIGH

Changing 
### **Actual behavior/ bugs** (count: 5+)

1) __Menus__ :
    - **Expected**: Counters for total attempts (gray settings box, under selected difficulty) = attempts left (blue info box) when starting 
    - **ACTUAL**: the total attempts allowed says 8 while the Attempts left says 7 and (previous) Attempts says 1, despite no attempts being made (counter starts at 1 instead of 0)
3) __After inputting guesses__:
    - **Expected**:
      - User guesses too low --> hint to go higher, and vice versa
      - User can view guesses in debug menu under history
      - New game button resets all information 
    - **Actual**:
      - Hints are reversed; it says "Go LOWER" when the guess is lower than the answer and vice versa.
      - Saving history is offset by 1 guess, so guessing 13 then 14 will show only 13.
      - Although Attempts remaining resets after clicking "Submit Guess"  button, score does not reset.
3) __Extra__:
    - **Expected**: As difficulty increases, allowed attempts goes down and/or number range gets wider. (so (for [attempts/range] ratio) easy = 5/50 AKA 10%; normal = 8/100 AKA 8% allowed; hard = 5/100 AKA 5%)  
    - **Actual**: Ratio of allowed attempts to range of numbers allowed doesn't match difficulty: Normal (8/100) and Hard (5/50)

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
### Explanation (using Claude and Copilot):
1) I started with VScode Chat panel and Claude, asking it specific questions mentioning the lines I thought affected the problem and it suggested a change to the line in question.
2) Otherwise, it suggested changes in-line, like when I changed HIGHER to LOWER manually, it suggested changing LOWER to HIGHER.
3) I used copilot to generate and run pytest tests meeting my requirements.

### Examples: 
1)  Correct: I asked Claude to fix the attempts saving between runs/difficulty switches. 
2)  Incorrect: I asked Claude to adapt the program so history would update on click, but even after claiming it was definitely fixed, the history still only updated on second click.
  - **Adaptation:** I reasoned that, since accidentally guessing the same thing twice would be bad anyways, this issue could be circumvented by keeping the second-click output and not penalizing reguessing the same number (so attempts won't update).   
  
---

## 3. Debugging and testing your fixes
Qs: 
- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
As: 

I ran the program again and observed if it stayed the same.
[DEMO video: testing my fixes](https://www.loom.com/share/0e20309cbfee496fa6cf12ea0429187c)

1) I deemed that bug was fixed when running the program again yielded new and expected responses
2) One manual test (in the video): 
  - I tested a lower answer than the secret number, which output a HINT to go HIGHER (correct updated behavior)
  - I tested input threshold and history:
    - entering the same input 2+ times doesn't count towards attempts
    - submitting input after winning doesn't add to score
    - history updates after 2nd click still, but doesn't save to attempts
    - 
3) I used AI for the pytest examples in test_game_logic.py, but I used my own understanding and manual tests to improve output


---

## 4. What did you learn about Streamlit and state?

- Q: How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- A: Running a program using streamlit from terminal means sending it from your IDE to render in browser as a locally hosted pseudo-website. The version in your browser remains the same even if you update the code and save it. Hitting Ctrl + R to Rerun the program only reloads from the stage you sent to your browser. You need to resend the code to your browser to update the website to reflect your changes.  

---

## 5. Looking ahead: your developer habits
Qs:
- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
As:

1) Habit to reuse: Using Claude to generate and run testing criteria for pytest
2) Habit to do differently: Ask AI to explaining the process more
3) This project showed me that AI could be used for UI, as a way to adapt terminal code to websites.
