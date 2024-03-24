from abc import ABC, abstractmethod
import logger

log = logger.logger()

class MathFunction(ABC):
    @abstractmethod
    def calculate(self, *args):
        pass

class AverageFunction(MathFunction):
    def calculate(self, *args):
        log.info(f"Average function arguements: {args}")
        if not args:
            return 0  # Ritorna 0 se non ci sono argomenti
        else:
            results = sum(args) / len(args)
            log.info(f"Average = {results}")
        return results

def input_arguements():
    values = [int(value) for value in input("Enter a list of numbers separated by spaces: ").split()]
    return values



average_function = AverageFunction()
arguements = input_arguements()

result_average = average_function.calculate(*arguements)

