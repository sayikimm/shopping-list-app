import logging

logging.basicConfig(level=logging.INFO, format= '%(asctime)s-%(levelname)s-%(message)s')

def add_item(item: str,shopping_list: list[str]) -> None:
    shopping_list.append(item)
    logging.info(f'Added {item} Successfully!')

def remove_item(item: str, shopping_list: list[str]) -> None:
    if item in shopping_list:
        shopping_list.remove(item)
        logging.info(f'Removed {item} Successfully!')
    else:
        logging.warning(f'There is no {item} in the list')