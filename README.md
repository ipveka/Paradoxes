# Paradoxes

Having fun with probability paradoxes

## Project Structure

- `app/`: Contains the Streamlit application.
  - `app.py`: Main entry point (Home page).
  - `pages/`: Individual paradox pages.
- `run_app.py`: Launcher script that installs dependencies and runs the app.
- `requirements.txt`: Python dependencies for all apps.
- `README.md`, `LICENSE`: Project documentation and license.

## Installation

1. Clone the repository and navigate to its directory.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Launch the Unified Paradoxes App

Run the following command to automatically install requirements and launch the app:
```bash
python run_app.py
```
Or manually:
```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## Experiments Included

- **Monty Hall**: 
  - **Description:** Simulate the classic game show problem. You pick one of three doors; Monty reveals a goat behind another door, and you choose whether to switch. 
  - **Why it's a paradox:** Intuitively, it seems like switching or staying should be 50/50, but switching actually gives you a 2/3 chance of winning. The host's knowledge and action change the probabilities in a non-obvious way. This paradox highlights how our intuition can be misled by conditional probability and the importance of considering all available information.
  - **Key insight:** Monty's action gives you information, making switching the better strategy. The problem is a classic example of how probability can defy our expectations.
  - **Further reading:** [Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem)

- **Birthday Paradox**: 
  - **Description:** Explore how likely it is for at least two people in a group to share a birthday. 
  - **Why it's a paradox:** Our intuition underestimates how quickly the probability grows. With just 23 people, there's over a 50% chance of a shared birthday, due to the rapid growth in the number of possible pairs. This paradox demonstrates the counterintuitive nature of combinatorics and probability in everyday situations.
  - **Key insight:** Probability grows with the number of pairs, not just the number of people. The paradox is a great illustration of how human intuition often fails with large numbers and combinations.
  - **Further reading:** [Wikipedia](https://en.wikipedia.org/wiki/Birthday_problem)

- **Two Envelopes Paradox**: 
  - **Description:** Pick one of two envelopes, each with money (one has twice as much as the other). Should you switch? 
  - **Why it's a paradox:** The expected value calculation seems to suggest you should always switch, but this leads to a logical loop. The reasoning ignores the prior distribution of amounts in the envelopes. This paradox exposes the subtleties of expectation and probability, and the importance of understanding the underlying assumptions in probabilistic reasoning.
  - **Key insight:** The calculation is misleading because it doesn't account for how the amounts were chosen. The paradox is a reminder to carefully consider the setup of probability problems.
  - **Further reading:** [Wikipedia](https://en.wikipedia.org/wiki/Two_envelopes_problem)

- **Sleeping Beauty Problem**: 
  - **Description:** Simulate the philosophical puzzle about self-locating belief. After being awakened, what probability should Sleeping Beauty assign to the coin toss being heads? 
  - **Why it's a paradox:** The answer seems to depend on how you count possibilities: is it 1/2 or 1/3? Philosophers and mathematicians still debate the correct answer. This paradox explores the difference between subjective and objective probability, and how to update beliefs when you have limited information about your own situation.
  - **Key insight:** The problem highlights the difference between subjective and objective probability, and how to update beliefs with self-locating uncertainty. It is a central example in the philosophy of probability.
  - **Further reading:** [Wikipedia](https://en.wikipedia.org/wiki/Sleeping_Beauty_problem)

- **Simpson's Paradox**: 
  - **Description:** See how trends in different groups can reverse when data is aggregated. 
  - **Why it's a paradox:** Aggregated data can hide or reverse trends present in subgroups, leading to misleading conclusions. Simpson's Paradox is a powerful reminder that data must be analyzed carefully, and that hidden variables can dramatically change the story told by statistics.
  - **Key insight:** Simpson's Paradox warns us to always check for hidden variables before drawing conclusions from data. It is a classic example of the dangers of ignoring confounding factors in data analysis.
  - **Further reading:** [Wikipedia](https://en.wikipedia.org/wiki/Simpson%27s_paradox)

## Adding a New Experiment
- Add your new page file to the `app/pages/` folder.
- Streamlit will automatically detect it.

## Deployment on Render

1. Create a new **Web Service** on Render.
2. Connect your GitHub repository.
3. Use the following settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app/app.py`


---

**Source:** This project is maintained at [ipveka/paradoxes](https://github.com/ipveka/paradoxes)
