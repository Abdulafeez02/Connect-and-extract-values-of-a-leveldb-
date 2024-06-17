# Hello World Chrome Extension with LevelDB Access

This project includes a simple Chrome extension that stores a value using the `chrome.storage` API and a Python script to fetch that value from the LevelDB database on disk.

## What the Code Does

### Chrome Extension
The Chrome extension initializes a key-value pair in the `chrome.storage` when installed and displays this value in a popup UI when the extension icon is clicked.

### Python Script
The Python script connects to the LevelDB database used by the Chrome extension, retrieves the stored key-value pair, and prints it to the console. It also iterates through all stored key-value pairs in the database and displays them.

## Summary

This project demonstrates how to create and use a Chrome extension to store data and how to access this data from the LevelDB database using a Python script. Follow the provided instructions to set up and use both the extension and the script.
