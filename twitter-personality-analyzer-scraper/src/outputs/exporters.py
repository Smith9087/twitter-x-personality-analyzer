thondef export_to_markdown(analysis_result, file_path):
    with open(file_path, 'w') as f:
        f.write(f"# {analysis_result['result'][0]['heading']}\n")
        f.write(analysis_result['result'][0]['response'])
    print(f"Analysis results exported to {file_path}")