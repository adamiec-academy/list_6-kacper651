def get_seats(seats_number, votes_data):
    votes_sum = sum(votes_data.values())
    mandates = {}
    party_quotients = {}

    for party in votes_data.keys():
        mandates[party] = 0
        if votes_data[party] < votes_sum * 0.05:
            continue
        elif 'Mniejszość' in party.lower() and votes_data[party] < votes_sum * 0.08:
            continue
        else:
            temp = []
            for i in range(seats_number + 1):
                temp.append(int(votes_data[party] / (i + 1)))
            party_quotients[party] = temp

    for _ in range(seats_number):
        max_quotient = 0
        max_party = ''
        for party in party_quotients.keys():
            quotients_list = party_quotients[party]
            if len(quotients_list) == 0:
                continue
            if quotients_list[0] > max_quotient:
                max_quotient = quotients_list[0]
                max_party = party
        mandates[max_party] += 1
        party_quotients[max_party].pop(0)

    return mandates
