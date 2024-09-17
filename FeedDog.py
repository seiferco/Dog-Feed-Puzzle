# Recursive solution
# def helper_func(hunger_level, biscuit_size, i, j, dogs_fed):

#     if i >= len(hunger_level):
#         return dogs_fed
#     if j >= len(biscuit_size):
#         return helper_func(hunger_level, biscuit_size, i + 1, 0, dogs_fed)
    
#     remainder = biscuit_size[j] / hunger_level[i]
#     if remainder >= 1:
#         dogs_fed += 1
#         biscuit_size.pop(j)
#         return helper_func(hunger_level, biscuit_size, i + 1, 0, dogs_fed)
#     else:
#         return helper_func(hunger_level, biscuit_size, i, j + 1, dogs_fed)

    

# def feedDog(hunger_level, biscuit_size):
#     hunger_level.sort(reverse=True)
#     biscuit_size.sort(reverse=True)

#     dogs_fed = helper_func(hunger_level, biscuit_size, 0, 0, 0)
#     return dogs_fed





# Iterative solution
def feedDog(hunger_level, biscuit_size):
    hunger_level.sort(reverse=True)
    biscuit_size.sort(reverse=True)

    print(hunger_level)
    print(biscuit_size)

    dogs_fed = 0

    for i in range(len(hunger_level)):
        for j in range(len(biscuit_size)):
            remainder = biscuit_size[j] / hunger_level[i]
            if remainder >= 1:
                dogs_fed += 1
                biscuit_size.pop(j)
                break
            
    return dogs_fed

    
def main():
    hunger_level1 = [2, 1]
    biscuit_size1 = [1,3,2]
    answer1 = feedDog(hunger_level1, biscuit_size1) 
    print(answer1)

    hunger_level2 = [1,2,3] 
    biscuit_size2 =[1,1]
    answer2 = feedDog(hunger_level2, biscuit_size2) 
    print(answer2)
main()