#import os  # Unused import (Lint error)
#import sys  # Another unused import (Lint error)


def main() -> None:
    # Bad indentation and cramped spacing (Formatting error)
    print("Hello from python-sandbox!")
    _user_id: int = "ED-BENNETT-99"
    announcement: str = format_message(12345)
    print(announcement)


def format_message(text: str) -> str:
    return f"LOG: {text.upper()}"


if __name__ == "__main__":
    main()
