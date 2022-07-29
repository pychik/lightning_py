
# lightning_py
python client for &lt;selenium> driver
* Features at the moment
  * WebDriver class made with inheritance to Session and Navigate classes- as attempt to divide this Api's
  * ContextApi, DocumentsApi, ScreenshotsApi represented as instances without dividing there methods

* Installing
  * docker run -d --name swagger-editor -p 8080:8080 swaggerapi/swagger-editor (generate code)
    * python -m venv venv (creating vitual environment)
    * cd "folder with setup.py" && python setup.py install" 
    * cd "main folder"
    * python test_lightning_api.py