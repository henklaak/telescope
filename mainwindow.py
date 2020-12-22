from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.Qt3DCore import Qt3DCore

from mainwindow_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.step_small = 0.01
        self.step_normal = 0.1
        self.step_large = 1.0

        self._telescope_hdg = 0
        self._telescope_lat = 45
        self._telescope_ra = 0
        self._telescope_dec = 90

        Qt3DCore.QEntity()
        self.update()

    def update(self):
        print(self._telescope_hdg, self._telescope_lat, self._telescope_ra, self._telescope_dec)
        self.edtHdg.setText(f"{self._telescope_hdg:.3f}")
        self.edtLat.setText(f"{self._telescope_lat:.3f}")
        self.edtRA.setText(f"{self._telescope_ra:.3f}")
        self.edtDec.setText(f"{self._telescope_dec:.3f}")

    @property
    def telescope_hdg(self):
        return self._telescope_hdg

    @telescope_hdg.setter
    def telescope_hdg(self, value):
        self._telescope_hdg = value
        self.update()

    @property
    def telescope_lat(self):
        return self._telescope_lat

    @telescope_lat.setter
    def telescope_lat(self, value):
        self._telescope_lat = value
        self.update()

    @property
    def telescope_ra(self):
        return self._telescope_ra

    @telescope_ra.setter
    def telescope_ra(self, value):
        self._telescope_ra = value
        self.update()

    @property
    def telescope_dec(self):
        return self._telescope_dec

    @telescope_dec.setter
    def telescope_dec(self, value):
        self._telescope_dec = value
        self.update()

    ###

    @QtCore.Slot()
    def on_btnHdgNeg3_clicked(self):
        self.telescope_hdg -= self.step_large

    @QtCore.Slot()
    def on_btnHdgNeg2_clicked(self):
        self.telescope_hdg -= self.step_normal

    @QtCore.Slot()
    def on_btnHdgNeg1_clicked(self):
        self.telescope_hdg -= self.step_small

    @QtCore.Slot()
    def on_btnHdgPos1_clicked(self):
        self.telescope_hdg += self.step_small

    @QtCore.Slot()
    def on_btnHdgPos2_clicked(self):
        self.telescope_hdg += self.step_normal

    @QtCore.Slot()
    def on_btnHdgPos3_clicked(self):
        self.telescope_hdg += self.step_large

    @QtCore.Slot()
    def on_btnLatNeg3_clicked(self):
        self.telescope_lat -= self.step_large

    @QtCore.Slot()
    def on_btnLatNeg2_clicked(self):
        self.telescope_lat -= self.step_normal

    @QtCore.Slot()
    def on_btnLatNeg1_clicked(self):
        self.telescope_lat -= self.step_small

    @QtCore.Slot()
    def on_btnLatPos1_clicked(self):
        self.telescope_lat += self.step_small

    @QtCore.Slot()
    def on_btnLatPos2_clicked(self):
        self.telescope_lat += self.step_normal

    @QtCore.Slot()
    def on_btnLatPos3_clicked(self):
        self.telescope_lat += self.step_large

    @QtCore.Slot()
    def on_btnRANeg3_clicked(self):
        self.telescope_ra -= self.step_large

    @QtCore.Slot()
    def on_btnRANeg2_clicked(self):
        self.telescope_ra -= self.step_normal

    @QtCore.Slot()
    def on_btnRANeg1_clicked(self):
        self.telescope_ra -= self.step_small

    @QtCore.Slot()
    def on_btnRAPos1_clicked(self):
        self.telescope_ra += self.step_small

    @QtCore.Slot()
    def on_btnRAPos2_clicked(self):
        self.telescope_ra += self.step_normal

    @QtCore.Slot()
    def on_btnRAPos3_clicked(self):
        self.telescope_ra += self.step_large

    @QtCore.Slot()
    def on_btnDecNeg3_clicked(self):
        self.telescope_dec -= self.step_large

    @QtCore.Slot()
    def on_btnDecNeg2_clicked(self):
        self.telescope_dec -= self.step_normal

    @QtCore.Slot()
    def on_btnDecNeg1_clicked(self):
        self.telescope_dec -= self.step_small

    @QtCore.Slot()
    def on_btnDecPos1_clicked(self):
        self.telescope_dec += self.step_small

    @QtCore.Slot()
    def on_btnDecPos2_clicked(self):
        self.telescope_dec += self.step_normal

    @QtCore.Slot()
    def on_btnDecPos3_clicked(self):
        self.telescope_dec += self.step_large
