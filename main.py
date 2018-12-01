import inquirer
from MeetUp import meetups
from hackathons import hackathon

def start():
    event_type = ["Hackathons", "Outdoors-Adventures", "Tech", "parent-Family", "Health-Wellness", "Sports-Fitness",
                  "Education", "Photography", "Food", "Writing", "Language", "Music", "Movements",
                  "LGBTQ", "Film", "Games-Sci-Fi", "Dancing", "Social", "Career-Business"]

    question = [inquirer.List('choice', message="Choose one from below?", choices=event_type)]
    answer = inquirer.prompt(question)

    # type_url = ["outdoors-adventures", "tech", "parents-family", "health-wellness", "sports-fitness", "education",
    #             "photography", "food", "writing", "language", "music", "movements", "lgbtq", "film", "games-sci-fi",
    #             "dancing", "social", "career-business"]

    print("\nPlease Enter the City Name. (Example. Delhi, Mumbai, etc.)")
    city = input()

    choice = answer['choice']

    if choice != 'Hackathons':
        meetups.main(city, choice)
    else:
        hackathon(city)

if __name__ == '__main__':
    start()