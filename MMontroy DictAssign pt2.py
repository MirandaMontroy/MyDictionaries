# create dictionary years
year_team = {}

# create dictionary team count
team_count = {}

# team list
team_list = []

# import file
infile = open("WorldSeriesWinners.txt", "r")

# goes through the lines
for line in infile:
    # strips off the newline
    line1 = line.strip("\n")

    # adds to list for later
    team_list.append(line1)

    # fills the dictionary
    if line1 not in team_count:
        team_count[line1] = 0

    if line1 in team_count:
        team_count[line1] += 1

infile.close()
# print(team_list)


# fill the year team dictionary
year = 1903
numlist = 0
while year < 2009:
    if year in (1904, 1994):
        year_team[year] = "No game was played this year"
        year += 1
    elif year == 2009:
        year_team[year] = team_list[numlist]
        year += 1
    else:
        year_team[year] = team_list[numlist]
        year += 1
        numlist += 1

user_year = int(input("Input a year between 1903 and 2008: "))
print()

if user_year > 2008 or user_year < 1903:
    while user_year > 2008 or user_year < 1903:
        print("Invalid year")
        user_year = int(input("Input a year between 1903 and 2008: "))

if user_year in (1904, 1994):
    print(year_team[user_year])
else:
    print(year_team[user_year], "won the World Series in", user_year)

if user_year not in (1904, 1994):
    print(
        year_team[user_year],
        "have won the World Series",
        team_count[year_team[user_year]],
        "times",
    )
print()