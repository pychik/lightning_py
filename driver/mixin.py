class Common:
    @property
    def session_id(self):
        return self._wd.session_id
    @property
    def navigation(self):
        return self._wd.navigation

    @property
    def sessions(self):
        return self._wd.sessions

    @property
    def document(self):
        return self._wd.document

    @property
    def screenshot(self):
        return self._wd.screenshot

    @property
    def context(self):
        return self._wd.context
