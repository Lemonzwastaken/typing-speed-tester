import customtkinter as ctk
from sentences import EASY, HARD, MEDIUM, PUNCTUATION
import random
import time

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
        self.wpm_var = ctk.StringVar(value="-- WPM")
        self.acc_var = ctk.StringVar(value="-- %")
        self.time_var = ctk.StringVar(value="0.0 s")

        self.build_ui()
        self.new_test()

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

        self.diff_buttons = {}
        for label, meta in DIFFICULTIES.items():
            btn = ctk.CTkButton(
                diff_frame, text=label, width=110,
                fg_color="#313244", hover_color="#45475a",
                text_color=meta["color"],
                font=ctk.CTkFont(size=13, weight="bold"),
                corner_radius=8,
                command=lambda l=label: self._select_difficulty(l)
            )
            btn.pack(side="left", padx=4)
            self.diff_buttons[label] = btn

        self._highlight_diff_btn("Easy")

        #PROMPT CARD
        prompt_frame = ctk.CTkFrame(self, corner_radius=12, fg_color=("#1e1e2e", "#1e1e2e"))
        prompt_frame.pack(padx=40, fill="x")
        self.prompt_label = ctk.CTkLabel(
            prompt_frame, text="[ sentence will appear here ]", wraplength=620,
            font=ctk.CTkFont(family="Courier", size=17),
            justify="center", text_color="#cdd6f4"
        )
        self.prompt_label.pack(padx=20, pady=18)

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
        self.entry.pack(padx=40, fill="x")
        self.entry.bind("<KeyRelease>", self._on_key)
        self.entry.bind("<Tab>", lambda e: (self.new_test(), "break")[1])

        #BUTTONS
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=18)
        ctk.CTkButton(btn_frame, text="New Test (TAB)", width=160,
                      command=self.new_test).pack(side="left", padx=8)
        ctk.CTkButton(btn_frame, text="Reset", width=100,
                      fg_color="#313244", hover_color="#45475a",
                      command=self.reset).pack(side="left", padx=8)

        #RESULTS
        self.result_banner = ctk.CTkLabel(
            self, text="", font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#a6e3a1"
        )
        self.result_banner.pack(pady=(0, 8))

    def _stat_box(self, parent, label, var, col):
        frame = ctk.CTkFrame(parent, corner_radius=10, fg_color=("#1e1e2e", "#1e1e2e"))
        frame.grid(row=0, column=col, padx=6, sticky="ew", ipady=8)
        ctk.CTkLabel(frame, text=label,
                     font=ctk.CTkFont(size=11), text_color="gray").pack()
        ctk.CTkLabel(frame, textvariable=var,
                     font=ctk.CTkFont(size=20, weight="bold"),
                     text_color="#cdd6f4").pack()

    def _highlight_diff_btn(self, active):
        for label, btn in self.diff_buttons.items():
            if label == active:
                btn.configure(fg_color=DIFFICULTIES[label]["color"], text_color="#1e1e2e")
            else:
                btn.configure(fg_color="#313244", text_color=DIFFICULTIES[label]["color"])

    #GAME LOGIC

    def _select_difficulty(self, label):
        self.difficulty.set(label)
        self._highlight_diff_btn(label)
        self.new_test()

    def new_test(self):
        pool = DIFFICULTIES[self.difficulty.get()]["sentences"]
        self.target_text = random.choice(pool)
        self.prompt_label.configure(text=self.target_text)
        self.reset()

    def reset(self):
        self.started = False
        self.timer_running = False
        self.start_time = None
        self.entry.delete("1.0", "end")
        self.entry.configure(border_color="#313244")
        self.entry.focus()
        self.wpm_var.set("-- WPM")
        self.acc_var.set("-- %")
        self.time_var.set("0.0 s")
        self.result_banner.configure(text="")

    def _on_key(self, event):
        typed = self.entry.get("1.0", "end-1c")

        #STARTS THE TIMER ON KEY PRESSING
        if not self.started and typed.strip():
            self.started = True
            self.timer_running = True
            self.start_time = time.time()
            self._tick()

        if not self.started:
            return

        #ACCURACY CHECK
        correct = sum(1 for a, b in zip(typed, self.target_text) if a == b)
        acc = int(correct / max(len(typed), 1) * 100) if typed else 0
        self.acc_var.set(f"{acc} %")

        if self.target_text.startswith(typed):
            self.entry.configure(border_color="#a6e3a1")
        else:
            self.entry.configure(border_color="#f38ba8")

        #CHECK FOR COMPLETING
        if typed == self.target_text:
            self.timer_running = False
            elapsed = time.time() - self.start_time
            words = len(self.target_text.split())
            wpm = int(words / (elapsed / 60))
            diff_color = DIFFICULTIES[self.difficulty.get()]["color"]

            self.wpm_var.set(f"{wpm} WPM")
            self.acc_var.set("100 %")
            self.time_var.set(f"{elapsed:.1f} s")
            self.result_banner.configure(
                text=f"FINISHED! {wpm} WPM  -  {elapsed:.1f}s  -  Press TAB for next",
                text_color=diff_color
            )
            self.entry.configure(border_color="#a6e3a1")

    def _tick(self):
        if self.timer_running and self.start_time:
            elapsed = time.time() - self.start_time
            self.time_var.set(f"{elapsed:.1f} s")
            self.after(100, self._tick)


if __name__ == "__main__":
    app = TypingApp()
    app.mainloop()