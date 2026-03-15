# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

Menus
a) I noticed the game has 3 different counters for attempts that don't match up: the total attempts allowed says 8 while the Attempts left says 7 and (previous) Attempts says 1, despite no attempts being made.

After inputting guesses
b) Hints are reversed; it says "Go LOWER" when the guess is lower than the answer and vice versa.
c) Saving history is offset by 1 guess, so guessing 13 then 14 will show only 13.
d) Although Attempts remaining resets after clicking "Submit Guess"  button, score does not reset.

Extra
e) Ratio of allowed attempts to range of numbers allowed doesn't match difficulty, Normal (8/100) and Hard (5/50)

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

a) I started with VScode Chat panel and Claude, asking it specific questions mentioning the lines I thought affected the problem and it suggested a change to the line in question. Otherwise, it suggested changes in-line, like when I changed HIGHER to LOWER manually, it suggested changing LOWER to HIGHER.
b) I used copilot to ask for pytest test... 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I ran the program again and observed if it stayed the same.


---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
