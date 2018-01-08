from MNIST_main import *


def main():
	#prompt user for parameters
	print("This program generates images using an evolutionairy algorithm.")
	num_images = int(input("How many images per generation would you like? (please select a positive integer)\n"))
	print("generating %i images per generation", num_images)

	selection = -1
	while selection == -1:
		selection = int(input("Select an option: \n(0) generate an MNIST number\n"))
		
		if selection == 0:
			print("You have selected to generate an MNIST number")
			number_to_generate = -1
			retrain = input("Would you like to Retrain [Y/n]\n")
			if retrain != "Y" and retrain != "n":
				retrain = "Y" 
				print("By default, the program will retrain")
			if retrain == "Y":
				while number_to_generate == -1:
					number_to_generate = int(input("What number would you like to generate from 0-9?\n"))
					if number_to_generate in range(10):
						print("Generating an image of the number %i", number_to_generate)
					else:
						number_to_generate = -1
						print("Please select a number from 0-9")
			MNIST_run(num_images, number_to_generate, retrain)

		else:
			selection = -1
			print("Please select a valid option from the list of numbers")








if __name__ == "__main__":
    setup = "from __main__ import main"
    print("Running Main")
    main()