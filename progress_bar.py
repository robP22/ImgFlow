def progress_b(progress, total, _bar='❚') -> None:
    ratio: float = progress / total
    percent: float = 100 * ratio

    width: int = 78
    fill_amount: int = round(width * ratio)
    empty_amount: int = width - fill_amount

    bar_str: str = _bar * fill_amount + '-' * empty_amount

    print(f'\r[{bar_str}] {percent:6.2f}%', end='\r')