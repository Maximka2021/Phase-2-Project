import json

def save_applications(applications):
    with open("applications.json", "w", encoding="utf-8") as file:
        json.dump(applications, file, indent=4)


def load_applications():
    try:
        with open("applications.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
       print("No saved applications found")
       return []
    except json.JSONDecodeError:
        print("Application file contains invalid JSON")
        return []

