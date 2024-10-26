import pandas as pd
import matplotlib.pyplot as plt


def plot_password():

    # Wczytanie danych z pliku
    file_path = "data/passwords_data/passwords.txt"  # Podaj właściwą ścieżkę do pliku
    data = pd.read_csv(file_path, sep="\t", header=None, names=["Password", "Age"])

    # Upewnij się, że kolumna Age zawiera liczby całkowite
    data['Age'] = pd.to_numeric(data['Age'], errors='coerce')

    # Klasyfikacja haseł na podstawie ich siły
    def classify_password(password):
        length = len(password)

        if length < 6 and password.islower():  # Bardzo słabe hasło (krótkie, tylko małe litery)
            return "bardzo słabe"
        elif length >= 6 and length < 8 and password.islower():  # Słabe hasło (tylko małe litery)
            return "słabe"
        elif length >= 8 and password.isalnum():  # W porządku (ma mieszane litery i cyfry, ale bez specjalnych znaków)
            return "w porządku"
        elif length >= 10 and any(c.isdigit() for c in password) and any(c.isupper() for c in password):  # Silne
            return "silne"
        else:  # Bardzo silne (długie, zawiera litery, cyfry i znaki specjalne)
            return "bardzo silne"

    # Dodanie kolumny klasyfikacji
    data['Strength'] = data['Password'].apply(classify_password)

    # Definiowanie nowych kategorii wiekowych
    bins = [18, 25, 35, 45, 55, 100]
    labels = ["18-25", "26-35", "36-45", "46-55", "55+"]
    data['Age Group'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

    # Funkcja do generowania wykresów kołowych w jednym oknie
    def plot_pie_charts():
        fig, axs = plt.subplots(1, 5, figsize=(20, 5))  # 5 wykresów obok siebie

        for i, age_group in enumerate(labels):
            group_data = data[data['Age Group'] == age_group]
            strength_counts = group_data['Strength'].value_counts()

            # Rysowanie wykresu kołowego
            axs[i].pie(strength_counts, labels=strength_counts.index, autopct='%1.1f%%', startangle=90,
                       colors=plt.cm.Paired.colors)
            axs[i].set_title(f'Siła haseł: {age_group}')
            axs[i].axis('equal')  # Zapewnia okrągły kształt wykresu

        plt.tight_layout()
        plt.show()

    # Generowanie wykresów
    plot_pie_charts()
