import ConfigParser
Config = ConfigParser.ConfigParser()
cfgfile = open("composeexample/config.ini", 'w')

# add the settings to the structure of the file, and lets write it out...
Config.add_section('database')
Config.set('database', 'name', 'test')
Config.set('database', 'user', 'test')
Config.set('database', 'password', 'test')
Config.write(cfgfile)
cfgfile.close()
