import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json

# 選択状態を保持するリスト
selected_values = []


def create_genotype_frame(frame, num):
    """遺伝子型選択用のフレームを作成"""
    ctk.CTkLabel(frame, text=f"遺伝子型を選択{num:02}").pack(side="left", padx=10)
    var = tk.IntVar(value=0)
    selected_values.append(var)
    for text, value in [("WT", 1), ("hetero", 2), ("mut", 3)]:
        ctk.CTkRadioButton(frame, text=text, variable=var, value=value).pack(
            side="left", padx=5
        )


def create_button_click():
    """作成ボタンが押されたときの処理"""
    output = {}
    unselected = [i for i, var in enumerate(selected_values, start=1) if var.get() == 0]

    if unselected:
        if not messagebox.askokcancel(
            "警告",
            f"以下の項目が選択されていません: {', '.join(map(str, unselected))}\n未選択の項目には 'no-type' が設定されます",
        ):
            return
        output.update({f"Genotype {i:02}": "no-type" for i in unselected})

    output.update(
        {
            f"Genotype {i:02}": ["WT", "hetero", "mut"][var.get() - 1]
            for i, var in enumerate(selected_values, start=1)
            if var.get() != 0
        }
    )

    # JSON形式で出力
    with open("setting_genotype.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    messagebox.showinfo("成功", "設定ファイルの出力完了")


root = ctk.CTk()
root.geometry("450x600")
root.title("Setting Genotype")
root.resizable(False, False)

scrollable_frame = ctk.CTkScrollableFrame(root, width=280, height=400)
scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

for i in range(16):
    frame = ctk.CTkFrame(scrollable_frame)
    frame.pack(fill="x", pady=5)
    create_genotype_frame(frame, i + 1)

ctk.CTkButton(root, text="設定ファイル作成", command=create_button_click).pack(pady=10)

root.mainloop()
