# 1- import the random module
import random
f = open("headlines.txt", "a" , encoding="utf-8")
# 2-creat subjects
subjects = [
      "Shahrukh khan",
      "Virat kohli",
      "Nirmala sitharaman",
      "A Mumbai cat",
      "A Group of Monkeys",
      "Prime Minister Modi",
      "Auto Rickshaw Driver from Delhi "
]


actions = [
      "launches",
      "cancels",
      "dances with",
      "eats",
      "declares war on",
      "orders",
      "celebrates",
]

place = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa ",
    "inside parliament ",
    "at Ganga  Ghat",
    "during Ipl Match",
    "at india gate"
]

# 3 start the headline generator loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing} "
    print("\n" + headline)
    f.write(headline + "\n")
    user_input = input("\n Do you want another headline? (yes/no): ").strip().lower()
    if user_input ==  "no":
        break

# print goodbye message
print("\nThanks for using fake news headline generator.Have a fun day")
f.close()