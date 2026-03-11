# boss_mini.py

# A tiny combat script for the GitHub Workflow Exam.



SECRET_CODE = "ADMIN_ACCESS_2025"



p_hp = 50

b_hp = 50



def attack():

  global b_hp

    print("You deal 10 damage!")



def heal():

  global p_hp

  p_hp += 20

  print(f"Healed! HP is now {p_hp}")



# --- Simple Game Loop ---

while p_hp > 0 and b_hp > 0:

  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")

  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()



  if choice == 'a':

    attack()

  elif choice == 'h':

    heal()

  elif choice == 'c':

    if input("Code: ") == SECRET_CODE:

      b_hp = 0

  

  if b_hp > 0:

    p_hp -= 10



print("Game Over!")