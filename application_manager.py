from storage import save_applications, load_applications

def add_application(applictions):
    while True:
        input_company = input("Enter your company => ").strip()
        if not input_company:
            print("Company cannot be blank")
        else:
            break
    while True:
        input_position = input("Enter your position => ").strip()
        if not input_position:
            print("Position cannot be empty")
        else:
            break    
    while True:
        input_date = input("Enter application date (YYYY-MM-DD) => ").strip()
        if not input_date:
            print("Date cannot be empty")
        else:
            break

    user_info = {"company": input_company, "position":input_position, "date":input_date, "status":"Applied"}
    save_applications(applictions.append(user_info))
    print("Application was added successfully")
    


def view_applications(applications):
    if not applications:
        print("No applications found")
    else:
        for index, application in enumerate(applications, start=1):
            print(f"{index}. {application['company']}")
            print(f"Position: {application['position']}")
            print(f"Date: {application['date']}")
            print(f"Status: {application['status']}")
            print()

        
def search_applications(applications):
    found = False
    founded_applications = []
    while True:
        search_input = input("Search (by company name) => ").lower().strip()
        
        if not search_input:
            print("Search cannont be blank")
        else:
            break
    for application in applications:
        if search_input == application["company"].lower():
            found = True
            founded_applications.append(application)
            print(f"{application['company']}")
            print(f"Position: {application['position']}")
            print(f"Date: {application['date']}")
            print(f"Status: {application['status']}")
            print()

    if not found:
        print("Nothing was found")

    return found, founded_applications

def update_application_status(applications):
    statuses = {"Applied", "Interview", "Rejected", "Offer"}

    is_founded, founded_applications = search_applications(applications)

    if not is_founded:
        return
    
    application_to_update = choose_application(founded_applications)

    while True:
        new_status_input = input("Enter a new status (Applied, Interview, Rejected, Offer)").strip().title()
        if not new_status_input:
            print("Field cannot be blank")
        elif new_status_input not in statuses:
            print("Invalid status type e.g (Applied, Interview, Rejected, Offer)")
        else:
            break

    application_to_update["status"] = new_status_input
    print(application_to_update)
    save_applications(applications)
    print("Status was updates succuessfully")
    

def choose_application(founded_applications):

    if len(founded_applications) == 1:
        application_to_update = founded_applications[0]
        return application_to_update

    for index, application in enumerate(founded_applications, start = 1):
        print(f"{index}. {application}")

    while True:
        try:
            user_input = int(input("Choose application by entering a corresponding number => "))
            if user_input < 1 or user_input > len(founded_applications):
                print("No such number")
                continue
            application_to_update = founded_applications[user_input-1]
        except ValueError:
            print("Invalid Input")
        except IndexError:
            print("No such number")
        else:
            return application_to_update
        

def delete_application(applications):
   is_found, founded_applications = search_applications(applications)

   if not is_found:
       return
   
   application_to_delete = choose_application(founded_applications)
   
   save_applications(applications.remove(application_to_delete))

def show_stats(applications):
    total = len(applications)
    interview = 0
    offer = 0
    rejected = 0
    applied = 0
    
    for application in applications:

        if application["status"] == "Offer":
            offer += 1
        elif application["status"] == "Interview":
            interview += 1
        elif application["status"] == "Rejected":
            rejected += 1
        elif application["status"] == "Applied":
            applied += 1

    print("Stats:")
    print(f"Total: {total}")
    print(f"Applied: {applied}")
    print(f"Interview: {interview}")
    print(f"Rejected: {rejected}")
    print(f"Offer: {offer}")





    
        



