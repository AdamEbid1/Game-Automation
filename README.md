# Game-Automation

This Python script uses the PyAutoGUI library to automate farming in Minecraft. The script first prompts the user to input the size of the square farm they want to create. Using the PyAutoGUI library, the script navigates the player to the correct position on the X and Z axes to plant crops. The script also uses the pytesseract library for optical character recognition to find the player's current coordinates in the game. Specifically, the find_coords_X() and find_coords_Z() functions use pytesseract to extract the player's X and Z coordinates from the game screen. The extracted coordinates are then used by the script to move the player to the correct position for planting crops in the farm.

The script opens the player's inventory, selects the appropriate seeds, and clicks on each spot in the farm to plant crops. The script repeats this process for each row in the farm until all crops have been planted.

This script is useful for Minecraft players who want to automate the farming process to save time and improve efficiency. I made it a while back but am now posting it on here
