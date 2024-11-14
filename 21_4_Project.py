# class User:
#    def set_attrs(self, login, password, name, email, role):
#        self.login = login
#        self.password = password
#        self.name = name
#        self.email = email
#        self.role = role
#
#    def create_task(self, project, description):
#        project.add_task(self, description)
#
# class Team:
#    def init_team(self, name, members=[]):
#        self.name = name
#        self.members = members
#
#    def add_member(self, user):
#        self.members.append(user)
#
#    def show_members(self):
#        print(f'Team {self.name} members:')
#        for i, user in enumerate(self.members):
#            print(f'№{i + 1}, login: {user.login}, name: {user.name}')
#
#    def get_team_size(self):
#        return len(self.members)
#
# user1 = User()
# user1.set_attrs("user1", "password1", "John Doe", "john.doe@example.com", 'TechLead')
#
# user2 = User()
# user2.set_attrs("user2", "password2", "Jane Doe", "jane.doe@example.com", 'Python Developer')
#
# user3 = User()
# user3.set_attrs("user3", "password3", "Bob Smith", "bob.smith@example.com", 'Python Developer')
#
# team = Team()
# team.init_team('my_team')
# team.add_member(user1)
# team.add_member(user2)
#
# print(f'Size of team "{team.name}" : {team.get_team_size()}')
#
# team.show_members()
#
# # Size of team "my_team": 2
# # Team Research Group members:
# # №1, login: JohnD, name: John Doe
# # №2, login: JaneD, name: Jane Doe

class User:
   def set_attrs(self, login, password, name, email, role):
       self.login = login
       self.password = password
       self.name = name
       self.email = email
       self.role = role

   def create_task(self, project, description):
       project.add_task(self, description)

class Team:
   def init_team(self, name, members=[]):
       self.name = name
       self.members = members

   def add_member(self, user):
       self.members.append(user)

   def show_members(self):
       print(f'Team {self.name} members:')
       for i, user in enumerate(self.members):
           print(f'№{i + 1}, login: {user.login}, name: {user.name}')

   def get_team_size(self):
       return len(self.members)

class Task:
   def create_task(self, description):
       self.description = description


class Project:
   def create_project(self, name, team):
       self.name = name
       self.team = team
       self.tasks = []

   def add_task(self, user, description):
       if user in self.team.members:
           task = Task()
           task.create_task(description)
           self.tasks.append(task)
           print(f"Task '{description}' added to project '{self.name}'")
       else:
           print(f"User '{user.name}' is not a member of the team working on project '{self.name}'")


user1 = User()
user1.set_attrs("JohnD", "mloz512qyt", "John Doe", "john.doe@example.com", 'TechLead')

user2 = User()
user2.set_attrs("JaneD", "qw1lbz", "Jane Doe", "jane.doe@example.com", 'Python Developer')

user3 = User()
user3.set_attrs("BobS", "gnsJqw12", "Bob Smith", "bob.smith@example.com", 'Python Developer')

team = Team()
team.init_team("Research Group")
team.add_member(user1)
team.add_member(user2)

team.show_members()

project = Project()
project.create_project("UAV Detectron", team)

user1.create_task(project, "Find best model")
user2.create_task(project, "Setup Environment")
user3.create_task(project, "Optimization")

# Team Research Group members:
# №1, login: JohnD, name: John Doe
# №2, login: JaneD, name: Jane Doe
# Task 'Find best model' added to project 'UAV Detectron'
# Task 'Setup Environment' added to project 'UAV Detectron'
# User 'Bob Smith' is not a member of the team working on project 'UAV Detectron'