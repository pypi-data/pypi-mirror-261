import sys
from pathlib import Path
from typing import Optional

from rdkit import Chem
from PySide6 import QtGui, QtWidgets, QtCore

from maligner.icons import pixmap
from maligner.widgets.MolGridView import MolGridViewWidget


class MainWindow(QtWidgets.QMainWindow):
    # Constructor function
    def __init__(self, filenames: Optional[list[Path | str]] = None):
        super(MainWindow, self).__init__()
        self.loglevels = ["Critical", "Error", "Warning", "Info", "Debug", "Notset"]
        # self.editor = MolEditWidget()
        # self.substructure_selector = SubstructureSelectorDialog()
        self._filenames = filenames
        self.molgridview = MolGridViewWidget()
        self.init_GUI()
        # TODO: selectionChanges ainda não existe
        # self.substructure_selector.selectionChanged.connect(self.setAtomTypeName)
        # self.editor.logger.setLevel(loglevel)

    #Properties
    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        if filename != self._filename:
            self._filename = filename
            self.setWindowTitle(str(filename))

    def init_GUI(self):
        self.setWindowTitle(r"maligner |\ An Open-Source Molecular Alignment Tool")
        self.setWindowIcon(QtGui.QIcon(pixmap("appicon.svg.png")))
        self.setGeometry(400, 400, 700, 500)

        self.setCentralWidget(self.molgridview)

        self.filters = "MOL Files (*.mol *.mol);;Any File (*)"
        self.setup_components()

        self.infobar = QtWidgets.QLabel("")
        self.myStatusBar.addPermanentWidget(self.infobar, 0)

        self.show()

    # Function to setup status bar, central widget, menu bar, tool bar
    def setup_components(self):
        self.myStatusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 10000)

        self.create_actions()
        self.create_menus()
        self.create_tool_bars()

    # Actual menu bar item creation
    def create_menus(self):
        self.fileMenu = self.menuBar().addMenu(self.tr("File"))
        self.toolMenu = self.menuBar().addMenu(self.tr("Tools"))
        self.helpMenu = self.menuBar().addMenu(self.tr("Help"))

        # File
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)

        # Tools
        self.toolMenu.addAction(self.anchorAction)
        self.toolMenu.addAction(self.deleteMoleculeAction)
        self.toolMenu.addAction(self.computeMCSAction)
        self.toolMenu.addAction(self.runAlignmentAction)

        #Help menu
        self.helpMenu.addAction(self.aboutAction)
        self.helpMenu.addAction(self.aboutQtAction)
        #Debug level sub menu
        # self.loglevelMenu = self.helpMenu.addMenu("Logging Level")
        # for loglevel in self.loglevels:
        #     self.loglevelMenu.addAction(self.loglevelactions[loglevel])

    def create_tool_bars(self):
        self.mainToolBar = self.addToolBar('Main')
        #Main action bar
        self.mainToolBar.addAction(self.openAction)
        self.mainToolBar.addAction(self.saveAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.anchorAction)
        self.mainToolBar.addAction(self.computeMCSAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.deleteMoleculeAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.runAlignmentAction)

    def load_mol_file(self, filename):
        self.filename = filename
        mol = Chem.MolFromMolFile(str(self.filename), sanitize=False, strictParsing=False)
        self.statusBar().showMessage(self.tr("File opened"))

    def open_file(self):
        self.molgridview.file_chooser()
        self.molgridview.load_molecules()

    def saveFile(self):
        if self.filename != None:
            Chem.MolToMolFile(self.editor.mol, str(self.filename))
        else:
            self.save_as_file()

    def save_as_file(self):
        self.filename, self.filterName = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                               filter=self.filters)
        if (self.filename != ''):
            if self.filename[-4:].upper() != ".MOL":
                self.filename = self.filename + ".mol"
            Chem.MolToMolFile(self.editor.mol, str(self.filename))
            self.statusBar().showMessage(self.tr("File saved"), 2000)

    def open_selector(self):
        citem = self.molgridview.listview.currentItem()
        if citem is None:
            self.statusBar().showMessage(self.tr("No molecule selected"), 2000)
            return
        self.molgridview.on_mol_double_click(citem)

    def clear_canvas(self):
        self.filenames = []
        self.molgridview.clear()
        self.exit_file()
        self.statusBar().showMessage(self.tr("Molecules removed"), 2000)

    def closeEvent(self, event):
        self.molgridview.clear()
        self.exit_file()
        event.ignore()

    def exit_file(self):

        # self.substructure_selector.close()
        exit(0)  #TODO, how to exit QtWidgets.QApplication from within class instance?

    def about_help(self):
        QtWidgets.QMessageBox.about(
            self, self.tr("About maligner"),
            self.
            tr("""maligner is an Open-Source Molecular Alignment Tool.\n\n\nBased on RDKit: http://www.rdkit.org/\nBased on rdeditor: https://github.com/EBjerrum/rdeditor\nSome icons from: http://icons8.com\nSource code: https://github.com/hellmrf/maligner\n\nReleased under GPL-v3.0."""
              ))

    def set_anchor(self):
        item = self.molgridview.listview.currentItem()
        if item is None:
            self.statusBar().showMessage(self.tr("No molecule selected"), 2000)
            return

        crow = self.molgridview.listview.currentRow()
        self.molgridview.set_anchor(crow)
        self.molgridview.populate_listwidget()

    def compute_MCS(self):
        self.molgridview.compute_MCS()
        self.molgridview.populate_listwidget()

    def run_alignment(self):
        self.molgridview.run_alignment()
        self.molgridview.populate_listwidget()

    def openSubsSelector(self):
        pass
        # self.substructure_selector.show()

    def set_log_level(self):
        pass
        # loglevel = self.sender().objectName().split(':')[-1].upper()
        # self.editor.logger.setLevel(loglevel)

    # Function to create actions for menus and toolbars
    def create_actions(self):
        self.openAction = QtGui.QAction(QtGui.QIcon(pixmap("open.png")),
                                        self.tr('Open'),
                                        self,
                                        shortcut=QtGui.QKeySequence.Open,
                                        statusTip=self.tr("Open an existing file"),
                                        triggered=self.open_file)

        self.saveAction = QtGui.QAction(QtGui.QIcon(pixmap("icons8-Save.png")),
                                        self.tr('Save'),
                                        self,
                                        shortcut=QtGui.QKeySequence.Save,
                                        statusTip=self.tr("Save file"),
                                        triggered=self.saveFile)

        self.exitAction = QtGui.QAction(QtGui.QIcon(pixmap("icons8-Shutdown.png")),
                                        self.tr('Exit'),
                                        self,
                                        shortcut="Ctrl+Q",
                                        statusTip=self.tr("Exit the Application"),
                                        triggered=self.exit_file)

        self.aboutAction = QtGui.QAction(QtGui.QIcon(pixmap("about.png")),
                                         self.tr('About'),
                                         self,
                                         statusTip=self.tr("Displays info about text editor"),
                                         triggered=self.about_help)

        self.aboutQtAction = QtGui.QAction(self.tr("About Qt"),
                                           self,
                                           statusTip=self.tr("Show the Qt library's About box"),
                                           triggered=QtWidgets.QApplication.aboutQt)

        #Misc Actions
        self.deleteMoleculeAction = QtGui.QAction(
            QtGui.QIcon(pixmap("icons8-Trash.png")),
            self.tr('Delete'),
            self,
            shortcut="Ctrl+X",
            statusTip=self.tr("Remove this molecule from canvas Ctrl+X"),
            triggered=self.clear_canvas,
            objectName="Clear Canvas")

        self.anchorAction = QtGui.QAction(
            QtGui.QIcon(pixmap('icons8-Anchor.png')),
            self.tr('Anchor current molecule'),
            self,
            shortcut="A",
            statusTip=self.tr("Set the selected molecule as the anchor for the alignment. (A)"),
            triggered=self.set_anchor,
            objectName="Set Anchor")

        self.openSelectorAction = QtGui.QAction(
            QtGui.QIcon(pixmap('icons8-Molecule.png')),
            'Open Selector',
            self,
            statusTip="Opens the molecule selector for some molecule",
            triggered=self.open_selector,
            objectName="Open selector")

        self.computeMCSAction = QtGui.QAction(
            QtGui.QIcon(pixmap('MCS.png')),
            self.tr('Compute MCS'),
            self,
            shortcut="S",
            statusTip=self.tr(
                "Computes and select the Maximum Common Substructure for the loaded molecules."),
            triggered=self.compute_MCS,
            objectName="Compute MCS")

        self.runAlignmentAction = QtGui.QAction(QtGui.QIcon(pixmap('icons8-Molecule.png')),
                                                self.tr('Run Alignment'),
                                                self,
                                                shortcut="R",
                                                statusTip=self.tr("Align all the molecules."),
                                                triggered=self.run_alignment,
                                                objectName="Run Alignment")

        self.loglevelactions = {}
        for key in self.loglevels:
            self.loglevelactions[key] = QtGui.QAction(key,
                                                      self,
                                                      statusTip="Set logging level to %s" % key,
                                                      triggered=self.set_log_level,
                                                      objectName="loglevel:%s" % key)
        self.loglevelactions["Debug"].setChecked(True)


def launch():
    "Function that launches the mainWindow Application"
    app = QtWidgets.QApplication(sys.argv)

    path = str(Path(__file__).parent / 'translations')
    translator = QtCore.QTranslator(app)
    if translator.load(QtCore.QLocale.system(), '', '', path):
        app.installTranslator(translator)

    mainWindow = MainWindow()

    fn = [
        f"C:/Users/helit/Documentos/UFMG_LOCAL/JOAO_PAULO/PROJETOS/MAlign/molecules/chemsketch_3d_heteroatom/any{i}.mol"
        for i in range(1, 4)
    ]
    # mainWindow.molgridview.filenames = fn
    mainWindow.molgridview.load_molecules()

    sys.exit(app.exec())


if __name__ == '__main__':
    launch()
