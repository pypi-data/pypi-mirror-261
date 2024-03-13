""" Robot Framework listener to add test cases to the current suite """

class RobotListener:
    """
    Robot Framework listener
    """
    ROBOT_LISTENER_API_VERSION = 3
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        # pylint: disable=invalid-name
        self.ROBOT_LIBRARY_LISTENER = self
        self.current_suite = None

    # pylint: disable=unused-argument
    def _start_suite(self, suite, result):
        self.current_suite = suite

    def add_test_case(self, name, kwname, *args):
        """Adds a test case to the current suite

        'name' is the test case name
        'kwname' is the keyword to call
        '*args' are the arguments to pass to the keyword

        Example:
            add_test_case  Example Test Case  
            ...  log  hello, world  WARN
        """
        test_case = self.current_suite.tests.create(name=name)
        test_case.body.create_keyword(name=kwname, args=args)
