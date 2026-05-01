# DEVLOG - Will be better formatted later

## Day 1 - Thursday 29th April

- Today the project was started!
- The basic idea I came up with was a turn based rogue like fantasy battler game based in the CLI
- I began by creating a python project with UV and creating a basic welcome screen
- The skeletons for a player class and an enemy class were created along with placeholder stats for attack, etc
- I wanted it to be in the CLI but wanted it to be formatted niceley so I googled for some libraries to help and came across "Rich"
- Rich seemed cool and wanted to test it so i implemented a very basic print round function to use Rich to print the stats of both combatents and it looked nice
- So probably going to stick with that

## Day 2 - Friday 1st May

- Basic combat now works, take turns to attack eachother with basic attack
- Added an action list to players and enemys for different actions (main, stamina, magic) which could allow me to extend them in the future
- Added some QoL to make it easier for the user to understand whats happening
  - Renamed round to turns: turns will be in a battle, rounds will be an enemy encounter
  - Clear the terminal before printing the round to make it clearer
  - Display possible actions in the printout
