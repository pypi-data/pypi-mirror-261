from logging import Logger
from typing import Any, Final
from pypomes_core import APP_PREFIX, env_get_int, env_get_str, str_sanitize

DB_ENGINE: Final[str] = env_get_str(f"{APP_PREFIX}_DB_ENGINE")
DB_NAME: Final[str] = env_get_str(f"{APP_PREFIX}_DB_NAME")
DB_HOST: Final[str] = env_get_str(f"{APP_PREFIX}_DB_HOST")
DB_PORT: Final[int] = env_get_int(f"{APP_PREFIX}_DB_PORT")
DB_PWD: Final[str] = env_get_str(f"{APP_PREFIX}_DB_PWD")
DB_USER: Final[str] = env_get_str(f"{APP_PREFIX}_DB_USER")

match DB_ENGINE:
    case "postgres":
        from . import _postgres_pomes
    case "sqlserver":
        from . import _sqlserver_pomes


def db_connect(errors: list[str] | None, logger: Logger = None) -> Any:
    """
    Obtain and return a connection to the database, or *None* if the connection cannot be obtained.

    :param errors: incidental error messages
    :param logger: optional logger
    :return: the connection to the database
    """
    result: Any = None
    match DB_ENGINE:
        case "postgres":
            result = _postgres_pomes.db_connect(errors, logger)
        case "sqlserver":
            result = _sqlserver_pomes.db_connect(errors, logger)

    return result


def db_exists(errors: list[str] | None, table: str,
              where_attrs: list[str], where_vals: tuple, logger: Logger = None) -> bool:
    """
    Determine whether the table *table* in the database contains at least one tuple.

    For this determination, the where *where_attrs* are made equal to the
    *where_values* in the query, respectively.
    If more than one, the attributes are concatenated by the *AND* logical connector.

    :param errors: incidental error messages
    :param table: the table to be searched
    :param where_attrs: the search attributes
    :param where_vals: the values for the search attributes
    :param logger: optional logger
    :return: True if at least one tuple was found
    """
    result: bool | None = None
    match DB_ENGINE:
        case "postgres":
            result = _postgres_pomes.db_exists(errors, table, where_attrs, where_vals, logger)
        case "sqlserver":
            result = _sqlserver_pomes.db_exists(errors, table, where_attrs, where_vals, logger)

    return result


def db_select_one(errors: list[str] | None, sel_stmt: str, where_vals: tuple,
                  require_nonempty: bool = False, logger: Logger = None) -> tuple:
    """
    Search the database and return the first tuple that satisfies the *sel_stmt* search command.

    The command can optionally contain search criteria, with respective values given
    in *where_vals*. The list of values for an attribute with the *IN* clause must be contained
    in a specific tuple. In case of error, or if the search is empty, *None* is returned.

    :param errors: incidental error messages
    :param sel_stmt: SELECT command for the search
    :param where_vals: values to be associated with the search criteria
    :param require_nonempty: defines whether an empty search should be considered an error
    :param logger: optional logger
    :return: tuple containing the search result, or None if there was an error, or if the search was empty
    """
    result: tuple | None = None
    match DB_ENGINE:
        case "postgres":
            result = _postgres_pomes.db_select_one(errors, sel_stmt, where_vals, require_nonempty, logger)
        case "sqlserver":
            result = _sqlserver_pomes.db_select_one(errors, sel_stmt, where_vals, require_nonempty, logger)

    return result


def db_select_all(errors: list[str] | None, sel_stmt: str,  where_vals: tuple,
                  require_min: int = None, require_max: int = None, logger: Logger = None) -> list[tuple]:
    """
    Search the database and return all tuples that satisfy the *sel_stmt* search command.

    The command can optionally contain search criteria, with respective values given
    in *where_vals*. The list of values for an attribute with the *IN* clause must be contained
    in a specific tuple. If the search is empty, an empty list is returned.

    :param errors: incidental error messages
    :param sel_stmt: SELECT command for the search
    :param where_vals: the values to be associated with the search criteria
    :param require_min: optionally defines the minimum number of tuples to be returned
    :param require_max: optionally defines the maximum number of tuples to be returned
    :param logger: optional logger
    :return: list of tuples containing the search result, or [] if the search is empty
    """
    result: list[tuple] | None = None
    match DB_ENGINE:
        case "postgres":
            result = _postgres_pomes.db_select_all(errors, sel_stmt, where_vals, require_min, require_max,  logger)
        case "sqlserver":
            result = _sqlserver_pomes.db_select_all(errors, sel_stmt, where_vals, require_min, require_max, logger)

    return result


def db_insert(errors: list[str] | None, insert_stmt: str,
              insert_vals: tuple, logger: Logger = None) -> int:
    """
    Insert a tuple, with values defined in *insert_vals*, into the database.

    :param errors: incidental error messages
    :param insert_stmt: the INSERT command
    :param insert_vals: the values to be inserted
    :param logger: optional logger
    :return: the number of inserted tuples (0 ou 1), or None if an error occurred
    """
    result: int | None = None
    match DB_ENGINE:
        case "postgres":
            result = _postgres_pomes.db_insert(errors, insert_stmt, insert_vals, logger)
        case "sqlserver":
            result = _sqlserver_pomes.db_insert(errors, insert_stmt, insert_vals, logger)

    return result


def db_update(errors: list[str] | None, update_stmt: str,
              update_vals: tuple, where_vals: tuple, logger: Logger = None) -> int:
    """
    Update one or more tuples in the database, as defined by the command *update_stmt*.

    The values for this update are in *update_vals*.
    The values for selecting the tuples to be updated are in *where_vals*.

    :param errors: incidental error messages
    :param update_stmt: the UPDATE command
    :param update_vals: the values for the update operation
    :param where_vals: the values to be associated with the search criteria
    :param logger: optional logger
    :return: the number of updated tuples, or None if an error occurred
    """
    result: int | None = None
    match DB_ENGINE:
        case "postgres":
            result = _postgres_pomes.db_update(errors, update_stmt, update_vals, where_vals,  logger)
        case "sqlserver":
            result = _sqlserver_pomes.db_update(errors, update_stmt, update_vals, where_vals, logger)

    return result


def db_delete(errors: list[str] | None, delete_stmt: str,
              where_vals: tuple, logger: Logger = None) -> int:
    """
    Delete one or more tuples in the database, as defined by the *delete_stmt* command.

    The values for selecting the tuples to be deleted are in *where_vals*.

    :param errors: incidental error messages
    :param delete_stmt: the DELETE command
    :param where_vals: the values to be associated with the search criteria
    :param logger: optional logger
    :return: the number of deleted tuples, or None if an error occurred
    """
    result: int | None = None
    match DB_ENGINE:
        case "postgres":
            result = _postgres_pomes.db_delete(errors, delete_stmt, where_vals,  logger)
        case "sqlserver":
            result = _sqlserver_pomes.db_delete(errors, delete_stmt, where_vals, logger)

    return result


def db_bulk_insert(errors: list[str] | None, insert_stmt: str,
                   insert_vals: list[tuple], logger: Logger = None) -> int:
    """
    Insert the tuples, with values defined in *insert_vals*, into the database.

    :param errors: incidental error messages
    :param insert_stmt: the INSERT command
    :param insert_vals: the list of values to be inserted
    :param logger: optional logger
    :return: the number of inserted tuples, or None if an error occurred
    """
    result: int | None = None
    match DB_ENGINE:
        case "postgres":
            result = _postgres_pomes.db_bulk_insert(errors, insert_stmt, insert_vals, logger)
        case "sqlserver":
            result = _sqlserver_pomes.db_bulk_insert(errors, insert_stmt, insert_vals, logger)

    return result


def db_exec_stored_procedure(errors: list[str] | None, proc_name: str, proc_vals: tuple,
                             require_nonempty: bool = False, require_count: int = None,
                             logger: Logger = None) -> list[tuple]:
    """
    Execute the stored procedure *proc_name* in the database, with the parameters given in *proc_vals*.

    :param errors: incidental error messages
    :param proc_name: name of the stored procedure
    :param proc_vals: parameters for the stored procedure
    :param require_nonempty: defines whether an empty search should be considered an error
    :param require_count: optionally defines the number of tuples required to be returned
    :param logger: optional logger
    :return: list of tuples containing the search result, or [] if the search is empty
    """
    result: list[tuple] | None = None
    match DB_ENGINE:
        case "postgres":
            result = _postgres_pomes.db_exec_stored_procedure(errors, proc_name, proc_vals,
                                                              require_nonempty, require_count,  logger)
        case "sqlserver":
            result = _sqlserver_pomes.db_exec_stored_procedure(errors, proc_name, proc_vals,
                                                               require_nonempty, require_count, logger)

    return result


def _db_except_msg(exception: Exception) -> str:
    """
    Format and return the error message corresponding to the exception raised while accessing the database.

    :param exception: the exception raised
    :return:the formatted error message
    """
    return f"Error accessing '{DB_NAME}' at '{DB_HOST}': {str_sanitize(f'{exception}')}"


def _db_build_query_msg(query_stmt: str, bind_vals: tuple) -> str:
    """
    Format and return the message indicative of an empty search.

    :param query_stmt: the query command
    :param bind_vals: values associated with the query command
    :return: message indicative of empty search
    """
    result: str = str_sanitize(query_stmt)

    if bind_vals:
        for val in bind_vals:
            if isinstance(val, str):
                sval: str = f"'{val}'"
            else:
                sval: str = str(val)
            result = result.replace("?", sval, 1)

    return result


def _db_log(errors: list[str], err_msg: str, logger: Logger,
            query_stmt: str, bind_vals: tuple = None) -> None:
    """
    Log *err_msg* and add it to *errors*, or else log the executed query, whichever is applicable.

    :param errors: incidental errors
    :param err_msg: the error message
    :param logger: the logger object
    :param query_stmt: the query statement
    :param bind_vals: optional bind values for the query statement
    """
    if err_msg:
        if logger:
            logger.error(err_msg)
        if errors is not None:
            errors.append(err_msg)
    elif logger:
        debug_msg: str = _db_build_query_msg(query_stmt, bind_vals)
        logger.debug(debug_msg)
