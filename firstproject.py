import csv
def make_file(info):
  with open('student_information.csv','a',newline='') as csv_file:
    sample=csv.writer(info)
    if csv.tell()==0:
      sample.writerow(["Name", "Age", "Contact Number", "Mail-ID"])
    
    sample.writerow(info)

if __name__=='__main__':
  no_of_students=0
  condition=True
  while(condition):
    print("Hello MyCaptain")
    student_info=input("Enter the student details in the order(name age phone_number mail_ID): ")

  
    split= student_info.split(' ')
    print("the entered info is\n",str(split))
    
    choice=print("If the information shown is correct then enter yes else enter no: ")
    if choice=='yes':
      no_of_students+=1
      make_file(split)

      condn=print("Enter yes if you want to store another student's info or just type no: ")
      if(condn=='yes'):
        condition=True
      elif(condn=='no'):
        condition=False
        print("Number of entries={}".format(no_of_students))

    elif(choice=='no'):
      condition=True 
