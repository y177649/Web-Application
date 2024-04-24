import flet as ft

def main(page: ft.Page):
    page.title = "Weekly To-Do List"
    page.vertical_alignment = "start"

    def open_task_dialog(sender, day):
        task_text = ft.TextField(hint_text="Enter a task for " + day, width=300)

        def on_ok(e):
            task = ft.Checkbox(label=task_text.value, value=False)
            task.on_change = strike_through_task
            sender.data.controls.append(task)  # コントロールをColumnに追加
            page.update()

        dialog = ft.Dialog(
            title="Add Task",
            content=task_text,
            actions=[ft.OKCancelButtons(on_ok=on_ok)]
        )
        page.dialog = dialog
        dialog.open()

    def strike_through_task(e):
        if e.control.value:
            e.control.label = f"<s>{e.control.label}</s>"
        else:
            e.control.label = e.control.label.replace("<s>", "").replace("</s>", "")
        page.update()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days_columns = []

    for day in days:
        day_column = ft.Column()  # Columnを作成
        button = ft.ElevatedButton(text=day, on_click=lambda e, day=day: open_task_dialog(e.sender, day))
        button.data = day_column  # ボタンに関連するColumnを保存
        day_column.controls.append(button)  # ボタンをColumnのコントロールリストに追加
        days_columns.append(day_column)

    days_row = ft.Row(wrap=True, controls=days_columns, spacing=10)  # RowにすべてのColumnを追加
    page.add(days_row)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
