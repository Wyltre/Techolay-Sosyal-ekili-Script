import requests
from bs4 import BeautifulSoup
import random
import tkinter as tk
from tkinter import messagebox

def get_usernames(url, page_count=1):
    usernames = []
    selected_usernames = set()
    for page in range(1, page_count + 1):
        response = requests.get(f"{url}?page={page}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            comments = soup.find_all(class_='message-userContent')
            for comment in comments:
                if "Katılıyorum." in comment.text:
                    username = comment.find_previous(class_='username').text.strip()
                    if username is None:
                        username = ""
                    if username not in selected_usernames:
                        usernames.append(username)
                        selected_usernames.add(username)
    return usernames

def select_winner(usernames):
    if usernames:
        winner = random.choice(usernames)
        return winner
    else:
        return None

def select_backup_winner(usernames, winner):
    remaining_users = [user for user in usernames if user != winner]
    if remaining_users:
        backup_winner = random.choice(remaining_users)
        return backup_winner
    else:
        return None

def run_giveaway():
    url = url_entry.get()
    page_count = int(page_count_entry.get())
    usernames = get_usernames(url, page_count)
    
    if usernames:
        usernames.pop(0)
    
    total_participants_label.config(text=f"Katılanlar: {len(usernames)}")
    
    participant_list.delete(0, tk.END)
    for username in usernames:
        participant_list.insert(tk.END, username)
    
    winner = select_winner(usernames)
    
    if winner:
        backup_winner = select_backup_winner(usernames, winner)
        
        if backup_winner:
            winner_label.config(text=f"Kazanan: {winner} (Asıl Kazanan)\nYedek Kazanan: {backup_winner}")
        else:
            winner_label.config(text=f"Kazanan: {winner}\nYedek Kazanan bulunamadı.")
    else:
        winner_label.config(text="Katılım gösteren kullanıcı bulunamadı.")

root = tk.Tk()
root.title("Çekiliş Kazanan Seçici")

url_label = tk.Label(root, text="Çekiliş konusunun linkini girin:")
url_entry = tk.Entry(root, width=50)
page_count_label = tk.Label(root, text="Sayfa sayısını girin:")
page_count_entry = tk.Entry(root, width=10)
run_button = tk.Button(root, text="Çekilişi Başlat", command=run_giveaway)
total_participants_label = tk.Label(root, text="")
participant_list = tk.Listbox(root, width=50, height=10)
participant_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
winner_label = tk.Label(root, text="")

url_label.pack()
url_entry.pack()
page_count_label.pack()
page_count_entry.pack()
run_button.pack()
total_participants_label.pack()
participant_list.pack(side=tk.LEFT, fill=tk.BOTH)
participant_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
participant_list.config(yscrollcommand=participant_scrollbar.set)
participant_scrollbar.config(command=participant_list.yview)
winner_label.pack()

winner_label.config(text="github.com/wyltre")  

root.mainloop()
