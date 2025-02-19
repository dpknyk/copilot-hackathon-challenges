# BLE Device Scanner and Connector

## Overview

This project aims to create a Web GUI application that allows users to scan for and connect to Bluetooth Low Energy (BLE) devices. The application will provide a user-friendly interface to manage BLE connections.

## Features

1. **Scan for BLE Devices**: The application will scan for available BLE devices and display them in a list.
2. **Connect to BLE Devices**: Users can select a device from the list and connect to it.
3. **Display Device Information**: Once connected, the application will display information about the connected device.
4. **Disconnect from BLE Devices**: Users can disconnect from the connected device.

## Requirements

### Functional Requirements

1. **Scan for BLE Devices**:
   - The application should provide a button to start scanning for BLE devices.
   - The application should display a list of discovered BLE devices, including their names and addresses.

2. **Connect to BLE Devices**:
   - Users should be able to select a device from the list and connect to it.
   - The application should display a success message upon successful connection.
   - The application should handle connection errors gracefully and display appropriate error messages.

3. **Display Device Information**:
   - Once connected, the application should display detailed information about the connected device, such as its name, address, and available services.

4. **Disconnect from BLE Devices**:
   - Users should be able to disconnect from the connected device.
   - The application should display a success message upon successful disconnection.

### Non-Functional Requirements

1. **User Interface**:
   - The application should have a clean and intuitive user interface.
   - The application should be responsive and work on various screen sizes.

2. **Performance**:
   - The application should quickly scan for and connect to BLE devices.
   - The application should handle multiple BLE devices efficiently.

3. **Compatibility**:
   - The application should work on modern web browsers (Chrome, Firefox, Edge, Safari).

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript, React (optional)
- **Backend**: Node.js, Express (optional)
- **BLE Library**: Web Bluetooth API

## Setup and Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ble-device-scanner.git
   cd ble-device-scanner