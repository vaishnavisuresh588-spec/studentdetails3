import sys
if len(sys.argv) == 3:
  script name = sys.argv[0]
  name = sys.argv[1]
  rollno = sys.argv[2]
   print("user provided input values:")
else:
  script name = sys.argv[0]
  name = "vaishnavi"
  rollno = "14"
   print("no input given - using default values:")
print("Script name:", script name)
print("Student name:", name)
print("Roll no:", rollno)
  
  
  
