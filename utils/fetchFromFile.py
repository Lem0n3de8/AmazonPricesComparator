import os 

from src.amazonFetcher import AmazonFetcher, AmazonProduct


class FetchFromTxt:
    """ Utility class to fetch links from a .txt file.
    
    This class can be used to automate data of mutiple products
    The content of the file used by this method must use the following formatting: 1 link per line.
    The class does not provide methods to alter the file content
    """


    def __init__(self, path:str = "links.txt"):
        self.path = path
        self.amazon_fetcher = AmazonFetcher()

        try:
            with open(self.path, 'r') as file:
                self.file_content = file.read().splitlines()
        except FileExistsError:
            open(self.path, 'x').close()
            self.file_content = []

    def _read_file(self):
        with open(self.path, 'r') as file:
            self.file_content = file.read().splitlines()
    
    def change_file_path(self,path:str):
        """Change the file from which the links are retrieved
        
        The file is assumed to exist before using this method
        """
        if not path.endswith(".txt"):
            raise ValueError("File must be a .txt file")
        if not os.path.exists(path):
            raise FileNotFoundError(path)

        self.pah = path
        self._read_file() 
    
    def fetch_first_link(self) -> AmazonProduct:
        """Fetch the first link of the links file"""

        self._read_file()
        if not self.file_content:
            raise ValueError("Links file is empty")
        
        fist_link = self.file_content[0].strip()
        product_info = self.amazon_fetcher(first_line)
        return product_info
    
    def fetch_link_n(self, link_number:int) -> AmazonProduct:
        """Fetch a specific link"""

        self._read_file()
        if not self.file_content:
            raise ValueError("Link file is empty")

        if link_number < 0 or link_number >= len(self.file_content):
            raise IndexError("Link number out of range")
        
        link = self.file_content[link_number].strip()

        return self.amazon_fetcher.fetch_product(link)

    def fetch_all_links(self) -> list[AmazonProduct]:
        """Fetch all links found in the links file"""

        self._read_file()
        if not self.file_content:
            raise ValueError("Links file is empty")
        
        output_lists = []

        for line in self.file_content:
            line = line.strip()
            product_info = self.amazon_fetcher.fetch_product(line)
            output_lists.append(product_info)
        
        return output_lists