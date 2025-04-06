import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json

# 選択状態を保持するリスト
selected_values = []


def create_genotype_frame(parent, num):
    """遺伝子型選択用のフレームを作成"""
    ctk.CTkLabel(parent, text=f"遺伝子型を選択{num:02}").pack(side="left", padx=10)
    var = tk.IntVar(value=0)
    selected_values.append(var)
    for text, value in [("WT", 1), ("hetero", 2), ("mut", 3)]:
        ctk.CTkRadioButton(parent, text=text, variable=var, value=value).pack(
            side="left", padx=5
        )


def generate_output(file_name):
    """選択された遺伝子型をJSON形式で出力"""
    unselected = [i for i, var in enumerate(selected_values, start=1) if var.get() == 0]
    output = {f"Genotype {i:02}": "no-type" for i in unselected}
    output.update(
        {
            f"Genotype {i:02}": ["WT", "hetero", "mut"][var.get() - 1]
            for i, var in enumerate(selected_values, start=1)
            if var.get() != 0
        }
    )
    file_path = f"setting_genotype_{file_name}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    return file_path


def create_button_click():
    """作成ボタンが押されたときの処理"""
    file_name = file_name_var.get().strip()
    if not file_name:
        messagebox.showerror("エラー", "ファイル名を入力してください")
        return

    unselected = [i for i, var in enumerate(selected_values, start=1) if var.get() == 0]
    if unselected and not messagebox.askokcancel(
        "警告",
        f"以下の項目が選択されていません: {', '.join(map(str, unselected))}\n未選択の項目には 'no-type' が設定されます",
    ):
        return

    file_path = generate_output(file_name)
    messagebox.showinfo("成功", f"設定ファイルの出力完了:\n{file_path}")


root = ctk.CTk()
root.geometry("450x600")
root.title("Setting Genotype")
root.resizable(False, False)

# ファイル名入力
file_name_var = tk.StringVar(value="")
file_name_frame = ctk.CTkFrame(root)
file_name_frame.pack(pady=5)
ctk.CTkLabel(file_name_frame, text="設定ファイル名入力:").pack(side="left", padx=5)
ctk.CTkEntry(file_name_frame, textvariable=file_name_var).pack(side="left", padx=5)

# 遺伝子型選択
scrollable_frame = ctk.CTkScrollableFrame(root, width=280, height=400)
scrollable_frame.pack(padx=5, fill="both", expand=True)
for i in range(16):
    frame = ctk.CTkFrame(scrollable_frame)
    frame.pack(fill="x", pady=5)
    create_genotype_frame(frame, i + 1)

ctk.CTkButton(root, text="設定ファイル作成", command=create_button_click).pack(pady=5)

root.mainloop()
