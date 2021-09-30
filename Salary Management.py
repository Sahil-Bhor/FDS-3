name = input("Enter employee name : ")
desig = input("Designation of the employee : ")
month = input("Enter the month : ")
workd = int(input("Total no of days worked : "))
over_time = int(input("Overtime Days : "))
over_time /= 2

dict = {"Manager":2000, "Leader":1800, "Member":1500}
mm = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30,
      "July":31, "August":30, "September":31, "October":30, "November":31,"December":30}

while True:
  if workd <= mm[month]:
    if desig in dict:
      print("\n--------------***********-----------------\n")
      print(f"Name is : {name} \nDesignation is : {desig} \nTotal salary : {(workd + over_time) * dict[desig] } ")
      print("\n--------------***********------------------\n")
      break

  else:
    print("Something went wrong :(")
    break