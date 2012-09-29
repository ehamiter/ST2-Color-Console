import os
import sublime, sublime_plugin


class ColorConsoleCommand(sublime_plugin.WindowCommand):
	def run(self):
		widgetSettings = self.createNewWidgetSettings()
		widgetSettingsLocation = os.path.join(sublime.packages_path(), "User", "Widget.sublime-settings")
		text_file = open(widgetSettingsLocation, "w")
		text_file.write(widgetSettings)
		text_file.close()
		view = self.window.open_file(widgetSettingsLocation)

	def createNewWidgetSettings(self):
		base_settings = sublime.load_settings("Base File.sublime-settings")
		current_theme = base_settings.get("color_scheme")
		
		widgetSettings = """{
	"syntax": \""""
		widgetSettings += os.path.join(sublime.packages_path(), "ColorConsole", "Console.tmLanguage")
		widgetSettings += """\",
	"color_scheme": \""""
		widgetSettings += current_theme
		widgetSettings += """\"
}
"""
		return widgetSettings

