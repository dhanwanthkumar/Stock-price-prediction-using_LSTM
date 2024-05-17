def find_intersections(data, sma):
    signals = []
    for i in range(1, len(data)):
        if data[i-1] < sma[i-1] and data[i] > sma[i]:
            signals.append((i, 'buy'))
        elif data[i-1] > sma[i-1] and data[i] < sma[i]:
            signals.append((i, 'sell'))
    return signals