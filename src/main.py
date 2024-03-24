import mathFunction
import logger

log = logger.logger()

def main():

    print("MATHEMATICAL FUNCTION: Arithmetic Average")
    log.info("Instantiating an object of the child class AverageFunction.")
    average_function = mathFunction.AverageFunction()
    arguements = mathFunction.input_arguements()

    result_average = average_function.calculate(*arguements)
    return result_average

if __name__ == "__main__":
    main()