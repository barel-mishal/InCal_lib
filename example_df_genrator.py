# calr
from incal_lib import create_dataframe
from incal_lib import readers


expriment1 = create_dataframe.create_calr_example_df(
    6, "2022-01-01")
expriment2 = create_dataframe.create_calr_example_df(
    10, "2022-01-02")


exps = "csvs/first_exp.csv", "csvs/secound_exp.csv"
expriment1.to_csv(exps[0])
expriment2.to_csv(exps[1])


groups = [('Group_1', [1]), ('Group_2', [2])]

df = readers.read_CalR_sable_file(
    exps,
    groups,
    'feature2',
    'Date_Time_1',
    add_prefix_cumul='A')

print(df)
print(df.index.get_level_values(0))
print(df.index.get_level_values(1))
print(df.index.get_level_values(2))
