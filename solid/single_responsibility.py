class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # # Breaks the rule
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # # Breaks the rule
    # def load(self, filename):
    #     pass
    #
    # # Breaks the rule
    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('One')
j.add_entry('Two')
print(f'Journal entries:\n{j}')

file = r'journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())
