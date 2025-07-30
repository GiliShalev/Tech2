# #
# #
# # x = 10
# # while x > 0:
# #     print(x)
# #     x -= 1
# #
# # for item in range(1, 5, 1):
# #     print(item)
# #
# # name = "Gil"
# # for letter in name:
# #     print(letter)
# #
# # names = ["Gil", "John", "Mary"]
# # for name in names:
# #     print(name)
# import time
# from pathlib import Path
#
# for i in range(1, 11, 1):
#     for j in range(1, 11, 1):
#         print(i * j, end='')
#     print()
#
# i = 1
# file_path = Path("C:/numbers.txt")
# while not file_path.exists():
#     time.sleep(2)
#     print(f"Waiting for file... {i}")
#     i += 1
#     if i > 10:
#         print("File not found")
#         break

for i in range(1, 11, 1):
    if i % 2 == 0:
        continue
    print(i)



