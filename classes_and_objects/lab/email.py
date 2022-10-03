class Email:
    def __init__(self, sender, recipient, subject):
        self.is_sent = False
        self.sender = sender
        self.recipient = recipient
        self.subject = subject

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.recipient}: {self.subject}. " \
               f"Sent: {self.is_sent}"


emails = []
information = input()

while information != "Stop":
    sender, *info = [int(x) if x.isdigit() else x for x in information.split()]
    email = Email(sender, info[0], info[1])
    emails.append(email)
    information = input()

# send_mails = list(map(int, input().split(', ')))
# for x in send_mails:
#     emails[x].send()
send_mails = [emails[int(x)].send() for x in input().split(", ")]

for email in emails:
    print(email.get_info())