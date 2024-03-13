from pathlib import Path
import jsonlines
import src.data_ingestion.simple_nhs_conditions_scrape as snhscs


def process_nhs_conditions_json(docs_directory, json_file):
    """Extracts text from the json file and writes it to a text files in the docs_directory
    Args:
        docs_directory (str): The directory to write the text files to
        json_file (str): The json file to extract the text from
    """
    Path(docs_directory).mkdir(parents=True, exist_ok=True)

    with jsonlines.open(json_file) as reader:
        for index, obj in enumerate(reader):
            extracted_text = snhscs.process_nhs_conditions_json(obj)

            page_name = obj["source_url"].split("/")[-2]

            if extracted_text != "":
                with open(
                    f"{docs_directory}/{page_name}.txt", "w", encoding="utf-8"
                ) as file:
                    file.write(extracted_text)

            print(index, ": ", obj["source_url"])
