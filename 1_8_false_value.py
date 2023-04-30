# 1.8 False values

q = [float('nan'), 0.0, 0, [], 'False',
     None, (), """""", True, [None, None], 0j, {}, set()]

for x in q:
    if not x:
        print('+')
    else:
        print('–')
