import flet as ft
from views.base import BaseFormView
from components.forms.post import PostForm
from utils.storage import storage
from services.post import post_service
from router import router


class PostFormView(BaseFormView):
    form = PostForm

    def show_action(self):
        if storage.get_or_none('current_post_id') is not None:
            data = post_service.get_post(id=storage.current_post_id)
            self.form_build.set_values(data)
            self.form_build.delete_button.visible = True
            self.form_build.delete_button.on_click = self.delete
            self.form_build.update()

    def hide_action(self):
        storage.pop('current_post_id')
        self.form_build.reset_form()
        self.form_build.delete_button.visible = False

    def submit(self, data):
        if storage.get_or_none('current_post_id') is not None:
            post_service.update_post(storage.get_or_none('current_post_id'), data)
        else:
            post_service.create_post(data)
        router.change_route('/')

    def delete(self, e=None):
        post_service.delete_post(storage.get_or_none('current_post_id'))
        router.change_route('/')
