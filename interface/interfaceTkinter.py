import tkinter as tk
import threading
import interface.styles as styles
import generate.generate as generate
import screenRecorder.screenRecorder as sr

class AutoBongPy(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.title('AutoBongPy')
        self.geometry('500x500')

        # Widgets
        self.label = tk.Label(self, text='AutoBongPy', font=styles.TITLE_FONT, fg=styles.TITLE_COLOR)
        self.label.pack(pady=10)

    

        self.button = tk.Button(self, text='GenerateVideo', bg=styles.BUTTON_BG, fg=styles.BUTTON_FG, font=styles.BUTTON_FONT, command=self.generate_video)
        self.button.pack(pady=10)


    def generate_video(self):

        # Thread pour le jeu Pygame
        thread_game = threading.Thread(target=generate.run_pygame)
        thread_game.daemon = True
        thread_game.start()

        # Thread pour l'enregistrement vidéo
        thread_record = threading.Thread(
            target=sr.screen_recorder,
            kwargs={'duration': 10}
        )
        thread_record.daemon = True
        thread_record.start()

if __name__ == '__main__':
    app = AutoBongPy()
    app.mainloop()
