
def show_contacts(data):
    return "\n".join(str(i) for i in data)

mylist = [1, 2, 3]

print(show_contacts(mylist))

class PhoneBook:
    def __init__(self, content):
        self.content = content

    def show_contacts(self) -> str:
        return "\n".join(str(i) for i in self.content)

if __name__ == "__main__":
    pb = PhoneBook
    mylist = [1, 2, 3]
    print(pb.show_contacts(mylist))