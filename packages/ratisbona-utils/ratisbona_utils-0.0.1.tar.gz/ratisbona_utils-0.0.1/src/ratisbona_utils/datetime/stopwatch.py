from datetime import datetime


class Stopwatch:
    """
    Class helpful to time operations.

    best use it with a with-statement like:
    ```python
        with Stopwatch() as stopwatch:
            do_something_expensive

        stopwatch.time_elapsed_millis # now contains elapsed time in milliseconds
        print(stopwatch) # prints nicely formatted timeing information.
    ```
    """

    def __init__(self):
        self.is_counting: bool = False
        self.time_elapsed_millis: int = 0
        self.last_advanced: datetime = None
        self.show_msec = True
        print(self.__dict__)

    def __enter__(self):
        self.start()
        print("Started: ", self.__dict__)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
        print("Stopped: ", self.__dict__)

    def start(self) -> None:
        """
        Starts the stopwatch
        """
        self.is_counting = True
        self.last_advanced = None
        self.advance()

    def stop(self) -> None:
        """
        Stops the stopwatch. You may restart it using `start()` in which case the
        times will add up!
        """
        self.advance()
        self.is_counting = False
        self.last_advanced = None

    def toggle(self) -> None:
        """
        Toggles the state of the stopwatch. If it is counting it will stop and vice versa.
        """
        if self.is_counting:
            self.stop()
        else:
            self.start()

    def reset(self):
        """
        Resets the stopwatch to zero. It will also stop counting if it was counting at the time of reset.
        So don't forget to call `start()` if you want to continue counting.
        """
        old_is_counting = self.is_counting
        self.is_counting = False
        self.time_elapsed_millis = False
        self.last_advanced = None
        self.is_counting = old_is_counting
        self.advance()

    def __str__(self):
        """
        Returns a nicely formatted string with the elapsed time.
        Format of the String is: `HH:MM:SS.mmm` where `HH` is hours, `MM` is minutes, `SS` is seconds and `mmm` is milliseconds.
        If `show_msec` is set to `False` the milliseconds part will be omitted.
        """
        raw_secs, milliseconds = divmod(self.time_elapsed_millis, 1000)
        raw_min, seconds = divmod(raw_secs, 60)
        hours, minutes = divmod(raw_min, 60)

        retval = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        if self.show_msec:
            retval += f".{milliseconds:03d}"

        return retval

    def advance(self):
        """
        Advances the time by the time that has passed since the last advance.
        Call it, if you want to have a in between-reading before stopping the clock.
        """
        if not self.is_counting:
            return
        the_now = datetime.now()
        if self.last_advanced:
            difference = the_now - self.last_advanced
            self.time_elapsed_millis += difference.microseconds // 1000
        self.last_advanced = the_now
