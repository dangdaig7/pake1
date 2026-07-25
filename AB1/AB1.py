"""
AB1 - Professional Application
Completely FREE - No Login, No Key, No Account

Features:
✓ Notes management
✓ Task tracking
✓ Built-in tools
✓ No registration
✓ Works offline
✓ Unlimited usage

Run: python AB1.py
Or: Double-click BUILD_AB1.bat to create AB1.exe
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import datetime
import json
from pathlib import Path

class AB1Application:
    def __init__(self, root):
        self.root = root
        self.root.title("AB1 - Professional Application")
        self.root.geometry("1300x800")
        self.root.configure(bg="#0f0f1e")
        self.data = {}
        self.load_data()
        self.create_ui()
    
    def load_data(self):
        try:
            if Path("AB1_data.json").exists():
                with open("AB1_data.json", "r", encoding="utf-8") as f:
                    self.data = json.load(f)
        except:
            pass
        if not self.data:
            self.data = {"notes": [], "tasks": [], "reminders": [], "settings": {}}
    
    def save_data(self):
        try:
            with open("AB1_data.json", "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
        except:
            pass
    
    def create_ui(self):
        header = tk.Frame(self.root, bg="#1a1a2e", height=80)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="AB1 - Professional Application", 
                        font=("Arial", 26, "bold"), fg="#00ff88", bg="#1a1a2e")
        title.pack(pady=8)
        
        status = tk.Label(header, text="✓ FREE Edition • ✓ No Login • ✓ No Key • ✓ Offline Ready",
                         font=("Arial", 10), fg="#88ff88", bg="#1a1a2e")
        status.pack()
        
        sep = tk.Frame(self.root, bg="#2a2a4e", height=2)
        sep.pack(fill=tk.X)
        
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background="#0f0f1e")
        style.configure('TFrame', background="#0f0f1e")
        
        self.create_dashboard_tab()
        self.create_notes_tab()
        self.create_tasks_tab()
        self.create_tools_tab()
        self.create_settings_tab()
    
    def create_dashboard_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📊 Dashboard")
        
        welcome_frame = tk.Frame(frame, bg="#0f0f1e")
        welcome_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        welcome = tk.Label(welcome_frame, text="Welcome to AB1 - Completely Free", 
                          font=("Arial", 20, "bold"), fg="#00ff88", bg="#0f0f1e")
        welcome.pack(pady=20)
        
        info_frame = tk.Frame(welcome_frame, bg="#1a1a2e", relief=tk.SUNKEN, bd=2)
        info_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        info_text = """AB1 - COMPLETELY FREE

✓ No Login Required
✓ No Account Creation
✓ No License Key
✓ No Registration
✓ No Email Verification
✓ No Ads or Tracking
✓ Works Offline
✓ Open Source
✓ Unlimited Usage

FEATURES:
  • Full Notes Management
  • Complete Task Tracking
  • Built-in Tools
  • Local Data Storage
  • Real-time Statistics
  • Text Processing
  • Calculator

DATA STORAGE:
  • File: AB1_data.json
  • Location: Same folder
  • Format: JSON
  • Backup: Just copy file"""
        
        info_label = tk.Label(info_frame, text=info_text, font=("Courier New", 11),
                             fg="#00ff88", bg="#1a1a2e", justify=tk.LEFT, padx=20, pady=20)
        info_label.pack(fill=tk.BOTH, expand=True)
        
        self.time_label = tk.Label(welcome_frame, text="", font=("Arial", 12),
                                   fg="#00ffff", bg="#0f0f1e")
        self.time_label.pack(pady=10)
        self.update_time_display()
    
    def update_time_display(self):
        try:
            now = datetime.datetime.now()
            time_str = now.strftime("%Y-%m-%d %H:%M:%S")
            self.time_label.config(text=f"Current Time: {time_str}")
            self.root.after(1000, self.update_time_display)
        except:
            pass
    
    def create_notes_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="📝 Notes")
        
        ctrl_frame = tk.Frame(frame, bg="#0f0f1e")
        ctrl_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(ctrl_frame, text="+ New Note", command=self.add_note, 
                 bg="#667eea", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(ctrl_frame, text="🗑️ Delete", command=self.delete_note, 
                 bg="#ff6b6b", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(ctrl_frame, text="💾 Save", command=self.save_note, 
                 bg="#51cf66", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        content_frame = tk.Frame(frame, bg="#0f0f1e")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        list_frame = tk.Frame(content_frame, bg="#0f0f1e")
        list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=5)
        
        tk.Label(list_frame, text="Notes:", font=("Arial", 11, "bold"), 
                fg="#00ff88", bg="#0f0f1e").pack()
        
        self.notes_listbox = tk.Listbox(list_frame, width=25, height=25,
                                       bg="#1a1a2e", fg="#00ff88", selectmode=tk.SINGLE)
        self.notes_listbox.pack(fill=tk.BOTH, expand=True, pady=5)
        self.notes_listbox.bind('<<ListboxSelect>>', self.on_note_select)
        
        editor_frame = tk.Frame(content_frame, bg="#0f0f1e")
        editor_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(editor_frame, text="Content:", font=("Arial", 11, "bold"),
                fg="#00ff88", bg="#0f0f1e").pack()
        
        self.notes_editor = scrolledtext.ScrolledText(editor_frame, width=60, height=25,
                                                     bg="#1a1a2e", fg="#00ff88", font=("Courier New", 10))
        self.notes_editor.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.refresh_notes_list()
    
    def add_note(self):
        if "notes" not in self.data:
            self.data["notes"] = []
        new_note = {"title": f"Note {len(self.data['notes']) + 1}", 
                   "content": "", "created": datetime.datetime.now().isoformat()}
        self.data["notes"].append(new_note)
        self.save_data()
        self.refresh_notes_list()
    
    def delete_note(self):
        selection = self.notes_listbox.curselection()
        if selection and "notes" in self.data:
            idx = selection[0]
            if idx < len(self.data["notes"]):
                del self.data["notes"][idx]
                self.save_data()
                self.refresh_notes_list()
                self.notes_editor.delete("1.0", tk.END)
    
    def save_note(self):
        selection = self.notes_listbox.curselection()
        if selection and "notes" in self.data:
            idx = selection[0]
            if idx < len(self.data["notes"]):
                self.data["notes"][idx]["content"] = self.notes_editor.get("1.0", tk.END)
                self.save_data()
                messagebox.showinfo("Success", "Note saved!")
    
    def on_note_select(self, event):
        selection = self.notes_listbox.curselection()
        if selection and "notes" in self.data:
            idx = selection[0]
            if idx < len(self.data["notes"]):
                content = self.data["notes"][idx].get("content", "")
                self.notes_editor.delete("1.0", tk.END)
                self.notes_editor.insert("1.0", content)
    
    def refresh_notes_list(self):
        self.notes_listbox.delete(0, tk.END)
        if "notes" in self.data:
            for i, note in enumerate(self.data["notes"]):
                self.notes_listbox.insert(tk.END, note.get("title", f"Note {i+1}"))
    
    def create_tasks_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="✓ Tasks")
        
        ctrl_frame = tk.Frame(frame, bg="#0f0f1e")
        ctrl_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(ctrl_frame, text="+ Add Task", command=self.add_task,
                 bg="#667eea", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        self.tasks_container = tk.Frame(frame, bg="#0f0f1e")
        self.tasks_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.refresh_tasks_list()
    
    def add_task(self):
        if "tasks" not in self.data:
            self.data["tasks"] = []
        new_task = {"title": f"Task {len(self.data['tasks']) + 1}",
                   "completed": False, "created": datetime.datetime.now().isoformat()}
        self.data["tasks"].append(new_task)
        self.save_data()
        self.refresh_tasks_list()
    
    def refresh_tasks_list(self):
        for widget in self.tasks_container.winfo_children():
            widget.destroy()
        
        if "tasks" in self.data and self.data["tasks"]:
            for i, task in enumerate(self.data["tasks"]):
                task_frame = tk.Frame(self.tasks_container, bg="#1a1a2e", relief=tk.RAISED, bd=1)
                task_frame.pack(fill=tk.X, pady=5)
                
                var = tk.BooleanVar(value=task.get("completed", False))
                
                def toggle_task(idx=i, v=var):
                    self.data["tasks"][idx]["completed"] = v.get()
                    self.save_data()
                
                cb = tk.Checkbutton(task_frame, text=task.get("title", f"Task {i+1}"),
                                   variable=var, command=toggle_task,
                                   bg="#1a1a2e", fg="#00ff88", font=("Arial", 11), selectcolor="#1a1a2e")
                cb.pack(fill=tk.X, padx=15, pady=10)
    
    def create_tools_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="🔧 Tools")
        
        calc_frame = tk.LabelFrame(frame, text="🧮 Calculator", bg="#1a1a2e",
                                   fg="#00ff88", font=("Arial", 11, "bold"), padx=10, pady=10)
        calc_frame.pack(padx=10, pady=10, fill=tk.X)
        
        calc_input = tk.Entry(calc_frame, bg="#0f0f1e", fg="#00ff88", width=40, font=("Arial", 12))
        calc_input.pack(side=tk.LEFT, padx=10)
        
        calc_result = tk.Label(calc_frame, text="Result: -", bg="#1a1a2e", fg="#00ff88", font=("Arial", 12))
        calc_result.pack(side=tk.LEFT, padx=10)
        
        def calculate():
            try:
                result = eval(calc_input.get())
                calc_result.config(text=f"Result: {result}")
            except:
                calc_result.config(text="Result: Error")
        
        tk.Button(calc_frame, text="Calculate", command=calculate, bg="#667eea", fg="white").pack(side=tk.LEFT, padx=5)
        
        text_frame = tk.LabelFrame(frame, text="📝 Text Tools", bg="#1a1a2e", fg="#00ff88",
                                   font=("Arial", 11, "bold"), padx=10, pady=10)
        text_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        text_input = scrolledtext.ScrolledText(text_frame, height=15, bg="#0f0f1e", fg="#00ff88")
        text_input.pack(fill=tk.BOTH, expand=True, pady=10)
        
        info_label = tk.Label(text_frame, text="", bg="#1a1a2e", fg="#00ff88", font=("Arial", 10))
        info_label.pack()
        
        def update_text_info():
            text = text_input.get("1.0", tk.END)
            chars = len(text) - 1
            words = len(text.split())
            lines = len(text.split("\n")) - 1
            info_label.config(text=f"Characters: {chars} | Words: {words} | Lines: {lines}")
        
        tk.Button(text_frame, text="📊 Analyze", command=update_text_info, bg="#667eea", fg="white").pack()
    
    def create_settings_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="⚙️ Settings")
        
        settings_text = tk.Label(frame, text="""AB1 - APPLICATION SETTINGS

FREE EDITION - COMPLETELY UNRESTRICTED

✓ No Login System
✓ No Account Required
✓ No License Key
✓ No Registration Form
✓ No Trial Period
✓ No Usage Limits
✓ Unlimited Everything
✓ Data Stored Locally
✓ Works 100% Offline
✓ Open Source Code

FEATURES ENABLED:
• Unlimited Notes
• Unlimited Tasks
• Full Tools Access
• All Utilities Available

DATA STORAGE:
• File: AB1_data.json
• Format: JSON
• Location: Application folder
• Backup: Copy the file
• Cloud: Not required
• Privacy: 100% local

SECURITY:
• No telemetry
• No tracking
• No analytics
• No ads
• No pop-ups

USAGE RIGHTS:
✓ Personal Use - YES
✓ Business Use - YES
✓ Commercial Use - YES
✓ Sharing - YES
✓ Modifications - YES
✓ Distribution - YES
✓ No Restrictions - YES

VERSION: 1.0 - Free Edition
LICENSE: Open Source
COST: $0.00
SUPPORT: Community

ENJOY UNLIMITED ACCESS!""", font=("Courier New", 11), fg="#00ff88",
                           bg="#0f0f1e", justify=tk.LEFT, padx=30, pady=30)
        settings_text.pack(fill=tk.BOTH, expand=True)

def main():
    root = tk.Tk()
    app = AB1Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()
