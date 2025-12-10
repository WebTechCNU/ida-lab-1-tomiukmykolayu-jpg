from src.webparser import parse_web_page
from src.apiparser import parse_api
from src.jsonparser import parse_json
from src.csvparser import parse_csv
from src.visualize import visualize_data


def main():
    print("=== Testing parse_web_page() ===")
    try:
        text_preview = parse_web_page("https://fmi.chnu.edu.ua/")[:255]
        print("Web page text preview:", text_preview)
    except Exception as e:
        print("Error in parse_web_page:", e)

    print("\n=== Testing parse_api() ===")
    try:
        parse_api("https://api.github.com/")
        print("Data saved to result.json")
    except Exception as e:
        print("Error in parse_api:", e)

    print("\n=== Testing parse_json() ===")
    try:
        date_to_find = "2024-8-19"
        json_result = parse_json(date_to_find)
        print(f"JSON result for {date_to_find}: {json_result}")
    except Exception as e:
        print("Error in parse_json:", e)

    print("\n=== Testing parse_csv() ===")
    try:
        date_to_find = "1997-5-22"
        csv_result = parse_csv(date_to_find)
        print(f"CSV result for {date_to_find}: {csv_result}")
    except Exception as e:
        print("Error in parse_csv:", e)

    print("\n=== Testing visualize_data() ===")
    try:
        visualize_data()
        print("Visualization created successfully.")
    except Exception as e:
        print("Error in visualize_data:", e)


if __name__ == "__main__":
    main()
