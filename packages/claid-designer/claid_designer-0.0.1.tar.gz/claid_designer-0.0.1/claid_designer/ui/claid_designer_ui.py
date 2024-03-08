import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGraphicsScene, QGraphicsView, QVBoxLayout, QHBoxLayout, QGraphicsPathItem, QPushButton, QFileDialog, QMessageBox, QAction
from PyQt5.QtGui import QPainter, QPainterPath, QColor, QPen, QBrush, QWindow, QKeySequence, QPolygonF
from PyQt5.QtCore import Qt, QPointF, QEvent, QCoreApplication

from ui.module_catalog import ModuleCatalog

import os
sys.path.append(os.getcwd() + "/dispatch/python")

from ui.host_graphics_item import HostGraphicsItem
from ui.module_graphics_item import ModuleGraphicsItem
from ui.channel import Channel
from ui.path_graphics_item import PathGraphicsItem

from claid import CLAID
from claid.module.module_factory import ModuleFactory
from claid.dispatch.proto.claidservice_pb2  import CLAIDConfig, HostConfig, ModuleConfig, ModuleAnnotation, DataPackage
from config.config import Config



class CLAIDDesignerUI(QMainWindow):
    def __init__(self, claid, server_ip):
        super(CLAIDDesignerUI, self).__init__()     

        self.claid = claid
        self.server_ip = server_ip

        self.claid.register_on_connected_to_server_callback(self.__on_connected_to_server)
        self.claid.register_on_disconnected_from_server_callback(self.__on_disconnected_from_server)

        # No channel clicked at beginning
        self.firstClickedChannel = None

        # Set flags
        QApplication.instance().installEventFilter(self)

        # Save all hosts and paths in a dictionary
        self.hosts = dict()
        self.paths = dict()

        # Initialize the UI
        self.initUI()

        self.closeEvent = self.exit_application

    def exit_application(self, event):
        os._exit(0)

    def initUI(self):
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing, True)

        # Add the view to the layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view)

        # Set a central widget
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)

        # Create button to start programming of the device
        self.program_device_button = QPushButton("Program devices")

        current_path = os.path.abspath(os.path.dirname(__file__))
        style_sheet_path = os.path.join(current_path, 'style.qss')
        stylesheet = Path(style_sheet_path).read_text()
        self.program_device_button.setStyleSheet(stylesheet)
        self.program_device_button.setFixedWidth(500)
        hbox = QHBoxLayout() 
        hbox.addStretch(1) 
        hbox.addWidget(self.program_device_button)
        hbox.addStretch(1)
        self.layout.addLayout(hbox)
        self.program_device_button.clicked.connect(self.program_device_button_clicked)

        # Create menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        open_config = QAction("Open Configuration", self)
        open_config.setShortcut(QKeySequence.Open)
        open_config.triggered.connect(self.openConfig)
        file_menu.addAction(open_config)

        save_config = QAction("Save Configuration", self)
        save_config.setShortcut(QKeySequence.Save)
        save_config.triggered.connect(self.saveConfig)
        file_menu.addAction(save_config)

        # Create two hosts, define their properties, and add them to the scene
        host1 = HostGraphicsItem("Smartwatch", 0, 0, 550, 450, self.claid)
        host2 = HostGraphicsItem("Laptop", 600, 0, 550, 450, self.claid)
        
        host1.set_type("android")
        host1.set_is_server(True)
        host1.set_server_address(self.server_ip)

        host2.set_type("laptop")
        host2.set_connect_to("Smartwatch")
        host2.set_is_server(False)

        host1.onChannelClicked.connect(self.onChannelClicked)
        host1.onModuleItemMoved.connect(self.onModuleItemMoved)

        host2.onChannelClicked.connect(self.onChannelClicked)
        host2.onModuleItemMoved.connect(self.onModuleItemMoved)

        self.hosts["Smartwatch"] = host1
        self.hosts["Laptop"] = host2

        #TODO: delete module instances as soon as modulecatalog is available
        # host1.add_module("Module1", "type1", 175, 60, ["input1", "input2", "input3", "input4"], ["output1", "output2", "output3"])
        # host1.add_module("Module2", "type2", 175, 190, ["input1", "input2"], ["output1", "output2"])
        # host1.add_module("Module3", "type2", 175, 320, ["input1", "input2"], ["output1", "output2"])
        # host2.add_module("Module4", "type1", 175, 60, ["input1", "input2"], ["output1", "output2"])
        # host2.add_module("Module5", "type2", 175, 190, ["input1", "input2"], ["output1", "output2"])
        # host2.add_module("Module6", "type3", 175, 320, ["input1", "input2"], ["output1", "output2"])

        self.scene.addItem(host1)
        self.scene.addItem(host2)

        self.__on_disconnected_from_server()



    def onChannelClicked(self, channel):
        if self.firstClickedChannel == None:
            self.firstClickedChannel = channel
        else:
            self.createPath(self.firstClickedChannel, channel)
            self.firstClickedChannel = None

    def eventFilter(self, source, event):
        # Ensures that self.firstClickedChannel is set to None when clicking on the scene
        if isinstance(source, QWindow):
            return super().eventFilter(source, event)
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
                pos = self.view.mapToScene(event.pos())
                # Find the item at the clicked position
                items = self.scene.items(pos)
                if items:
                    channel_found = None
                    for item in items:
                        if item != None and isinstance(item, Channel):
                            channel_found = item
                            break                     
                    if channel_found == None:
                        self.firstClickedChannel = None
        return super().eventFilter(source, event)
    
    def makeUniqueChannelTuple(self, channel1: Channel, channel2: Channel):
        # Sort the channels as following: channel1 is output channel, channel2 is input channel
        # Alternatively: Sort the channels based on memory address, hence making
        # This function work regardless of the order the channels were passed.
        if channel1 in channel1.parentItem().input_channel_map.values():
            channel1,channel2 = channel2,channel1
        
        return (channel1, channel2)

    # Draw path between two channels
    def createPath(self, channel1: Channel, channel2: Channel):
        # Check if channels are children of the same module
        if channel1.parentItem() == channel2.parentItem():
            return
        
        # Ensure that channel1 is an output channel and channel2 an input channel
        if channel1 in channel1.parentItem().output_channel_map.values() and channel2 in channel2.parentItem().output_channel_map.values():
            return
        elif channel1 in channel1.parentItem().input_channel_map.values() and channel2 in channel2.parentItem().input_channel_map.values():
            return
        elif channel1 in channel1.parentItem().input_channel_map.values():
            temp_channel = channel1
            channel1 = channel2
            channel2 = temp_channel

        print("Checking type")
        if not channel1.has_same_data_type_as_channel(channel2):
            QMessageBox.critical(None, "Invalid channel types", "Cannot connect channel \"{}\" to channel \"{}\" due to incompatible channel types.\n\n"\
                                 "Channel \"{}\" has data type \"{}\", but Channel \"{}\" has data type \"{}\".".format(channel1.get_name(), channel2.get_name(),\
                                                                                                                        channel1.get_name(), channel1.get_data_type_name(),
                                                                                                                        channel2.get_name(), channel2.get_data_type_name()))
            return
    
        print("Checked type")

        # Check if this path is already existing
        if self.pathExists(channel1, channel2):
            return

        # Calculate the path
        path = self.calculatePath(channel1, channel2)         
        
        # Create a QGraphicsPathItem
        pathItem = PathGraphicsItem(path)

        # Stack the path before hosts
        for host in self.hosts.values():
            pathItem.stackBefore(host)

        # Add the path to the scene
        self.scene.addItem(pathItem)
        
        # Add the path to the path dictionary in current class && ModuleGraphicsItem
        # && Add the modules to the PathGraphicsItem
        self.paths[self.makeUniqueChannelTuple(channel1, channel2)] = pathItem
        channel1.parentItem().add_path(pathItem)
        channel2.parentItem().add_path(pathItem)
        pathItem.set_output_module(channel1.parentItem())
        pathItem.set_input_module(channel2.parentItem())

        # Connect a signal that is emitted on deletion of the path
        channel1.parentItem().pathDeleted.connect(self.delete_path)

    def calculatePath(self, channel1: Channel, channel2: Channel):
        #TODO: NEED TO ADJUST PATH IN EDGE CASES TO INCLUDE FULL ARROWS
        # Ensure that channel1 is an output channel and channel2 an input channel
        if channel1 in channel1.parentItem().input_channel_map.values():
            temp_channel = channel1
            channel1 = channel2
            channel2 = temp_channel
       
        # Create a QPainterPath
        path = QPainterPath()

        # Calculate start and end points
        ch1_x = channel1.boundingRect().right()
        ch2_x = channel2.boundingRect().left()
        ch1_y = channel1.boundingRect().top() + (channel1.boundingRect().height() / 2)
        ch2_y = channel2.boundingRect().top() + (channel2.boundingRect().height() / 2) 
        start = channel1.mapToScene(ch1_x, ch1_y)
        end = channel2.mapToScene(ch2_x, ch2_y)

        # Minimum offset between modules and path
        offset = 10

        # Arrow head length
        arrow_length = 8

        # Case 1: Output channel module is to the left of the input channel module
        if (channel1.scenePos().x() + channel1.parentItem().circle_diameter) <= channel2.scenePos().x():
            # Calculate midpoints
            midX = (start.x() + end.x()) / 2
            midY1 = start.y()
            midY2 = end.y()
            midpoint1 = QPointF(midX, midY1)
            midpoint2 = QPointF(midX, midY2)

            # Construct the path
            path.moveTo(start)
            path.lineTo(midpoint1)
            path.moveTo(midpoint1)
            path.lineTo(midpoint2)
            path.moveTo(midpoint2)
            path.lineTo(end)

        # Case 2: Output channel module is to the right of the input channel module
        else:
            # Case 2_1: Output channel module is positioned above input channel module
            if channel1.parentItem().scenePos().y() <= channel2.parentItem().scenePos().y():
                # Case 2_1_1 Only slightly above
                if (channel1.parentItem().scenePos().y() + channel1.parentItem().boundingRect().bottom()) > (channel2.parentItem().scenePos().y() - (2 * offset)):
                    # Case 2_1_1_1: Output channel module is positioned to the left of input channel module
                    if channel1.parentItem().scenePos().x() < channel2.parentItem().scenePos().x():
                        # Calculate midX1
                        midX1 = start.x() + (channel2.parentItem().scenePos().x() - channel1.parentItem().scenePos().x()) - (channel1.parentItem().circle_diameter / 2) + offset
                    # Case 2_1_1_2: Output channel module is positioned to the right of input channel module
                    else:
                        # Calculate midX1
                        midX1 = start.x() - (channel1.parentItem().circle_diameter / 2) + offset
                    # Calculate all other midpoints
                    midY1 = start.y()
                    midX2 = midX1
                    midY2 = channel2.parentItem().scenePos().y() + channel2.parentItem().boundingRect().bottom() + offset
                    midX3 = channel2.parentItem().scenePos().x() - offset - arrow_length
                    midY3 = midY2
                    midX4 = midX3
                    midY4 = end.y()
                # Case 2_1_2: Significantly above
                else:
                    midX1 = start.x() - (channel1.parentItem().circle_diameter / 2) + offset
                    midY1 = start.y()
                    midX2 = midX1
                    midY2 = ((channel1.parentItem().scenePos().y() + channel1.parentItem().boundingRect().bottom())  + channel2.parentItem().scenePos().y()) / 2
                    midX3 = channel2.parentItem().scenePos().x() - offset - arrow_length
                    midY3 = midY2
                    midX4 = midX3
                    midY4 = end.y()
            # Case 2_2: Output channel module is positioned below input channel module
            else:
                # Case 2_2_1: Only slightly below
                if (channel1.parentItem().scenePos().y() - (2 * offset)) < (channel2.parentItem().scenePos().y() + channel2.parentItem().boundingRect().bottom()):
                    # Case 2_2_1_1: Output channel module is positioned to the left of input channel module
                    if channel1.parentItem().scenePos().x() < channel2.parentItem().scenePos().x():
                        # Calculate midX1
                        midX1 = start.x() + (channel2.parentItem().scenePos().x() - channel1.parentItem().scenePos().x()) - (channel1.parentItem().circle_diameter / 2) + offset
                    # Case 2_2_1_2: Output channel module is positioned to the right of input channel module
                    else:
                        # Calculate midX1
                        midX1 = start.x() - (channel1.parentItem().circle_diameter / 2) + offset
                    # Calculate all other midpoints
                    midY1 = start.y()
                    midX2 = midX1
                    midY2 = channel2.parentItem().scenePos().y() - offset
                    midX3 = channel2.parentItem().scenePos().x() - offset - arrow_length
                    midY3 = midY2
                    midX4 = midX3
                    midY4 = end.y()
                # Case 2_2_2: Significantly below
                else:
                    midX1 = start.x() - (channel1.parentItem().circle_diameter / 2) + offset
                    midY1 = start.y()
                    midX2 = midX1
                    midY2 = (channel1.parentItem().scenePos().y() + (channel2.parentItem().scenePos().y() + channel2.parentItem().boundingRect().bottom())) / 2
                    midX3 = channel2.parentItem().scenePos().x() - offset - arrow_length
                    midY3 = midY2
                    midX4 = midX3
                    midY4 = end.y()

            # Define midpoints
            midpoint1 = QPointF(midX1, midY1)
            midpoint2 = QPointF(midX2, midY2)
            midpoint3 = QPointF(midX3, midY3)
            midpoint4 = QPointF(midX4, midY4)


            # Construct the path
            path.moveTo(start)
            path.lineTo(midpoint1)
            path.moveTo(midpoint1)
            path.lineTo(midpoint2)
            path.moveTo(midpoint2)
            path.lineTo(midpoint3)
            path.moveTo(midpoint3)
            path.lineTo(midpoint4)
            path.moveTo(midpoint4)
            path.lineTo(end)   

        # Add arrow head
        path.moveTo(end)
        path.addPolygon(QPolygonF([end, QPointF((end.x() - arrow_length), (end.y() - (arrow_length / 2))), QPointF((end.x() - arrow_length), (end.y() + (arrow_length / 2))), end]))
        path.closeSubpath()

        return path

    # Check if a path already exists
    def pathExists(self, channel1: Channel, channel2: Channel):
        
        path_key = self.makeUniqueChannelTuple(channel1, channel2)

        return path_key in self.paths

    #! Understand how this works again -> can I delete the arguments?
    # Redraw the path if a module is moved
    def onModuleItemMoved(self, module, change):
        # Iterate over all paths
        for entry in self.paths:

            channel1, channel2 = entry
            path_item = self.paths[(channel1, channel2)]

            path = self.calculatePath(channel1, channel2)
            path_item.setPath(path)

    def openConfig(self):
        #* Open file dialog
        downloads_path = os.path.expanduser(os.getcwd())
        while True:
            file_path, _ = QFileDialog.getOpenFileName(self, "Open File", downloads_path, "JSON Files (*.json);; All Files (*)")
            
            # Return if file dialog was cancelled
            if not file_path:
                return
            
            # Check if the selected file is a JSON file
            if not file_path.endswith(".json"):
                QMessageBox.warning(self, "Invalid File", "Please select a JSON file.")
                continue
            
            # Check if the JSON file contains compatible content
            try:
                config = Config()
                config.load_config_from_file(file_path)
            except Exception as e:
                QMessageBox.warning(self, "Error", "An error occurred while loading the file. Please check if the JSON file contains a compatible configuration. " + repr(e))
                continue

            # If a valid file was selected, break the loop
            break
        
        reply = QMessageBox.question(self, "Save Configuration", "Unsaved changes will be lost. Do you want to save before continuing?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.saveConfig()

        config = Config()
        config.load_config_from_file(file_path)

        #TODO: (Better call a delete configuration function that should also delete all paths)
        #* Delete old configuration
        # Delete hosts (will automatically delete mdodules and channels, too)
        for host in self.hosts.values():
            self.scene.removeItem(host)
        self.hosts.clear()

        # Delete paths
        for path in self.paths.values():
            self.scene.removeItem(path)
        self.paths.clear()

        #* Create hosts and modules
        # Positions of first host and first module in this host
        x_host = 0
        y_host = 0
        x_module = 175
        y_module = 60

        for host in config.get_config_data().hosts:
            # Calculate dimensions of host
            host_width = 550
            num_modules = len(host.modules)
            if num_modules <= 3:
                host_height = 450
            else:
                host_height = 450 + (num_modules - 3) * 130
            
            # Create a HostGraphicsItem
            host_graphics_item = HostGraphicsItem(host.hostname, x_host, y_host, host_width, host_height, self.claid)
            host_graphics_item.onChannelClicked.connect(self.onChannelClicked)
            host_graphics_item.onModuleItemMoved.connect(self.onModuleItemMoved)
     
            for module in host.modules:
                # Get the input channels and output channels of the module
                if module.type not in self.available_modules.keys():
                    QMessageBox.warning(self, "Invalid Module Type", "Cannot load config with module type " + module.type + ". This module tpye is unknown to CLAID.")
                    return
                module_description = self.available_modules[module.type]
                module_input_channels = self.claid.get_input_channels_of_module(module_description)
                module_output_channels = self.claid.get_output_channels_of_module(module_description)

                module_input_channel_types = self.claid.get_input_channel_types_of_module(module_description)
                module_output_channel_types = self.claid.get_output_channel_types_of_module(module_description)

                # Create a ModuleGraphicsItem 
                host_graphics_item.add_module(module.id, x_module, y_module, module_input_channels, module_output_channels, module_input_channel_types, module_output_channel_types)
                y_module += 130
            
            # Store host and its modules in the dictionary && add the hosts to the scene
            self.hosts[host.hostname] = host_graphics_item
            self.scene.addItem(host_graphics_item)

            x_host += 650
            y_module = 60

        #* Re-Initialize MainWindow and UI
        # No channel clicked at beginning
        self.firstClickedChannel = None
                
        #TODO: There needs to be a dialog in case for uncertain cases (connection vs no connection)
        #* Create paths
        # Step 1: Iterate over connected output channels to find each connection id
        channel_descriptions = config.get_channel_descriptions()

        for connection in channel_descriptions:

            publishers = channel_descriptions[connection].publisher_modules
            subscribers = channel_descriptions[connection].subscriber_modules

            for pub in publishers:
                pub_host, pub_module, pub_channel = pub

                for sub in subscribers:
                    sub_host, sub_module, sub_channel = sub

                    channel1 = None
                    channel2 = None

                    #TODO: Add dict (host, module, channel) <-> ChannelItem
                    for target_out_module in self.hosts[pub_host].get_modules():
                        if target_out_module.id == pub_module:
                            channel1 = target_out_module.output_channel_map[pub_channel]
                            break
                    for target_in_module in self.hosts[sub_host].get_modules():
                        if target_in_module.id == sub_module:
                            channel2 = target_in_module.input_channel_map[sub_channel]
                            break

                    if channel1 != None and channel2 != None:
                        # Step 2: Create paths between the two found channels
                        self.createPath(channel1, channel2)

    def saveConfig(self):
        #* Open file dialog
        downloads_path = os.path.expanduser(os.getcwd())
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", downloads_path, "JSON Files (*.json);; All Files (*)")
        
        # Return if file dialog was cancelled
        if not file_path:
            return
        
        # Add .json extension to the file path if it doesn't have one
        if not file_path.endswith(".json"):
            file_path += ".json"

        claid_config = self.generateCLAIDConfigFromUI()

        config = Config()   
        Config.save_config_to_file(claid_config, file_path)        

    def generateCLAIDConfigFromUI(self):
        #* Build a "connections" dict that contains tuple (hostname, module_id, channel_name) and its corresponding connection name
        # Create empty dictionary for connections
        connections = dict()

        # Initial connection number, used for naming the connections
        connect_num = 0

        # Iterate over all paths
        for (channel1, channel2) in self.paths:
            h1 = channel1.parentItem().parentItem().get_name()
            h2 = channel2.parentItem().parentItem().get_name()
            m1 = channel1.parentItem().get_id()
            m2 = channel2.parentItem().get_id()
            c1 = channel1.get_name()
            c2 = channel2.get_name()

            # Case1: channel1 (output channel) already in connections
            if (h1, m1, c1) in connections:
                if (h2, m2, c2) not in connections:
                    connections[(h2, m2, c2)] = connections[(h1, m1, c1)]
                elif connections[(h2, m2, c2)] != connections[(h1, m1, c1)]:
                    for (h, m, c) in connections:
                        if connections[(h, m, c)] == connections[(h2, m2, c2)]:
                            connections[(h, m, c)] = connections[(h1, m1, c1)]
                else:
                    continue
            
            # Case 2: channel1 (output channel) not in connections && channel2 (input channel) already in connections
            elif (h2, m2, c2) in connections:
                connections[(h1, m1, c1)] = connections[(h2, m2, c2)]
            
            # Case 3: channel1 (output channel) and channel2 (input channel) not in connections
            else:
                connection_name = "connection" + str(connect_num)
                connections[(h1, m1, c1)] = connection_name
                connections[(h2, m2, c2)] = connection_name
                connect_num += 1

        # for (host, module, channel) in connections:
        #     print("Host: " + host + ", Module: " + module + ", Channel: " + channel + ", Connection: " + connections[(host, module, channel)])

        #* Save hosts, modules and connections into config
        claid_config = CLAIDConfig()
        
        for host in self.hosts.values():
            host_config = HostConfig()
            
            # Gather all host properties:
            host_name = host.get_name()
            host_type = host.get_type()
            host_is_server = host.get_is_server()
            host_server_address = host.get_server_address()
            host_connect_to = host.get_connect_to()
            
            # Save all host properties into host_config
            host_config.hostname = host_name
            host_config.type = host_type
            host_config.is_server = host_is_server
            if host_server_address != None:
                host_config.host_server_address = host_server_address
            if host_connect_to != None:
                host_config.connect_to = host_connect_to
            if host_is_server:
                host_config.is_server = host_is_server

            for module in host.modules:
                module_config = ModuleConfig()

                # Gather all module properties:
                module_id = module.get_id()
                module_type = module.get_type()
                module_properties = module.get_properties()
                module_output_channels = dict()
                module_input_channels = dict()

                for (channel1, channel2) in self.paths:
                    # Check if channel1 (output channel) is child of module
                    if channel1.parentItem() == module:
                        pub_host = host_name
                        pub_module = module_id
                        pub_channel = channel1.get_name()
                        connection_name = connections[(pub_host, pub_module, pub_channel)]

                        # Store connection name. No need to check if name is already stored as the name is unique
                        module_output_channels[pub_channel] = connection_name

                    # Check if channel2 (input channel) is child of module
                    elif channel2.parentItem() == module:
                        sub_host = host_name
                        sub_module = module_id
                        sub_channel = channel2.get_name()
                        connection_name = connections[(sub_host, sub_module, sub_channel)]

                        # Store connection name. No need to check if name is already stored as the name is unique
                        module_input_channels[sub_channel] = connection_name

                # Save all module properties into module_config
                module_config.id = module_id
                module_config.type = module_type
                #TODO: Check if the if condition is really necessary
                if module_properties:
                    module_config.properties.update(module_properties)
                if module_output_channels:
                    module_config.output_channels.update(module_output_channels)
                if module_input_channels:
                    module_config.input_channels.update(module_input_channels)

                # Append module_config to host_config
                host_config.modules.append(module_config)

            # Append host_config to claid_config
            claid_config.hosts.append(host_config)
         
        return claid_config

    def __on_connected_to_server(self):
        
        self.hosts["Smartwatch"].set_connected()

    def __on_disconnected_from_server(self):

        self.hosts["Smartwatch"].set_disconnected()

    def program_device_button_clicked(self):
        print("program device button clicked")

        if not self.hosts["Smartwatch"].is_connected():
            QMessageBox.critical(None, "Smartwatch not connected", "Cannot program devices. Smartwatch is not connected.")
            return
        
        reply = QMessageBox.question(self, "Program devices", "Devices are ready. Upload configuration now?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:

            if not self.hosts["Smartwatch"].is_connected():
                QMessageBox.critical(None, "Smartwatch not connected", "Cannot program devices. Smartwatch is not connected.")
                return
            
            config = self.generateCLAIDConfigFromUI()

            self.claid.upload_config_to_host(self.claid.get_current_host_id(), config)

            self.claid.upload_config_to_host("Smartwatch", config)

    def delete_path(self, del_path):
        for (channel1, channel2) in self.paths:
            if self.paths[(channel1, channel2)] == del_path:
                del self.paths[(channel1, channel2)]
                break

    def get_hosts(self):
        return self.hosts