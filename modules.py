import chennai_module as cm
from rock_paper_scissors import play_rock_paper_scissors
import random as rdm

# To print what is in the module
for item in dir(cm):
    print(item)
# for item in dir(rdm):
#     print(item)

print("From module: ", cm.capital)
cm.random_fun_fact()

print("Time to Play")
play_rock_paper_scissors()
