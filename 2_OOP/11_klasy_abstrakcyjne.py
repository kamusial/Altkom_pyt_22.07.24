from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def load_data(self, source):
        # Załaduj dane z okreslonego źródła
        pass

    @abstractmethod
    def process_data(self):
        # Przetwarzaj załadowane dane
        pass

class CSVProcessor(DataProcessor):
    def load_data(self, source):
        print(f'Zadowanie danych z CSV: {source}')

    def process_data(self):
        print(f'Przetwarzanie danych')

 class JSONProcessor(DataProcessor):
    def load_data(self, source):
        print(f"Ładowanie danych z pliku JSON: {source}")

        def process_data(self):
            print("Przetwarzanie danych JSON...")

csv_processor = CSVProcessor()
csv_processor.load_data("data.csv")
csv_processor.process_data()

json_processor = JSONProcessor()
json_processor.load_data("data.json")
json_processor.process_data()
