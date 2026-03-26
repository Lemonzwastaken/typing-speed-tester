import customtkinter as ctk
import random
import time
from sentences import EASY, HARD, MEDIUM, PUNCTUATION

#DIFFICULTIES
DIFFICULTIES = {
    "Easy": {"sentences": EASY, "color": "#a6e3a1"},
    "Medium" : {"sentences": MEDIUM, "color": "#f9e2af"},
    "Hard" : {"sentences" : HARD, "color": "#f38ba8"},
    "Punctuation" : {"sentences": PUNCTUATION, "color": "#89b4fa"}
}


#APPERANCE OF THE INTERFACE
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("Blue")

#BUILDING APP
class TypingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Typing speed tester")
        self.geometry("750x580")
        self.resizable(False, False)

        self.target_test = ""
        self.start_time = None
        self.started = False
        self.timer_running = False
        self.difficulty = ctk.StringVar(value="Easy")

        self.new_test()
        self.build_ui()

    def build_ui(self):
        #Title
        ctk.CTkLabel(self, text="⌨  Typing Speed Test",
             font=ctk.CTkFont(size=26, weight="bold")).pack(pady=(28, 4))
        
        ctk.CTkLabel(self, text="Start typing to begin  •  Tab for new sentence",
             font=ctk.CTkFont(size=13), text_color="gray").pack(pady=(0, 14))
        

        #Selecting Difficulty
        diff_frame = ctk.CTkFrame(self, fg_color="transparent")
        diff_frame.pack(pady=(0, 14))

        ctk.CTkLabel(diff_frame, text="Difficulty:",
                     font=ctk.CTkFont(size=13, weight="bold"),
                     text_color="gray").pack(side="left", padx=(0, 10))
    

        self.diff_buttons = {}
        for label, meta in DIFFICULTIES.items():
            btn = ctk.CTkButton(
                diff_frame, text=label, width=110,
                fg_color="#313244", hover_color="#45475a",
                text_color=meta["color"],
                font=ctk.CTkFont(size=13, weight="bold"),
                corner_radius=8,
                command=lambda l=label: self._set_difficulty(l)
            )
            btn.pack(side = "left", padx = 4)
            self.diff_buttons[label] = btn

        self.highlight_diff_btn("Easy")

        #PROMPT CARD
        self.prompt_frame = ctk.CTkFrame(self, corner_radius=12, fg_color=("#1e1e2e", "#1e1e2e"))
        self.prompt_frame.pack(padx=40, fill="x")
        self.prompt_label = ctk.CTkLabel(
            self.prompt_frame, text="", wraplength=620,
            font=ctk.CTkFont(family="Courier", size=17),
            justify="center", text_color="#cdd6f4"
        )
        self.prompt_label.pack(padx=20, pady=18)

        #Stats row
        stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        stats_frame.pack(pady = 18, padx=40, fill = "x")
        for col in range(3):
            stats_frame.columnconfigure(col, weight = 1)


if __name__ == "__main__":
    app = TypingApp()
    app.mainloop()
