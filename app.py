import os

DATA_FILE = "data.txt"

def load_tasks():
    """Read tasks from file into a list of dicts."""
    tasks = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 2:
                        tasks.append({"task": parts[0], "done": parts[1] == "1"})
    return tasks

def save_tasks(tasks):
    """Write tasks list back to file."""
    with open(DATA_FILE, "w") as f:
        for t in tasks:
            f.write(f"{t['task']}|{'1' if t['done'] else '0'}\n")

def list_tasks(tasks):
    print("\n📋 Your Tasks:")
    if not tasks:
        print(" (no tasks yet)")
    else:
        for i, t in enumerate(tasks, 1):
            status = "✓ Done" if t["done"] else "⏳ Pending"
            print(f" {i}. {t['task']} [{status}]")

def add_task(tasks):
    new_task = input("➕ Enter new task: ").strip()
    if new_task:
        tasks.append({"task": new_task, "done": False})
        print("✅ Task added!")
    else:
        print("⚠️ Empty task ignored.")

def mark_done(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("✅ Task marked as done!")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ Deleted task: {removed['task']}")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== Personal Tracker ===")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("👋 Goodbye! Your tasks are saved.")
            break
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main()
