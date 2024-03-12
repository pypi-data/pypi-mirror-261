import os
import subprocess
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))


from openai import AzureOpenAI
from configparser import ConfigParser
from time import perf_counter
import AIUT_Helper

MODEL_TEMP = 0.7
MAX_TOKENS = 5000
RESULT_SUCCESS = "TEST Case Generated"
RESULT_ERROR = ""

class utils():
    def __init__(self):
        pass

    def cient(self, client):
        self.__client = client

    def client(self):
        return self.__client

    def api_end_point(self, api_end_point):
        self.__api_end_point = api_end_point

    def api_end_point(self):
        return self.__api_end_point

    def api_key(self, api_key):
        self.__api_key = api_key

    def api_key(self):
        return self.__api_key

    def api_version(self, api_version):
        self.__api_version = api_version

    def api_version(self):
        return self.__api_version

    def model_deployment_name(self, model_deployment_name):
        self.__model_deployment_name = model_deployment_name

    def model_deployment_name(self):
        return self.__model_deployment_name

    def src_files_location(self, src_files_location):
        self.__src_files_location = src_files_location

    def src_files_location(self):
        return self.__src_files_location

    def dest_test_files_location(self, dest_test_files_location):
        self.__dest_test_files_location = dest_test_files_location

    def dest_test_files_location(self):
        return self.__dest_test_files_location

    def code_base_location(self, code_base_location):
        self.__code_base_location = code_base_location

    def code_base_location(self):
        return self.__code_base_location

    def unit_test_framework(self, unit_test_framework):
        self.__unit_test_framework = unit_test_framework

    def unit_test_framework(self):
        return self.__unit_test_framework

    def src_file_name(self, src_file_name):
        self.__src_file_name = src_file_name

    def src_file_name(self):
        return self.__src_file_name

    def src_file_location(self, src_file_location):
        self.__src_file_location = src_file_location

    def src_file_location(self):
        return self.__src_file_location

    def test_file_name(self, test_file_name):
        self.__test_file_name = test_file_name

    def test_file_name(self):
        return self.__test_file_name

    def test_file_location(self, test_file_location):
        self.__test_file_location = test_file_location

    def test_file_location(self):
        return self.__test_file_location

    def test_count(self, test_count):
        self.__test_count = test_count

    def test_count(self):
        return self.__test_count

    def read_config(self):
        try:
            configur = ConfigParser()
            cur_dir = os.path.dirname(os.path.abspath(__file__))
            par_dir = os.path.dirname(cur_dir)
            settings_dir = os.path.join(par_dir,'settings')
            settings_file_path = os.path.join(settings_dir,"UT_Settings.ini")
            configur.read(settings_file_path)
            self.api_end_point = configur.get('Default','azure_endpoint')
            self.api_key = configur.get('Default','api_key')
            self.api_version = configur.get('Default','api_version')
            self.model_deployment_name = configur.get('Default','model_deployment_name')
            #self.src_files_location = configur.get('CSharp','src_files_location')
            self.dest_test_files_location = configur.get('CSharp','dest_test_files_location')
            self.code_base_location = configur.get('CSharp','code_base_location')
            
            if self.dest_test_files_location[-1] != '\\':
                self.dest_test_files_location += '\\'

            if self.code_base_location[-1] != '\\':
                self.code_base_location += '\\'

            return True
        except Exception as err:
            print(err)
            return False

    def create_azure_connection(self):
        try:
            self.client = None
            if (self.read_config()):
                self.client = AzureOpenAI(
                    azure_endpoint=self.api_end_point,
                    api_key=self.api_key,
                    api_version=self.api_version)
                return self.client
            else:
                return False
        except Exception as err:
            print("Error while initiating the connection to Azure OpenAI: "+err)
            return False

def gen_no_of_tc(class_to_test, unit_test_framework):
    try:
        global NO_OF_TC
        global NO_OF_LARGE_TC
        count = 1
        for letter in class_to_test:

            if unit_test_framework.lower()=="nunit" or unit_test_framework.lower()=="mstest":
                if letter == ';' or letter == "{":
                    count += 1

        NO_OF_TC = count // 10

        if count > 100:
            NO_OF_TC = count // 10
        else:
            NO_OF_TC = 10

        if count > 100:
            NO_OF_LARGE_TC = count // 100
        else:
            NO_OF_LARGE_TC = 1

        return True
    except Exception as err:
        print(err)
        return  False

def gen_prompt(class_to_test,unit_test_framework):
    try:
        global execute_messages
        execute_system_message = {}
        execute_user_message = {}
        if unit_test_framework.lower() =="mstest":
            execute_system_message = {
                "role": "system",
                "content":
                    "You are a world-class developer with an eagle eye for unintended bugs and edge cases. You write careful, accurate unit tests. When asked to reply only with the language of the function, code, you write all of your code in a single block.",
            }
            execute_user_message = {
                "role": "user",
                "content":
                    f"""
                ```csharp
              {class_to_test}
              ```
              A good unit test suite should aim to:
              - Test the function's behavior for a wide range of possible inputs
              - Test edge cases that the author may not have foreseen
              - Take advantage of the features of `{unit_test_framework}` to make the tests easy to write and maintain
              - Be easy to read and understand, with clean code and descriptive names
              - Be deterministic, so that the tests always pass or fail in the same way.
              Using the required framework for that language, mentioning the framework used, write a suite of unit tests for the function, following the cases above. Also create an object of all the classes while generating test cases. Use <classname>.<function_name> before calling the function every time. If there's any class being created in the given program, include it in the generated program also and make sure to create an object of it in the test cases program as well. 
              All the using statements from the provided source to be added also in the generated program.
              Include helpful comments to explain each line. Reply only with code.
              Since you're using `{unit_test_framework}`, Use Asserts to compare expected result, so include using Microsoft.VisualStudio.TestTools.UnitTesting;. Make sure there are no syntax errors in the generated code. Feel free to import any other packages that are used. 
              Also create the cases to cover the exceptions block if added in methods in provided code.
              Ensure 100% Code Coverage, so include all unexpected edge cases also.
              Make sure there are no missed branches or lines while generating test cases. Ensure 100% cyclomatic complexity. Have atleast {NO_OF_TC} test cases + unexpected edge cases and atleast {NO_OF_LARGE_TC} large test case. 
              """,
            }
        elif unit_test_framework.lower() =="nunit":
            execute_system_message = {
                "role": "system",
                "content":
                    "You are a world-class developer with an eagle eye for unintended bugs and edge cases. You write careful, accurate unit tests. When asked to reply only with the language of the function, code, you write all of your code in a single block.",
            }
            execute_user_message = {
                "role": "user",
                "content":
                    f"""
                ```csharp
              {class_to_test}
              ```
              A good unit test suite should aim to:
              - Test the function's behavior for a wide range of possible inputs
              - Test edge cases that the author may not have foreseen
              - Take advantage of the features of `{unit_test_framework}` to make the tests easy to write and maintain
              - Be easy to read and understand, with clean code and descriptive names
              - Be deterministic, so that the tests always pass or fail in the same way.
              Using the required framework for that language, mentioning the framework used, write a suite of unit tests for the function, following the cases above. Also create an object of all the classes while generating test cases. Use <classname>.<function_name> before calling the function everytime. If there's any class being created in the given program, include it in the generated program also and make sure to create an object of it in the test cases program as well. 
              All the using statements from the provided source to be added also in the generated program.
              Include helpful comments to explain each line. Reply only with code.
              Since you're using `{unit_test_framework}`, Use Asserts to compare expected result, so inclue using NUnit.Framework;. 
              Make sure there are no syntax errors in the generated code. Feel free to import any other packages that are used. 
              Ensure 100% Code Coverage, so include all unexpected edge cases also.
              Also create the cases to cover the exceptions block if added in methods in provided code.
              Make sure there are no missed branches or lines while generating test cases. Ensure 100% cyclomatic complexity. Have at least {NO_OF_TC} test cases + unexpected edge cases and at least {NO_OF_LARGE_TC} large test case. 
              """,
            }
        execute_messages = [execute_system_message, execute_user_message]
        return True
    except Exception as err:
        print(err)
        return False

def read_src_file(objUtils, file):
    try:
        objUtils.src_file_location = file
        objUtils.src_file_name = file.split("\\")[-1]
        objFile = open(file, "r+")
        class_to_test = objFile.read()
        print(class_to_test)
        if (gen_no_of_tc(class_to_test, objUtils.unit_test_framework)):
            if(gen_prompt(class_to_test, objUtils.unit_test_framework)):
                return True
            else:
                return  False
        else:
            return False
    except Exception as err:
        print(err)
        return False

def create_testcase_file(objUtils, response):
    try:
        objUtils.test_file_name = objUtils.src_file_name
        code_in_response = ""
        testcase_file_name = ""
        for chunk in response.choices[0].message.content:
            code_in_response += chunk
            print(code_in_response)

        generated_code = code_in_response.split("```csharp")[1].split("```")[0].strip()
        classs = ""
        words = generated_code.split(" ")
        x = words.index("class")
        classs = words[x + 1]
        location = objUtils.dest_test_files_location
        #testcase_file_name = classs.strip() + ".cs"
        testcase_file_name = objUtils.test_file_name
        location = location + testcase_file_name
        objUtils.test_file_location= location
        #objUtils.test_file_name = testcase_file_name
        f = open(location, "w+")
        f.write(generated_code)
        f.close()
        objUtils.test_count = AIUT_Helper.count_test(generated_code, objUtils.unit_test_framework)
        return location, testcase_file_name
    except Exception as err:
        print(err)
        return False

def execute_test_cases(framework):
    response=""
    try:
        objUtils = utils()
        objUtils.read_config()
        #if framework.lower() == "nunit":
        #    pass
        #elif framework.lower() == "mstest":
        command0 = "del *.html"
        command1 = 'dotnet test --collect:"Xplat Code Coverage" -l:html -r htmlresultsfolder'
        command2 = "ren *.html index.html"
        command3 = 'reportgenerator -reports:"../**/coverage.cobertura.xml" -targetdir:"TestResults/CoverageReport" -reporttypes:"html"'
        result0 = subprocess.run(command0, shell=True, capture_output=True, text=True, cwd=objUtils.code_base_location + "TestResults\\")
        if result0.returncode == 0:
            #print("Command executed successfully.")
            #print("Output:")
            #print(result0.stdout)
            str_find = "Html test results file"
            result1 = subprocess.run(command1, shell=True, capture_output=True, text=True, cwd=objUtils.code_base_location)
            if str(result1).find(str_find) > 0:
                #print("Command executed successfully.")
                #print("Output:")
                #print(result1.stdout)
                response = [True, result1.stdout]
                result2 = subprocess.run(command2, shell=True, capture_output=True, text=True, cwd=objUtils.code_base_location+ "TestResults\\")
                result3 = subprocess.run(command3, shell=True, capture_output=True, text=True, cwd=objUtils.code_base_location)
                print(result3)
                if result3.returncode == 0:
                    #print("Command executed successfully.")
                    #print("Output:")
                    #print(result3.stdout)
                    # Open the Test Run Result HTML file in the default web browser
                    subprocess.run("start index.html", shell=True, text=True,
                                   cwd=objUtils.code_base_location + "TestResults\\")

                    # Open the Code Coverage Report HTML file in the default web browser
                    subprocess.run("start index.html", shell=True, text=True,
                                   cwd=objUtils.code_base_location + "TestResults\\CoverageReport\\")
                else:
                    print("Command execution failed.")
                    print("Error:")
                    print(result3.stderr)
                    response = [False, result3.stderr]
            else:
                print("Command execution failed.")
                print("Error:")
                print(result1.stderr)
                response = [False, result1.stderr]
        else:
            print("Command execution failed.")
            print("Error:")
            print(result0.stderr)
            response = [False, result0.stderr]
    except Exception as err:
        print(err)
        response = [False, err]
    finally:
        return response

def generate_unit_cases(file_path, framework):
    try:
        t1_start = perf_counter()
        objUtils = utils()
        if objUtils.create_azure_connection():
            objUtils.unit_test_framework = framework
            read_src_file(objUtils,file_path)
            response = objUtils.client.chat.completions.create(
               model=objUtils.model_deployment_name,  # model = "deployment_name".
               messages=execute_messages,
               temperature=MODEL_TEMP,
               max_tokens=MAX_TOKENS
            )
            testcase_file_name = create_testcase_file(objUtils, response)
            t1_stop = perf_counter()

            elapsed_time_sec = t1_stop - t1_start
            elapsed_time_min = elapsed_time_sec / 60
            print("Elapsed time sec: ", round(elapsed_time_sec, 4))
            print("Elapsed time min: ", round(elapsed_time_min, 2))

            cost_testcase = AIUT_Helper.calculate_price(response.usage.prompt_tokens, response.usage.completion_tokens)
            print(f"Metrics:"
                  f"Source File Name {objUtils.src_file_name}, "
                  f"Source File Path {objUtils.src_file_location}, "
                  f"Generated Test Case File {objUtils.test_file_name}, "
                  f"Generated Test Case File Path {objUtils.test_file_location}, "
                  f"No. of Test Cases Generated {objUtils.test_count}, "
                  f"Token sent in Prompt as request {response.usage.prompt_tokens}, "
                  f"Token received as response {response.usage.completion_tokens}, "
                  f"Total Tokens processed {response.usage.total_tokens},"
                  f"Open AI Cost USD {cost_testcase},"
                  f"Result {RESULT_SUCCESS}",
                  f"Elapsed Time {round(elapsed_time_min, 2)} minutes")
            metrics = f"{objUtils.src_file_name}," \
                  f"{objUtils.src_file_location}," \
                  f"{objUtils.test_file_name}," \
                  f"{objUtils.test_file_location}," \
                  f"{objUtils.test_count}," \
                  f"{response.usage.prompt_tokens}," \
                  f"{response.usage.completion_tokens}," \
                  f"{response.usage.total_tokens}," \
                  f"$ {cost_testcase}," \
                  f"{RESULT_SUCCESS}," \
                  f"{round(elapsed_time_min, 2)}"
            return metrics
    except Exception as err:
        print(err)
        RESULT_ERROR = err
        metrics = f"{objUtils.src_file_name}, " \
                  f"{objUtils.src_file_location}, " \
                  f"{objUtils.test_file_name}, " \
                  f"{objUtils.test_file_location}, " \
                  f"{RESULT_ERROR}"
        return metrics