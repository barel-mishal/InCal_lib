from incal_lib import readers

PATH, PATHS = '', [
    "csvs\meital\hebrew_2021-10-10_07_36_ido_accessdoors_1021_script1_w1_m_calr.csv",
    "csvs\meital\hebrew_2021-10-17_10_05_ido_accessdoors_1021_script2_w2_m_calr.csv",
]
GROUPS_EXP_DESIGN_STRACTURE = list(
    OrderedDict(GROUP1=[i for i in range(1, 17)]).items())
DATETIME = 'Date_Time_1'
CUMULETIVE_COLUMNS_NAMES = "|".join(
    ['food', 'water', 'allmeters', 'wheelmeters', 'pedmeters'])
PREFIX_CUMUL = 'actual_'


# TODO: document each function
# TODO: make a reggertion test with names
# TODO: expline the importence for the public function
# TODO: read me


# read files and print it in screen
print(readers.read_CalR_sable_file(
    PATHS,
    GROUPS_EXP_DESIGN_STRACTURE,
    DATETIME,
    CUMULETIVE_COLUMNS_NAMES,
    PREFIX_CUMUL))

print(readers.read_macro_sable_file(
    PATHS,
    GROUPS_EXP_DESIGN_STRACTURE,
    DATETIME,
    CUMULETIVE_COLUMNS_NAMES,
    PREFIX_CUMUL))

print(readers.read_tse_file(
    PATHS,
    GROUPS_EXP_DESIGN_STRACTURE,
    DATETIME,
    CUMULETIVE_COLUMNS_NAMES,
    PREFIX_CUMUL))
