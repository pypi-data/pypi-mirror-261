import itertools
from typing import Dict, List, Optional

from tensorfuse_python.oss_telemtery import track_event
from tensorfuse_python.testing.constants import global_variables, global_processor, processor_type, global_evaluator, \
    evaluator_type, tests, output_csv, name, provider_api_key, passthrough, collision_resolution, number_repeats, omit_repeats
from tensorfuse_python.testing.evaluators.evaluator import Evaluator
from tensorfuse_python.testing.evaluators.evaluator_service import get_evaluator
from tensorfuse_python.testing.preprocessor import get_processor
from tensorfuse_python.testing.testing_utils import create_csv_headers_and_row, create_output_file_name

import logging
from colorama import Fore, Style

import csv
import os


# data -> Processor -> ev1 + ev2 + ev3 -> csv

def run_processor_and_evaluators_for_test_case(processor: Dict, testCase: Dict, evaluators: List[dict], csv_file: str,
                                               curr_vars: Dict, index: int, collision_resolution_type: str, 
                                               api_key: Optional[str] = None):
    # preprocess test case
    preprocessor = get_processor(processor[processor_type], processor)
    processed_output = preprocessor.process(testCase)

    eval_results = []
    # evaluate test case
    for evaluator in evaluators:
        evaluator_obj: Evaluator = get_evaluator(evaluator[evaluator_type], evaluator, provider_api_key=api_key)
        result, reason = evaluator_obj.evaluate(processed_output)
        track_event('test_case_run')
        # write to command line
        if result:
            logging.info(
                Fore.GREEN + '✓ Test passed for evaluator: %s, test case index: %d, variables: %s' + Style.RESET_ALL,
                evaluator_obj.name, index, curr_vars)
        else:
            logging.error(
                Fore.RED + '✗ Test failed for evaluator: %s, test case index: %d, variables: %s' + Style.RESET_ALL,
                evaluator_obj.name, index, curr_vars)

        eval_results.append((evaluator_obj, result, reason))  # append reason here
    # now write to csv testCase, processed_output, eval_1_result, eval_1_reason, eval_2_result, eval_2_reason, eval_3_result, eval_3_reason ...
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        # write headers if file is empty
        header_eval_arr = []
        data_eval_arr = []
        for eval in eval_results:
            header_eval_arr.append(f'{eval[0].name}_result')
            data_eval_arr.append(eval[1])
            header_eval_arr.append(f'{eval[0].name}_reason')
            data_eval_arr.append(eval[2])

        if processor[processor_type] == passthrough:
                collision_resolution_type = omit_repeats
        headers, data = create_csv_headers_and_row(collision_resolution=collision_resolution_type, 
                                                   input_data=testCase, processed_output=processed_output)
        headers.extend(header_eval_arr)
        data.extend(data_eval_arr)
        if os.stat(csv_file).st_size == 0:
            writer.writerow(headers)
        # write data
        writer.writerow(data)
    return True


def run_individual_test_case(processor: Dict, testCase: Dict, evaluator: Dict, csv_file: str):
    # preprocess test case
    preprocessor = get_processor(processor[processor_type], processor)
    processed_output = preprocessor.process(testCase)

    # evaluate test case
    evaluator: Evaluator = get_evaluator(evaluator[evaluator_type], evaluator)
    result, reason = evaluator.evaluate(processed_output)

    # append testCase, processed_output, and result to csv file
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)

        # write headers if file is empty
        if os.stat(csv_file).st_size == 0:
            headers = list(testCase.keys()) + list(processed_output.keys()) + ['result'] + [name] + [evaluator_type]
            writer.writerow(headers)
        # write data
        data = list(testCase.values()) + list(processed_output.values()) + [result] + [evaluator.name] + [
            evaluator.type]
        writer.writerow(data)
    return result


def run_tests(test_config: Dict):
    # configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    llm_api_key = test_config[provider_api_key] if provider_api_key in test_config else None

    # get global processors
    processors = test_config.get(global_processor, None)
    evaluator_results = {}  # dictionary to store results for each evaluator
    all_evaluator_results = []  # list to store all evaluator results
    file_name =test_config[output_csv]
    if file_name[-4:] == ".csv":
        file_name = file_name[:-4]
    processors_info = {}

    if not processors:
        processors = [{processor_type: passthrough}]
    for processor in processors:
        logging.info(Fore.BLUE + 'Running Processor Type: %s, Name: %s' + Style.RESET_ALL, 
                     processor[processor_type], processor.get(name, "Not Defined"))
        # get global evaluator
        evaluators = test_config[global_evaluator]
        collision_resolution_type = test_config.get(collision_resolution, number_repeats)
        if len(processors) > 1:
            output_file_name = create_output_file_name(file_name, processor, processors_info)
        else:
            output_file_name = file_name + ".csv"

        # get global variables
        variables = test_config[global_variables]
        # generate all combinations of global variables
        var_names = variables.keys()
        var_values = variables.values()
        for values in itertools.product(*var_values):
            current_vars = dict(zip(var_names, values))
            for index, test_case in enumerate(test_config[tests]):
                test_case.update(current_vars)
                try:
                    run_processor_and_evaluators_for_test_case(processor, test_case, evaluators,
                                                               output_file_name, current_vars, 
                                                               index, api_key=llm_api_key, 
                                                               collision_resolution_type=collision_resolution_type)
                except Exception as e:
                    logging.error(Fore.RED + 'An error occurred while running test case for index: %d, '
                                             'variables: %s. Error: %s' + Style.RESET_ALL, index, current_vars, str(e))

    logging.info('All tests completed!')

    return all_evaluator_results
