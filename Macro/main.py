from mainwindow import Ui_MainWindow
from console import Ui_Console
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QMainWindow
from PySide6.QtCore import QFile
import sys
import subprocess
import json
import time
data = {
    "ShakeEnabled": True,
    "CastDuration": 1.0,
    "ShowVisualIndicators": True,
    "ShakeSpeed": 0.5,
    "Control": 0.0,
}
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.runbutton.clicked.connect(self.start_macro)
        #self.ui.browsepath.clicked.connect(self.select_jar_file)
        self.ui.stopbutton.clicked.connect(self.stop_macro)
        self.sikulix_path = "sikulix.jar"
        self.load_data()
        #console
        self.console = QWidget()
        self.consoleui = Ui_Console()
        self.consoleui.setupUi(self.console)
        self.setsimplejson_path = "simplejson"
        self.process = None
    def load_data(self):
        try:
            with open("macro.sikuli/data.json","r") as w:
                data = json.load(w)
                self.ui.castduration.setValue(data.get("CastDuration"))
                self.ui.skipshake.setChecked(data.get("ShakeEnabled"))
                self.ui.latency.setValue(data.get("ShakeSpeed"))
                self.ui.visual_indicators.setChecked(data.get("ShowVisualIndicators"))
                self.ui.control.setValue(data.get("Control"))
        except FileNotFoundError:
            self.show_error_dialog("data.json doesnt exist!")
    def show_error_dialog(self, message):
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)  # Critical icon for error
        error_dialog.setWindowTitle("Error")       # Title for the dialog
        error_dialog.setText("An error occurred!")
        error_dialog.setInformativeText(message)
        error_dialog.setStandardButtons(QMessageBox.Ok)  # Only "OK" button
        error_dialog.exec()    
    def start_macro(self):
        print("Start Macro button clicked!")
        if self.sikulix_path != "":
            data = {
                "CastDuration": self.ui.castduration.value(),
                "ShakeEnabled": self.ui.skipshake.isChecked(),
                "ShakeSpeed": self.ui.latency.value(),
                "ShowVisualIndicators": self.ui.visual_indicators.isChecked(),
                "Control": self.ui.control.value(),
            }
            with open("macro.sikuli/data.json","w") as f:
                json.dump(data,f,indent=4)
            self.ui.runbutton.setEnabled(False)
            self.process = subprocess.Popen(["java", "-jar", self.sikulix_path, "-r", "macro.sikuli", "-c", "-v"])
            time.sleep(5)
            self.ui.stopbutton.setEnabled(True)
        else:
            self.show_error_dialog("Can't run without a path to SikuliX Jar!")
    def stop_macro(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
            print("Terminated")
            self.process = None
            self.ui.stopbutton.setEnabled(False)
            self.ui.runbutton.setEnabled(True)
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())