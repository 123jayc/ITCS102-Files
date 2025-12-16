import os
import json

os.system('cls')
print("======================================")
print("===== STUDENT INFORMATION SYSTEM =====")
print("======================================\n")

student_record = {}

while True:
    print("===== OPTIONS =====")
    print("A = Add student record.")
    print("B = Print all student record.")
    print("C = Search student record.")
    print("D = Delete student record.")
    print("E = Edit student record.")
    print("F = Export student record.")
    print("G = Exit.")
    print("====================\n")
    
    choice = input('SELECT FROM THE OPTION ABOVE: ').lower()
    
    if choice == 'a':
        os.system('cls')
        print("\n=== ADDING STUDENT RECORD ===\n")
        id_no = input('Student ID: ').upper()
        first_name = input('First Name: ').upper()
        last_name = input('Last Name: ').upper()
        age = eval(input('Age: '))
        course = input('Course: ').upper()
        section = input('Section: ').upper()
        
        student_record[id_no] = [first_name, last_name, age, course, section]
        print("\n======== DATA SAVED ========\n")
        continue

    elif choice == 'b':
        os.system('cls')
        print("===== STUDENT RECORD =====")
        for id_key, info in student_record.items():
            print(f"CODE - {id_key}, INFORMATION - {info}")
        print("==========================\n")
        continue

    elif choice == 'c':
        os.system('cls')
        print("=== SEARCH STUDENT RECORD ===")
        search_id = input('STUDENT ID NO: ').upper()
        
        if search_id in student_record:
            print("=====RECORD FOUND=====")
            print(f'RECORD FOR: {search_id}')
            # Print details nicely like the second code
            details = student_record[search_id]
            print(f"- Name: {details[0]} {details[1]}")
            print(f"- Age: {details[2]}")
            print(f"- Course: {details[3]}")
            print(f"- Section: {details[4]}")
            print("======================")
        else:
            print("NO RECORD FOUND")
        continue

    elif choice == 'd':
        os.system('cls')
        print("=== DELETE STUDENT RECORD ===")
        delete_id = input('STUDENT ID NO: ').upper()
        
        if delete_id in student_record:
            print("=====RECORD FOUND=====")
            print(f'RECORD FOR: {delete_id}')
            print(f'Info: {student_record[delete_id]}')
            print("======================")
            
            confirm = input("CONFIRM DELETE (Y/N): ").lower()
            if confirm == 'y':
                del student_record[delete_id]
                print("RECORD DELETED")
            elif confirm == 'n':
                print("NOT DELETED")
            else:
                print("Invalid Option")
        else:
            print("NO RECORD FOUND")
        continue

    elif choice == 'e':
        os.system('cls')
        print("=== EDIT STUDENT RECORD ===")
        edit_id = input('STUDENT ID NO: ').upper()
        
        if edit_id in student_record:
            print("=====RECORD FOUND=====")
            print(f'Current Info: {student_record[edit_id]}')
            print("======================")
            
            print("ENTER NEW DETAILS:")

            current = student_record[edit_id]
            
            fn = input(f"First Name ({current[0]}): ").upper() or current[0]
            ln = input(f"Last Name ({current[1]}): ").upper() or current[1]
            
            new_age_input = input(f"Age ({current[2]}): ")
            age = eval(new_age_input) if new_age_input else current[2]
            
            course = input(f"Course ({current[3]}): ").upper() or current[3]
            section = input(f"Section ({current[4]}): ").upper() or current[4]
            
            student_record[edit_id] = [fn, ln, age, course, section]
            print("\nDATA IS NOW UPDATED")
        else:
            print("NO RECORD FOUND")
        continue

    elif choice == 'f':
        os.system('cls')
        print("===== EXPORT RECORD =====")
        with open('student_records.json', 'w') as file:
            json.dump(student_record, file, indent=4)
        print("Data exported to 'student_records.json' successfully.")
        continue

    # G - EXIT SYSTEM
    elif choice == 'g':
        print("SYSTEM EXIT")
        break
    
    else:
        print("Invalid Choice")