import random as r
import sys, os


class RPS:

  def __init__(self):
    print("Welcome.....")
    self.l1 = []
    self.l2 = []
    self.moves = {"r": "🪨", "p": "📜", "s": "✂️"}
    self.valid = list(self.moves.keys())

  def play(self):
    user = input("\nEnter r,p,s >>").lower()
    os.system('clear')
    ai = r.choice(self.valid)
    if user == "e":
      print("Thank You...")
      sys.exit()
    if user not in self.valid:
      print("Invalid Input...")
      return self.play()
    self.display(user, ai)
    self.check(user, ai)
    self.points(self.l1, self.l2)

  def display(self, user, ai):
    print('--------------')
    print(f"user: {self.moves[user]}")
    print(f"ai: {self.moves[ai]}")
    print('--------------')

  def check(self, user, ai):
    if user == ai:
      print("Draw..")
      self.l1.append("-")
      self.l2.append("-")
    elif user == "r" and ai == "s":
      self.l1.append(1)
      self.l2.append(0)
      print("You won...")
    elif user == "s" and ai == "p":
      self.l1.append(1)
      self.l2.append(0)
      print("You won...")
    elif user == "p" and ai == "r":
      self.l1.append(1)
      self.l2.append(0)
      print("You won...")
    else:
      self.l1.append(0)
      self.l2.append(1)
      print("You lost...")

  def points(self, l1, l2):
    print('--------------')
    print("points:- \n")

    print(" " * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+")
    print(" " * 7 + "|" + "YOU".center(7, ' ') + "|" + "AI".center(7, ' ') +
          "|")
    print(" " * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+")
    t1 = 0
    t2 = 0
    for i in self.l1:
      if i == "-":
        i = 0
      t1 += i
    for j in self.l2:
      if j == "-":
        j = 0
      t2 += j
    for _ in range(len(l1)):
      print(
        f"{' '*7}| {f'{l1[_]}'.center(5,' ')} | {f'{l2[_]}'.center(5,' ')} |")
    print("+" + "-" * 6 + "+" + "-" * 7 + "+" + "-" * 7 + "+")
    print(f"|Total:| {f'{t1}'.center(5,' ')} | {f'{t2}'.center(5,' ')} |")
    print("+" + "-" * 6 + "+" + "-" * 7 + "+" + "-" * 7 + "+")
    if t1 > t2:
      print(f"You are leading by {t1-t2} points...")
    elif t1 < t2:
      print(f"AI are leading by {t2-t1} points...")
    else:
      print(f"Both have same {t1} points...")

    # comment if u don't want
    if len(self.l1) == 10:
      self.l1 = []
      self.l1.append(t1)
      self.l2 = []
      self.l2.append(t2)


if __name__ == '__main__':
  rps = RPS()
  while True:
    rps.play()
