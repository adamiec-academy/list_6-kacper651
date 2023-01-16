import pytest
from test_data import GENERATE_ASSIGNMENTS_DATA, GET_SEATS_DATA, PLAY_DATA


def _data_args(data, with_er=True):
    if not data:
        return
    size = len(data[0])
    names = []
    for entry in data:
        name = []
        adj_size = size - 1 if with_er else size
        for arg in range(adj_size):
            name.append(str(entry[arg]))
        names.append(", ".join(name))
    return names


class ValidationException(Exception):
    pass


def check_if_all_coders_have_reviewer(coders, new_assignments):
    if sorted(coders) != sorted(list(new_assignments.keys())):
        raise ValidationException("Not all reviewers assigned!")


def check_if_anyone_is_self_reviewing(new_assignments):
    for reviewed in new_assignments.keys():
        if reviewed == new_assignments[reviewed]:
            raise ValidationException("Self review!")


def check_for_symmetric_reviewing(new_assignments):
    for reviewed in new_assignments.keys():
        if new_assignments[new_assignments[reviewed]] == reviewed:
            raise ValidationException("Symmetric review!")


def check_for_subsequent_reviewing(previous_assignments, new_assignments):
    for reviewed in new_assignments:
        if reviewed in previous_assignments and new_assignments[reviewed] == previous_assignments[reviewed]:
            raise ValidationException("Subsequent review!")


def validate_assignments(previous_assignments, coders, new_assignments):
    check_if_all_coders_have_reviewer(coders, new_assignments)
    check_if_anyone_is_self_reviewing(new_assignments)
    check_for_symmetric_reviewing(new_assignments)
    check_for_subsequent_reviewing(previous_assignments, new_assignments)


@pytest.mark.parametrize("previous_assignments, coders", GENERATE_ASSIGNMENTS_DATA, ids=_data_args(GENERATE_ASSIGNMENTS_DATA, with_er=False))
def test_task_1_generate_assignments(previous_assignments, coders):
    from task_1 import generate_assignments
    
    for _ in range(100):
        new_assignments = generate_assignments(previous_assignments, coders)
        validate_assignments(previous_assignments, coders, new_assignments)


@pytest.mark.parametrize("seats_number, votes_data, expected_output", GET_SEATS_DATA, ids=_data_args(GET_SEATS_DATA))
def test_task_2_get_seats(seats_number, votes_data, expected_output):
    from task_2 import get_seats
    actual_output = get_seats(seats_number, votes_data)
    assert actual_output == expected_output


@pytest.mark.parametrize("starting_board, turns, expected_output", PLAY_DATA, ids=_data_args(PLAY_DATA))
def test_task_3_play(starting_board, turns, expected_output):
    from task_3 import play
    actual_output = play(starting_board, turns)
    assert actual_output == expected_output
