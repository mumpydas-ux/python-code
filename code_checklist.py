total_chores = 4
original_count = total_chores
print(f"you have {original_count} chores to finish  today")

completed_count = 0
chores_num = 1



while chores_num <= total_chores:
 if  chores_num == 1: next_chores = "make your bed"
 elif  chores_num == 2: next_chores = "feed the pet"
 elif  chores_num == 3: next_chores = "take out the trash"
 else: next_chores = "wash the dishes"

 answer = input(f"Have you finished {next_chores}? (yes/no): ")

 if answer == "yes":
    completed_count += 1
    chores_num += 1
    print(f"Great job you have completed your chore")
 else:
    print("Okay, finish it and check again")

 print("chores remaining", total_chores - completed_count)
 print()
 

