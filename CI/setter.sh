python -m pip install --upgrade pip
pip install flake8==4.0.1
pip install pytest==7.1.2
pip install pydantic==1.9.1
pip install testcontainers==3.6.0
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

cd /home/runner/work/lightning_py/lightning_py
curl -O https://raw.githubusercontent.com/aerokube/selenium-openapi/master/selenium.yaml

git clone https://github.com/swagger-api/swagger-codegen
cd swagger-codegen
git checkout 3.0.0
mvn clean package
java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \
   -i /home/runner/work/lightning_py/lightning_py/selenium.yaml \
   -l python \
   -o /home/runner/work/lightning_py/lightning_py/python
cd /home/runner/work/lightning_py/lightning_py
cd /home/runner/work/lightning_py/lightning_py/python && python setup.py install && cd ..
ls && pwd
