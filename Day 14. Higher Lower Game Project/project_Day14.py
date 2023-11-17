countries = {
    'China': 1444216107,
    'India': 1393409038,
    'United States': 332915073,
    'Indonesia': 276361783,
    'Pakistan': 225199937,
    'Brazil': 213993437,
    'Nigeria': 211400708,
    'Bangladesh': 166303498,
    'Russia': 145912025,
    'Mexico': 130262216,
    'Japan': 126050804,
    'Ethiopia': 120675821,
    'Philippines': 113266317,
    'Egypt': 104258327,
    'Vietnam': 97490013,
    'DR Congo': 92043735,
    'Turkey': 85042716,
    'Iran': 84828907,
    'Germany': 83900473,
    'Thailand': 69950879,
    'United Kingdom': 68207116,
    'France': 65341916,
    'Italy': 60367477,
    'South Africa': 60041948,
    'Tanzania': 61697486,
    'Myanmar': 54818011,
    'South Korea': 51269183,
    'Colombia': 51515817,
    'Kenya': 53771296,
    'Spain': 46615331,
    'Argentina': 45605820,
    'Algeria': 44616626,
    'Sudan': 44909353,
    'Ukraine': 41390273,
    'Iraq': 42183989,
    'Afghanistan': 39835428,
    'Poland': 37887768,
    'Canada': 37978558,
    'Morocco': 37124191,
    'Saudi Arabia': 35562237,
    'Uzbekistan': 34777203,
    'Peru': 33465661,
    'Angola': 33745222,
    'Malaysia': 32722438,
    'Mozambique': 31825295,
    'Ghana': 31950144,
    'Yemen': 30707901,
    'Nepal': 30069481,
    'Venezuela': 28746027,
    'Madagascar': 28246733,
    'Cameroon': 28194037,
    'North Korea': 25799163,
    'Australia': 25788230,
    'Taiwan': 23694815,
    'Niger': 25360487,
    'Sri Lanka': 21803000,
    'Burkina Faso': 21399325,
    'Mali': 20250833,
    'Malawi': 19129952,
    'Kazakhstan': 19116115,
    'Syria': 18068418,
    'Chile': 19116201,
    'Romania': 19221932,
    'Guatemala': 18240146,
    'Zambia': 18383955,
    'Ecuador': 18143285,
    'Netherlands': 17134872,
    'Senegal': 16743930,
    'Cambodia': 16718971,
    'Chad': 16913325,
    'Somalia': 16044286,
    'Zimbabwe': 14899771,
    'Guinea': 14030338,
    'Rwanda': 13599405,
    'Benin': 12677298,
    'Burundi': 12282878,
    'Tunisia': 11935131,
    'Bolivia': 11729855,
    'Belgium': 11589623,
    'Haiti': 11518619,
    'Cuba': 11338138,
    'South Sudan': 11466756,
    'Czech Republic': 10737712,
    'Jordan': 10704378,
    'Greece': 10708939,
    'Portugal': 10262822,
    'Azerbaijan': 10213721,
    'Sweden': 10160174,
    'Honduras': 10138832,
    'United Arab Emirates': 10118809,
    'Hungary': 9660351,
    'Tajikistan': 9685986,
    'Belarus': 9468774,
    'Austria': 9047100,
    'Papua New Guinea': 9191045,
    'Serbia': 6865985,
    'Israel': 8872100,
    'Switzerland': 8715172,
    'Togo': 8278737,
    'Sierra Leone': 8103146,
    'Hong Kong': 7482940,
    'Laos': 7377065,
    'Paraguay': 7204569,
    'Bulgaria': 6927288,
    'Lebanon': 6855713,
    'Libya': 6855097,
    'Nicaragua': 6661516,
    'El Salvador': 6670440,
    'Kyrgyzstan': 6626328,
    'Turkmenistan': 6101692,
    'Denmark': 5810752,
    'Singapore': 5694033,
    'Finland': 5540720,
    'Congo': 5518087,
    'Slovakia': 5446771,
    'Norway': 5465992,
    'Oman': 5080064,
    'State of Palestine': 5193160,
    'Costa Rica': 5111239,
    'Liberia': 5100278,
    'Ireland': 4937786,
    'Central African Republic': 4845705,
    'New Zealand': 5100278,
    'Mauritania': 4671324,
    'Panama': 4369033,
    'Kuwait': 4270571,
    'Croatia': 4087843,
    'Moldova': 4054640,
    'Georgia': 3989167,
    'Eritrea': 3546421,
    'Uruguay': 3518552,
    'Bosnia and Herzegovina': 3301000,
    'Mongolia': 3286628,
    'Armenia': 2982342,
    'Jamaica': 2955020,
    'Qatar': 2925228,
    'Albania': 2821977,
    'Lithuania': 2716789,
    'Namibia': 2587809,
    'Gambia': 2416668,
    'Botswana': 2384118,
    'Gabon': 2254126,
    'Lesotho': 2142249,
    'North Macedonia': 2083459,
    'Slovenia': 2078895,
    'Guinea-Bissau': 2068076,
    'Latvia': 1886278,
    'Bahrain': 1769175,
    'Equatorial Guinea': 1449702,
    'Trinidad and Tobago': 1398328,
    'Estonia': 1326535,
    'Timor-Leste': 1343036,
    'Mauritius': 1282697,
    'Cyprus': 1207359,
    'Eswatini': 1179015,
    'Djibouti': 987861,
    'Fiji': 896445,
    'Réunion': 895312,
    'Comoros': 880000,
    'Guyana': 786126,
    'Bhutan': 779666,
    'Solomon Islands': 703996,
    'Montenegro': 621383,
    'Luxembourg': 634730,
    'Suriname': 608459,
    'Cabo Verde': 531239,
    'Maldives': 521326,
    'Guadeloupe': 400124,
    'Brunei': 442400,
    'Malta': 514564,
    'Bahamas': 396913,
    'Martinique': 375554,
    'Iceland': 366149,
    'Belize': 405632,
    'French Guiana': 302229,
}

from random import randint
score = 0
game_over = False

# It's generating an random index (randint), from 0 to the length of the dictionary.
# I was having an issue trying to access the dictionary.keys by its 'index'.
# But I found out that dict hasn't an fixed order, so I converted it to a list.

def random_countries():
    global country1, country2, population1, population2
    
    countries_list = list(countries.keys())
    length = len(countries_list)

    index1 = randint(0, length - 1)
    index2 = randint(0, length - 1)
    if index1 == index2:
        index2 = randint(0, length - 1)

    country1 = countries_list[index1]
    country2 = countries_list[index2]

    population1 = countries[country1]
    population2 = countries[country2]

def game():
    global game_over, score
    random_countries()

    while True:
        guess = input(f"Which one has more population? {country1} or {country2}? type 'a' or 'b': ").lower()
        if guess in ['a', 'b']:
            break
        else:
            print("Invalid input. Enter 'a' or 'b")
    if (guess == 'a' and population1 > population2) or (guess == 'b' and population2 > population1):
            print("That's right!")
            score += 1
    else:
        game_over = True
        print("That's wrong.")
    print(f"Your score: {score}\n")

while not game_over:
    game()
print('Game Over!')