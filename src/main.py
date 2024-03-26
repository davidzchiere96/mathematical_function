import mathFunction
import logger


def main():
    log = logger.logger()

    print("MATHEMATICAL FUNCTION: Arithmetic Average")
    log.info("Instantiating an object of the child class AverageFunction.")

    # Instantiating the class and calling the input interface
    average_function = mathFunction.AverageFunction()
    arguements = mathFunction.input_arguements()

    # Calculating
    result_average = average_function.calculate(*arguements)
    return result_average

if __name__ == "__main__":
    main()