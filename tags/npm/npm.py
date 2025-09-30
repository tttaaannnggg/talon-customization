from talon import Context, Module

mod = Module()
mod.tag("npm", desc="npm package manager commands")

ctx = Context()
ctx.matches = r"""
tag: terminal
"""
# Enable npm commands in terminal
ctx.tags = ["user.npm"]


@mod.action_class
class Actions:
    def npm_run_dev():
        """Run npm run dev"""

    def npm_run_lint():
        """Run npm run lint"""

    def npm_run_check_type():
        """Run npm run check-type"""

    def npm_run_script(script: str):
        """Run an npm script"""

    def npm_install():
        """Run npm install"""

    def npm_install_package(package: str):
        """Install a specific npm package"""

    def npm_install_dev_package(package: str):
        """Install a development dependency"""

    def npm_build():
        """Run npm run build"""

    def npm_test():
        """Run npm test"""

    def npm_start():
        """Run npm start"""
