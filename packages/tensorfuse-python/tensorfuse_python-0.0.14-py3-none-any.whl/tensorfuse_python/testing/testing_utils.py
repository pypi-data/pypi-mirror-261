from tensorfuse_python.testing.constants import ignore_collisions, omit_repeats, number_repeats, processor_type, name

def create_csv_headers_and_row(collision_resolution: str, input_data: dict, processed_output: dict) -> tuple[list, list]:
    headers = []
    headers.extend(input_data.keys())
    row = [input_data[key] for key in headers]
    if collision_resolution == ignore_collisions:
        for key, val in processed_output.items():
            headers.append(key)
            row.append(val)
    elif collision_resolution == omit_repeats:
        for key, val in processed_output.items():
            if key not in headers:
                headers.append(key)
                row.append(val)
    elif collision_resolution == number_repeats:
        for key, val in processed_output.items():
            if key in headers:
                i = 1
                new_key = "{}_{}".format(key, i)
                while new_key in headers:
                    i += 1
                    new_key = "{}_{}".format(key, i)
                headers.append(new_key)
            else:
                headers.append(key)    
            row.append(val)
    else:
        raise NotImplementedError
    
    return headers, row


def create_output_file_name(file_name: str, processor, processors_info: dict):
    processor_name = processor.get(name, None)
    if processor_name:
        return file_name + "_" + processor_name + ".csv"
    else: 
        i = processors_info.get(processor[processor_type], 0)
        processors_info[processor[processor_type]] = i+1
        return file_name + "_" + processor[processor_type] + "_" + str(i+1) + ".csv"

