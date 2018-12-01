import inquirer
from common import colors
from common import handle_event
from MeetUp import meetups
from hackathons import hackathon


def start():
    event_type = ["Hackathons", "Outdoors-Adventures", "Tech", "parent-Family", "Health-Wellness", "Sports-Fitness",
                  "Education", "Photography", "Food", "Writing", "Language", "Music", "Movements",
                  "LGBTQ", "Film", "Games-Sci-Fi", "Dancing", "Social", "Career-Business"]

    question = [inquirer.List('choice', message="Choose one from below?", choices=event_type)]
    answer = inquirer.prompt(question)

    print("\nPlease Enter the City Name. (Example. Delhi, Mumbai, etc.)")
    city = input()

    choice = answer['choice']

    if choice != 'Hackathons':
        meets = meetups.main(city, choice)
        print(colors(meets, '32'))
        # handle_event(meets)
    else:
        hack = hackathon(city)
        print(colors(hack, '32'))
        # handle_event(hack)



if __name__ == '__main__':
    start()
