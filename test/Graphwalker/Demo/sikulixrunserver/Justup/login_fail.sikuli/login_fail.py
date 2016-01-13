import ConfigParser

config = ConfigParser.ConfigParser()
config.read('Justup/Config/justup.cfg')

wait(config.get('LOGIN', 'i_login'))

click(config.get('LOGIN', 'i_email'))
type("a", KEY_CTRL)
type(Key.DELETE)
type(config.get('LOGIN', 'f_email'))

click(config.get('LOGIN', 'i_pwd'))
type("a", KEY_CTRL)
type(Key.DELETE)
type(config.get('LOGIN', 'f_pwd'))

click(config.get('LOGIN', 'i_login'))

#wait('login-fail.png')
