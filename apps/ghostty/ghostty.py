import os

from talon import Context, Module, actions, ui

ctx = Context()
mod = Module()

mod.apps.ghostty = """
os: mac
and app.bundle: com.mitchellh.ghostty
"""

ctx.matches = r"""
app: ghostty
"""

directories_to_remap = {}
directories_to_exclude = {}


@ctx.action_class("edit")
class EditActions:
    def delete_line():
        actions.key("ctrl-u")

    def line_insert_down():
        """Override slap command to use regular enter instead of going to line end first"""
        actions.key("enter")


@ctx.action_class("user")
class UserActions:
    def file_manager_current_path():
        title = ui.active_window().title

        # take the first split for the zsh-based terminal
        if " — " in title:
            title = title.split(" — ")[0]

        if "~" in title:
            title = os.path.expanduser(title)

        if title in directories_to_remap:
            title = directories_to_remap[title]

        if title in directories_to_exclude:
            title = None

        return title

    def file_manager_show_properties():
        """Shows the properties for the file"""

    def file_manager_open_directory(path: str):
        """opens the directory that's already visible in the view"""
        actions.insert("cd ")
        path = f'"{path}"'
        actions.insert(path)
        actions.key("enter")

    def file_manager_open_parent():
        actions.insert("cd ..")
        actions.key("enter")

    def file_manager_select_directory(path: str):
        """selects the directory"""
        actions.insert(path)

    def file_manager_new_folder(name: str):
        """Creates a new folder in a gui filemanager or inserts the command to do so for terminals"""
        name = f'"{name}"'

        actions.insert("mkdir " + name)

    def file_manager_open_file(path: str):
        """opens the file"""
        actions.insert(path)
        actions.key("enter")

    def file_manager_select_file(path: str):
        """selects the file"""
        actions.insert(path)

    def file_manager_refresh_title():
        return

    def tab_jump(number: int):
        actions.key(f"cmd-{number}")

    def tab_final():
        actions.key("cmd-9")

    def terminal_clear_screen():
        """Clear screen"""
        actions.key("ctrl-l")


@ctx.action_class("app")
class AppActions:
    def tab_previous():
        actions.key("cmd-shift-[")

    def tab_next():
        actions.key("cmd-shift-]")

    def tab_close():
        actions.key("cmd-w")

    def tab_open():
        actions.key("cmd-t")

    def window_close():
        actions.key("cmd-w")

    def window_open():
        actions.key("cmd-n")