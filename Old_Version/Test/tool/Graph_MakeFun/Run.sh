#!/bin/bash

#merge graphml
if [ "$1"	 ];then
	echo 'merge graphml...$1'
	python ./lib/graph_merge.py $1
else
	echo 'merge graphml ./Graph'
	python ./lib/graph_merge.py ./Graph
fi


#graphml -> dot
echo 'graphml -> dot... (merged.dot)'
java -jar ./lib/graphwalker-cli-3.4.0-SNAPSHOT.jar convert -i merged.graphml merged.dot


#dot -> png  , please install graphviz
echo 'dot -> png... (merged.png)'
dot -Tpng merged.dot > merged.png

#del dot
rm merged.dot

# show merged png to chack graph Completeness
# echo 'show png... (merged.png)'
# display merged.png &


#output merged.py
#echo 'Generate python stub source code... (merged.py)'
java -jar ./lib/graphwalker-cli-3.4.0-SNAPSHOT.jar source -i merged.graphml ./lib/python.template > merged.py

#stripping function
echo 'Generate python stub source code & graphwalker Runner ... (script.py & GW.py)'
python ./lib/stripping.py

#del merged
rm merged.py

