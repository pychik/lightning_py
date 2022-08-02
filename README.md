
# lightning_py
python client for &lt;selenium> driver

<p align="left">
    <a href="https://www.python.org/" target="blank">
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    </a>
    <a href="https://swagger.io/" target="blank">
        <img src="https://img.shields.io/badge/Swagger-23000.svg?style=for-the-badge&logo=swagger&logoColor=white"/>
    </a>
</p>
<p>
    <a href="https://aerokube.com/selenoid/" target="blank">
        <img src="/images/ac_logo.png" width="50"/>
    </a>
</p>

* Features at the moment
  * WebDriver class made with inheritance to Session and Navigate classes- as attempt to divide this Api's
  * ContextApi, DocumentsApi, ScreenshotsApi represented as instances without dividing there methods

* Installing
  * docker run -d --name swagger-editor -p 8080:8080 swaggerapi/swagger-editor (generate code)
    * python -m venv venv (creating vitual environment)
    * cd "folder with setup.py" && python setup.py install" 
    * cd "main folder"
    * python test_lightning_api.py