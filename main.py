from prettytable import PrettyTable
from MeetUp import meetup_main

def start():
    columns = ["S.No", "Event Type"]
    table = PrettyTable(columns)

    event_type = ["Hackathons", "Outdoors & Adventures", "Tech", "Family", "Health & Wellness", "Sports & Fitness",
                  "Learning", "Photography", "Food & Drinks", "Writings", "Language & Culture", "Music", "Movements",
                  "LGBTQ", "Film", "Sci-Fi & Games", "Dance", "Social", "Career & Business"]

    type_url = ["outdoors-adventures", "tech", "parents-family", "health-wellness", "sports-fitness", "education",
                "photography", "food", "writing", "language", "music", "movements", "lgbtq", "film", "games-sci-fi",
                "dancing", "social", "career-business"]

    for i in range(len(event_type)):
        table.add_row([i+1, event_type[i]])

    print(table)

    print("-------------------------")
    print("Choose the event. (Example. Enter 1 for Hackathons, 2 for Outdoors & Adventures, etc.)")

    choice = int(input())

    print("\nPlease Enter the City Name. (Example. Delhi, Mumbai, etc.)")
    city = input()

    if choice>1:
        meetup_main.make_url(city, type_url[i-2])


if __name__ == '__main__':
    start()