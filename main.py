import customtkinter as ctk
from sentences import EASY, HARD, MEDIUM, PUNCTUATION

DIFFICULTIES = {
    "Easy":        {"sentences": EASY,        "color": "#a6e3a1"},
    "Medium":      {"sentences": MEDIUM,       "color": "#f9e2af"},
    "Hard":        {"sentences": HARD,         "color": "#f38ba8"},
    "Punctuation": {"sentences": PUNCTUATION,  "color": "#89b4fa"},
}
#APP APPEARANCE
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class TypingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Tester")
        self.geometry("750x580")
        self.resizable(False, False)

        self.difficulty = ctk.StringVar(value="Easy")
        self.wpm_var = ctk.StringVar(value="--WPM")
        self.acc_var = ctk.StringVar(value="--%")
        self.time_var = ctk.StringVar(value="0.0 s")

        self.build_ui()

    def build_ui(self):

        ##TITLE
        ctk.CTkLabel(self, text="⌨  Typing Speed Test",
                     font=ctk.CTkFont(size=26, weight="bold")).pack(pady=(28, 4))
        ctk.CTkLabel(self, text="Start typing to begin  •  Tab for new sentence",
                     font=ctk.CTkFont(size=13), text_color="gray").pack(pady=(0, 14))

        #DIFFICULTY
        diff_frame = ctk.CTkFrame(self, fg_color="transparent")
        diff_frame.pack(pady=(0, 14))

        ctk.CTkLabel(diff_frame, text="Difficulty:",
                     font=ctk.CTkFont(size=13, weight="bold"),
                     text_color="gray").pack(side="left", padx=(0, 10))

        for label, meta in DIFFICULTIES.items():
            ctk.CTkButton(
                diff_frame, text=label, width=110,
                fg_color="#313244", hover_color="#45475a",
                text_color=meta["color"],
                font=ctk.CTkFont(size=13, weight="bold"),
                corner_radius=8,
                command=lambda: None  # no functionality yet
            ).pack(side="left", padx=4)

        #PROMPT CARD
        prompt_frame = ctk.CTkFrame(self, corner_radius=12, fg_color=("#1e1e2e", "#1e1e2e"))
        prompt_frame.pack(padx=40, fill="x")
        ctk.CTkLabel(
            prompt_frame, text="[ sentence will appear here ]", wraplength=620,
            font=ctk.CTkFont(family="Courier", size=17),
            justify="center", text_color="#cdd6f4"
        ).pack(padx=20, pady=18)

        #STATISTICS
        stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        stats_frame.pack(pady=18, padx=40, fill="x")
        for col in range(3):
            stats_frame.columnconfigure(col, weight=1)
 
        self._stat_box(stats_frame, "Speed",    self.wpm_var,  0)
        self._stat_box(stats_frame, "Accuracy", self.acc_var,  1)
        self._stat_box(stats_frame, "Time",     self.time_var, 2)

        #INPUT TEXTBOX
        self.entry = ctk.CTkTextbox(
            self, height=90, corner_radius=10,
            font=ctk.CTkFont(family="Courier", size=15),
            border_width=2, border_color="#313244"
        )
        self.entry.pack(padx = 40, fill = "x")

        #BUTTONS(To do)
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady = 18)
        ctk.CTkButton(btn_frame, text="New Test (TAB)",width=160,
                      command=lambda: None ).pack(side = "left", padx = 8)
        ctk.CTkButton(btn_frame, text="Reset", width=100,
                      fg_color="#313244", hover_color="#45475a",
                      command=lambda: None).pack(side="left", padx=8)
        
        #RESULTS
        self.result_banner = ctk.CTkLabel(
            self, text="", font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#a6e3a1"
        )

        self.result_banner.pack(pady = (0,8))


    def _stat_box(self, parent, label, var, col):
        frame = ctk.CTkFrame(parent, corner_radius=10, fg_color=("#1e1e2e", "#1e1e2e"))
        frame.grid(row=0, column=col, padx=6, sticky="ew", ipady=8)
        ctk.CTkLabel(frame, text=label,
                     font=ctk.CTkFont(size=11), text_color="gray").pack()
        ctk.CTkLabel(frame, textvariable=var,
                     font=ctk.CTkFont(size=20, weight="bold"),
                     text_color="#cdd6f4").pack()
        
    def _highlight_diff_btn(self, active):
        for label, btn in self.diff_buttons:
        



if __name__ == "__main__":
    app = TypingApp()
    app.mainloop()