import tkinter as tk
from tkinter import messagebox, simpledialog
import random

def failist_to_dict(f:str):
    riik_pealinn = {}
    pealinn_riik = {}
    riigid = []
    with open(f, 'r', encoding="utf-8-sig") as file:
        for line in file:
            k, v = line.strip().split('-')
            riik_pealinn[k] = v
            pealinn_riik[v] = k
            riigid.append(k)
    return riik_pealinn, pealinn_riik, riigid

riik_pealinn, pealinn_riik, riigid = failist_to_dict("TARgv24_Python/dictionary/riigid_pealinnad.txt")
pealinnad = list(riik_pealinn.values())

def leida_pealinn_või_riik():
    päring = simpledialog.askstring("otsing", "sisesta riik või pealinn (eesti keeles, suure algustähega!):")
    if not päring:
        return
    
    if päring in riik_pealinn:
        messagebox.showinfo("tulemus", f"{päring}: {riik_pealinn[päring]}")
    elif päring in pealinn_riik:
        messagebox.showinfo("tulemus", f"{päring}: {pealinn_riik[päring]}")
    else:
        lisa(päring)

def lisa(päring):
    response = messagebox.askyesno("ei leitud!", "kas tahad lisada seda sõnastikusse?")
    if response:
        if päring.istitle():
            capital = simpledialog.askstring("lisamine", "sisestage selle riigi pealinn:")
            riik_pealinn[päring] = capital
            pealinn_riik[capital] = päring
        else:
            riik = simpledialog.askstring("lisamine", "sisestage selle pealinna riik:")
            riik_pealinn[riik] = päring
            pealinn_riik[päring] = riik
        messagebox.showinfo("edukas", "andmed on lisatud!")

def muuda_lisa():
    riik = simpledialog.askstring("parandamine", "sisesta riik, milline tahad parandada:")
    if riik in riik_pealinn:
        uus_pealinn = simpledialog.askstring("parandamine", f"sisesta uus pealinn {riik}-le:")
        vana_pealinn = riik_pealinn[riik]
        riik_pealinn[riik] = uus_pealinn
        pealinn_riik.pop(vana_pealinn)
        pealinn_riik[uus_pealinn] = riik
        with open("TARgv24_Python/dictionary/riigid_pealinnad.txt", 'w', encoding="utf-8-sig") as file:
            for country, capital in riik_pealinn.items():
                file.write(f"{country}-{capital}\n")
        messagebox.showinfo("edukas", "andmed on lisatud!")
    else:
        messagebox.showerror("viga", "riik ei leitud!")

def viktoriin():
    tulemus = 0
    kokku = 10
    keys = list(riik_pealinn.keys())
    random.shuffle(keys)
    
    for riik in keys[:10]:
        answer = simpledialog.askstring("viktoriin", f"sisesta pealinn: {riik}")
        if answer and answer.lower() == riik_pealinn[riik].lower():
            tulemus += 1
            messagebox.showinfo("tulemus", "õige!!!")
        else:
            messagebox.showerror("tulemus", f"vale! :(\nõige vastus: {riik_pealinn[riik]}")
    
    percentage = (tulemus / kokku) * 100
    messagebox.showinfo("kokkuvõte", f"sinu tulemus: {tulemus} punkt(-id) {kokku}-st ({percentage:.2f}%)")

menüü = tk.Tk()
menüü.title("riigide & pealinnade sõnastik")
menüü.geometry("300x300")

tk.Button(menüü, text="leida pealinn/riik", command=leida_pealinn_või_riik).pack(pady=10)
tk.Button(menüü, text="paranda viga", command=muuda_lisa).pack(pady=10)
tk.Button(menüü, text="pane oma teadmised proovile :)", command=viktoriin).pack(pady=10)
tk.Button(menüü, text="välja", command=menüü.quit).pack(pady=10)

menüü.mainloop()