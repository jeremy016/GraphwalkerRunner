wait('login-icon.png')

click("email-icon.png")
type("a", KEY_CTRL)
type(Key.DELETE)
type('lumy')

click("pwd-icon.png")
type("a", KEY_CTRL)
type(Key.DELETE)
type('123456')

click('login-icon.png')

wait('login-fail.png')