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
    applictions.append(user_info)
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
    while True:
        search_input = input("Search (by company name) => ").lower().strip()
        
        if not search_input:
            print("Search cannont be blank")
        else:
            break
    for application in applications:
        if search_input == application["company"].lower():
            found = True
            print(f"{application['company']}")
            print(f"Position: {application['position']}")
            print(f"Date: {application['date']}")
            print(f"Status: {application['status']}")
            print()
    if not found:
        print("Nothing was found")

    return found

def update_application_status(applications):
    statuses = {"Applied", "Interview", "Rejected", "Offer"}

    if not  search_applications(applications):
        return
    while True:
        new_status_input = input("Enter a new status (Applied, Interview, Rejected, Offer)").strip().title()
        if not new_status_input:
            print("Field cannot be blank")
        elif new_status_input not in statuses:
            print("Invalid status type e.g (Applied, Interview, Rejected, Offer)")
        else:
            break
    
    print("Status success")

