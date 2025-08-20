def sentiment_analysis(word):
    """
    Simple sentiment analysis function.
    Returns 'positive', 'negative', or 'neutral' for a given word.
    This is a basic implementation and may not cover all edge cases.
    """
    # Example positive and negative word lists (expand as needed)
    positive_words = {"happy", "joy", "love", "excellent", "good", "great", "fantastic", "amazing", "wonderful", "delight"}
    negative_words = {"sad", "hate", "bad", "terrible", "awful", "horrible", "angry", "disgust", "pain", "worst"}

    # Convert word to lowercase for case-insensitive matching
    word_lower = word.lower()

    # Bias Mitigation Strategies:
    # 1. Ensure the positive and negative word lists are balanced in size and diversity.
    # 2. Regularly review and update word lists to avoid cultural or social bias.
    # 3. Remove or flag potentially offensive or loaded terms from both lists.
    # 4. Consider using a larger, more representative dataset or pretrained models for production use.

    if word_lower in positive_words:
        return "positive"
    elif word_lower in negative_words:
        return "negative"
    else:
        # For words not in the lists, return 'neutral'
        return "neutral"

# Example usage:
# print(sentiment_analysis("happy"))   # Output: positive
# print(sentiment_analysis("terrible")) # Output: negative
# print(sentiment_analysis("table"))    # Output: neutral

if __name__ == "__main__":
    import sys

    # If words are passed as command-line args, analyze each
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            print(sentiment_analysis(arg))
    else:
        # Interactive mode
        try:
            while True:
                user_input = input("Enter a word (or 'exit' to quit): ").strip()
                if user_input.lower() in {"exit", "quit", ""}:
                    break
                print(sentiment_analysis(user_input))
        except KeyboardInterrupt:
            pass
