snack_box1 = {"chips","coco-cola","cake","ice-cream","cookies"}
snack_box2 = {"biscuits","cheeseballs","oreo","sprite","makhanas"}
print("snackbox1",snack_box1)
print("snackbox2",snack_box2)

snack_box1.add("apple")
print("Added snack is banana and snack box is:",snack_box1)

common_snacks = snack_box2.intersection (snack_box1)
print("Common snacks in both boxes are",common_snacks)

import array as arr
snack_counts = arr.array('i',[4 , 6 , 3, 5 , 70000000])
print("Snack counts after array are:",snack_counts)

snack_counts.insert(0 , 2)
snack_counts.append(7)
print("Snack counts after adding items are:",snack_counts)

count_of_70000000 = snack_counts.count(70000000)
print("Number of times 70000000 appears:", count_of_70000000)

snack_counts.reverse()
print("Reversed snack counts array:", snack_counts)

print("")
print("===== SCHOOL SNACK COUNTER =====")
print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)
print("Shared snacks:", common_snacks)
print("Snack counts:", snack_counts)
print("================================")

