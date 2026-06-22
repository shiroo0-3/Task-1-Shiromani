my_tasks=[]
task1=input("Enter task 1:")
my_tasks.append(task1)
task2=input("Enter task 2:")
my_tasks.append(task2)
task3=input("Enter task 3:")
my_tasks.append(task3)
task4=input("Enter task 4:")
my_tasks.append(task4)
print("\nYour Tasks:")
for index,task in enumerate(my_tasks,start=1):
    print(index,task)