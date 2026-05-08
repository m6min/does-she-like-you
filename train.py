from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train_model(file_name: str) -> None:
    """ Splits data, trains model and saves it to models/brain.joblib """
    path = Path("data") / file_name
    df = pd.read_csv(path)
    y = df['She_Likes_You'].copy()
    X = df.drop(columns=['She_Likes_You']).copy()
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = RandomForestClassifier(n_estimators=100, random_state=0)
    model.fit(x_train, y_train)
    guesses = model.predict(x_test)
    # Accuracy is 0.85 for dataset
    """print(f"Accuracy: {accuracy_score(y_test, guesses)}")
    for index, (guess, real) in enumerate(zip(guesses.tolist(), y_test)):
        result = 'She likes you' if guess == 1 else 'Sorry... Find someone else.'
        result_real = 'She likes you' if real == 1 else 'Sorry... Find someone else.'
        print(f"Guess {index}: {result} / Real: {result_real}")
        if result != result_real:
            print(f"Wrong Prediction! Columns: {x_test.iloc[index].tolist()}")"""
    models_dir = Path("models")
    joblib.dump(model, models_dir / "brain.joblib")
    print("Model is saved on models directory.")
