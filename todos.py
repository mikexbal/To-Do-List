def showList():
  if len(taskList) == 0:
    print("\nYour list is currently empty!")
  else: 
    print(taskList)

def add():
  task = input("\nEnter task: ")
  taskList.append(task)
  position = taskList.index(task)
  taskList[position] = (f'{position + 1}. {task}')
  
def remove():
  #Remove from list
  print(taskList)
  task = int(input("\nEnter task number: "))

  print(f"\n {taskList[task - 1]} removed!")
  taskList.pop(task - 1)

def complete():
  taskNum = int(input("Enter task completed: ")) - 1
  if taskNum < 0 or taskNum > len(taskList):
    print("Invalid task number entered!")
  else: 
    task = taskList[taskNum]
    print(f"You have completed {task}!")
    taskList.pop(taskNum)

def deleteList():
  taskList.clear()
  print("\nList cleared!")

isRunning = True
taskList = []

while isRunning:
  print("\n**********************")
  print("  Welcome to Listify  ")
  print("**********************")
  print("1. Show List")
  print("2. Add task")
  print("3. Remove task")
  print("4. Mark task complete")
  print("5. Clear list")
  print("6. Exit")
  print("**********************\n")
  choice = input("Enter your choice (1-4): ")
  
  if choice == "1":
    showList()
  elif choice == "2":
    add()
  elif choice == "3":
    remove()
  elif choice == "4":
    complete()
  elif choice == "5":
    deleteList()
  elif choice == "6":
    print("\nThanks for using Listify! Enjoy your day.")
    isRunning = False
  else:
    print("Invalid choice! Choose and option from list. \n")
    
    
  
