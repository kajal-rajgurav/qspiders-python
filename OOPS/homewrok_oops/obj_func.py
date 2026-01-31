class student:
    def __init__(self,name,roll_no,address):
        self.name=name
        self.roll_no=roll_no
        self.address=address
    def display(self):
        print("name:-",self.name)
        print("roll_no:-",self.roll_no)
        print("address:-",self.address)
##objects##
stud1=student("kajal",23,"andheri")
stud2=student("vidya",24,"malad")
stud1.display()
stud2.display()

    