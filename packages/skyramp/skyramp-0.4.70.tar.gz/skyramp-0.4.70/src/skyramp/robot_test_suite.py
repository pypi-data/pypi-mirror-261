""" This module contains the robot test suite runner """
import os
from robot import run


ROBOT_CONTENT = """
*** Settings ***
Library           skyramp.RobotListener
Library     ${SKYRAMP_TEST_FILE}           

*** Test Cases ***
Skyramp Test Cases
    @{TestsList}    Execute Test  ${ADDRESS}    ${OVERRIDE_CODE_PATH}    ${GLOBAL_VARS}
    FOR    ${test}    IN    @{TestsList}
        Add Test Case    ${test[0].test_case_name}   Keyword To Execute    ${test}
    END

*** Keywords ***
Keyword To Execute
    [Arguments]    ${test}
    Run Keyword If    '${test[0].test_case_status}' != '[]'    Fail    ${test}
    Run Keyword If    '${test[0].test_case_status}' == '[]'    Log    ${test}
"""
SKYRAMP_ROBOT_TEMPLATE_PATH ="../robot_report"
SKYRAMP_ROBOT_FILE_NAME = "skyramp_tests.robot"

def run_robot_test_suite(robot_file="", variable=None, output_dir=None,):
    """
    Run the robot test suite
    :param robot_file: The robot file to run
    :param variable: The variables to pass to the robot file
    :param output_dir: The output directory to store the robot report
    """
    robot_path = robot_file
    if robot_path == "":
        # Create a file to store the robot content
        if not os.path.exists(SKYRAMP_ROBOT_TEMPLATE_PATH):
            os.makedirs(SKYRAMP_ROBOT_TEMPLATE_PATH)
        robot_path = os.path.join(SKYRAMP_ROBOT_TEMPLATE_PATH,SKYRAMP_ROBOT_FILE_NAME)
        if not os.path.exists(robot_path):
            with open(robot_path, 'w') as file:
                file.write(ROBOT_CONTENT)

    # Create output directory if it does not exist
    if output_dir is not None:
        # Convert the relative path to an absolute path
        output_dir = os.path.abspath(output_dir)
        # Check if the directory exists, if not create it
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    run(robot_path, variable=variable, outputdir=output_dir)
