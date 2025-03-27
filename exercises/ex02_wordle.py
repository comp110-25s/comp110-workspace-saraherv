"""Wordle!"""

__author__: str = "730485927"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret: str, character: str) -> bool:
    """See if any of the characters are in the secret word."""
    assert len(character) == 1, f"len('{character}') is not 1"
    idx: int = 0
    while idx < len(secret):
        if secret[idx] == character:
            return True
        idx = idx + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Green: correct place, Yellow: correct character, White: both incorrect."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    idx: int = 0
    result: str = ""
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx = idx + 1
    return result


def input_guess(exp_length: int) -> str:
    """Prompts guess until it is the expected length."""
    while True:
        guess = input(f"Enter a {exp_length} character word:")
        if len(guess) != exp_length:
            print(f"That wasn't {exp_length} chars! Try again:")
        else:
            return str(guess)


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    exp_length = len(secret)
    idx: int = 1

    while idx <= 6:
        print(f"=== Turn {idx}/6 ===")
        guess = input_guess(exp_length)
        print(emojified(guess, secret))

        if guess == secret:
            print(f"You won in {idx}/6 turns!")
            return None
        idx = idx + 1

    print("X/6 - Sorry, try again tomorrow!")
    return None


if __name__ == "__main__":
    main(secret="codes")
