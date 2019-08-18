import unittest
from selenium import webdriver
from time import sleep


url = 'https://www.empik.com/'

class SearchBoardGamesPage_ch(unittest.TestCase):

    def setUp(self, browser="chrome"):
        if browser == "chrome" or browser == "ch":
            self.driver = webdriver.Chrome(executable_path=r'../Drivers/ChromeDrive_75/chromedriver.exe')
        elif browser == "mozilla" or browser == "ff":
            self.driver = webdriver.Firefox(executable_path=r'../Drivers/FirefoxDrive_24/geckodriver.exe')
        else:
            print("Brak przeglądarki")
            raise Exception("Brak przeglądarki")
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver



    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_searchBoardGames(self):
        searchGames = self.driver.find_element_by_id("bq")
        searchGames.click()
        searchGames.send_keys("zmiennicy ")
        listCategory = self.driver.find_element_by_class_name("search-categories__trigger")
        listCategory.click()
        categoryZabawki = self.driver.find_element_by_xpath("//label[@for='_sc23']")
        categoryZabawki.click()
        searchButton = self.driver.find_element_by_class_name("search-field__button")
        searchButton.click()
        searchProducts = self.driver.find_element_by_class_name("lazy")
        searchProducts.click()


        #
        # titleGame = self.driver.find_element_by_xpath("//*[@class='productBaseInfo__title']//*[@itemprop='name']")
        #
        # print(self.driver.find_element_by_xpath(titleGame).text)
        # assert self.driver.find_element_by_xpath(titleGame).text == "Inte-gra, gra planszowa Zmiennicy"




if __name__ == '__main__':
    unittest.main()
