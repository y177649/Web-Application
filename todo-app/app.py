import flet as ft

def main(page: ft.Page):
    page.title = "Weekly To-Do List"
    page.vertical_alignment = "start"

    def add_task(control, text_field):
        if text_field.value.strip() != "":
            task = ft.Checkbox(label=text_field.value, value=False)
            task.on_change = strike_through_task
            control.controls.append(task)
            text_field.value = ""  # テキストフィールドをクリア
            page.update()

    def strike_through_task(e):
        if e.control.value:
            e.control.text_color = 0xAAAAAA  # 灰色に設定
        else:
            e.control.text_color = 0x000000  # 黒色に戻す
        page.update()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days_columns = []

    for day in days:
        day_column = ft.Column(spacing=5)  # Columnを作成
        label = ft.Text(value=day, size=20, weight="bold")
        text_field = ft.TextField(width=150)
        add_button = ft.ElevatedButton(text="Add Task", on_click=lambda e, day_column=day_column, text_field=text_field: add_task(day_column, text_field))
        day_column.controls.extend([label, text_field, add_button])
        days_columns.append(day_column)

    days_row = ft.Row(wrap=True, controls=days_columns, spacing=10)  # RowにすべてのColumnを追加
    page.add(days_row)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
