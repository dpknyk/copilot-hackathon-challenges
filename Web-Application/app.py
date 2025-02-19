import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget, QLabel, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout
from bleak import BleakScanner, BleakClient
import asyncio
from asyncqt import QEventLoop

class BLEScannerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('BLE Scanner')
        self.setGeometry(100, 100, 400, 400)

        self.scanButton = QPushButton('Scan', self)
        self.scanButton.clicked.connect(self.scanDevices)

        self.deviceList = QListWidget(self)

        self.connectButton = QPushButton('Connect', self)
        self.connectButton.clicked.connect(self.connectDevice)

        self.statusLabel = QLabel('Status: Disconnected', self)

        self.searchInput = QLineEdit(self)
        self.searchInput.setPlaceholderText('Enter MAC address')
        self.searchButton = QPushButton('Search', self)
        self.searchButton.clicked.connect(self.searchDevice)

        searchLayout = QHBoxLayout()
        searchLayout.addWidget(self.searchInput)
        searchLayout.addWidget(self.searchButton)

        layout = QVBoxLayout()
        layout.addWidget(self.scanButton)
        layout.addLayout(searchLayout)
        layout.addWidget(self.deviceList)
        layout.addWidget(self.connectButton)
        layout.addWidget(self.statusLabel)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    async def asyncScanDevices(self):
        self.deviceList.clear()
        devices = await BleakScanner.discover()
        for device in devices:
            self.deviceList.addItem(f"{device.name} ({device.address})")

    async def asyncConnectDevice(self):
        selected_device = self.deviceList.currentItem().text()
        address = selected_device.split('(')[-1].strip(')')
        async with BleakClient(address) as client:
            if await client.is_connected():
                self.statusLabel.setText('Status: Connected')
            else:
                self.statusLabel.setText('Status: Failed to Connect')

    async def asyncSearchDevice(self):
        mac_address = self.searchInput.text().strip()
        if not mac_address:
            self.statusLabel.setText('Status: Enter a MAC address')
            return

        self.deviceList.clear()
        devices = await BleakScanner.discover()
        for device in devices:
            if device.address.lower() == mac_address.lower():
                self.deviceList.addItem(f"{device.name} ({device.address})")
                return

        self.statusLabel.setText('Status: Device not found')

    def scanDevices(self):
        asyncio.ensure_future(self.asyncScanDevices())

    def connectDevice(self):
        asyncio.ensure_future(self.asyncConnectDevice())

    def searchDevice(self):
        asyncio.ensure_future(self.asyncSearchDevice())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    ex = BLEScannerApp()
    ex.show()
    with loop:
        loop.run_forever()