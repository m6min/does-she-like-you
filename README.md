# Does She Like You ?

My first use of Random Forest Classifier.

[Try it on Streamlit](https://does-she-like-you.streamlit.app/app)

## How it works

- Trained on a dataset with 6 features using Random Forest
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

## Requirements

```
streamlit
pandas
scikit-learn
joblib
```