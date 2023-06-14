def histogram(s):
    hist = {}
    for ch in s:
        hist[ch] = hist.get(ch, 0) + 1
    return hist

def print_hist(hist):
    keys = sorted(hist.keys())
    for key in keys:
        print(key, hist[key])

# Example usage
data = (str(input("Enter a string"))).replace(" ","")
hist = histogram(data)
print_hist(hist)

