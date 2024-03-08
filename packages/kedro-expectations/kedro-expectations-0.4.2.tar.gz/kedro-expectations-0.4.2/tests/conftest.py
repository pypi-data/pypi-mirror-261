import great_expectations as ge
import shutil
import tempfile
import os
import pytest
from pathlib import Path

from great_expectations.core import ExpectationConfiguration
from kedro.framework.startup import bootstrap_project

from kedro_expectations.cli.init_ge import init_ge_and_create_datasources

_created_project_dirs = set()

test_dir = Path(__file__).parent


def _create_test_expectation_suites():
    # Initialize GX base structure
    init_ge_and_create_datasources()

    # Create a suite
    ge_context = ge.get_context()

    # Write failing suite
    not_true_expectation = ExpectationConfiguration(
        expectation_type="expect_column_values_to_not_be_null",
        kwargs={"column": "company_rating"
                },
    )
    ge_context.add_expectation_suite(f"companies_unexpected.failing_test_suite", expectations=[not_true_expectation])

    # Write succeeding suite
    true_expectation = ExpectationConfiguration(
        expectation_type="expect_column_values_to_not_be_null",
        kwargs={"column": "id"
                },
    )
    ge_context.add_expectation_suite(f"companies.succeeding_test_suite", expectations=[true_expectation])


@pytest.fixture(scope="session", autouse=True)
def initialize_kedro_project(request):
    # Set up a temporary directory for the Kedro project
    temp_dir = tempfile.mkdtemp(prefix="kedro_expectation_tests_")
    project_dir = Path(temp_dir)

    # Change the working directory to the project directory
    os.chdir(project_dir)

    # Create a new Kedro project
    exit_code = os.system(
        f"kedro new --starter={str(test_dir.joinpath('template_project'))}"
    )
    if exit_code != 0:
        raise Exception("Failed to initialize Kedro project")

    project_dir = project_dir.joinpath("test-project").resolve()
    os.chdir(project_dir)

    # register the project directory in Kedro
    bootstrap_project(project_dir)

    # create gx and the test expectations in the project dir
    _create_test_expectation_suites()

    # Return the project directory
    _created_project_dirs.add(project_dir)
    yield project_dir

    # Clean up the temporary project directory after the tests
    try:
        shutil.rmtree(temp_dir)
    except (FileNotFoundError, PermissionError):
        pass


def pytest_sessionfinish(session, exitstatus):
    # Cleanup any remaining temporary directories
    for project_dir in _created_project_dirs:
        try:
            shutil.rmtree(project_dir)
        except (FileNotFoundError, PermissionError):
            pass
