from abc import ABC, abstractmethod


class FileProcessor(ABC):

    @abstractmethod
    def read_file(self, filename, extension):
        ...


class CSVFileProcessor(FileProcessor):

    def read_file(self, filename, extension):
        print("Did some CSV reader specific setup")
        print(f"Read the [{filename}.{extension}] CSV file ")


class XMLFileProcessor(FileProcessor):

    def read_file(self, filename, extension):
        print("Did some XML reader specific setup")
        print(f"Read the [{filename}.{extension}] XML file ")


class FileService(ABC):

    @abstractmethod
    def create_file_processor(self):
        ...

    def read_file(self, filename, extension):
        self.verify_file()
        file_processor = self.create_file_processor()
        file_processor.read_file(filename, extension)
    
    def verify_file(self):
        print("Verified file exists")


class CSVFileService(FileService):

    def create_file_processor(self):
        print("Did some special CSV file initialization stuff")
        return CSVFileProcessor()


class XMLFileService(FileService):

    def create_file_processor(self):
        return XMLFileProcessor()


FILE_HANDLER_MAP = {
        "xml": XMLFileService,
        "csv": CSVFileService,
    }


def get_file():
    while True:
        filename = input("Input filename with extension: ").lower()
        filename, extension = filename.split('.')
        if extension in FILE_HANDLER_MAP.keys():
            return filename, extension

def get_function():
    while True:
        func = input("Read (r) or Write (w) file? ").lower()
        if func in ('r', 'w'):
            return func


def main():
    func = get_function()
    filename, extension = get_file()

    file_handler_service = FILE_HANDLER_MAP.get(extension)()

    if func == 'r':
        file_handler_service.read_file(filename, extension)
    else:
        # TODO: Write the file
        ...


if __name__ == "__main__":
    main()
