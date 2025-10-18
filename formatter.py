def format_process_output(target_string: str, symbol: str=chr(0x305), width: int=78) -> str:
    """ Formats the string for a 78 character terminal width. """
    target: int = (width - len(target_string) // 2) - 1
    left: str = symbol * (target//4) # divide by 4 as the symbol is 2 characters wide
    right: str = symbol * (target//4)
    return left + target_string + right

def summary(fails_len: int, files_len: int) -> None:
    """ Print a formatted summary of the image processing function."""
    try:
        fail_percent: float = (fails_len / files_len) * 100
        _success: str = f"Completed: \033[4m{100.0 - fail_percent:5.1f}%\033[0m"
        _failed: str = f"Failed: \033[4m{fail_percent:5.1f}%\033[0m"
        _items: str = f"Processed: \033[4m{files_len - fails_len}\033[0m"
        _summary: str = f" SUMMARY {_success} | {_failed} | {_items} "
        print(f"\n|{format_process_output(_summary, '一', width=70)}|\n")
    except ZeroDivisionError:
        print(f"[NUMBER OF FILES] = {files_len} | The list of files must be empty.")
