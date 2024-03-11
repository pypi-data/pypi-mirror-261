from liveramp_automation.helpers.file import FileHelper


def test_read_init_file():
    file_name = "test.ini"
    ini_file = FileHelper.read_init_file("tests/test_helpers/", file_name)
    assert ini_file


def test_read_json_file():
    file_path = "tests/test_helpers/test.json"
    json_str = FileHelper.read_json_report(file_path)
    assert json_str


def test_load_env_yaml():
    file_prefix = "test"
    env_str = "stg"
    yaml_str = FileHelper.load_env_yaml("tests/test_helpers/", file_prefix, env_str)
    assert yaml_str


def test_deal_testcase_json():
    file_path = "tests/test_helpers/test.json"
    testcase = FileHelper.read_testcase_json(file_path)
    assert testcase


def test_read_junit_xml_report():
    file_path = "tests/test_helpers/junit.xml"
    testcase = FileHelper.read_junit_xml_report(file_path)
    print(testcase)
    assert testcase
