"""
Simple Machine Learning Model: Iris Flower Classifier

This script trains a machine learning model to classify iris flowers into three species
(Setosa, Versicolor, Virginica) based on their petal and sepal measurements.

Responsible Usage Guidelines:
-----------------------------
- **Explainability**: This model uses a Decision Tree, which is relatively interpretable.
  You can visualize the tree to understand how decisions are made.
- **Accuracy Limits**: The model is trained on the classic Iris dataset. It may not generalize
  well to data outside the range or distribution of this dataset.
- **Fairness Considerations**: The Iris dataset is balanced across classes, but if you use
  this code with your own data, ensure your dataset is representative and not biased.
- **Responsible Deployment**: Do not use this model for high-stakes decisions without
  further validation, explainability analysis, and fairness checks.

How to Use:
-----------
- The model expects four numeric features as input:
    1. Sepal length (cm)
    2. Sepal width (cm)
    3. Petal length (cm)
    4. Petal width (cm)
- For best results, input values should be within the range of the original Iris dataset.
- Example input: [5.1, 3.5, 1.4, 0.2]
- The output will be the predicted species: 'setosa', 'versicolor', or 'virginica'.

What this code does:
--------------------
- Loads the Iris dataset.
- Splits the data into training and test sets.
- Trains a Decision Tree Classifier.
- Evaluates the model's accuracy.
- Provides a function to predict the species of a new iris flower based on user input.

"""

try:
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    SKLEARN_AVAILABLE = True
except Exception:
    # Graceful fallback if scikit-learn is not installed or unavailable
    SKLEARN_AVAILABLE = False

if SKLEARN_AVAILABLE:
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data  # Features: sepal length, sepal width, petal length, petal width
    y = iris.target  # Labels: 0=setosa, 1=versicolor, 2=virginica

    # Split into train and test sets for evaluation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Decision Tree Classifier
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Evaluate accuracy
    accuracy = clf.score(X_test, y_test)
    print(f"Model accuracy on test set: {accuracy:.2f}")
else:
    # Minimal stand-in so the rest of the code works
    class _Fallback:
        pass
    clf = _Fallback()
    # Create a small mimic of the real target names for consistent output
    class _IrisNames:
        target_names = ['setosa', 'versicolor', 'virginica']
    iris = _IrisNames()
    print("scikit-learn not available. Using a simple rule-based classifier (demo only).")

def predict_iris_species(features):
    """
    Predict the species of an iris flower given its features.

    Args:
        features (list or array): [sepal_length, sepal_width, petal_length, petal_width]

    Returns:
        str: Predicted species ('setosa', 'versicolor', or 'virginica')
    """
    if SKLEARN_AVAILABLE:
        pred = clf.predict([features])[0]
        return iris.target_names[pred]
    # Rule-based fallback (very rough heuristic):
    sepal_length, sepal_width, petal_length, petal_width = features
    if petal_length < 2.5:
        return 'setosa'
    elif petal_width < 1.8:
        return 'versicolor'
    else:
        return 'virginica'


def prompt_float(prompt_text: str) -> float:
    """
    Prompt the user for a single floating-point number with validation.
    Re-prompts only if the input is invalid; returns once a valid float is entered.
    """
    while True:
        try:
            value_str = input(prompt_text).strip()
            value = float(value_str)
            return value
        except ValueError:
            print("Please enter a valid number (e.g., 5.1).")

# Example usage:
if __name__ == "__main__":
    print("\nEnter iris flower features to predict its species.")
    print("Please provide the following measurements in centimeters (cm):")
    try:
        sepal_length = prompt_float("Enter sepal length (cm), e.g., 5.1: ")
        sepal_width = prompt_float("Enter sepal width (cm), e.g., 3.5: ")
        petal_length = prompt_float("Enter petal length (cm), e.g., 1.4: ")
        petal_width = prompt_float("Enter petal width (cm), e.g., 0.2: ")

        features = [sepal_length, sepal_width, petal_length, petal_width]
        species = predict_iris_species(features)
        print(f"Predicted species: {species}")
    except Exception as e:
        print("Invalid input. Please enter numeric values for all features.")

"""
Responsible AI Notice:
----------------------
- This model is for educational/demo purposes only.
- Always validate model performance on your own data before deployment.
- Consider the ethical implications of automated decision-making.
- For more explainability, consider visualizing the decision tree or using feature importance tools.
"""
