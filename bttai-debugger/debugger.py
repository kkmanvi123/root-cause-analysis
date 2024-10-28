#!/usr/bin/env python3

import re
import os
import sys
import argparse
import pickle
import pandas as pd

def check_memory_leak_features(code_snippet):
    features = {
        "static_instance_variable": "static " in code_snippet,
        "multiple_instances": code_snippet.count("new ") > 1,
        "missing_finally_blocks": "finally" not in code_snippet,
        "no_try_with_resources": "try (" not in code_snippet,
        "no_explicit_close": "close()" not in code_snippet,
        "no_close_call": "close()" not in code_snippet,
        "exceptions_not_handled": "catch (" not in code_snippet,
        "present_static_inner_classes": "static" in code_snippet,
        "uninitialized_variables": "null" in code_snippet and ";" in code_snippet,
        "method_called_on_null": code_snippet.count("->") > 1 and "null" in code_snippet,
        "null_check_after_dereference": (
            "== null" in code_snippet and code_snippet.index("== null") > code_snippet.index(".")
        ),
    }

    # Comments with keywords
    comment_keywords = re.findall(r'//.*\b(TODO|FIXME|HACK)\b', code_snippet, re.IGNORECASE)
    features["comments_with_keywords"] = len(comment_keywords) > 0

    # Shared resources without synchronization
    shared_resources = re.findall(r'\b(List|HashMap|HashSet|Vector)\b', code_snippet)
    sync_blocks = re.findall(r'\bsynchronized\b', code_snippet)
    features["shared_resources_no_sync"] = len(shared_resources) > 0 and len(sync_blocks) == 0

    # Variables set to null
    variables_set_to_null = re.findall(r'=\s*null\b', code_snippet)
    features["num_variables_set_to_null"] = len(variables_set_to_null)

    # Resource allocations
    resource_allocations = re.findall(r'\bnew\b', code_snippet)
    features["num_resource_allocations"] = len(resource_allocations)

    # Null checks
    null_checks_equals = re.findall(r'==\s*null\b', code_snippet)
    null_checks_notequals = re.findall(r'!=\s*null\b', code_snippet)
    features["num_null_checks"] = len(null_checks_equals) + len(null_checks_notequals)

    # Mutable objects used
    mutable_objects = re.findall(r'\b(ArrayList|HashMap|HashSet|LinkedList|Vector)\b', code_snippet)
    features["num_mutable_objects_used"] = len(mutable_objects)

    return features

def main():
    parser = argparse.ArgumentParser(
        description="Analyze Java code for potential memory leaks and related issues."
    )
    parser.add_argument(
        "file", metavar="FILE", type=str, help="Path to the Java file to analyze."
    )

    args = parser.parse_args()
    file_path = args.file

    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    with open(file_path, 'r') as f:
        code_snippet = f.read()

    features = check_memory_leak_features(code_snippet)

    print(f"\nAnalyzing the file {file_path}...:\n")
    
    # Load the model
    with open('random_forest_model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    # Make predictions
    feature = pd.DataFrame([features])
    new_predictions = loaded_model.predict(feature)
    if new_predictions[0] == 0:
        pred_label = "NULL_DEREFERENCE"
    else:
        pred_label = "MEMORY_LEAK"
    print(f"Predicted bug: {pred_label}")

if __name__ == "__main__":
    main()
