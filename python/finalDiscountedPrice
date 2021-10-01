# stack = []
# finalPrice = items[:]

# for i, item in enumerate(items):
#     while stack and stack[-1][1] >= item:
#         index, value = stack.pop()
#         finalPrice[index] = value - item

#     stack.append((i, item))

# print(sum(finalPrice))
# print(finalPrice)


def finalDiscountedPrice(items):
     stack = []
     finalPrice = items[:]
     for i, item in enumerate(items):
          while stack and stack[-1][1] >= item:
               index, value = stack.pop()
               finalPrice[index] = value - item

          stack.append((i, item))

     print(sum(finalPrice))
     print(finalPrice)


if __name__ == "__main__":
    print( finalDiscountedPrice([2, 3, 1, 2, 4, 2]))