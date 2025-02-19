import unittest
from unittest.mock import patch, AsyncMock
from PyQt5.QtWidgets import QApplication
import sys
from main import BLEScannerApp  # Assuming your main file is named main.py

class TestBLEScannerApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.window = BLEScannerApp()

    @patch('main.BleakScanner.discover', new_callable=AsyncMock)
    def test_scanDevices(self, mock_discover):
        mock_discover.return_value = [
            AsyncMock(name='Device1', address='00:11:22:33:44:55'),
            AsyncMock(name='Device2', address='66:77:88:99:AA:BB')
        ]
        asyncio.run(self.window.asyncScanDevices())
        self.assertEqual(self.window.deviceList.count(), 2)
        self.assertEqual(self.window.deviceList.item(0).text(), 'Device1 (00:11:22:33:44:55)')
        self.assertEqual(self.window.deviceList.item(1).text(), 'Device2 (66:77:88:99:AA:BB)')

    @patch('main.BleakClient', new_callable=AsyncMock)
    def test_connectDevice(self, mock_client):
        mock_client.return_value.is_connected.return_value = True
        self.window.deviceList.addItem('Device1 (00:11:22:33:44:55)')
        self.window.deviceList.setCurrentRow(0)
        asyncio.run(self.window.asyncConnectDevice())
        self.assertEqual(self.window.statusLabel.text(), 'Status: Connected')

    @patch('main.BleakScanner.discover', new_callable=AsyncMock)
    def test_searchDevice(self, mock_discover):
        mock_discover.return_value = [
            AsyncMock(name='Device1', address='00:11:22:33:44:55'),
            AsyncMock(name='Device2', address='66:77:88:99:AA:BB')
        ]
        self.window.searchInput.setText('00:11:22:33:44:55')
        asyncio.run(self.window.asyncSearchDevice())
        self.assertEqual(self.window.deviceList.count(), 1)
        self.assertEqual(self.window.deviceList.item(0).text(), 'Device1 (00:11:22:33:44:55)')

if __name__ == '__main__':
    unittest.main()