import random

import requests
from bs4 import BeautifulSoup


def get_usernames(url, page_count=1):
    usernames = []
    selected_usernames = set()
    for page in range(1, page_count + 1):
        response = requests.get(f"{url}?page={page}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            comments = soup.find_all(class_="message-userContent")
            for comment in comments:
                if "Katılıyorum." in comment.text:
                    username = comment.find_previous(class_="username").text.strip()
                    if username is None:
                        username = ""
                    if username not in selected_usernames:
                        usernames.append(username)
                        selected_usernames.add(username)
    return usernames


def select_winner(usernames):
    if usernames:
        winner = random.choice(usernames)
        print("Kazanan:", winner)
    else:
        print("Katılım gösteren kullanıcı bulunamadı.")


def main():
    url = input("Çekiliş konusunun linkini girin: ")
    page_count = int(input("Sayfa sayısını girin: "))
    usernames = get_usernames(url, page_count)
    print("Toplam katılımcı sayısı:", len(usernames))
    print("Çekilişe katılan kullanıcılar:")
    for username in usernames:
        print(username)
    select_winner(usernames)


if __name__ == "__main__":
    print("wyltre tarafından yapılmıştır. github.com/wyltre")
    main()
