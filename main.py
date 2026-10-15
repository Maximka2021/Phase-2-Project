from application_manager import add_application
from application_manager import view_applications
from application_manager import search_applications
from application_manager import update_application_status
from application_manager import delete_application
from application_manager import show_stats
from storage import load_applications

def main():
    applications = load_applications()
    while True:
        show_menu()
        try:
            user_input = int(input("Enter a corresponding number =>"))
        except ValueError:
            print("Error: Invalid Input")
        else:
            if user_input == 1:
                add_application(applications)
            elif user_input == 2:
                view_applications(applications)
            elif user_input == 3:
                search_applications(applications)
            elif user_input == 4:
                update_application_status(applications)
            elif user_input == 5:
                delete_application(applications)
            elif user_input == 6:
                show_stats(applications)
            elif user_input == 7:
                break
            else:
                print(f"{user_input} is Invalid")


def show_menu():
    print("1. Add application")
    print("2. View applications")
    print("3. Search applications")
    print("4. Update application status")
    print("5. Delete application")
    print("6. Show statistics")
    print("7. Exit")


if __name__ == "__main__":
    main()
