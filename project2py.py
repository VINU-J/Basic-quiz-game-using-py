print("welcome the game players!")
player = input('Do you want to play? ')
if player.lower() != "yes":
    quit()
else:
  print("ok lets play")
score = 0


question = input ("how many month in a year?")
if question.lower() == "twell":
  print('correct')
  score +=1
else:
  print('incorrect')

question = input ("how many weeks in a year?")
if question.lower() == "fifty two":
  print('correct')
  score +=1
else:
  print('incorrect')

question = input ("how many days do we have in a week?")
if question.lower() == "seven":
  print('correct')
  score +=1
else:
  print('incorrect')

print("your score : "+ str(score))