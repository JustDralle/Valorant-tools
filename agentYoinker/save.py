import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    'player.py',
    'game.py',
    '--name', 'MyGame',
    '--onefile',
    '--console',  # Open a console window
    '--add-data', 'settings.json;.'  
])
