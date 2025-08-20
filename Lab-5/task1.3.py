"""
Product Recommendation System with Ethical Guidelines

- Transparency: The system explains why recommendations are made.
- Fairness: The system avoids favoritism and ensures diverse recommendations.
- User Feedback: Users can provide feedback to improve recommendations.
"""

def get_user_history():
    """
    Simulate fetching user purchase/view history.
    In a real system, this would come from a database.
    """
    # Example: user has interacted with electronics and books
    return ["laptop", "smartphone", "novel", "headphones"]

def get_product_catalog():
    """
    Simulate a product catalog.
    Each product has a category and a name.
    """
    return [
        {"name": "Laptop", "category": "Electronics"},
        {"name": "Smartphone", "category": "Electronics"},
        {"name": "Headphones", "category": "Electronics"},
        {"name": "Novel", "category": "Books"},
        {"name": "Cookbook", "category": "Books"},
        {"name": "Running Shoes", "category": "Sportswear"},
        {"name": "Yoga Mat", "category": "Sportswear"},
        {"name": "Board Game", "category": "Toys"},
        {"name": "Puzzle", "category": "Toys"},
    ]

def recommend_products(user_history, catalog, num_recommendations=3):
    """
    Recommend products based on user history.
    - Recommends products from categories the user likes.
    - Ensures at least one product from a new category for diversity (fairness).
    - Explains the reason for each recommendation (transparency).
    """
    # Count categories in user history
    from collections import Counter
    history_categories = []
    for item in user_history:
        for product in catalog:
            if product["name"].lower() == item.lower():
                history_categories.append(product["category"])
    category_counts = Counter(history_categories)

    # Find top categories
    top_categories = [cat for cat, _ in category_counts.most_common()]

    # Recommend products from top categories, but ensure diversity
    recommended = []
    explained = []
    used_names = set([item.lower() for item in user_history])

    # 1. Recommend from top categories (not already interacted with)
    for cat in top_categories:
        for product in catalog:
            if product["category"] == cat and product["name"].lower() not in used_names:
                recommended.append(product)
                explained.append(
                    f"Recommended '{product['name']}' because you like {cat} products."
                )
                if len(recommended) >= num_recommendations - 1:
                    break
        if len(recommended) >= num_recommendations - 1:
            break

    # 2. Add at least one product from a new category for fairness/diversity
    all_categories = set([p["category"] for p in catalog])
    new_categories = all_categories - set(top_categories)
    for cat in new_categories:
        for product in catalog:
            if product["category"] == cat and product["name"].lower() not in used_names:
                recommended.append(product)
                explained.append(
                    f"Recommended '{product['name']}' to introduce you to {cat} products for a diverse experience."
                )
                break
        if len(recommended) >= num_recommendations:
            break

    # If not enough recommendations, fill with random products not in history
    if len(recommended) < num_recommendations:
        for product in catalog:
            if product["name"].lower() not in used_names and product not in recommended:
                recommended.append(product)
                explained.append(
                    f"Recommended '{product['name']}' to expand your options."
                )
            if len(recommended) >= num_recommendations:
                break

    return recommended[:num_recommendations], explained[:num_recommendations]

def get_user_feedback(recommended):
    """
    Allow user to provide feedback on recommendations.
    """
    print("\nWe value your feedback! Please rate the recommendations (1-5):")
    feedback = {}
    for product in recommended:
        while True:
            try:
                rating = int(input(f"How do you rate '{product['name']}'? (1=Bad, 5=Great): "))
                if 1 <= rating <= 5:
                    feedback[product["name"]] = rating
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")
    print("Thank you for your feedback! This will help us improve fairness and relevance.")

def main():
    print("Welcome to the Ethical Product Recommendation System!\n")
    user_history = get_user_history()
    catalog = get_product_catalog()
    print(f"Your recent activity: {', '.join(user_history)}")

    recommended, explanations = recommend_products(user_history, catalog)
    print("\nRecommended products for you:")
    for product, reason in zip(recommended, explanations):
        print(f"- {product['name']} ({product['category']}): {reason}")

    # Transparency: Show how recommendations were made
    print("\n[Transparency] Recommendations are based on your past interests and include diverse options to ensure fairness.")

    # User feedback
    get_user_feedback(recommended)

if __name__ == "__main__":
    main()
