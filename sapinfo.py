class Student:

    def __init__(self, name, asset, reference, building, floor, manager):

        self.name = name

        self.asset = asset

        self.reference = reference

        self.building = building

        self.floor = floor

        self.manager = manager

 

    def display(self):

        print(f"Name: {self.name}")

        print(f"Asset Tag Number: {self.asset}")

        print(f"Reference Number: {self.reference}")

        print(f"Building: {self.building}")

        print(f"Floor: {self.floor}")

        if self.manager:

            print(f"Manager: {self.manager}")

        print()

 

def get_student_input():

    name = input("What is the name? ")

    asset = input("What is the asset tag number? ")

    reference = input("What is the ticket number? ")

    building = input("Which building? ")

    floor = input("Which floor / office? ")

   

    is_new_student = input("Are they a new student? Enter 1 for yes, 0 for no: ").strip() == '1'

    manager = input("Paste ex-1: ") if is_new_student else ''

   

    return Student(name, asset, reference, building, floor, manager)

 

def main():

    people = []

    ongoing = True

 

    print("SAP INFORMATION CREATOR")

 

    while (ongoing):

        print("Do you have an asset to change on SAP?")

        answer = str(input("Enter y for yes or n for no: "))

 

        if (answer == 'y'):        

            people.append(get_student_input())

 

        if (answer == 'n'):

            ongoing = False

            print("*******************************************************************************")

            print("SAP INFORMATION - Copy Paste Results and Send")

 

            for person in people:

                Student.display(person)

 

if __name__ == "__main__":

    main()