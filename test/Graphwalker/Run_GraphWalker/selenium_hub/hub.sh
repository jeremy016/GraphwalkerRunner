JAR_FILE='/home/sqa/.jenkins/workspace/GraphWalker/auto_test/Graphwalker/selenium_hub/selenium-server-standalone-2.48.2.jar'

java -jar $JAR_FILE -role hub -port 7777 -nodeTimeout 600000 -timeout 600000
