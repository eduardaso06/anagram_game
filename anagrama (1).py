import random
import json
import tkinter as tk

def word_prompt(data, length):
    all_words = list(data.keys())
    while True:
        word = random.choice(all_words)
        if len(word) < length and len(word) > 2:
            return word

def shuffle_word(word):
    array = list(word)
    shuffled = word
    while True:
        random.shuffle(array)
        shuffled = ''.join(array)
        if shuffled != word:
            return shuffled

def check_guess():
    guess = guess_entry.get().lower()
    if guess == current_word:
        result_label.config(text="Correto!", font=("arial", 15, "bold"), bg="#000000", fg="#03FF2D")
        submit_button.config(state=tk.DISABLED)
    else:
        attempts_left = int(attempts_label.cget("text")) - 1
        attempts_label.config(text=str(attempts_left))
        if attempts_left == 0:
            result_label.config(text="A resposta correcta era: " + current_word, font=("arial", 15, "bold"), bg="#000000", fg="#FF03E2")
            submit_button.config(state=tk.DISABLED)

def continue_game():
    global current_word
    global current_question
    global current_meaning

    current_word = word_prompt(data, 5)
    current_question = shuffle_word(current_word)
    current_meaning = data[current_word]

    current_question = current_question.lower()
    current_word = current_word.lower()

    question_label.config(text="A palavra baralhada é: " + current_question)
    attempts_label.config(text="5")
    guess_entry.delete(0, tk.END)
    result_label.config(text="")
    submit_button.config(state=tk.NORMAL)

# Carregar dados do arquivo JSON
filename = 'dicionario.json'
file = open(filename)
data = json.load(file)

# Configuração da janela principal
window = tk.Tk()
window.title("Jogo de Anagrama")
window.configure(bg="#000000")

# Rótulos
welcome_label = tk.Label(window, text="☆ BEM-VINDO AO ANAGRAMA ☆",  font=("arial", 40, "bold"), bg="#000000", foreground="#4DFFED")
welcome_label.pack(pady=10)

question_label = tk.Label(window, text="", font=("arial",15), bg="#000000", foreground="#FFFFFF")
welcome_label.pack(pady=20)

# conceito da palavra
hint_label = tk.Label(window, text="", font=("arial",10), bg="#000000")
welcome_label.pack(pady=20)



attempts_label = tk.Label(window, text="5",font=("arial",14), bg="#000000", foreground="#FFFFFF")
welcome_label.pack(pady=20)
                          
attempts_left_label = tk.Label(window, text="Tentativas restantes:", font=("arial",12), bg="#000000", foreground="#FFFB03")
welcome_label.pack(pady=20)


guess_label = tk.Label(window, text="Adivinha a palavra:", font=("arial",12), bg="#000000", foreground="#FFFFFF")
welcome_label.pack(pady=20)

result_label = tk.Label(window, text="")


# Entrada
guess_entry = tk.Entry(window)

# Botão de envio
submit_button = tk.Button(window, text="Verificar", command=check_guess, bg="#FFFFFF")

# Botão de continuação
continue_button = tk.Button(window, text="Próxima palavra", command=continue_game, bg="#FFFFFF")

# Posicionamento dos widgets
welcome_label.pack()
question_label.pack()
hint_label.pack()
attempts_left_label.pack()
attempts_label.pack()
guess_label.pack()
guess_entry.pack()
submit_button.pack()
result_label.pack()
continue_button.pack()

# Variáveis do jogo
current_word = ""
current_question = ""
current_meaning = ""

# Iniciar o primeiro jogo
continue_game()

# Iniciar a janela principal
window.mainloop()