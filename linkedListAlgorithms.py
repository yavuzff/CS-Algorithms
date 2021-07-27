#Using linked lists with example of employee information

def outputDetails(): #function to output the details of the employees
    global employee, firstEmployee
    #global values used as we want to change the value of the original variables

    currentPointer = firstEmployee #the temporary pointer is set to the first employee
    if employee[currentPointer][0] == "": #if the first element is empty
        print("There are no employees.")
        return #leave function
    
    while currentPointer != None: #loop until null pointer is reached
        empData = employee[currentPointer] #the employee data is output
        print("Name: " + empData[0]+"\nEmail: " + empData[1] + "\nWork Location: " + empData[2]+'\n')
        currentPointer = empData[3] #the pointer is updated to next pointer


def insertEmployee(): #function to insert a new employee to the linked list
    global employee, firstEmployee
    newName = input("Enter Name: ") #info of the new employee is input
    newEmail = input("Enter Email: ")
    newWork = input("Enter Work Location: ")

    size = len(employee) #the maximum number of employees
    index = '' #the index of the next free spot in the list
    i = 0 #counter to check if end of list is reached

    while index == '' and i < size:
        #loops until an empty element is found or the whole list is traversed
        
        if employee[i][0] == '': #if the next element is free
            index = i #the index is set to this value
        else:
            i += 1

    if index == "": #if there are no free spaces/no free index
        print("There is no space left in the array.")
        return None
    
    if employee[firstEmployee][0] == '': # if the list is fully empty
        firstEmployee = index 
        employee[index][0],employee[index][1],employee[index][2] = newName, newEmail, newWork
        #the employee information is stored at this index and function is exit
        return
    
    employee[index][0],employee[index][1],employee[index][2] = newName, newEmail, newWork
    #the employee information are stored in the found index

    #adjusting pointers
    if employee[firstEmployee][0] > newName: #if the new element is less than the first element
        employee[index][3] = firstEmployee
        firstEmployee = index #new element is set to being first employee
    else:
        currentPointer = firstEmployee
        nextPointer = employee[firstEmployee][3] #temporary pointers used
        
        while employee[currentPointer][0] <= newName: #loops until the new name is greater than an index
            previousPointer = currentPointer #pointers adjusted
            currentPointer = employee[currentPointer][3]
            if currentPointer == None: #if a null pointer is reached, exit
                break

        employee[index][3] = currentPointer #pointers updated to point to next element in list
        employee[previousPointer][3] = index

    
def deleteEmployee(): #function to delete an employee
    global firstEmployee, employee
    
    target = input("Enter name of the employee to be deleted: ") #target employee input
    currentEmployee = firstEmployee
    deleted = False #variable used to check if employee is deleted

    if employee[firstEmployee][0] == target: #if the target is first element
        employee[firstEmployee][0] = '' #it is removed
        if employee[firstEmployee][3] != None: #its pointer is adjusted if needed
            firstEmployee = employee[firstEmployee][3]
            return 
        
    while not deleted and currentEmployee != None:
        #loops until element is deleted or end of list is reached
        
        nextEmployee = employee[currentEmployee][3] #temporary pointer used
        if nextEmployee == None: #if a null pointer, end of list is reached
            print(target,'was already not in the list.')
            return
        
        if employee[nextEmployee][0] == target: #if target is found
            employee[currentEmployee][3] = employee[nextEmployee][3]
            employee[nextEmployee][0] = '' #element is deleted and pointers updated
            deleted = True
        currentEmployee = nextEmployee #temp pointer updated to point to next element

def outputLocation(): #function to output every employee at a given work location
    targetLocation = input("Enter the desired work location: ")
    output = False #variable used to see if any employee is output
    
    currentPointer = firstEmployee #temporray pointer used
    if employee[currentPointer][0] == "": #if the list is empty, error message is shown
        print ("There are no employees working at this location.")
        return
    
    while currentPointer != None: #loops until end of list is reached
        empData = employee[currentPointer]
        if empData[2] == targetLocation: #if employee works at given work location
            output = True #variable set to true and info is output
            print("Name: " + empData[0]+"\nEmail: " + empData[1] +'\n')
        currentPointer = empData[3] #temporary pointer updated to point to next in list

    if not output: #if no elements were output, error message shown
        print ("There are no employees working at this location.")
        
arraySize = 11 #defines the size of the array i.e. the maximum number of employees 
employee = [['','','',None] for i in range (0,arraySize)] #creates a 2d array of size arraySize
firstEmployee = 0 #firstEmployee pointer initialised

#for pre-input arrays:
#employee = [['Sam','samemail','homes',None],['Bert','bertemail','berth',2],['Oona','oonaemail','home',0],['','','',None],['','','',None]]

#updating the firstEmployee pointer:
minimum = None #minimum value is stored
for i in range (0,len(employee)): #loops for each element in the array
    name = employee[i][0]
    if name != '' and (minimum == None or name<minimum):
        #if the name is not empty and it is smaller than current min name
        firstEmployee = i #the firstEmployee pointer and minimum value is updated
        minimum = name
