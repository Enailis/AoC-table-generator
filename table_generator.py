from dotenv import load_dotenv
import bs4
import requests
import re
import os
import pyperclip


def get_rankings(YEAR, SESSION_COOKIE):
    # Get the leaderboard page
    url = "https://adventofcode.com/" + YEAR + "/leaderboard/self"
    headers = {'Cookie': 'session='+SESSION_COOKIE}
    r = requests.get(url, headers=headers)

    # Get the table from the page
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    pre = soup.find_all('pre')

    # Remove useless lines
    table = [i for i in pre[0].text.splitlines()]
    table = table[::-1]
    del table[-2:]

    ranking_per_day = {}

    for line in table:
        line_splitted = (' '.join(line.split())).split(' ')
        for i in line_splitted:
            if not i.isdigit():
                line_splitted.remove(i)
        line_splitted = [i for i in line_splitted if i != '0']

        values = re.findall(r'\d+', ' '.join(line_splitted))
        
        ranking_per_day[line_splitted[0]] = values[1:]

    return ranking_per_day


def generate_table(ranking_per_day, YEAR):
    table = "| Day | Challenge | Part 1 | Part 2 | Rank Part 1 | Rank Part 2 |\n|:---:|:---|:---:|:---:|:---:|:---:|\n"

    for day, ranking in ranking_per_day.items():
        # Add "Day" column
        table += f"| {day} |"
        
        # Add "Challenge" column
        url = "https://adventofcode.com/" + YEAR + "/day/" + day
        r = requests.get(url)

        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        title = soup.find_all('h2')[0].text
        title = title[11:-4]

        table += f" [{title}]({url}) |"

        # Add "Part 1" and "Part 2" columns
        table += f" [part 1](./Day{int(day):02d}/part1.py) |"
        table += f" [part 2](./Day{int(day):02d}/part2.py) |"

        # Add "Score" columns
        table += f" {ranking[0]} |"
        table += f" {ranking[1]} |" if len(ranking) > 1 else " N/A |"

        table += "\n"
    table += "\n*generated using [ENA's table generator](https://github.com/Enailis/AoC-table-generator)*"

    try:    
        pyperclip.copy(table)
        print("Table copied to clipboard!")
    except:
        print("Table could not be copied to clipboard...")
        print(table)


if __name__ == '__main__':
    load_dotenv()
    YEAR = os.getenv('YEAR')
    SESSION_COOKIE = os.getenv('SESSION_COOKIE')

    generate_table(get_rankings(YEAR, SESSION_COOKIE), YEAR)
