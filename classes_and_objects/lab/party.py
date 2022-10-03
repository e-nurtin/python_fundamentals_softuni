# class Party:
#     def __init__(self):
#         self.people = []
#
#
# invited = Party()
# command = input()
# while command != "End":
#     invited.people.append(command)
#     command = input()


class Person:
    def __init__(self, person):
        self.person = person


class Party:
    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def name_of_guests(self):
        return ', '.join(self.people)

    def guest_count(self):
        return len(self.people)


party = Party()
command = input()
while command != "End":
    name = command
    person = Person(name)
    party.invite(name)
    command = input()

print(f"Going: {party.name_of_guests()}")
print(f"Total: {party.guest_count()}")
