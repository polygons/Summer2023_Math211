test = {   'name': 'q3_1_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> type(event_result) in '
                                               'set([np.ndarray])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Your list should have 5 '
                                               'elements.;\n'
                                               '>>> len(event_result) == 5\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Every element of your '
                                               'list should be a string.;\n'
                                               '>>> [type(i) in set([np.str_, '
                                               'str]) for i in event_result] \n'
                                               '[True, True, True, True, True]',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> event_result == '
                                               "make_array('E', 'L', 'L', 'S', "
                                               "'N')\n"
                                               'array([ True,  True,  True,  '
                                               'True,  True], dtype=bool)',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
