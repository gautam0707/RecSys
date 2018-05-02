"""
helpers for user actions and corresponding action strengths association
"""


def event_strength_dict_from_list(actions, strengths):
    """
    returns a dictionary based on user actions and corresponding action strengths
    :param actions: user actions e.g. LIKE, SHARE, COMMENT etc
    :param strengths: corresponding action strengths e.g. 1,2,-1 etc
    :return: dictionary representing user actions and corresponding action strengths
    """
    assert len(actions) == len(strengths) and actions
    assert all([float(x) for x in strengths])
    return dict(zip(actions, strengths))
