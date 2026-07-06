class Team:
    def __init__(self,members):
        self.members=members

    def __contains__(self,name):
        return name in self.members

obj=Team(["Avantika","Rahul","Priya"])

print("Rahul" in obj)
print("Riya" in obj)