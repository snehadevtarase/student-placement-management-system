import json
import os

students = []
companies = []
placements = []

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"


# ---------------- SAVE DATA ----------------
def save_data():
    with open("students.json", "w") as f:
        json.dump(students, f)

    with open("companies.json", "w") as f:
        json.dump(companies, f)

    with open("placements.json", "w") as f:
        json.dump(placements, f)


# ---------------- LOAD DATA ----------------
def load_data():
    global students, companies, placements

    try:
        if os.path.exists("students.json"):
            with open("students.json", "r") as f:
                students = json.load(f) or []

        if os.path.exists("companies.json"):
            with open("companies.json", "r") as f:
                companies = json.load(f) or []

        if os.path.exists("placements.json"):
            with open("placements.json", "r") as f:
                placements = json.load(f) or []

    except Exception:
        students = []
        companies = []
        placements = []


load_data()


# ---------------- LOGIN ----------------
print("\n===== LOGIN =====")

username = input("Username: ").strip()
password = input("Password: ").strip()

if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
    print("Invalid Username or Password")
    exit()

print("Login Successful!")


# ---------------- MENU ----------------
while True:

    print("\n===== STUDENT PLACEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Company")
    print("4. View Companies")
    print("5. Add Placement")
    print("6. View Placements")
    print("7. Search Student")
    print("8. Update Student")
    print("9. Delete Student")
    print("10. Delete Company")
    print("11. Placement Report")
    print("12. Dashboard")
    print("13. Placement Percentage")
    print("14. Company Report")
    print("15. Export Report")
    print("16. Search Company")
    print("17. Exit")

    choice = input("Enter choice: ").strip()

    # ---------------- ADD STUDENT ----------------
    if choice == "1":

        name = input("Name: ").strip()
        roll = input("Roll No: ").strip()
        course = input("Course: ").strip()

        if name == "" or roll == "" or course == "":
            print("All fields required!")
            continue

        for s in students:
            if s["roll_no"] == roll:
                print("Roll already exists!")
                break
        else:
            students.append({
                "name": name,
                "roll_no": roll,
                "course": course
            })
            save_data()
            print("Student added!")

    # ---------------- VIEW STUDENTS ----------------
    elif choice == "2":

        if not students:
            print("No students found.")
        else:
            for s in students:
                print("\nName:", s["name"])
                print("Roll:", s["roll_no"])
                print("Course:", s["course"])

    # ---------------- ADD COMPANY (NO DUPLICATES FIXED) ----------------
    elif choice == "3":

        cname = input("Company Name: ").strip()
        pos = input("Position: ").strip()

        if cname == "" or pos == "":
            print("All fields required!")
            continue

        for c in companies:
            if c["company_name"].strip().lower() == cname.lower():
                print("Company already exists!")
                break
        else:
            companies.append({
                "company_name": cname,
                "position": pos
            })
            save_data()
            print("Company added!")

    # ---------------- VIEW COMPANIES ----------------
    elif choice == "4":

        if not companies:
            print("No companies found.")
        else:
            for c in companies:
                print("\nCompany:", c["company_name"])
                print("Position:", c["position"])

    # ---------------- ADD PLACEMENT (FIXED DUPLICATE STUDENT ISSUE) ----------------
    elif choice == "5":

        student_name = input("Student Name: ").strip()
        company_name = input("Company Name: ").strip()
        status = input("Status (Selected/Pending/Rejected): ").strip()

        if student_name == "" or company_name == "" or status == "":
            print("All fields required!")
        else:

            already_placed = False

            for p in placements:
                if p["student_name"].strip().lower() == student_name.lower():
                    already_placed = True
                    break

            if already_placed:
                print("This student is already placed!")
            else:
                placements.append({
                    "student_name": student_name,
                    "company_name": company_name,
                    "status": status
                })

                save_data()
                print("Placement added!")

    # ---------------- VIEW PLACEMENTS ----------------
    elif choice == "6":

        if not placements:
            print("No placements found.")
        else:
            for p in placements:
                print("\nStudent:", p["student_name"])
                print("Company:", p["company_name"])
                print("Status:", p["status"])

    # ---------------- SEARCH STUDENT ----------------
    elif choice == "7":

        search = input("Enter Roll No or Name: ").strip()

        for s in students:
            if s["roll_no"] == search or s["name"].lower() == search.lower():
                print("\nFound Student")
                print("Name:", s["name"])
                print("Roll:", s["roll_no"])
                print("Course:", s["course"])
                break
        else:
            print("Student not found")

    # ---------------- UPDATE STUDENT ----------------
    elif choice == "8":

        roll = input("Enter Roll No: ").strip()

        for s in students:
            if s["roll_no"] == roll:
                s["name"] = input("New Name: ").strip()
                s["course"] = input("New Course: ").strip()
                save_data()
                print("Updated!")
                break
        else:
            print("Student not found")
            # ---------------- DELETE STUDENT ----------------
    elif choice == "9":

        roll = input("Enter Roll No: ").strip()

        found = False

        for s in students:
            if s["roll_no"].strip() == roll:
                students.remove(s)
                save_data()
                print("Deleted!")
                found = True
                break

        if not found:
            print("Student not found")

    # ---------------- DELETE COMPANY ----------------
    elif choice == "10":

        name = input("Company Name: ").strip()

        for c in companies:
            if c["company_name"].lower() == name.lower():
                companies.remove(c)
                save_data()
                print("Company deleted!")
                break
        else:
            print("Company not found")

    # ---------------- PLACEMENT REPORT ----------------
    elif choice == "11":

        selected = rejected = pending = 0

        for p in placements:
            status = p["status"].lower()

            if status == "selected":
                selected += 1
            elif status == "rejected":
                rejected += 1
            elif status == "pending":
                pending += 1

        print("\n===== REPORT =====")
        print("Selected:", selected)
        print("Rejected:", rejected)
        print("Pending:", pending)

    # ---------------- DASHBOARD ----------------
    elif choice == "12":

        placed_students = len(placements)

        print("\n===== DASHBOARD =====")
        print("Total Students :", len(students))
        print("Total Companies :", len(companies))
        print("Total Placements :", placed_students)

    # ---------------- PLACEMENT PERCENTAGE ----------------
    elif choice == "13":

        total_students = len(students)

        selected_students = 0

        for p in placements:
            if p["status"].lower() == "selected":
                selected_students += 1

        percentage = (
            (selected_students / total_students) * 100
            if total_students > 0 else 0
        )

        print("\n===== PLACEMENT PERCENTAGE =====")
        print("Total Students :", total_students)
        print("Placed Students :", selected_students)
        print("Percentage :", round(percentage, 2), "%")

    # ---------------- COMPANY REPORT ----------------
    elif choice == "14":

        company_count = {}

        for p in placements:
            company = p["company_name"]

            if company in company_count:
                company_count[company] += 1
            else:
                company_count[company] = 1

        print("\n===== COMPANY REPORT =====")

        if not company_count:
            print("No placements found.")
        else:
            for c, count in company_count.items():
                print(c, ":", count)

    # ---------------- EXPORT REPORT ----------------
    elif choice == "15":

        with open("placement_report.txt", "w") as file:
            file.write("===== REPORT =====\n")
            file.write(f"Students: {len(students)}\n")
            file.write(f"Companies: {len(companies)}\n")
            file.write(f"Placements: {len(placements)}\n")

        print("Report exported!")

    # ---------------- SEARCH COMPANY ----------------
    elif choice == "16":

        name = input("Company Name: ").strip().lower()

        found = False

        for c in companies:
            if c["company_name"].strip().lower() == name:
                print("\nCompany Found")
                print("Name:", c["company_name"])
                print("Position:", c["position"])
                found = True
                break

        if not found:
            print("Company not found")

    # ---------------- EXIT ----------------
    elif choice == "17":

        save_data()
        print("Thank you!")
        break

    else:
        print("Invalid choice")