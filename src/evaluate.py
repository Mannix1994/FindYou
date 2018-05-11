# -*- coding: utf-8 -*-


# 评估这个人是她的可能性有多大
def evaluate(info, her_info):
    probability = 0

    # gender
    if info['gender'] == her_info['gender']:
        probability += 1
    else:
        return 0

    # address
    address = info['address']
    match_address = False
    for ad in her_info['address']:
        if address == ad:
            probability += 1
            match_address = True
            break
    # no address match
    if not match_address:
        return 0

    # follow number and fans number
    if int(info['followNumber']) < her_info['follow_max'] \
            and int(info['fansNumber']) < her_info['fans_max']:
        probability += 1

    if int(info['followNumber']) > her_info['follow_min'] \
            and int(info['fansNumber']) > her_info['fans_min']:
        probability += 1

    # name
    name = info['name']
    for a_key_word in her_info['name_key_words']:
        if name.find(a_key_word) > -1:
            probability += 1

    return probability
