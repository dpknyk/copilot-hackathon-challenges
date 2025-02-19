import requests
import re
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to fetch the content of the scroll from the given URL
def fetch_scroll_content(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    return response.text

# Function to extract secrets from the scroll content using regular expressions
def extract_secrets(content):
    pattern = r'\{\*(.*?)\*\}'
    secrets = re.findall(pattern, content)
    return secrets

# Function to display the extracted secrets in a structured manner with colors
def display_secrets(secrets):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    print("Extracted Secrets:")
    for i, secret in enumerate(secrets):
        color = colors[i % len(colors)]
        print(f"{color}- {secret}")

# Main function to orchestrate fetching, extracting, and displaying secrets
def main():
    url = "https://raw.githubusercontent.com/sombaner/copilot-hackathon-challenges/main/Data/Scrolls.txt"
    scroll_content = fetch_scroll_content(url)
    secrets = extract_secrets(scroll_content)
    display_secrets(secrets)

if __name__ == "__main__":
    main()