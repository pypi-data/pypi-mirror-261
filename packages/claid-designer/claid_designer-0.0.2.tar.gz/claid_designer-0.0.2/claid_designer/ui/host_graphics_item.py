from pathlib import Path
from PyQt5.QtWidgets import QMessageBox, QWidget, QGraphicsItem, QGraphicsObject, QVBoxLayout, QGraphicsEllipseItem, QGraphicsTextItem, QPushButton, QGraphicsProxyWidget, QGraphicsPixmapItem
from PyQt5.QtGui import QPen, QColor, QPainterPath, QIcon, QPixmap
from PyQt5.QtCore import Qt, QRectF, pyqtSignal, QPointF
from ui.module_catalog import ModuleCatalog

from ui.module_graphics_item import ModuleGraphicsItem
import os
import sip
class HostGraphicsItem(QGraphicsObject):

    onHostItemMoved = pyqtSignal(QGraphicsObject, QPointF)
    onHostItemResized = pyqtSignal(int, int)
    onAddModuleButtonClicked = pyqtSignal(QGraphicsObject)

    onModuleItemMoved = pyqtSignal(QGraphicsObject, QPointF)
    onChannelClicked = pyqtSignal(QGraphicsObject)

    def __init__(self, hostname: str, x: int, y: int, width: int, height: int, claid, parent=None):
        if parent != None:
            super(HostGraphicsItem, self).__init__(parent)
        else:
            super(HostGraphicsItem, self).__init__()

        # Initialize major host attributes
        self.hostname = hostname
        self.type = ""
        self.is_server = False
        self.server_address = ""
        self.connect_to = ""
        self.modules = list()
        self.claid = claid

        # Set dimensions of modules
        self.module_width = 150
        self.module_height = 100

        # Set border color
        self.color = QColor("#A5C2E8")        

        # Create a QRectF object that represents the host
        self.rectf = QRectF(x, y, width, height)
        self.draw = True
        self.to_draw = self.rectf

        # Create resizeHandle
        self.resizeHandle = QGraphicsEllipseItem(x + self.rect().width() - 10,  y + self.rect().height() - 10, 10, 10, self)
        self.resizeHandle.setBrush(Qt.darkGray)
        self.resizing = False

        self.mouseMove = False

        # Create add_module_button
        current_path = os.path.abspath(os.path.dirname(__file__))
        self.add_module_button = QPushButton(QIcon(os.path.join(current_path, "icons/add_white.svg")), "Add module")
        current_path = os.path.abspath(os.path.dirname(__file__))
        style_sheet_path = os.path.join(current_path, 'style.qss')
        stylesheet = Path(style_sheet_path).read_text()
        self.add_module_button.setStyleSheet(stylesheet)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.add_module_button)
        widget = QWidget()
        widget.setLayout(layout)
        proxy = QGraphicsProxyWidget(self)
        proxy.setWidget(widget)
        proxy.setPos((x + 10), (y + 30))
        self.add_module_button.clicked.connect(self.on_add_module_button_clicked)

        # Set flags
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setAcceptHoverEvents(True)

        self.connected = True

        current_path = os.path.abspath(os.path.dirname(__file__))

        self.icon_connected = QPixmap(os.path.join(current_path, "icons/wifi_connected.png")).scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.icon_disconnected = QPixmap(os.path.join(current_path, "icons/wifi_disconnected.png")).scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.icon_item = QGraphicsPixmapItem(self.icon_connected, self)
        #TODO: VERY IMPORTANT: SET THE POSITION DEPENDING ON TEXT HEIGHT IN PAINTER METHOD
        self.icon_item.setPos(self.rectf.right() - self.icon_connected.width() - 5, self.rectf.top() + 25)


    def on_add_module_button_clicked(self):
        if not self.connected:
            QMessageBox.critical(None, "Error", "Cannot currently add Modules to host \"{}\". Host is not connected.".format(self.hostname))
            return 
        
        self.module_catalog = ModuleCatalog(self, self.claid, self.hostname)
        self.module_catalog.show()
        self.module_catalog.on_catalog_closed.connect(self.on_catalog_closed)

    def on_catalog_closed(self):
        print("Catalog closed")
        sip.delete(self.module_catalog)

    def add_module(self, module_id, module_type, x, y, input_channels, output_channels, \
                   input_channel_types, output_channel_types, properties, property_descriptions, property_hints):
        
        module_graphics_item = ModuleGraphicsItem(module_id, module_type, x, y, self.module_width, self.module_height, \
                                                  input_channels, output_channels, input_channel_types, output_channel_types, \
                                                    properties, property_descriptions, property_hints, self)
        self.modules.append(module_graphics_item)
    
        for channel in module_graphics_item.input_channel_map.values():
            channel.onChannelClicked.connect(self.onChannelClickedSlot)
        for channel in module_graphics_item.output_channel_map.values():
            channel.onChannelClicked.connect(self.onChannelClickedSlot)
        module_graphics_item.onModuleItemMoved.connect(self.onModuleItemMovedSlot)

        return module_graphics_item
    
    def onChannelClickedSlot(self, channel):
        self.onChannelClicked.emit(channel)

    def onModuleItemMovedSlot(self, graphics_item, change):
        self.onModuleItemMoved.emit(graphics_item, change)

    def boundingRect(self):
        return self.rectf
    
    def rect(self):
        return self.rectf
    
    def setRect(self, x, y, new_width, new_height):
        self.draw = False
        self.to_draw = QRectF(x, y, new_width, new_height)
        self.update()

    def paint(self, painter, option, widget):

        if self.draw:
            self.rectf = self.to_draw
            self.repaint(painter)
        else:
            self.draw = True
            self.update()

    def mousePressEvent(self, event):
        # Clear selection of other GraphicsItems
        if not self.isSelected():
            self.scene().clearSelection()

        if self.resizeHandle.isUnderMouse():
            self.resizing = True
        elif event.button() == Qt.LeftButton:
            self.mousePressPos = event.pos()
            self.origPos = self.pos()
            self.mouseMove = False
        super(HostGraphicsItem, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.resizing:
            self.resizeItem(event.pos())
        elif event.buttons() == Qt.LeftButton:
            self.mouseMove = True
            super(HostGraphicsItem, self).mouseMoveEvent(event)
        else:
            super(HostGraphicsItem, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.resizing:
            self.resizing = False
        if event.button() == Qt.LeftButton:
            if not self.mouseMove:
                # Handle click event here if needed
                pass
        super(HostGraphicsItem, self).mouseReleaseEvent(event)

    def hoverMoveEvent(self, event):
        if self.resizeHandle.isUnderMouse():
            self.setCursor(Qt.SizeFDiagCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
        super(HostGraphicsItem, self).hoverMoveEvent(event)

    #TODO: Ensure that host always contains all modules + some offset
    def resizeItem(self, pos):
        new_width = max(pos.x() - self.rect().x(), 10)
        new_height = max(pos.y() - self.rect().y(), 10)
        self.setRect(self.rect().x(), self.rect().y(), new_width, new_height)
        self.resizeHandle.setRect(self.rect().x() + self.rect().width() - 10, self.rect().y() + self.rect().height() - 10, 10, 10)
        self.onHostItemResized.emit(new_width, new_height)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            new_pos = value
            # TODO: Implement restrictMovement to ensure that host objects cannot overlap
            # changed_pos = self.restrictMovement(new_pos)
            absolute_change = new_pos - self.pos()
            self.onHostItemMoved.emit(self, absolute_change)
            return super(HostGraphicsItem, self).itemChange(change, new_pos)
        else:
            return super(HostGraphicsItem, self).itemChange(change, value)

    def repaint(self, painter):
        # Set border thickness
        border_thickness = 3

        # Draw rectangle
        corner_radius = 10
        rect = self.rect()
        painter.setPen(QPen(self.color, border_thickness))
        painter.setBrush(Qt.white)
        painter.drawRoundedRect(rect, corner_radius, corner_radius)

        # Draw smaller rectangle at the top for the text
        text_dimensions = painter.boundingRect(QRectF(), Qt.AlignLeft, self.hostname)   
        text_rect_height = 1.35 * text_dimensions.height()
        text_rect = QRectF(rect.x(), rect.y(), rect.width(), text_rect_height)
        path = QPainterPath()
        path.moveTo(text_rect.left(), text_rect.top() + corner_radius)
        path.arcTo(text_rect.left(), text_rect.top(), 2 * corner_radius, 2 * corner_radius, 180, -90)
        path.lineTo(text_rect.right() - corner_radius, text_rect.top())
        path.arcTo(text_rect.right() - 2 * corner_radius, text_rect.top(), 2 * corner_radius, 2 * corner_radius, 90, -90)
        path.lineTo(text_rect.right(), text_rect.bottom())
        path.lineTo(text_rect.left(), text_rect.bottom())
        path.closeSubpath()
        painter.setBrush(self.color)
        painter.drawPath(path)

        # Set color for text
        painter.setPen(Qt.white)

        # Draw text of host name
        x = rect.x()
        y = rect.y()
        width = rect.width()
        x_position = x + (width / 2) - (text_dimensions.width() / 2)
        y_position = y + text_dimensions.height()
        painter.drawText(int(x_position), int(y_position), self.hostname)        

    def get_color(self, ) -> QColor:
        color = self.color
        return color

    def set_color(self, color: QColor) -> None:
        self.color = color
        # Use this color for errors or warnings: 
        self.update()

    def set_name(self, hostname: str):
        self.hostname = hostname
        self.update()

    def get_name(self) -> str:
        return self.hostname
    
    def set_type(self, type: str):
        self.type = type

    def get_type(self) -> str:
        return self.type

    def set_is_server(self, is_server: bool):
        self.is_server = is_server

    def get_is_server(self) -> bool:
        return self.is_server

    def set_server_address(self, server_address: str):
        self.server_address = server_address

    def get_server_address(self) -> str:
        return self.server_address
    
    def set_connect_to(self, connect_to: str):
        self.connect_to = connect_to
    
    def get_connect_to(self) -> str:
        return self.connect_to

    def get_modules(self):
        return self.modules
    
    def does_module_with_name_exist(self, module_name: str):

        for module in self.modules:
            if module.get_id() == module_name:
                return True

        return False
    
    def delete_module(self, module_id: str) -> None:
        for module in self.modules:
            if module.get_id() == module_id:
                self.modules.remove(module)
    
    def set_connected(self):
        self.set_color(QColor("#A5C2E8"))
        self.connected = True
        self.icon_item.setPixmap(self.icon_connected)

    def set_disconnected(self):
        self.set_color(QColor("#A50000"))
        self.connected = False
        self.icon_item.setPixmap(self.icon_disconnected)

    def is_connected(self):
        return self.connected

