from copy import copy
from random import shuffle


def generate_assignments(previous_assignments, coders):
    shuffled_coders = copy(coders)
    while True:
        shuffle(shuffled_coders)
        new_assignments = {}
        for i in range(len(coders)):
            new_assignments[coders[i]] = shuffled_coders[i]
        if are_assignments_correct(previous_assignments, new_assignments):
            return new_assignments


def are_assignments_correct(previous_assignments, new_assignments):
    for coder in new_assignments:
        # nie można być swoim własnym recenzentem
        if coder == new_assignments[coder]:
            return False
        # nie można recenzować dwa razy z rzędu tej samej osoby
        if new_assignments[coder] == previous_assignments[coder]:
            return False
        # nie można być recenzentem swojego recenzenta
        if new_assignments[coder] == new_assignments[new_assignments[coder]]:
            return False
    return True


coders = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
previous_assignments = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G', 'G': 'H', 'H': 'I', 'I': 'J', 'J': 'A'}
new_assignments = generate_assignments(previous_assignments, coders)
print(new_assignments)
new_assignments2 = generate_assignments(new_assignments, coders)
print(new_assignments2)
