# for i in range(7):
#
#     if not i % 3 and i != 0:
#
#         continue
#
#     print(i)

print([i for i in range(7) if i % 3 != 0 or i == 0 ])
