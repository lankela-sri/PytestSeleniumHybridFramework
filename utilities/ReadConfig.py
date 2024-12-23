from configparser import ConfigParser




def read_configurations(category,key):
    config = ConfigParser()
    config.read("C:/Users/srinivas_lankela/PycharmProjects/pytest/TestPytestSelenium/configurations/config.ini")
    return  config.get(category,key)
