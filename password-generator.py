"""
Advanced Password Generator — Console edition
Features:
 - Cryptographically secure generation (secrets)
 - Options: length, uppercase, lowercase, digits, symbols
 - Avoid ambiguous chars (like l, I, 0, O)
 - FEATURING YO MAMA
 - Pronounceable (syllable-based) mode
 - Passphrase mode (wordlist file or internal sample)
 - Entropy calculation and strength rating
 - Generate multiple passwords, save to file, copy to clipboard (optional)
 - Robust input validation and helpful errors
 - IM BORED ASF SO IDGAF
"""

import secrets
import string
import math
import sys
from typing import List

# Try optional clipboard support
try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except Exception:
    CLIPBOARD_AVAILABLE = False

# Small fallback wordlist (for passphrase mode if user has no file)
FALLBACK_WORDLIST = [
    'apple', 'brick', 'cloud', 'drift', 'ember', 'flint', 'glow', 'harbor',
    'iron', 'jolt', 'kettle', 'lunar', 'moss', 'nectar', 'orbit', 'pylon',
    'quartz', 'raven', 'sable', 'timber', 'umbra', 'vapor', 'wisp', 'yarrow', 'zinc'
]

AMBIGUOUS = {'l', 'I', '1', '0', 'O'}

SYLLABLES = [
    'ba','be','bi','bo','bu','da','de','di','do','du','fa','fe','fi','fo','fu',
    'ka','ke','ki','ko','ku','la','le','li','lo','lu','ma','me','mi','mo','mu',
    'na','ne','ni','no','nu','pa','pe','pi','po','pu','ra','re','ri','ro','ru',
    'sa','se','si','so','su','ta','te','ti','to','tu','za','ze','zi','zo','zu'
]

def get_pool(upper, lower, digits, symbols, avoid_ambiguous):
    pool = ''
    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digits:
        pool += string.digits
    if symbols:
        # choose a set of symbols shits
        pool += '!@#$%^&*()-_=+[]{};:,.<>?'
    if avoid_ambiguous:
        pool = ''.join(ch for ch in pool if ch not in AMBIGUOUS)
    # ensure no duplicates and return as list
    return list(dict.fromkeys(pool))

def entropy_bits(length, pool_size):
    # entropy = length * log2(pool_size)
    if pool_size <= 1 or length <= 0:
        return 0.0
    return length * math.log2(pool_size)

def strength_label(bits: float) -> str:
    # wow stronggg grapeeeeeee
    if bits < 28:
        return "Very Weak"
    elif bits < 36:
        return "Weak"
    elif bits < 60:
        return "Moderate"
    elif bits < 80:
        return "Strong"
    else:
        return "Very Strong"

def generate_password(length:int, pool:List[str]) -> str:
    if length <= 0:
        raise ValueError("Length must be positive.")
    return ''.join(secrets.choice(pool) for _ in range(length))

def generate_pronounceable(length:int) -> str:
    if length < 2:
        return generate_password(length, list(string.ascii_lowercase))
    pwd = []
    while len(''.join(pwd)) < length:
        s = secrets.choice(SYLLABLES)
        pwd.append(s)
    passwd = ''.join(pwd)[:length]
    # random capitalization and maybe digits/symbols can be post-processed by caller
    return passwd

def generate_passphrase(num_words:int, wordlist:List[str], separator:'str' = '-') -> str:
    if num_words <= 0:
        raise ValueError("num_words must be > 0")
    if not wordlist:
        raise ValueError("wordlist is empty")
    words = [secrets.choice(wordlist) for _ in range(num_words)]
    return separator.join(words)

def load_wordlist_from_file(path: str) -> List[str]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip()]
            return words if words else FALLBACK_WORDLIST
    except Exception:
        return FALLBACK_WORDLIST

def validate_positive_int(value: str, name='value') -> int:
    try:
        n = int(value)
        if n <= 0:
            raise ValueError
        return n
    except Exception:
        raise ValueError(f"{name} must be a positive integer.")

def prompt_bool(question: str, default=True) -> bool:
    yn = "Y/n" if default else "y/N"
    ans = input(f"{question} ({yn}): ").strip().lower()
    if ans == '':
        return default
    return ans in ('y', 'yes')

def main_menu():
    print("\n=== Advanced Password Generator ===\n")
    print("Modes:")
    print(" 1) Random password (character pool)")
    print(" 2) Pronounceable password (syllables)")
    print(" 3) Passphrase (words from wordlist)")
    print(" 4) Exit")

    choice = input("[!] Pick mode [1-4]: ").strip()
    return choice

def generate_loop():
    while True:
        try:
            mode = main_menu()
            if mode == '4':
                print("\n[!] Good. Go secure your accounts, Goodbye.\n")
                return

            if mode == '1':
                # character-based
                length = validate_positive_int(input("\n[!] Length? (e.g. 16): ").strip(), 'Length')
                use_upper = prompt_bool("[!] Include UPPERCASE?", True)
                use_lower = prompt_bool("[!] Include lowercase?", True)
                use_digits = prompt_bool("[!] Include digits?", True)
                use_symbols = prompt_bool("[!] Include symbols?", True)
                avoid_amb = prompt_bool("[!] Avoid ambiguous characters (O,0,l,1)?", True)

                pool = get_pool(use_upper, use_lower, use_digits, use_symbols, avoid_amb)
                if not pool:
                    print("[!] Error: character pool is empty. Enable at least one charset.")
                    continue

                count = validate_positive_int(input("[!] How many passwords to generate? (1): ").strip() or "1", "Count")
                passwords = [generate_password(length, pool) for _ in range(count)]
                pool_size = len(pool)
                bits = entropy_bits(length, pool_size)
                label = strength_label(bits)

                print(f"\n[!] Pool size: {pool_size} characters. Estimated entropy: {bits:.1f} bits ({label})")
                for i, p in enumerate(passwords, 1):
                    print(f"{i}) {p}")

                post_actions(passwords)

            elif mode == '2':
                # pronounceable
                length = validate_positive_int(input("\n[!] Length? (approx, e.g. 12): ").strip(), 'Length')
                count = validate_positive_int(input("[!] How many passwords to generate? (1): ").strip() or "1", "Count")
                passwords = []
                for _ in range(count):
                    base = generate_pronounceable(length)
                    # sprinkle random caps and optionally digits/symbols
                    # ask the retarded user:
                add_caps = prompt_bool("[!] Randomly capitalize some letters?", True)
                add_digits = prompt_bool("[!] Append a random digit?", True)
                add_symbol = prompt_bool("[!] Append a random symbol?", False)

                for _ in range(count):
                    p = generate_pronounceable(length)
                    if add_caps:
                        # randomly capitalize ~30% of chars
                        p = ''.join(ch.upper() if secrets.randbelow(100) < 30 else ch for ch in p)
                    if add_digits:
                        p += secrets.choice(string.digits)
                    if add_symbol:
                        p += secrets.choice('!@#$%^&*()')
                    passwords.append(p)

                # estimate entropy: approximate pool for pronounceable is tricky; use crude estimate
                approx_bits = len(passwords[0]) * math.log2(26 * 0.6)  # rough
                print(f"\n[!] Pronounceable passwords (approx entropy per password: {approx_bits:.1f} bits)")
                for i, p in enumerate(passwords, 1):
                    print(f"{i}) {p}")
                post_actions(passwords)

            elif mode == '3':
                # passphrase
                num_words = validate_positive_int(input("[!] Number of words (recommended 4+): ").strip(), 'Number of words')
                wordfile = input("[!] Wordlist file (press Enter to use built-in small list): ").strip()
                if wordfile:
                    wordlist = load_wordlist_from_file(wordfile)
                else:
                    wordlist = FALLBACK_WORDLIST
                sep = input("[!] Separator between words (default '-') : ").strip() or '-'
                passwords = [generate_passphrase(num_words, wordlist, separator=sep)]
                # entropy: log2(len(wordlist)) * num_words
                bits = num_words * math.log2(len(wordlist))
                label = strength_label(bits)
                print(f"\n[!] Using wordlist size {len(wordlist)}. Estimated entropy: {bits:.1f} bits ({label})")
                print(f"[!] Passphrase: {passwords[0]}")
                post_actions(passwords)
            else:
                print("\n[!] Invalid selection, try again.")
        except ValueError as ve:
            print("\n[!] Input error:", ve)
        except KeyboardInterrupt:
            print("\n[!] Interrupted. Exiting.")
            return
        except Exception as e:
            print("\n[!] Unexpected error:", e)

def post_actions(passwords: List[str]):
    # save or copy shit after generation blah blah wuhadwihwdjiadajdwandkafajdndnwndwncnwjkd
    while True:
        print("\nActions:")
        print(" 1) Copy a password to clipboard (requires pyperclip)")
        print(" 2) Save all to file")
        print(" 3) Done / back to main menu")
        act = input("[!] Choose action [1-3]: ").strip()
        if act == '1':
            if not CLIPBOARD_AVAILABLE:
                print("[!] pyperclip not available. Install with: pip install pyperclip")
                continue
            idx = validate_positive_int(input(f"[!] Which password index to copy (1-{len(passwords)}): ").strip(), 'index')
            if 1 <= idx <= len(passwords):
                pyperclip.copy(passwords[idx-1])
                print("[!] Copied to clipboard.")
            else:
                print("[!] Index out of range.")
        elif act == '2':
            path = input("[!] File path to save (e.g. passwords.txt): ").strip() or "passwords.txt"
            try:
                with open(path, 'a', encoding='utf-8') as f:
                    for p in passwords:
                        f.write(p + '\n')
                print(f"[!] Saved {len(passwords)} password(s) to {path}")
            except Exception as e:
                print("[!] Failed to save:", e)
        elif act == '3':
            return
        else:
            print("[!] Invalid action. Choose 1, 2, or 3.")

if __name__ == "__main__":
    generate_loop()
