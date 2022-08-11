
# installing python test libraries
python -m pip install --upgrade pip
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# download <swagger.yaml> file
cd /home/runner/work/lightning_py/lightning_py
curl -O https://raw.githubusercontent.com/aerokube/selenium-openapi/master/selenium.yaml

# install swagger codegen

git clone https://github.com/swagger-api/swagger-codegen
cd swagger-codegen
git checkout 3.0.0
mvn clean package
java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \

   -i /home/runner/work/lightning_py/lightning_py/selenium.yaml \
   -l python \
   -o /home/runner/work/lightning_py/lightning_py/python
cd /home/runner/work/lightning_py/lightning_py

# setup swagger API
cd /home/runner/work/lightning_py/lightning_py/python && python setup.py install && cd ..
ls && pwd
