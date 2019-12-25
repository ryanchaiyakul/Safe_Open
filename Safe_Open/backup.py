import pathlib
import logging
import subprocess


class Backup():

    def __init__(self, path: pathlib.Path, check_func=None):
        self._logger = logging.getLogger(__name__)

        self.path = path
        if check_func is None:
            self._logger.warning("No check_function passed")
        self.check_func = check_func
        self._stream = None

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            self._logger.info(
                "{} does not exist, creating a blank file".format(self.path))
            with self.path.open('w') as stream:
                stream.write("")

        with self.path.open('r') as stream:
            self._temp = stream.read()
            self._logger.debug("current file status: {}".format(self._temp))

        self._stream = self.path.open('r+')
        return self._stream

    def __exit__(self, exception_type, exception_value, traceback):
        if self._stream is not None:
            self._logger.error("self._stream was not set")
            return self.revert()
        self._stream.close()

        if exception_value is not None:
            self._logger.error("exception found : {} {}".format(
                exception_type, exception_value))
            return self.revert()

        if self.check_func is not None:
            if self.check_func(self._temp):
                self._logger.error("Error found, reseting to a previous state")
                return self.revert()
        return True

    def revert(self):
        with self.path.open('w') as stream:
               stream.write(self._temp)
        return True
