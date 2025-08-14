import re

def extract_urls(text):
    """
    Extract all URLs from the given text using regular expressions.

    Args:
        text (str): The input text containing URLs.

    Returns:
        list: A list of extracted URLs.
    """
    # Regex pattern for URLs (http, https, www)
    url_pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    urls = re.findall(url_pattern, text)
    return urls

# Example usage
if __name__ == "__main__":
    sample_text = """
    Here are some useful links:
    - Visit our website at https://www.example.com for more info.
    - Our documentation is at http://docs.example.com.
    - You can also check www.testsite.org for resources.
    - Not a link: ftp://files.example.com
    """
    found_urls = extract_urls(sample_text)
    print("Extracted URLs:")
    for url in found_urls:
        print(url)
