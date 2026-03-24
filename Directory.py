# Use function 
def Display_menu():
    # this will show all items on the terminal 
    print("\n**** Secure Contact Directory **** ")
    print("2.*** Add Items ***")
    print("3. *** Update Items *** ")
    print("4. *** Search Items *** ")
    print("5. *** Display Items *** ") 
    print("6. *** Exit *** ") 
    print("-----------------------------")
def add_items(directory):
    # this function is used for adding information 
    name=input("Enter The Name : ")
    if name in directory:
        # it will check if name is alread occur in information then it will show print message 
        print("Error. This is already exists in directory :-")
    else:
        phone=input("Enter the Phone Number *** ")
        email=input("Enter the Email *** ")
        # Use of Tuple occur here 
        directory[name]=(phone,email)
        print(f"Contact {name} added successfully *** ")
def Updated_items(directory):
    #contact update karne k liye function

    name=input("Enter the Name : ")
    if name in directory:
        print(f"Current Info , Phone : {directory[name][0]}, Email : {directory[name][1]}")
        new_phone=input("Enter new Phone number : ")
        new_email=input("Enter new Email : ")
        directory[name]=(new_phone, new_email)
        print("Contact Updated Successfully")
    else:
        print("Contact not found")
def search_contact(directory):
    # searching algorithm 
    name=input("*** Enter the name for search *** ")
    if name in directory:
        detail=directory[name]
        print(f"\n *** Result *** ")
        print(f"Name : ",{name})
        print(f"Phone : ", {detail[0]})
        print(f"Email : ", {detail[1]})
    else:
        print("No contact found ")
def show_items(directory):
    # for showing all contacts 
    if not directory:
        print("*** : Directory Empty : *** ")
    else:
        print("\n All Contacts ")
        for name,info in directory.items():
            print(f"Name : {name} | Phone: {info[0]} | Email: {info[1]}")
def main():
    # Database as a dictionary 
    contact_db={}
    while True:
        Display_menu()
        choice=input("Enter your choice here (1-5)")
        if choice=="1":
            add_items(contact_db)
        elif choice=="2":
            Updated_items(contact_db)
        elif choice=="3":
            search_contact(contact_db)
        elif choice=="4":
            show_items(contact_db)
        elif choice=="5":
            print("*** Existing Security Directory Closed *** ")
            break
        else:
            print("Invalid Number : ")

# this is program entry point 
if __name__=="__main__":
    main()