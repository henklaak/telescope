from PySide2 import QtWidgets, QtGui
from PySide2.Qt3DCore import Qt3DCore
from PySide2.Qt3DExtras import Qt3DExtras
from PySide2.Qt3DInput import Qt3DInput
from PySide2.Qt3DRender import Qt3DRender
from qtpy import QtCore


class ViewWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._x = 0.5
        self._y = 0.5


    def setpos(self, x,y, roll):
        self._x = x
        self._y = y
        self._roll = roll
        self.update()

    def paintEvent(self, event):
        p = QtGui.QPainter(self)
        p.translate(self.width()/2, self.height()/2)
        p.rotate(self._roll * 3.1415/180.0)
        p.setPen(QtGui.QColor('black'))

        x0 = 0
        y0 = 0

        x = self._x * self.size().width()
        y = -self._y * self.size().height()
        x1 = self._x/50 * self.size().width()
        y1 = -self._y/50 * self.size().height()

        p.drawEllipse(QtCore.QPointF(x0,y0),8,8)

        p.setPen(QtGui.QColor('red'))
        p.drawEllipse(QtCore.QPointF(x1,y1), 4,4)

        p.setPen(QtGui.QColor('green'))
        p.drawEllipse(QtCore.QPointF(x,y), 4,4)
