import pytest
from db.DB import DB
from model.Human import Human

db = DB()

@pytest.fixture
def human():
    return Human()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        print('Я запустился строго полсе теста', report.nodeid, report.outcome)
        db.insertTestResult(report.nodeid, report.outcome)