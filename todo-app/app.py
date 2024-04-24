import flet as ft
from flet.controls import TextField, Checkbox, Row, Column, ElevatedButton, Dialog, OKCancelButtons

def main(page: ft.Page):
    page.title = "Weekly To-Do List"
    page.vertical_alignment = "start"

    # タスクを追加するためのダイアログを表示する関数
    def open_task_dialog(sender, day):
        task_text = TextField(hint_text="Enter a task for " + day, width=300)

        def on_ok(e):
            # チェックボックスとともにタスクを追加
            task = Checkbox(label=task_text.value, value=False)
            task.data = sender.data
            task.on_change = strike_through_task
            sender.data.controls.insert(0, task)
            page.update()

        # ダイアログの設定
        dialog = Dialog(
            title="Add Task",
            content=task_text,
            actions=[OKCancelButtons(on_ok=on_ok)]
        )
        page.dialog = dialog
        dialog.open()

    # チェックボックスの状態が変更されたときの処理
    def strike_through_task(e):
        e.control.label = "<s>" + e.control.label + "</s>" if e.control.value else e.control.label.replace("<s>", "").replace("</s>", "")
        page.update()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # 週の各日にボタンとタスクリストを配置
    days_columns = [Column(content=[ElevatedButton(text=day, on_click=lambda e, day=day: open_task_dialog(e.sender, day), data=Column())]) for day in days]
    days_row = Row(wrap=True, controls=days_columns, spacing=10)

    page.add(days_row)
    page.update()

# Fletアプリケーションを起動
ft.app(target=main)
