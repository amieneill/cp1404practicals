"""
CP1404 - Practical_05
Name: Amie Neill
Wimbledon Exercise
Estimate: 90 minutes
Actual: 97 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Run wimbledon champions and countries program."""
    data = load_data()
    champion_to_win, countries = calculate_data(data)
    display_results(champion_to_win, countries)


def display_results(champion_to_win, countries):
    """Display wimbledon champions and countries summary."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_win.items():
        print(f"{champion} {wins}")
    print(f"These {len(countries)} countries have won Wimbledon: \n{', '.join(sorted(countries))}")


def calculate_data(data):
    """Create a dictionary of champions, wins and countries set from data."""
    champion_to_win = {}
    countries = set()
    for data_point in data:
        champion = data_point[2]
        countries.add(data_point[1])
        if champion in champion_to_win:
            champion_to_win[champion] += 1
        else:
            champion_to_win[champion] = 1
    return champion_to_win, countries


def load_data():
    """Load data from 'wimbledon.csv' file."""
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data


main()
