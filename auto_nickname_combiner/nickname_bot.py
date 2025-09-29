import random
import time

nickname_history = []  # keep nicknames generated in this session

# ---------------- Core Combination Styles ----------------
def style_basic(name1, name2):
    return name1[:2] + name2[-2:]

def style_half(name1, name2):
    return name1[:len(name1)//2] + name2[len(name2)//2:]

def style_random(name1, name2):
    return "".join(random.choice(name1 + name2) for _ in range(6))

def style_first3(name1, name2):
    return name1[:3] + name2[:3]

def style_reversed(name1, name2):
    return name1[::-1][:3] + name2[::-1][:3]

# ---------------- Fun Meaning Generator ----------------
def nickname_meaning(nickname):
    meanings = [
        f"{nickname} means 'The Cool One 😎'",
        f"{nickname} means 'Master of Mischief 🌀'",
        f"{nickname} is 'Guardian of Snacks 🍫'",
        f"{nickname} represents 'Swift & Smart ⚡'",
        f"{nickname} = 'The Unstoppable Dreamer 🌙'"
    ]
    return random.choice(meanings)

# ---------------- Generate Suggestions ----------------
def generate_nicknames(name1, name2):
    styles = [
        ("Basic (2+2 letters)", style_basic),
        ("Half + Half", style_half),
        ("Random Mix", style_random),
        ("First 3 + First 3", style_first3),
        ("Reversed Combo", style_reversed)
    ]

    results = []
    for label, func in styles:
        nickname = func(name1, name2)
        results.append((label, nickname))
        nickname_history.append(nickname)

    return results

# ---------------- Main Loop ----------------
def main():
    print("=== 🎭 Auto Nickname Combiner ===")
    while True:
        name1 = input("Enter first name: ").strip().capitalize()
        name2 = input("Enter second name: ").strip().capitalize()

        print("\nGenerating nicknames...\n")
        time.sleep(1)

        results = generate_nicknames(name1, name2)
