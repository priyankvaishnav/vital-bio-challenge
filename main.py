import csv
import random


class SecretSanta:
    def __init__(self):
        self.info = {}
        self.selection = {}

    def assign_gift(self):
        """Assign gifts to participants."""
        choices = list(self.info.keys())

        """ Handle the case where there's only one participant"""
        if len(choices) == 1:
            print("Only one participant. Secret Santa can't proceed.")
            return

        for person in self.info:
            receiver = random.choice(choices)
            while receiver == person or receiver in self.selection.values():
                receiver = random.choice(choices)
                # If only one choice is left and it's the same as the current person
                if len(choices) == 1 and receiver == person:
                    # Swap the last person's receiver with the current person
                    last_person = list(self.selection.keys())[-1]
                    self.selection[person] = self.selection[last_person]
                    self.selection[last_person] = receiver
                    break
            else:
                self.selection[person] = receiver
                choices.remove(receiver)
            print("Notifying {} that they are assigned to get a gift for {}".format(self.info[person], receiver))

    def file_reader(self):
        """Read participants from the CSV file."""
        file_path = "resources/participants.csv"
        with open(file_path, mode='r', encoding="utf8") as file:
            csv_dict_reader = csv.DictReader(file)
            for row in csv_dict_reader:
                self.info[row['name']] = row['email']

    def start(self):
        """Start the Secret Santa process."""
        self.file_reader()
        self.assign_gift()


def main():
    print("Secret gift generator")
    secret_santa = SecretSanta()
    secret_santa.start()


if __name__ == "__main__":
    main()
