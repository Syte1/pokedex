ECHO This provides first initial test. It includes Pokemon Mode, Input Data, Expanded, and Output String
python driver.py pokemon --inputdata 5 --output output.txt

ECHO This provides a test, where the Mode is set to Move, Input file, Expanded, Output File
python driver.py move --inputfile data.txt --output output.txt

ECHO This is test, where we set Ability, Input file, not expanded, and Output Console.
python driver.py ability --inputfile data.txt --expanded

ECHO This is test, where we set Pokemon, Input data, not expanded and Output Console.
python driver.py pokemon --inputdata pikachu

ECHO This is test, where we set Pokemon, Input data, not expanded and Output Console.
python driver.py poke --inputdata pikachu

ECHO write to screen
python driver.py --inputfile input_ability.txt ability
python driver.py --inputdata 2 move
python driver.py --inputdata 2 pokemon
python driver.py --inputfile input_move.txt move

ECHO write to file
python driver.py --inputfile input_move.txt --output output_move.txt move
python driver.py --inputfile input_ability.txt --output output_ability.txt ability
python driver.py --inputfile input_pokemon.txt --output output.txt pokemon

ECHO write to file expanded
python driver.py --inputfile input_pokemon.txt --output output_pokemon_expand.txt pokemon --expanded

ECHO error
python driver.py --inputfile input_error.txt --output output_error.txt mov
