"""
Digital Clock - Completely FREE Edition
No Login • No Key • No Account • No Ads • 100% Free

Simple to use:
1. Run: python digital_clock_free.py
2. Or: Double-click the .exe file after building
3. Enjoy the clock!
"""

import tkinter as tk
from tkinter import font
import datetime
import pytz
import threading

class FreeDigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock - FREE (No Login)")
        self.root.geometry("1400x850")
        self.root.configure(bg="#0a0e27")
        
        # Time zones
        self.time_zones = [
            ("New York", "America/New_York"),
            ("Los Angeles", "America/Los_Angeles"),
            ("London", "Europe/London"),
            ("Paris", "Europe/Paris"),
            ("Tokyo", "Asia/Tokyo"),
            ("Hong Kong", "Asia/Hong_Kong"),
            ("Sydney", "Australia/Sydney"),
            ("Dubai", "Asia/Dubai"),
            ("Singapore", "Asia/Singapore"),
            ("Bangkok", "Asia/Bangkok"),
            ("Istanbul", "Europe/Istanbul"),
            ("São Paulo", "America/Sao_Paulo"),
        ]
        
        self.clock_labels = {}
        self.date_labels = {}
        
        self.create_ui()
        self.start_update()
    
    def create_ui(self):
        """Create the interface"""
        
        # Top banner
        banner = tk.Frame(self.root, bg="#1a1a3a", height=60)
        banner.pack(fill=tk.X)
        
        # Title
        title_font = font.Font(family="Arial", size=24, weight="bold")
        title = tk.Label(
            banner,
            text="⏰ Digital Clock - FREE Edition (No Login Required!)",
            font=title_font,
            fg="#00ff88",
            bg="#1a1a3a"
        )
        title.pack(pady=10)
        
        # Info
        info_font = font.Font(family="Arial", size=9)
        info = tk.Label(
            banner,
            text="✓ Completely Free • ✓ No Account • ✓ No License Key • ✓ Works Offline",
            font=info_font,
            fg="#88ff88",
            bg="#1a1a3a"
        )
        info.pack()
        
        # Main clock grid
        main_frame = tk.Frame(self.root, bg="#0a0e27")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        for idx, (city, zone) in enumerate(self.time_zones):
            row = idx // 4
            col = idx % 4
            
            # Clock card
            card = tk.Frame(main_frame, bg="#1a1a3a", relief=tk.RAISED, bd=2)
            card.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")
            
            # City name
            city_font = font.Font(family="Arial", size=13, weight="bold")
            city_label = tk.Label(
                card, text=city, font=city_font,
                fg="#00ffff", bg="#1a1a3a"
            )
            city_label.pack(pady=10)
            
            # Time
            time_font = font.Font(family="Courier New", size=36, weight="bold")
            time_label = tk.Label(
                card, text="--:--:--", font=time_font,
                fg="#00ff88", bg="#1a1a3a"
            )
            time_label.pack(pady=15)
            
            # Date
            date_font = font.Font(family="Courier New", size=10)
            date_label = tk.Label(
                card, text="Loading...", font=date_font,
                fg="#88ff00", bg="#1a1a3a"
            )
            date_label.pack(pady=5)
            
            # Store labels
            self.clock_labels[zone] = time_label
            self.date_labels[zone] = date_label
            
            # Configure grid
            main_frame.grid_rowconfigure(row, weight=1)
            main_frame.grid_columnconfigure(col, weight=1)
    
    def start_update(self):
        """Start updating time"""
        thread = threading.Thread(target=self.update_loop, daemon=True)
        thread.start()
    
    def update_loop(self):
        """Update time loop"""
        while True:
            try:
                for city, zone in self.time_zones:
                    tz = pytz.timezone(zone)
                    now = datetime.datetime.now(tz)
                    
                    time_str = now.strftime("%H:%M:%S")
                    date_str = now.strftime("%a, %b %d, %Y")
                    
                    self.clock_labels[zone].config(text=time_str)
                    self.date_labels[zone].config(text=date_str)
            except:
                pass
            
            import time
            time.sleep(1)

def main():
    root = tk.Tk()
    app = FreeDigitalClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
