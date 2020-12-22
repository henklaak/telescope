from PySide2 import QtWidgets, QtGui
from PySide2.Qt3DCore import Qt3DCore
from PySide2.Qt3DExtras import Qt3DExtras
from PySide2.Qt3DInput import Qt3DInput
from PySide2.Qt3DRender import Qt3DRender


class TelescopeWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = Qt3DExtras.Qt3DWindow()
        self.view.defaultFrameGraph().setClearColor(QtGui.QColor("#4d4d4f"))
        self.container = QtWidgets.QWidget.createWindowContainer(self.view)
        self.vLayout = QtWidgets.QVBoxLayout(self)
        self.vLayout.addWidget(self.container, 1)

        self.input_aspect = Qt3DInput.QInputAspect()
        self.view.registerAspect(self.input_aspect)

        self.rootEntity = Qt3DCore.QEntity()

        cameraEntity = self.view.camera()

        cameraEntity.lens().setPerspectiveProjection(45.0, 16.0 / 9.0, 0.1, 1000.0)
        cameraEntity.setPosition(QtGui.QVector3D(20, 20, 20.0))
        cameraEntity.setUpVector(QtGui.QVector3D(0, 1, 0))
        cameraEntity.setViewCenter(QtGui.QVector3D(0, 0, 0))

        self.lightEntity = Qt3DCore.QEntity(self.rootEntity)
        self.light = Qt3DRender.QPointLight(self.lightEntity)
        self.light.setColor("white")
        self.light.setIntensity(1)
        self.lightEntity.addComponent(self.light)

        self.lightTransform = Qt3DCore.QTransform(self.lightEntity)
        self.lightTransform.setTranslation(cameraEntity.position())
        self.lightEntity.addComponent(self.lightTransform)

        ###
        self.camController = Qt3DExtras.QOrbitCameraController(self.rootEntity)
        self.camController.setCamera(cameraEntity)

        self.view.setRootEntity(self.rootEntity)

        ###

        self.torus = Qt3DExtras.QTorusMesh(radius=1.0,
                                           minorRadius=0.4,
                                           rings=100,
                                           slices=20)

        self.torusTransform = Qt3DCore.QTransform(
            scale=2.0,
            rotation=QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, 1.0, 0.0), 0.0),
            translation=QtGui.QVector3D(0.0, 0.0, 0.0))

        self.torusMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#beb32b"))

        self.torusEntity = Qt3DCore.QEntity(self.rootEntity)
        self.torusEntity.addComponent(self.torus)
        self.torusEntity.addComponent(self.torusMaterial)
        self.torusEntity.addComponent(self.torusTransform)