# boss_mini.py

# A tiny combat script for the GitHub Workflow Exam.

MAX_HP = 50
p_hp = MAX_HP
b_hp = 50


def attack():
  global b_hp
  # Attack logic fix: the original code only printed damage text and never reduced boss HP.
  # Required logic: subtract 10 from b_hp every attack and clamp at 0 to avoid negative health.
  b_hp = max(0, b_hp - 10)
  print("You deal 10 damage!")


def heal():
  global p_hp
  # Healing guardrail: prevent healing from a defeated state (0 or less HP).
  if p_hp <= 0:
    print("You cannot heal after being defeated.")
    return

  # Healing guardrail: cap healing so player HP cannot exceed the max (50).
  p_hp = min(MAX_HP, p_hp + 20)
  print(f"Healed! HP is now {p_hp}")


# --- Simple Game Loop ---

while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  # Security audit fix: cheat/backdoor input path was removed to close the hardcoded credential vulnerability.
  choice = input("Action [a]ttack, [h]eal: ").lower()

  if choice == 'a':
    attack()
    # Win condition fix: when boss HP reaches 0, print Victory and terminate the loop immediately.
    if b_hp <= 0:
      print("Victory!")
      break
  elif choice == 'h':
    heal()

  if b_hp > 0:
    p_hp -= 10

print("Game Over!")