def minWindow(s, t):
    windowStart = 0
    windowEnd = 0
    windowSize = len(s)
    maxSize = 100000
    new_string = ""
    d = dict()

    for i in t:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    count = len(d)
    while windowEnd < windowSize:
        charString = s[windowEnd]
        if charString in d:
            d[charString] -= 1
            if d[charString] == 0:
                count -= 1

        if count != 0:
            windowEnd += 1

        elif count == 0:
            while count == 0:
                chString = s[windowStart]
                if chString in d:
                    d[chString] += 1
                    if d[chString] == 1:
                        count += 1
                size = windowEnd - windowStart + 1
                if size < maxSize:
                    maxSize = size
                    new_string = s[windowStart:windowEnd + 1]
                windowStart += 1
            windowEnd += 1
    return new_string
