from abc import ABC, abstractmethod


class FileReader(ABC):

    @abstractmethod
    def read_file(self, filename, extension):
        ...


class CSVFileReader(FileReader):

    def read_file(self, filename, extension):
        print("Did some CSV reader specific setup")
        print(f"Read the [{filename}.{extension}] CSV file ")


class XMLFileReader(FileReader):

    def read_file(self, filename, extension):
        print("Did some XML reader specific setup")
        print(f"Read the [{filename}.{extension}] XML file ")


class FileService(ABC):

    @abstractmethod
    def create_file_reader(self):
        ...

    def read_file(self, filename, extension):
        self.verify_file()
        file_reader = self.create_file_reader()
        file_reader.read_file(filename, extension)
    
    def verify_file(self):
        print("Verified file exists")


class CSVFileService(FileService):

    def create_file_reader(self):
        print("Did some special CSV file initialization stuff")
        return CSVFileReader()


class XMLFileService(FileService):

    def create_file_reader(self):
        return XMLFileReader()


FILE_SERVICE_MAP = {
        "xml": XMLFileService,
        "csv": CSVFileService,
    }


def get_file():
    while True:
        filename = input("Input filename with extension: ").lower()
        filename, extension = filename.split('.')
        if extension in FILE_SERVICE_MAP.keys():
            return filename, extension

def get_function():
    while True:
        func = input("Read (r) or Write (w) file? ").lower()
        if func in ('r', 'w'):
            return func


def main():
    func = get_function()
    filename, extension = get_file()

    file_service = FILE_SERVICE_MAP.get(extension)()

    if func == 'r':
        file_service.read_file(filename, extension)
    else:
        # TODO: Write the file
        print("File writing not yet supported")


if __name__ == "__main__":
    main()
