import flet as ft
from pydantic import ValidationError


class FormInput(ft.UserControl):
    def __init__(self, default_value=None):
        super().__init__()
        self.default_value = default_value
        self.value = default_value

    def on_change(self, e):
        self.value = e.control.value

    def set_error(self, error):
        self.controls[0].error_text = error
        self.update()

    def reset_error(self):
        self.controls[0].error_text = None
        self.update()

    def reset(self):
        self.controls[0].value = self.default_value
        self.value = self.default_value
        self.controls[0].error_text = None
        self.update()

    def set_value(self, value):
        self.controls[0].value = value
        self.value = value
        self.update()


class CheckBoxInput(FormInput):
    def __init__(self, label: str, value: bool = True, data=None):
        super().__init__(value)
        self.label = label
        self.data = data

    def build(self):
        return ft.Checkbox(label=self.label, value=self.value, data=self.data, on_change=self.on_change)


class DropBoxInput(FormInput):
    def __init__(self, label: str, options: list[str], value=None, data=None):
        super().__init__(value)
        self.options = options
        self.label = label
        self.data = data

    def build(self):
        items = []
        for option in self.options:
            items.append(ft.dropdown.Option(option))
        return ft.Dropdown(label=self.label,
                           options=items,
                           value=self.value,
                           data=self.data,
                           on_change=self.on_change)


class StringInput(FormInput):
    def __init__(self, label: str, value: str = '', data=None):
        super().__init__(value)
        self.label = label
        self.value = value
        self.data = data

    def build(self):
        return ft.TextField(label=self.label, value=self.value, data=self.data, on_change=self.on_change)


class SubmitInput(FormInput):
    def __init__(self, label: str, on_click):
        super().__init__()
        self.label = label
        self.on_click = on_click

    def build(self):
        return ft.ElevatedButton(text=self.label, on_click=self.on_click)


class BaseForm(ft.UserControl):
    """
    Базовый класс формы

    Для создания использует pydantic схему

    Дока по полям (mapping полей)
        str -> StringInput

        int -> StringInput

        bool -> CheckBoxInput

        Literal['foo', 'bar'] -> DropBoxInput


    Sample:


    class Form(BaseForm):
        class Schema(BaseModel):
            login: str = Field(title='Введите логин', default='какая то дефолтная строчка')

            password: str = Field(title='string')

            email: EmailStr = Field(title='string')

            num: int = Field(title='integer ')

            dropbox: Literal['foo', 'bar'] = Field(title='selector', default='foo')

            some_bool: bool = Field(title='bool input', default=True)

        schema = Schema

        data = {'login': '123', ....} # <--- если нужна форма с данными (обязательно перечислять все поля)

    """
    schema = None
    values = None

    def __init__(self, submit_func, submit_label='Save', with_submit=True):
        super().__init__()
        self.submit_label = submit_label
        self.submit_func = submit_func
        self.with_submit = with_submit

    def build(self):
        self.main_item = ft.Column(alignment=ft.MainAxisAlignment.CENTER, width=600)
        self.items_dict = {}
        for i in self.schema.schema()['properties']:
            item = self.schema.schema()['properties'][i]
            item_type = item['type']
            item_title = item['title']
            item_default = None
            if self.values is not None:
                item_default = self.values[i]
            elif 'default' in item.keys():
                item_default = item['default']
            if 'enum' in item.keys():
                self.main_item.controls.append(DropBoxInput(item_title, item['enum'], item_default, data=i))
            elif item_type == 'string':
                self.main_item.controls.append(StringInput(item_title, item_default, data=i))
            elif item_type == 'integer':
                self.main_item.controls.append(StringInput(item_title, item_default, data=i))
            elif item_type == 'boolean':
                self.main_item.controls.append(CheckBoxInput(item_title, item_default, data=i))
            self.items_dict[i] = self.main_item.controls[-1]
        if self.with_submit:
            self.main_item.controls.append(SubmitInput(label=self.submit_label, on_click=self.validate_form))
            # кнопка удаления по дефолту невидимая важно задавать видимость потом и ставить событие on_click
            self.delete_button = ft.ElevatedButton(text='Delete', color='red', visible=False)
            self.main_item.controls.append(self.delete_button)
        return ft.Row([self.main_item], alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.CENTER)

    def validate_form(self, e: ft.ControlEvent = None):
        inputs = self.main_item.controls
        data = {}
        for item in inputs:
            if not isinstance(item, SubmitInput) and not isinstance(item, ft.ElevatedButton):
                data[item.data] = item.value
        self.reset_errors()
        try:
            self.schema.model_validate(data)
            self.submit_func(data)
        except ValidationError as error:
            for err in error.errors():
                self.items_dict[err['loc'][0]].set_error(err['msg'])

    def reset_errors(self, e=None):
        for item in self.main_item.controls:
            if isinstance(item, FormInput):
                item.reset_error()

    def reset_form(self, e=None):
        for key in self.items_dict.keys():
            if isinstance(self.items_dict[key], FormInput):
                self.items_dict[key].reset()

    def set_values(self, values):
        for key in self.items_dict.keys():
            if isinstance(self.items_dict[key], FormInput):
                self.items_dict[key].set_value(values[key])
