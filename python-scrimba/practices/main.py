from dis import dis
from operator import ne


# name = input("enter your name: ")
# distanceInKm = input("enter distance in km:  ")
# distanceInMi = float(distanceInKm)/1.609
# print(f'Hi {name.title()}! {distanceInKm}km is equivalent to  {round(distanceInMi, 1)} miles')


friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
cars = [911, 130, 328, 535, 740, 308]

# # friends.insert(1, 'terryG')
# friends[2] = ('terryG')

# friends.extend(cars)
# friends.pop(-1)

# friends.remove("Terry")
# friends.clear()
# del friends[3]

# newFriends = friends[:]

# # new_friends = friends.copy()
# new_friends = list(friends)

# print(friends)

# sales_w1 = [7, 3, 42, 19, 15, 35, 9]
# sales_w2 = [12, 4, 26, 10, 7, 28]
# sales = []
# newDay = input("enter #of lemonades for new day: ")
# sales_w2.append(int(newDay))
# # sales.extend(sales_w1)
# # sales.extend(sales_w2)
# sales = sales_w1 + sales_w2
# # sales.sort()
# # print(sales)
# worst_day_prof = min(sales) * 1.5
# best_day_prof = max(sales) * 1.5
# # worst_day_prof = sales[0] * 1.5
# # best_day_prof = sales[-1] * 1.5
# print(f'worst day profit: ${worst_day_prof}')
# print(f'best day profit: ${best_day_prof}')
# print(f'combined profit: ${worst_day_prof + best_day_prof}')

# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# # print(msg.split(), type(msg.split(' ')))
# # print(csv.split(','))
# print(' '.join(friends_list))

# print(''.join(msg.split()))
# print(msg.replace(' ', ''))

# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# # print(','.join(csv.split(';')))
# # print(','.join(csv.split(';')).split(':'))
# # print((','.join(','.join(csv.split(';')).split(':'))).split(','))
# # friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
# # print(friends_list)
# print('replace', csv.replace(';', ',').replace(':', ',').split(','))
# friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
# friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')
# friends_set = {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Eric'}
# my_friends_set = {'Reg', 'Loretta', 'Colin', 'Eric', 'Graham'}
# print(friends)
# print(friends_tuple)
# print(friends_set)

# print(friends_set.intersection(my_friends_set))
# print(friends_set.difference(my_friends_set))
# print(friends_set.union(my_friends_set))

# friends = {'john','michael','terry','eric','graham'}
# my_friends = {'reg','loretta','colin','john','graham'}
# cars =['900','420','v70','911','911','5','328','900']


# print('eric' and 'john' in friends)

# print(friends.union(my_friends))
# print(friends | my_friends)
# print(friends.intersection(my_friends))
# print(friends.union(my_friends))
# print(friends & my_friends)

# print(friends.difference(my_friends))
# print(friends - my_friends)

# print(my_friends.symmetric_difference(friends))
# print(my_friends ^ friends)

# cars_no_dupl = set(cars)
# print(cars_no_dupl)

name = "Default"
name = input("Enter your silly name: ")
print("Thank you " + name + "!")
print("for applying to")
print("the Minstry of Silly Walks")