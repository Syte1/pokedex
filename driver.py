# Name: Aryan Jand & Belal Kourkmas
# Student number: A01169131 & A01264033
import argparse
import asyncio
from pokedex import PokeDex, PokedexMode
from request import Request





def setup_request_commandline() -> Request:
    """
    Sets up a command line interface to take in user inputs and creates a Request object.

    Returns:
        Request: An object containing user inputs for the PokeDex API request.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("mode", choices=['pokemon', 'move', 'ability'], help="The mode to use to set teh Pokedex."
                                                                             " It can be {'pokemon' | 'ability' | 'move'}")
    parser.add_argument("--inputfile", help="The inputfile is used pass inputs to the program. "
                                            "Input file has to be .txt format.")
    parser.add_argument("--inputdata", help="The inputdata is used to pass inputs to the program. "
                                            "These arguments are name and id. Note: Input data has to be a String.")
    parser.add_argument("--expanded", action='store_const', const=True,
                        help="When this is provided a certain attributes are expanded.")

    parser.add_argument("--output", default=None, help="When this provided with filename and .txt extension, "
                                                       "then the output will printed to specified textfile. If it is "
                                                       "not provided it will be logged to the console.")

    try:
        args = parser.parse_args()
        request = Request()
        request.poke_dex_mode = PokedexMode(args.mode.lower())
        request.data_input = [args.inputdata]
        request.input_file = args.inputfile
        request.expanded = args.expanded
        request.output_type = args.output
        if request.input_file:
            with open(request.input_file) as file:
                request.data_input = tuple(line.rstrip() for line in file)
        return request
    except Exception as e:
        print(f"Cannot instantiate a request object.\n{e}")
        exit(-1)


def main():
    """
    Main function that executes a PokeDex API request based on user inputs from the command line.
    """
    request = setup_request_commandline()
    pokedex = PokeDex()
    asyncio.run(pokedex.execute_request(request))


if __name__ == '__main__':
    main()
