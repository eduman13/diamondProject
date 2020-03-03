def dropColumns(df):
    df.drop(columns=["table", "y", "z", "depth"], inplace=True)
    return df

def categoricalToNumber(df):
    pass

def cutToNumber(cut):
    if cut == "Ideal":
        cut = 5
    if cut == "Premium":
        cut = 4
    if cut == "Very Good":
        cut = 3
    if cut == "Good":
        cut = 2
    if cut == "Fair":
        cut = 1
    return cut

def colorToNumber(color):
    if color == "G":
        color = 4
    if color == "E":
        color = 6
    if color == "F":
        color = 5
    if color == "H":
        color = 3
    if color == "D":
        color = 7
    if color == "I":
        color = 2
    if color == "J":
        color = 1
    return color

def clarityToNumber(clarity):
    if clarity == "SI1":
        clarity = 3
    if clarity == "VS2":
        clarity = 4
    if clarity == "SI2":
        clarity = 2
    if clarity == "VS1":
        clarity = 5
    if clarity == "VVS2":
        clarity = 6
    if clarity == "VVS1":
        clarity = 7
    if clarity == "IF":
        clarity = 8
    if clarity == "I1":
        clarity = 1
    return clarity