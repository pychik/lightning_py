# installing python test libraries
python -m pip install --upgrade pip
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# download <swagger.yaml> file
cd /home/runner/work/lightning_py/lightning_py
curl -O https://raw.githubusercontent.com/aerokube/selenium-openapi/master/selenium.yaml

# install swagger codegen
#git clone https://github.com/swagger-api/swagger-codegen
wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.34/swagger-codegen-cli-3.0.34.jar -O swagger-codegen-cli.jar
#chmod +x swagger-codegen-cli.jar
#cd swagger-codegen
#git checkout 3.0.0
ls && pwd
mvn clean package
java -jar swagger-codegen-cli.jar generate \
#   -i /home/runner/work/lightning_py/lightning_py/selenium.yaml \
  -i selenium.yaml \
   -l python \
   -o python
ls && pwd
#cd /home/runner/work/lightning_py/lightning_py

# setup swagger API
pushd python/ && python setup.py install && cd ..
# checking code with flake8
flake8 driver/ --count --select=E9,F63,F7,F82,E302,W391,W292 --show-source --statistics
# testing code
pytest tests/
