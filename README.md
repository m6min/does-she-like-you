# Does She Like You?

A machine learning app that tries to answer the question you're too afraid to ask.

Note: The model is only as good as the data it was trained on. If it's wrong, maybe that's not the worst outcome.

## What it does

You rate a few things about yourself, her, and the situation. The model gives you an answer.
That's it.

## How it works

- Trained on a dataset with 6 features using Random Forest
- Achieves 85% accuracy on test data
- Built with Streamlit for the interface

## Features

| Feature | Description |
|---|---|
| Look Score (You) | How you rate yourself on looks |
| Look Score (Her) | How you rate her on looks |
| Relationship Score | How close you two already are |
| Your Social Score | Your social skills |
| Her Social Score | Her social skills |
| Probability | Your gut feeling about the two of you |

## Setup

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Train the model**
```bash
python train.py
```

**3. Run the app**
```bash
streamlit run app/main.py
```

## Project Structure

```
project/
├── data/
│   └── data.csv
├── models/
│   └── brain.joblib
├── app/
│   └── main.py
├── train.py
└── requirements.txt
```

## Requirements

```
streamlit
pandas
scikit-learn
joblib
```