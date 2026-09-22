class Employee:

    def work(self):
        return "writing code"

class manager(Employee):
    def work(self):
        return f"` and attending meetings"


if __name__ == "__main__":
    mgr = manager()
    print(mgr.work())