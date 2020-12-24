import random

from PySide2 import QtWidgets, QtGui
from PySide2.Qt3DCore import Qt3DCore
from PySide2.Qt3DExtras import Qt3DExtras
from PySide2.Qt3DInput import Qt3DInput
from PySide2.Qt3DRender import Qt3DRender


class TelescopeWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rnd_lat = random.randrange(5200,5300)  / 100.0
        self.rnd_hdg = random.randrange(-300,300)  / 100.0
        self.rnd_dec = random.randrange(-50,50) / 10.0

        print(self.rnd_lat, self.rnd_hdg, self.rnd_dec)

        self.view = Qt3DExtras.Qt3DWindow()
        self.view.defaultFrameGraph().setClearColor(QtGui.QColor("#4d4d4f"))
        self.container = QtWidgets.QWidget.createWindowContainer(self.view)
        self.vLayout = QtWidgets.QVBoxLayout(self)
        self.vLayout.addWidget(self.container, 1)

        self.input_aspect = Qt3DInput.QInputAspect()
        self.view.registerAspect(self.input_aspect)

        self.rootEntity = Qt3DCore.QEntity()
        self.view.setRootEntity(self.rootEntity)

        ###

        cameraEntity = self.view.camera()
        cameraEntity.lens().setPerspectiveProjection(5.0, 16.0 / 9.0, 10, 100000.0)
        cameraEntity.setPosition(QtGui.QVector3D(0, 1000, 50000))
        cameraEntity.setUpVector(QtGui.QVector3D(0, 1, 0))
        cameraEntity.setViewCenter(QtGui.QVector3D(0, 1000, 0))

        self.camController = Qt3DExtras.QOrbitCameraController(self.rootEntity)
        self.camController.setCamera(cameraEntity)

        ###

        self.lightEntity = Qt3DCore.QEntity(self.rootEntity)
        self.light = Qt3DRender.QPointLight(self.lightEntity)
        self.light.setColor("white")
        self.light.setIntensity(1)

        self.lightTransform = Qt3DCore.QTransform(self.lightEntity)
        self.lightTransform.setTranslation(cameraEntity.position())

        self.lightEntity.addComponent(self.light)
        self.lightEntity.addComponent(self.lightTransform)

        ### sky
        # self.skyMesh = Qt3DExtras.QSphereMesh(radius=5000, rings=94, slices=48)
        # self.skyMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#ff0000"))

        # self.skyEntity = Qt3DCore.QEntity(self.rootEntity)
        # self.skyEntity.addComponent(self.skyMesh)
        # self.skyEntity.addComponent(self.skyMaterial)

        ### hdg, x right, y up

        # Cylinder cog = (0,0,0) long direction = y
        self.hdgMesh = Qt3DExtras.QCylinderMesh(length=1200.0, radius=100.0, rings=100, slices=20)
        rotation = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, 0.0, 1.0), 15.0)
        translation = QtGui.QVector3D(0.0, 600.0, 0.0)
        self.hdgTransform = Qt3DCore.QTransform(translation=translation, rotation=rotation)
        self.hdgMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#ff0000"))
        self.hdgEntity = Qt3DCore.QEntity(self.rootEntity)
        self.hdgEntity.addComponent(self.hdgMesh)
        self.hdgEntity.addComponent(self.hdgMaterial)
        self.hdgEntity.addComponent(self.hdgTransform)

        ### lat x up, y left
        self.latMesh = Qt3DExtras.QCylinderMesh(length=200.0, radius=100.0, rings=100, slices=20)
        rotation = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, 0.0, 1.0), 90.0)
        translation = QtGui.QVector3D(0.0, 700.0, 0.0)
        self.latTransform = Qt3DCore.QTransform(rotation=rotation, translation=translation)
        self.latMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#00ff00"))
        self.latEntity = Qt3DCore.QEntity(self.hdgEntity)
        self.latEntity.addComponent(self.latMesh)
        self.latEntity.addComponent(self.latMaterial)
        self.latEntity.addComponent(self.latTransform)

        ### ra x up, y left

        self.raMesh = Qt3DExtras.QCylinderMesh(length=500.0, radius=100.0, rings=100, slices=20)
        rotation1 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, 0.0, -1.0), 90)
        rotation2 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(-1.0, 0.0, 0.0), 90)
        rotation = rotation1 * rotation2
        translation = QtGui.QVector3D(200.0, 0.0, 0.0)
        self.raTransform = Qt3DCore.QTransform(rotation=rotation, translation=translation)
        self.raMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#beb32b"))
        self.raEntity = Qt3DCore.QEntity(self.latEntity)
        self.raEntity.addComponent(self.raMesh)
        self.raEntity.addComponent(self.raMaterial)
        self.raEntity.addComponent(self.raTransform)

        ### dec

        self.decMesh = Qt3DExtras.QCylinderMesh(length=500.0, radius=100.0, rings=100, slices=20)
        rotation = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(1.0, 0.0, 0.0), 90.0)
        translation = QtGui.QVector3D(0.0, 350.0, 0.0)
        self.decTransform = Qt3DCore.QTransform(rotation=rotation, translation=translation)
        self.decMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#0000ff"))
        self.decEntity = Qt3DCore.QEntity(self.raEntity)
        self.decEntity.addComponent(self.decMesh)
        self.decEntity.addComponent(self.decMaterial)
        self.decEntity.addComponent(self.decTransform)

        ### tube

        self.tubeMesh = Qt3DExtras.QCylinderMesh(length=1200.0, radius=100.0, rings=100, slices=20)

        rotation = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(-1.0, 0.0, 0.0), 90.0)
        translation = QtGui.QVector3D(0.0, 350.0, 100.0)
        self.tubeTransform = Qt3DCore.QTransform(rotation=rotation, translation=translation)
        self.tubeMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#ffffff"))
        self.tubeEntity = Qt3DCore.QEntity(self.decEntity)
        self.tubeEntity.addComponent(self.tubeMesh)
        self.tubeEntity.addComponent(self.tubeMaterial)
        self.tubeEntity.addComponent(self.tubeTransform)

        self.ocuMesh = Qt3DExtras.QCylinderMesh(length=100.0, radius=50.0, rings=100, slices=20)
        translation = QtGui.QVector3D(0.0, -650.0, 0.0)
        self.ocuTransform = Qt3DCore.QTransform(translation=translation)
        self.ocuMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#ffffff"))
        self.ocuEntity = Qt3DCore.QEntity(self.tubeEntity)
        self.ocuEntity.addComponent(self.ocuMesh)
        self.ocuEntity.addComponent(self.ocuMaterial)
        self.ocuEntity.addComponent(self.ocuTransform)

        self.fakeMesh = Qt3DExtras.QCuboidMesh(xExtent=500, yExtent=500, zExtent=500)
        translation = QtGui.QVector3D(-1000.0, 0, 0.0)
        self.fakeTransform = Qt3DCore.QTransform(translation=translation)
        self.fakeMaterial = Qt3DExtras.QPhongMaterial(diffuse=QtGui.QColor("#ffffff"))
        self.fakeEntity = Qt3DCore.QEntity(self.rootEntity)
        self.fakeEntity.addComponent(self.fakeMesh)
        self.fakeEntity.addComponent(self.fakeMaterial)
        self.fakeEntity.addComponent(self.fakeTransform)

        self._heading = 0
        self._latitude = 45
        self._ra = 0
        self._dec = 90

    @property
    def pointing(self):
        # Start with x right, y up

        rotation1 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(1.0, 0.0, 0.0), 90-self.rnd_lat)
        rotation2 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, -1.0, 0.0), self.rnd_hdg)
        rotation3 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, -1.0, 0.0), self._heading)
        rotation_hdg = rotation1*rotation2*rotation3

        rotation1 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, 0.0, 1.0), 90.0)
        rotation2 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, -1.0, 0.0), self._latitude)
        rotation_lat = rotation1 * rotation2

        rotation1 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, 0.0, -1.0), 90)
        rotation2 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(-1.0, 0.0, 0.0), 90)
        rotation3 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, 1.0, 0), self._ra)
        rotation_ra = rotation1 * rotation2 * rotation3

        rotation1 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(1.0, 0.0, 0.0), 90.0)
        rotation2 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, 1.0, 0.0), self._dec - 90 + self.rnd_dec)
        rotation_dec = rotation1 * rotation2

        rotation_tube = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(-1.0, 0.0, 0.0), 90.0)

        rotation = rotation_hdg*rotation_lat*rotation_ra*rotation_dec*rotation_tube

        self.fakeTransform.setRotation(rotation)
        vec = rotation.toEulerAngles()

        roll, pitch, yaw = vec.x(), vec.y(), vec.z()
        #print(f"roll_z={roll} pitch_x={pitch} yaw_y={yaw}")

        return roll, pitch, yaw

    @property
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, value):
        self._heading = value
        rotation1 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(1.0, 0.0, 0.0), 90-self.rnd_lat)
        rotation2 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, -1.0, 0.0), self.rnd_hdg)
        rotation3 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, -1.0, 0.0), self._heading)
        rotation = rotation1 * rotation2*rotation3
        self.hdgTransform.setRotation(rotation)

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
        rotation1 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, 0.0, 1.0), 90.0)
        rotation2 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, -1.0, 0.0), self._latitude)

        rotation = rotation1 * rotation2
        self.latTransform.setRotation(rotation)

    @property
    def ra(self):
        return self._ra

    @ra.setter
    def ra(self, value):
        self._ra = value
        rotation1 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, 0.0, -1.0), 90)
        rotation2 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(-1.0, 0.0, 0.0), 90)
        rotation3 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, 1.0, 0), self._ra)
        rotation = rotation1 * rotation2 * rotation3
        self.raTransform.setRotation(rotation)

    @property
    def dec(self):
        return self._dec

    @dec.setter
    def dec(self, value):
        self._dec = value
        rotation1 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(1.0, 0.0, 0.0), 90.0)
        rotation2 = QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(0.0, 1.0, 0.0), self._dec - 90 + self.rnd_dec)

        rotation = rotation1 * rotation2
        self.decTransform.setRotation(rotation)
